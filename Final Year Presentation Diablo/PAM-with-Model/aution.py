# !/usr/bin/env python
# coding=utf-8
# pip3 install -r requirements.txt  -i https://pypi.douban.com/simple/
#
import concurrent.futures
import configparser
import datetime
import os
import re
import sys
import time
from math import ceil
import json
from copy import deepcopy
from urllib.parse import urljoin


import pandas as pd
import requests
from loguru import logger
from parsel import Selector
from dateutil.parser import parse as date_parse
import pymongo

sys.setrecursionlimit(1000000)


CURRENT_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))


config = configparser.RawConfigParser()
config.read(os.path.join(CURRENT_DIR, 'config.ini'), encoding='utf-8-sig')

DEFAULT = dict(config['DEFAULT'])
print(DEFAULT)
DEFAULT['retry_times'] = 50
DEFAULT['max_workers'] = 20
DEFAULT['proxy'] = ''

if DEFAULT.get('proxy'):
    proxies = {
        'http': DEFAULT['proxy'],
        'https': DEFAULT['proxy'],
    }
else:
    proxies = {}


class Base():
    def __init__(self):
        self.session = requests.Session()
        self.db = pymongo.MongoClient()['whisky']

    def _requests(self, *args, **kwargs):
        _headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
            'Cache-Control': 'no-cache',
        }
        if kwargs.get('headers'):
            _headers.update(kwargs['headers'])
            kwargs.pop('headers')
        for i in range(int(DEFAULT['retry_times'])):
            try:
                response = requests.request(
                    *args, **kwargs, headers=_headers, proxies=proxies, timeout=180)
                logger.info(f"response status code:{response.status_code}")
                if response.status_code != 200:
                    time.sleep(5)
                    continue
                break
            except Exception as e:
                time.sleep(5)
                logger.error(f"requests error: {e}")
        else:
            logger.error(f"response is None")
            return None
        return response

    def thread_pool(self, func, task_total_count, *params):
        with concurrent.futures.ThreadPoolExecutor(max_workers=int(DEFAULT['max_workers'])) as executor:
            for index, result in enumerate(executor.map(func, *params)):
                logger.info(f"{index}/{task_total_count} {result}")


class Scotchwhiskyauctions(Base):
    '''
    1ï¼Œhttps://www.scotchwhiskyauctions.com/auctions/ 
    '''

    def __init__(self):
        super(Scotchwhiskyauctions, self).__init__()
        self.collection = self.db['Scotchwhiskyauctions']

    def list(self, task):
        url = "https://www.scotchwhiskyauctions.com/ajax/ajaxer.php"
        payload = {
            'mode': 'form',
            'action': task['action'],
            'method': 'get',
            'id': '',
            'json': json.dumps({"page": task['page']})
        }
        headers = {
            'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'Cookie': 'PHPSESSID=28p7sp2pqtnhemmet7u61elep3; lastauction=176; _ga=GA1.1.1554672960.1656088534; ageok=1; perpage=500; sortby=name; sortorder=ASC; _ga_065PL0LN18=GS1.1.1656087940.8.1.1656088554.0',
        }
        response = self._requests("POST", url, headers=headers, data=payload)
        data = response.json()
        sel = Selector(data['content'])
        for index, i in enumerate(sel.xpath('//*[@id="lots"]/a')):
            logger.info(index)
            item = {}
            item['page'] = task['page']
            item['index'] = index
            item['website'] = 'Scotchwhiskyauctions'
            item['add_time'] = datetime.datetime.now()
            item['date'] = str(task['date'])
            item['url'] = 'https://www.scotchwhiskyauctions.com/' + \
                i.xpath('./@href').get('').strip()
            image_url = i.xpath(
                './/div[@class="aucimgw"]/div/@style').get('').strip()
            try:
                item['image_url'] = re.findall(
                    "url\('(.*?)'\);", image_url, re.S)[0]
            except:
                item['image_url'] = ''
            item['title'] = i.xpath('.//h4/text()').get('').strip()
            item['lot'] = i.xpath(
                './/h6/text()').get('').replace('Lot no', '').strip()
            item['sold'] = i.xpath(
                './/p[@class="sold"]/text()').get('').replace('Sold for', '').strip()
            item['_id'] = item['url']
            try:
                self.collection.insert_one(item)
                logger.success(item)
            except Exception as e:
                logger.error(e)
                logger.warning(item)

    def main(self):
        url = 'https://www.scotchwhiskyauctions.com/auctions/'
        response = self._requests('get', url=url)
        sel = Selector(response.text)
        task_list = []
        for i in sel.xpath('//a[@class="auction"]'):
            action = 'https://www.scotchwhiskyauctions.com/' + \
                i.xpath('./@href').get('').strip()
            date = i.xpath('.//h5/text()').get('').replace('Ends',
                                                           '').replace('Ended', '').strip()
            date = date_parse(date).date()
            lots_num = i.xpath('.//h6/text()').get('').replace(',', '').strip()
            try:
                lots_num = re.findall(
                    'There are (\d+) lots in this auction', lots_num, re.S)[0]
                lots_num = int(lots_num)
            except:
                lots_num = 0
            total_page = ceil(lots_num/500)
            for page in range(1, total_page+1):
                task = {}
                task['action'] = action
                task['date'] = date
                task['page'] = page
                task_list.append(task)
                logger.success(task)
        logger.info(len(task_list))
        self.thread_pool(self.list, len(task_list), task_list)


