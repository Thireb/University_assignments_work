<?php
include 'connection.php';

$id = $_REQUEST["i_d"];
$firstName = $_REQUEST["f-name"];
$lastName = $_REQUEST["l-name"];
$gender = $_REQUEST["gender"];
$bloodGroup = $_REQUEST["bloodgroup"];
$contactNumber = $_REQUEST["contact_numb"];
$cnic = $_REQUEST["cnic_"];
$address = $_REQUEST["address_"];

$sql = "UPDATE donors SET FirstName ='$firstName', LastName='$lastName', Gender='$gender', BloodGroup='$bloodGroup', ContactNumber='$contactNumber', CNIC='$cnic', Addres='$address' WHERE id = '$id'";
$conn->query($sql);

header( 'Location: table.php' ) ;
?>
