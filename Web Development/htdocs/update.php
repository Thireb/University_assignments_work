<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Client Registration</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <?php 
    include('navbar/nav.html'); 
    include 'connection.php';

    $id = trim($_GET["id"]);
    $sql = "SELECT * FROM donors WHERE id = $id ";
    if($result = $conn->query($sql)){
      if($result->num_rows > 0){
        while($row = $result->fetch_assoc()){

          $fn = $row['FirstName'];
          $ln = $row['LastName'];
          $g = $row['Gender'];
          $bg = $row['BloodGroup'];
          $cn = $row['ContactNumber'];
          $cnic = $row['CNIC'];
          $ad = $row['Addres'];
        }
      }
    }

    ?>
    <div class="container">
      <form action="update-pr.php" method="POST">
        <div class="heading">Client Update</div>
        <div class="main">
          <label for="first_name">First Name:</label><br />
          <input
            type="text"
            name="f-name"
            id="f_name"
            required
            value="<?php echo $fn; ?>"
          /><br />
          <label for="last_name">Last Name:</label><br />
          <input
            type="text"
            name="l-name"
            id="l_name"
            required
            value="<?php echo $ln; ?>"
          /><br />
          <label for="gender">Gender:</label><br />
          <?php echo "<p>Orignal Value:".$g."</p>";?>
          <input type="radio" name="gender" id="male" value="male" required />
          Male
          <br />
          <input type="radio" name="gender" id="female" value="female" /> Female
          <br />
          <label for="bloodgroup">Blood Group</label>
          <?php echo "<p>Orignal Value:".$bg."</p>";?>
          <select name="bloodgroup" id="blood_group">
            <option value="A+">A+</option>
            <option value="A-">A-</option>
            <option value="AB+">AB+</option>
            <option value="AB-">AB-</option>
            <option value="B+">B+</option>
            <option value="B-">B-</option>
            <option value="O+">O+</option>
            <option value="O-">O-</option></select
          >
          <label for="contactnumber">Contact Number</label>
          <input
            type="number"
            name="contact_numb"
            id="contact_number"
            minlength="10"
            maxlength="11"
            required
            value="<?php echo $cn; ?>"
          /><br />
          <label for="cnic">CNIC</label>
          <input
            type="number"
            name="cnic_"
            id="_cnic"
            minlength="10"
            maxlength="14"
            required
            value="<?php echo $cnic; ?>"
          />
          <label for="address">Address</label>
          <input
            type="text"
            name="address_"
            id="addr_ess"
            value="<?php echo $ad; ?>"
          /><br />
          <input type="hidden" name="i_d" value="<?php echo $id; ?>">
          <div class="button">
            <input type="submit" value="Update" />
            <a href="table.php">cancel</a>
          </div>
        </div>
      </form>
    </div>
  </body>
</html>