class Whiskyauction(Base):
    '''
    2ï¼Œhttps://whiskyauction.com/
    '''

    def __init__(self):
        super(Whiskyauction, self).__init__()
        self.collection = self.db['Whiskyauction']

    def list(self, page=1):
        logger.info(f'page:{page}')
        url = "https://whiskyauction.com/auction/Hauptseite_all.php"
        params = {
            'aFilter': 'select',
            'bFilterMax': '',
            'bFilterMin': '',
            'cFilter': 'select',
            'cat': 'All',
            'currentPage': page,
            'filter': 'on',
            'itemArrow': 'ASC',
            'itemFilter': '',
            'multipleCompany': '',
            'numOfItems': '200',
            'searchFilter': '',
            'theAuctionYears': '',
            'theId': '1',
            'theLimit': 'Limit',
            'theLimitMax': '200',
            'theLimitMin': '0',
            'theOrder': 'ASC',
            'theSort': 'item'
        }
        response = self._requests("GET", url, params=params)
        sel = Selector(response.text)
        for index, i in enumerate(sel.xpath('//table[3]/tr')):
            if index == 0:
                continue
            item = {}
            item['page'] = page
            item['index'] = index
            item['website'] = 'Whiskyauction'
            item['add_time'] = datetime.datetime.now()
            item['date'] = i.xpath('.//td[3]/text()').get('').strip()
            item['url'] = i.xpath('.//td[1]/a/@href').get('').strip()
            item['image_url'] = i.xpath('.//td[2]/a//img/@src').get('').strip()
            item['title'] = i.xpath('string(.//td[6])').get('').strip()
            item['lot'] = i.xpath('.//td[1]/a/text()').get('').strip()
            item['sold'] = i.xpath('.//td[4]/text()').get('').strip()
            item['_id'] = item['url']
            try:
                self.collection.insert_one(item)
                logger.success(item)
            except Exception as e:
                logger.error(e)
                logger.warning(item)
        if page == 1:
            total_page = re.findall(
                '<i>Page \d+ of (\d+)</i>', response.text, re.S)[0]
            total_page = int(total_page)
            task_list = [page for page in range(2, total_page+1)]
            self.thread_pool(self.list, len(task_list), task_list)

    def main(self):
        self.list()


