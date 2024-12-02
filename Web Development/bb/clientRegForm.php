<?php
include 'connection.php';

$firstName = $_REQUEST["f-name"];
$lastName = $_REQUEST["l-name"];
$gender = $_REQUEST["gender"];
$bloodGroup = $_REQUEST["bloodgroup"];
$contactNumber = $_REQUEST["contact_numb"];
$cnic = $_REQUEST["cnic_"];
$address = $_REQUEST["address_"];

$sql = "INSERT INTO donors (FirstName, LastName, Gender, BloodGroup, ContactNumber, CNIC, Addres ) values ('$firstName','$lastName','$gender','$bloodGroup','$contactNumber','$cnic','$address') ";
$conn->query($sql);

header( 'Location: table.php' ) ;
?>
