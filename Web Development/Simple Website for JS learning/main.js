/*
First ever java script of mine

const myHeading = document.querySelector('h2')
myHeading.textContent = 'Hello World'

Event Handler:

document.querySelector("html").addEventListener("click", function () {
  alert("Ouch! Stop poking me!");
});


*/



const myImage = document.querySelector('img')

myImage.onclick =()=>{
    const myFile = myImage.getAttribute('src')
    if (myFile === 'images/file-earmark-plus.svg') {
        myImage.setAttribute('src','images/pencil-fill.svg')
    } else {
        myImage.setAttribute("src", "images/file-earmark-plus.svg");
    }
}

let myButton = document.querySelector('button')
let myheading = document.querySelector("h2");

function username() {
    const myName = prompt('Enter your name')
    if (!myName){
        username()
    }
    localStorage.setItem('name',myName)
    myheading.textContent = `Mozilla is cool, ${myName}`;
}

if (!localStorage.getItem('name')){
    username()
}else{
    const storedName = localStorage.getItem('name')
    myheading.textContent = `Mozilla is cool, ${storedName}`;
}

myButton.onclick = () =>{
    username()
}