class JustWhisky(Base):
    '''
    3ï¼Œ https://www.just-whisky.co.uk/
    '''

    def __init__(self):
        super(JustWhisky, self).__init__()
        self.collection = self.db['JustWhisky']

    def list(self, task):
        url = 'https://www.just-whisky.co.uk/modules/blocklayered_mod/blocklayered_mod-ajax.php'
        logger.info(task)
        params = {
            'layered_auction_1': 'all',
            'id_category_layered': task['id_category_layered'],
            'orderby': 'reference',
            'orderway': 'desc',
            'n': '100',
            'p': task['page'],
            '_': int(time.time()*1000),
        }
        response = self._requests('get', url, params=params)
        data = response.json()
        productList = data['productList']
        sel = Selector(productList)
        for index, i in enumerate(sel.xpath('//*[@id="product_list"]/li')):
            item = {}
            item['page'] = task['page']
            item['index'] = index
            item['website'] = 'JustWhisky'
            item['add_time'] = datetime.datetime.now()
            item['date'] = task['date']
            item['url'] = i.xpath(
                './/a[@class="product_img_link"]/@href').get('').strip()
            item['image_url'] = i.xpath(
                './/a[@class="product_img_link"]/img/@src').get('').strip()
            item['title'] = i.xpath(
                './/a[@class="product_img_link"]/@title').get('').strip()
            item['lot'] = i.xpath(
                './/div[@class="lot"]/span/text()').get('').strip()
            item['sold'] = i.xpath(
                './/span[@class="price"]/text()').get('').replace('Winning Bid:', '').strip()
            item['_id'] = item['lot']
            try:
                self.collection.insert_one(item)
                logger.success(item)
            except Exception as e:
                logger.error(e)
                logger.warning(item)
        if task['page'] == 1:
            categoryCount = data['categoryCount']
            total_count = int(re.findall(
                'There are (\d+) products', categoryCount)[0])
            total_page = ceil(total_count/100)
            task_list = []
            for page in range(2, total_page+1):
                new_task = deepcopy(task)
                new_task['page'] = page
                task_list.append(new_task)
            self.thread_pool(self.list, len(task_list), task_list)

    def main(self):
        response = self._requests('get', url='https://www.just-whisky.co.uk/')
        sel = Selector(response.text)
        task_list = []
        for index, url in enumerate(sel.xpath('//*[text()="Past Auctions"]/..//ul/li/ul/li/a/@href').getall()):
            task = {}
            task['id_category_layered'] = re.findall(
                'whisky.co.uk/(\d+)-', url)[0]
            date = re.findall('whisky.co.uk/\d+-(.*)', url)[0]
            try:
                task['date'] = str(date_parse(date))[:7]
            except:
                task['date'] = '2021-SMWS-Special'
            task['page'] = 1
            task_list.append(task)
        self.thread_pool(self.list, len(task_list), task_list)


class Speysidewhiskyauctions(Base):
    '''
    4ï¼Œhttps://www.speysidewhiskyauctions.co.uk/past-auctions
    '''

    def __init__(self):
        super(Speysidewhiskyauctions, self).__init__()
        self.collection = self.db['Speysidewhiskyauctions']

    def list(self, task):
        logger.info(task)
        url = f'https://www.speysidewhiskyauctions.co.uk/{task["url_in"]}'
        payload = f"search_filter=&auction_id={task['selected_auction_id']}&sort=highest-bids&page={task['page']}&per_page=100"
        headers = {
            'accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        response = self._requests(
            'post', url=url, data=payload, headers=headers)
        data = response.json()
        for index, i in enumerate(data['items']):
            item = {}
            item['page'] = task['page']
            item['index'] = index
            item['website'] = 'Speysidewhiskyauctions'
            item['add_time'] = datetime.datetime.now()
            item['date'] = str(date_parse(i['ends_at']).date())
            item['url'] = i['url']
            item['image_url'] = "https://www.speysidewhiskyauctions.co.uk/" + \
                i['thumb_image']
            item['title'] = i['name']
            item['lot'] = i['lot_id']
            item['sold'] = i['bid_value']
            item['_id'] = i['url']
            logger.success(item)
            try:
                self.collection.insert_one(item)
                logger.success(item)
            except Exception as e:
                logger.error(e)
                logger.warning(item)

    def main(self):
        url = 'https://www.speysidewhiskyauctions.co.uk/past-auctions'
        response = self._requests('get', url=url)
        sel = Selector(response.text)
        task_list = []
        for url in sel.xpath('//ul[@class="itemsList"]/li/div/a/@href').getall():
            detail_url = 'https://www.speysidewhiskyauctions.co.uk'+url
            detail_response = self._requests('get', url=detail_url)

            num_results = int(re.findall(
                'num-results="(\d+)"', detail_response.text, re.S)[0])
            selected_auction_id = int(re.findall(
                'selected-auction-id="(\d+)"', detail_response.text, re.S)[0])
            url_in = re.findall('url-in="/(.*?)"',
                                detail_response.text, re.S)[0]

            total_page = ceil(num_results/100)
            for page in range(1, total_page+1):
                task = {}
                task['selected_auction_id'] = selected_auction_id
                task['url_in'] = url_in
                task['page'] = page
                logger.success(task)
                task_list.append(task)
        self.thread_pool(self.list, len(task_list), task_list)


