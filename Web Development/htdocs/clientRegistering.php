<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Client Registration</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <?php include('navbar/nav.html') ?>
    <div class="container">
      <form action="clientRegForm.php" method="POST">
        <div class="heading">Client Registrations</div>
        <div class="main">
          <label for="first_name">First Name:</label><br />
          <input
            type="text"
            name="f-name"
            id="f_name"
            placeholder="Enter your First Name."
            required
          /><br />
          <label for="last_name">Last Name:</label><br />
          <input
            type="text"
            name="l-name"
            id="l_name"
            placeholder="Enter your Last Name."
            required
          /><br />
          <label for="gender">Gender:</label><br />
          <input type="radio" name="gender" id="male" value="male" required />
          Male
          <br />
          <input type="radio" name="gender" id="female" value="female" /> Female
          <br />
          <label for="bloodgroup">Blood Group</label>
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
            placeholder="Enter Contact Number"
            minlength="10"
            maxlength="11"
            required
          /><br />
          <label for="cnic">CNIC</label>
          <input
            type="number"
            name="cnic_"
            id="_cnic"
            placeholder="Enter Your CNIC Number"
            minlength="10"
            maxlength="14"
            required
          />
          <label for="address">Address</label>
          <input
            type="text"
            name="address_"
            id="addr_ess"
            placeholder="Enter Your Address"
          /><br />
          <div class="button">
            <input type="submit" value="Submit" />
          </div>
        </div>
      </form>
    </div>
  </body>
</html>
