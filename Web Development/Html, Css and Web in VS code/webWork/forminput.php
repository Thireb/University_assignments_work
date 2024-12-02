<?php
    include 'connection.php';
    $sql = "CREATE TABLE yoga(
        yoga_id int(4) PRIMARY KEY,
        First_name varchar(20),
        Last_name varchar(20),
        email varchar(20),
        dob date
            )";
    if($conn->query($sql)){
        echo "Yoga table created successfully";
    }
    else{
        echo "false, table not created ".$conn->error;
    };
    $y_id = $_REQUEST["id"];
    $f_name = $_REQUEST["fn"];
    $l_name = $_REQUEST["ln"];
    $y_email = $_REQUEST["email"];
    $y_dob = $_REQUEST["dob"];
    $sql = "INSERT INTO yoga(yoga_id,First_name,Last_name,email,dob) VALUES('$y_id','$f_name','$l_name','$y_email','$y_dob')";

    if($conn->query($sql) === TRUE){
        echo "New record added successfully" ."<br>";
    }else{
        echo "Couldn't add new records, shut up ".$conn->error;
    }


?>