class Thegrandwhiskyauction(Base):
    '''
    5ï¼Œhttps://www.thegrandwhiskyauction.com/past-auctions
    '''

    def __init__(self):
        super(Thegrandwhiskyauction, self).__init__()
        self.collection = self.db['Thegrandwhiskyauction']

    def list(self, task):
        logger.info(task)
        url = f'https://www.thegrandwhiskyauction.com/{task["url_in"]}'
        payload = f"search_filter=&auction_id={task['selected_auction_id']}&sort=highest-bids&page={task['page']}&per_page=100"
        headers = {
            'accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        response = self._requests(
            'post', url=url, data=payload, headers=headers)
        data = response.json()
        for index, i in enumerate(data['items']):
            item = {}
            item['page'] = task['page']
            item['index'] = index
            item['website'] = 'Speysidewhiskyauctions'
            item['add_time'] = datetime.datetime.now()
            item['date'] = str(date_parse(i['ends_at']).date())
            item['url'] = i['url']
            item['image_url'] = "https://www.thegrandwhiskyauction.com/" + \
                i['thumb_image']
            item['title'] = i['name']
            item['lot'] = i['lot_id']
            item['sold'] = i['bid_value']
            item['_id'] = i['url']
            logger.success(item)
            try:
                self.collection.insert_one(item)
                logger.success(item)
            except Exception as e:
                logger.error(e)
                logger.warning(item)

    def main(self):
        url = 'https://www.thegrandwhiskyauction.com/past-auctions'
        response = self._requests('get', url=url)
        sel = Selector(response.text)
        task_list = []
        for url in sel.xpath('//ul[@class="itemsList"]/li/div/a/@href').getall():
            detail_url = 'https://www.thegrandwhiskyauction.com'+url
            detail_response = self._requests('get', url=detail_url)
            num_results = int(re.findall(
                'num-results="(\d+)"', detail_response.text, re.S)[0])
            selected_auction_id = int(re.findall(
                'selected-auction-id="(\d+)"', detail_response.text, re.S)[0])
            url_in = re.findall('url-in="/(.*?)"',
                                detail_response.text, re.S)[0]
            total_page = ceil(num_results/180)
            for page in range(1, total_page+1):
                task = {}
                task['selected_auction_id'] = selected_auction_id
                task['url_in'] = url_in
                task['page'] = page
                logger.success(task)
                task_list.append(task)
        self.thread_pool(self.list, len(task_list), task_list)


