<?php
    $db = mysqli_connect("172.20.0.8","root","123456","blog");
    if(mysqli_connect_error()){
        error_log("failed to connect".mysqli_connect_error());
    }
?>
