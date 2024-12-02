<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Table</title>
    <link rel="stylesheet" href="table.css">
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="faw/css/all.css">
</head>
<body>
<?php include('navbar/nav.html'); ?>
<div class="container">
    <form action="search.php" method="post">
        <input type="text" name="search" id="sea_rch" placeholder="Enter ID to search">
        <input type="submit" value="Search">
    </form>
</div>
<?php
// Include config file
include 'connection.php';
// Attempt select query execution
$id_d = trim($_POST["search"]);
$sql = "SELECT * FROM donors WHERE id = $id_d ";
if($result = $conn->query($sql)){
if($result->num_rows > 0){
echo "<table class='don'>";
echo "<thead>";
echo "<tr>";
echo "<th>#</th>";
echo "<th>First Name</th>";
echo "<th>Last Name</th>";
echo "<th>Gender</th>";
echo "<th>Blood Group</th>";
echo "<th>Contact#</th>";
echo "<th>CNIC</th>";
echo "<th>Address</th>";
echo "<th>Action</th>";
echo "</tr>";
echo "</thead>";
echo "<tbody>";
while($row = $result->fetch_assoc()){
echo "<tr>";
echo "<td>" . $row['id'] . "</td>";
echo "<td>" . $row['FirstName'] . "</td>";
echo "<td>" . $row['LastName'] . "</td>";
echo "<td>" . $row['Gender'] . "</td>";
echo "<td>" . $row['BloodGroup'] . "</td>";
echo "<td>" . $row['ContactNumber'] . "</td>";
echo "<td>" . $row['CNIC'] . "</td>";
echo "<td>" . $row['Addres'] . "</td>";
echo "<td id='action'>";
echo "<a href='update.php?id=".$row['id'] ."' ><i class='fas fa-edit'></i></a>&nbsp;&nbsp;";
echo "<a href='delete.php?id=".$row['id'] ."' ><i class='fas fa-trash'></i></a>";
echo "</td>";
echo "</tr>";
}
echo "</tbody>";
echo "</table>";
// Free result set
mysqli_free_result($result);
} else{
echo "<p><em>No records were
found.</em></p>";
}
} else{
echo "ERROR: Could not able to execute $sql. " .
mysqli_error($conn);
}
// Close connection
$conn->close();
?>

</body>
</html>