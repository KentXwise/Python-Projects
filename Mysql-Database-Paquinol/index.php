<!-- iinclude sa taas ang imong database connection para waw tan awon
 kay ug di nimo iinclude ang database connection sa index.php (sa file na gamitan nimog database) di na mag work -->
<?php
include 'db/database.php';

// diri ra nako ibutang ang pag retrieve ug data sa database kay ganahan rako
$sql = "SELECT * FROM tasks";
$result = mysqli_query($conn, $sql);

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <title>Practice Database Connection</title>
</head>
<body>
    <div class="container">
        <h1 class="text-center">Practice Database Connection using PHP native (TodoList)</h1>
        <form action="db/add-task.php" method="get"> 
            <input type="text" name="task_title" placeholder="Add a task">
            <button type="submit" class="btn btn-primary">Add Task</button>
        </form>
        <table class="table">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Task Title</th>
                </tr>
            </thead>
            <tbody> 
                <?php // diri nako gigamit tong sa pag retrieve ug data
                // pwede man sad gud na diri nimo ibutang tong $sql = "SELECT * FROM tasks"; ug $result = mysqli_query($conn, $sql);
                // nya while loop dayun ka same thing pero samokan rako :D 
                while ($row = mysqli_fetch_assoc($result)) {
                    echo "<tr>";
                    echo "<td>" . $row['id'] . "</td>";
                    echo "<td>" . $row['task_title'] . "</td>";
                    echo "</tr>";
                }
                ?>
            </tbody>
        </table>
    </div>
</body>
</html>