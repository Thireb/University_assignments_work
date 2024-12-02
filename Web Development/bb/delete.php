<?php
// Process delete operation after confirmation
if(isset($_POST["id"]) && !empty($_POST["id"])){
// Include config file
include "connection.php";
// Prepare a delete statement
$d_id = trim($_POST["id"]);
$sql = "DELETE FROM donors WHERE Donor_ID= '$d_id'";
if ($conn->query($sql)) {
//Redirecting to landing page
header("location: table.php");
exit();
}else{
echo "Oops! Something went wrong. Please try again later.";
}

// Close connection
$link->close();
} else{
// Check existence of id parameter
if(empty(trim($_GET["id"]))){
// URL doesn't contain id parameter. Redirect to error page
header("location: error.php");
exit();
}
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Delete Record</title>
    <link rel="stylesheet" href="style.css">
    <link
      href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap"
      rel="stylesheet"
    />
</head>
<body>
<div class="container">
    <h1>Delete Record</h1>   
    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
        <input 
            type="hidden" 
            name="id" 
            value="<?php echo trim($_GET["id"]); ?>"
        />
        <p>Are you sure you want to delete this record?</p>
        <input 
            type="submit" 
            value="Yes"
        />
        <a 
        href="table.php">
        No
        </a>
    </form>
</div>  
</body>
</html>