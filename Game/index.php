<!DOCTYPE html>
<html>
<head>
	<title>Log into game</title>
	<link rel="stylesheet" a href="style.css">
	<!-- <link rel="stylesheet" a href="font-awesome.min.css"> -->
</head>
<body>
	<div class="container">
		<form method="POST" action="game.php">
            <?php
                if (isset($error_msg))
                echo '<p color="red">'.$error_msg.'</p>';
            ?>

			<div class="form-input">
				<input type="text" name="username" placeholder="Enter the User Name"/>	
			</div>
			<input type="submit" value="submit" class="btn-login"/>
		</form>
	</div>

    <?php
        $url = 'game.php';
        require_once("connect.php");
            
        // check to see if there is a user already exists
        session_start(); 
            
        if (isset($_POST['registerBtn'])){ 
            // get all of the form data 
            $username = $_POST['username'];
        }

        $query = mysqli_query($conn, "SELECT * FROM score WHERE username='{$username}'");
        if (mysqli_num_rows($query) == 1){
            echo '<META HTTP-EQUIV=REFRESH CONTENT="1; '.$url.'">';
        }
    ?>
</body>
</html>