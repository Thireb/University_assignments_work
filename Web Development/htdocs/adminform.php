<?php
#include 'connection.php'

$adname = $_REQUEST["user"];
$pass = $_REQUEST["pass"];
$preName = "None";
$prePass = "none";
if( $adname == $preName && $pass == $prePass){
    //redirect
    header( 'Location: table.php' ) ;

}else{
    echo "<h1>Wrong Username or Password. </h1>";
}

?>