class Whiskyshop(Base):
    '''
    6ï¼Œhttps://www.whiskyshop.com/auctions/past-months
    '''

    def __init__(self):
        super(Whiskyshop, self).__init__()
        self.collection = self.db['Whiskyshop']

    def list(self, task):
        response = self._requests('get', task['url'])
        if not response:
            return
        sel = Selector(response.text)
        for index, i in enumerate(sel.xpath('//ol[@class="products list items product-items"]/li')):
            item = {}
            item['page'] = task['page']
            item['index'] = index
            item['website'] = 'Whiskyshop'
            item['add_time'] = datetime.datetime.now()
            item['date'] = task['date']
            item['url'] = i.xpath(
                './/a[@class="product-item-link"]/@href').get('')
            item['image_url'] = i.xpath('.//img/@data-original').get('')
            if not item['image_url']:
                item['image_url'] = i.xpath('.//img/@src').get('')
            item['title'] = i.xpath(
                './/a[@class="product-item-link"]/text()').get('')
            item['lot'] = i.xpath(
                './/div[@class="ribbon ribbon-lotno"]/span/text()').get('').replace('Lot', '').strip()
            item['sold'] = i.xpath(
                './/a[@data-price]/@data-price').get('').strip()
            item['_id'] = item['url']
            try:
                self.collection.insert_one(item)
                logger.success(item)
            except Exception as e:
                logger.error(e)
                logger.warning(item)

    def main(self):
        task_list = []
        response = self._requests(
            'get', url='https://www.whiskyshop.com/auctions/past-months')
        sel = Selector(response.text)
        for i in sel.xpath('//ol[@class="products list items product-items"]/li'):
            date = i.xpath('.//a[@class="product-item-link"]/text()').get('')
            date = str(date_parse(date).date())
            url = "https://www.whiskyshop.com" + \
                i.xpath('.//a[@class="product-item-link"]/@href').get('')
            total_lots = i.xpath(
                './/div[@class="product-item-name legal-attrs"]/text()').get('').replace('lots', '').strip()
            total_lots = int(total_lots)
            total_page = ceil(total_lots/140)
            for page in range(1, total_page+1):
                task = {}
                task['url'] = url+f"&p={page}"
                task['date'] = date
                task['page'] = page
                task_list.append(task)
                logger.info(task)
        # åˆåçˆ¬ï¼Œç”¨å•çº¿ç¨‹
        for task in task_list:
            self.list(task=task)


class Wvawhiskyauctions(Base):
    '''
    7ï¼Œhttps://www.wvawhiskyauctions.co.uk/past-auctions
    '''

    def __init__(self):
        super(Wvawhiskyauctions, self).__init__()
        self.collection = self.db['Wvawhiskyauctions']

    def list(self, page):
        url = 'https://www.wvawhiskyauctions.co.uk/past-auctions'
        payload = f"search_filter=&auction_id=-1&sort=highest-bids&page={page}&per_page=80"
        headers = {
            'accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        response = self._requests(
            'post', url=url, data=payload, headers=headers)
        data = response.json()
        for index, i in enumerate(data['items']):
            item = {}
            item['page'] = page
            item['index'] = index
            item['website'] = 'Wvawhiskyauctions'
            item['add_time'] = datetime.datetime.now()
            item['date'] = str(date_parse(i['ends_at']).date())
            item['url'] = i['url']
            item['image_url'] = "https://www.wvawhiskyauctions.co.uk" + \
                i['thumb_image']
            item['title'] = i['name']
            item['lot'] = i['lot_id']
            item['sold'] = i['bid_value']
            item['_id'] = i['url']
            logger.success(item)
            try:
                self.collection.insert_one(item)
                logger.success(item)
            except Exception as e:
                logger.error(e)
                logger.warning(item)
        if page == 1:
            result_count = data['result_count']
            total_page = ceil(result_count/80)
            task_list = list(range(2, total_page+1))
            self.thread_pool(self.list, len(task_list), task_list)

    def main(self):
        self.list(page=1)


