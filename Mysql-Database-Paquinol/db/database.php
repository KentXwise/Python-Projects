<?php
// Database connection
// diri na part usually pag wala kay gihilabtan sa XAMPP PHPMYADMIN (or dunno kung unsay gamit nimo sa database) like creating an account or something
// default jud ning "localhost", "root", "", pero sa last kay ("Database name")
// syempre pagbuhat sa pud daan ug database sa XAMPP PHPMYADMIN (or dunno kung unsay gamit nimo sa database)
$db_host = "localhost";
$db_user = "root";
$db_pass = "";
$db_name = "todo_list";

// Connect to the database
$conn = mysqli_connect($db_host, $db_user, $db_pass, $db_name);

// diri na part icheck kung nakaconnect ka sa database
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
} else {
    echo "Connected successfully"; // iremove lang ni ug makita nimo sa page ang "Connected successfully" kay goods nana sya for confirmation rajud ni siya
}