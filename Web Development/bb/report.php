<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="table.css">
    <link
      href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap"
      rel="stylesheet"
    />
    <title>Report</title>
</head>
<body>

<?php
include ('navbar/nav.html');
include 'connection.php';
$sql = "SELECT BloodGroup, COUNT(BloodGroup) as 'Blood Count' FROM donors GROUP By BloodGroup";
$result = $conn->query($sql);


?>

            <table id='action' class="tableWD">
            <thead>
              <tr>
                <th scope="col">Blood Group</th>
                <th scope="col">Blood Count</th>

              </tr>
            </thead>
               
        <tbody>
            <?php  
              if ($result -> num_rows > 0){
             
                while($row = $result->fetch_assoc()){
                    echo " <tr>
                      <td>".$row['BloodGroup']."</td>
                      <td>".$row['Blood Count']."</td>

                    </tr>";
                }
        
        
        
            echo "</table>";
            }else{
                echo "No results found.";
            }
            $conn->close();
        
        ?>
            </tbody>
          </table>
<?php
            include 'connection.php';
            $sql="SELECT COUNT(BloodGroup) as 'Blood Count' FROM donors";
            $result=$conn->query($sql);
            //$row = $result->fetch_assoc();
            if ($result -> num_rows > 0){
                while($row = $result->fetch_assoc()){
                    echo "<h2>Total Blood Bottles Donated: ".$row['Blood Count']."</h2>";
                }
            }
            else{
                    echo 'No Results found';
            }
            $sql="SELECT COUNT(Donor_ID) as 'Total donors' FROM donors";
            $result=$conn->query($sql);
            //$row = $result->fetch_assoc();
            if ($result -> num_rows > 0){
                while($row = $result->fetch_assoc()){
                    echo "<h2>Total Donators: ".$row['Total donors']."</h2>";
                }
            }
            else{
                    echo 'No Results found';
            }
                $conn->close();

?>
</body>
</html>