class Whiskyauctioneer(Base):
    '''
    8ï¼Œhttps://whiskyauctioneer.com/auctions/past-auctions
    '''

    def __init__(self):
        super(Whiskyauctioneer, self).__init__()
        self.collection = self.db['Whiskyauctioneer']
        self.task_list = []

    def detail(self, task):
        response = self._requests('get', task['url'])
        sel = Selector(response.text)
        for index, i in enumerate(sel.xpath('//div[@class="view-content"]/div')):
            item = {}
            item['page'] = task['page']
            item['index'] = index
            item['website'] = 'Whiskyauctioneer'
            item['add_time'] = datetime.datetime.now()
            item['date'] = task['date']
            item['url'] = i.xpath('./a/@href').get('').strip()
            item['image_url'] = i.xpath('.//img/@src').get('').strip()
            item['title'] = i.xpath('./a/@_title').get('').strip()
            item['lot'] = i.xpath(
                './a/span[@class="lotnumber label-lot"]/text()').get('').strip()
            item['sold'] = i.xpath(
                './/span[@class="uc-price"]/text()').get('').strip()
            item['_id'] = item['url']
            try:
                self.collection.insert_one(item)
                logger.success(item)
            except Exception as e:
                logger.error(e)
                logger.warning(item)

    def list(self, page=0):
        url = 'https://whiskyauctioneer.com/auctions/past-auctions'
        url_set = set()
        params = {
            'page': page
        }
        logger.info(f"page:{page}")
        response = self._requests('get', url, params=params)
        sel = Selector(response.text)

        for url in sel.xpath('//*[@id="block-system-main"]/div/div/div[@class="cell md-lg-4"]//a[@class="listing-image"]/@href').getall():
            url = url.replace('http://', 'https://')
            if '/lot/' in url:
                continue
            if url in url_set:
                continue
            url_set.add(url)
            url = urljoin('https://whiskyauctioneer.com/', url)
            logger.info(url)
            detail_response = self._requests('get', url)
            Total_Lots = re.findall(
                'Total: (\d+) Lots', detail_response.text, re.S)[0]
            Total_Lots = int(Total_Lots)
            total_page = ceil(Total_Lots/500)
            for _page in range(0, total_page):
                task = {}
                task['page'] = _page+1
                task['url'] = f"{url}?text=&sort=auc_high_bid_amt%20DESC&items_per_page=500&page={_page}"
                date_ = url.split('/')[-1].replace('-auction', '')
                try:
                    task['date'] = str(date_parse(date_).date())
                except:
                    task['date'] = date_
                logger.info(task)
                self.task_list.append(task)
        next_page_exists = sel.xpath('//a[@title="Go to next page"]')
        if next_page_exists:
            page += 1
            self.list(page=page)

    def main(self):
        self.list(page=0)
        self.thread_pool(self.detail, len(self.task_list), self.task_list)


class Whiskyhammer(Base):
    '''
    9ï¼Œhttps://www.whiskyhammer.com/previous-auctions
    '''

    def __init__(self):
        super(Whiskyhammer, self).__init__()
        self.collection = self.db['Whiskyhammer']

    def list(self, task):
        params = {
            'url': f"{task['url']}?page={task['page']}&ps=500",
            'type': "past",
        }
        response = self._requests(
            'get', url='https://www.whiskyhammer.com/modules/Auction/browse/ajax.php', params=params)
        data = response.json()
        for index, i in enumerate(data['items']):
            item = {}
            item['page'] = task['page']
            item['index'] = index
            item['website'] = 'Whiskyhammer'
            item['add_time'] = datetime.datetime.now()
            item['date'] = task['date']
            item['url'] = i['url']
            item['image_url'] = 'https://www.whiskyhammer.com'+i['default_image']
            item['title'] = i['name']
            item['lot'] = i['id']
            item['sold'] = i['item_price']
            item['_id'] = i['id']
            try:
                self.collection.insert_one(item)
                logger.success(item)
            except Exception as e:
                logger.error(e)
                logger.warning(item)

    def main(self):
        task_list = []
        response = self._requests(
            'get', url='https://www.whiskyhammer.com/previous-auctions')
        sel = Selector(response.text)
        for i in sel.xpath('//ul[@class="itemsList"]/li'):
            url = i.xpath('./a/@href').get('').strip()
            title = i.xpath('./a/@title').get('').strip()
            try:
                title = title.split('-')[-1].strip()
                date = str(date_parse(title).date())
            except:
                date = title
            detail_response = self._requests(
                'get', url='https://www.whiskyhammer.com'+url)
            numberOfProducts = Selector(detail_response.text).xpath(
                '//div[@class="numberOfProducts"]/text()').get('').replace('Items', '').strip()
            numberOfProducts = int(numberOfProducts)
            total_page = ceil(numberOfProducts/500)
            for page in range(1, total_page+1):
                task = {}
                task['url'] = url
                task['date'] = date
                task['page'] = page
                logger.info(task)
                task_list.append(task)
        self.thread_pool(self.list, len(task_list), task_list)


