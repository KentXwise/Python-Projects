<?php
// irequire jud ang database nimo para kabalo ni na file ug asa niya istore ang data
require 'database.php';

$task_title = $_GET['task_title'];


$sql = "INSERT INTO tasks (task_title) VALUES ('$task_title')";

$result = mysqli_query($conn, $sql);
if ($result) {
    header("Location: ../index.php");
} else {
    echo "Error: " . mysqli_error($conn);
}