class Whiskyworm(Base):
    '''
    10ï¼Œhttps://www.whiskyworm.com/index_auction.php#pageObject/{%22flag%22:1}
    '''

    def __init__(self):
        super(Whiskyworm, self).__init__()
        self.collection = self.db['Whiskyworm']

    def list(self, page=1):
        params = {
            'action': 'conlist',
            'time_status': 'isover',
            'contype': '7',
            'page': page,
            '_': int(time.time())*1000,
        }
        response = self._requests(
            'get', url='https://sdata.whiskyworm.com/app/conlist.php', params=params)
        data = response.json()
        for index, i in enumerate(data['list']):
            item = {}
            item['page'] = page
            item['index'] = index
            item['website'] = 'Whiskyworm'
            item['add_time'] = datetime.datetime.now()
            item['date'] = datetime.datetime.fromtimestamp(int(i['overtime']))
            item['url'] = i['shareurl']
            item['image_url'] = i['litpic']
            item['title'] = i['title']
            item['lot'] = i['id']
            item['sold'] = i['price']
            item['_id'] = i['id']
            try:
                self.collection.insert_one(item)
                logger.success(item)
            except Exception as e:
                logger.error(e)
                logger.warning(item)
        if page == 1:
            maxpage = data['maxpage']
            task_list = list(range(2, maxpage+1))
            self.thread_pool(self.list, len(task_list), task_list)

    def main(self):
        self.list()


def run():
    text = '''
    1ï¼Œhttps://www.scotchwhiskyauctions.com/auctions/ 
    2ï¼Œhttps://whiskyauction.com/
    3ï¼Œhttps://www.just-whisky.co.uk/
    4ï¼Œhttps://www.speysidewhiskyauctions.co.uk/past-auctions
    5ï¼Œhttps://www.thegrandwhiskyauction.com/past-auctions
    6ï¼Œhttps://www.whiskyshop.com/auctions/past-months
    7ï¼Œhttps://www.wvawhiskyauctions.co.uk/past-auctions
    8ï¼Œhttps://whiskyauctioneer.com/auctions/past-auctions
    9ï¼Œhttps://www.whiskyhammer.com/previous-auctions
    10ï¼Œhttps://www.whiskyworm.com/index_auction.php#pageObject/{%22flag%22:1}
    0,all
    '''
    mode = input(text)
    if mode == '1':
        Scotchwhiskyauctions().main()
        # Scotchwhiskyauctions().list(task={'action': 'https://www.scotchwhiskyauctions.com/auctions/176-the-132nd-auction/', 'date': datetime.datetime(2022, 6, 12, 0, 0), 'page': 2})
    elif mode == '2':
        Whiskyauction().main()
    elif mode == '3':
        JustWhisky().main()
    elif mode == '4':
        Speysidewhiskyauctions().main()
    elif mode == '5':
        Thegrandwhiskyauction().main()
    elif mode == '6':
        Whiskyshop().main()
        # Whiskyshop().list({'url': 'https://www.whiskyshop.com/auctions/ended?product_list_order=price_desc&auction_ended=September+2019&p=3', 'date': '2019-09-28', 'page': 3})
    elif mode == '7':
        Wvawhiskyauctions().main()
    elif mode == '8':
        # Whiskyauctioneer().detail(task={'page': 4, 'url': 'https://whiskyauctioneer.com/august-2016-auction?text=&sort=auc_high_bid_amt%20DESC&items_per_page=500&page=3', 'date': '2016-08-28'})
        Whiskyauctioneer().main()
    elif mode == '9':
        # Whiskyhammer().list(task={'url': 'https://www.whiskyhammer.com/modules/Auction/browse/ajax.php?url=/auction/past/auc-71/?ps=500&type=past', 'date': '2021-11-28', 'page': 7})
        Whiskyhammer().main()
    elif mode == '10':
        Whiskyworm().main()


if __name__ == '__main__':
    run()
