<?php
    echo "O nome é " . $_POST["nome"] . "<br>";
    echo "A senha é " . $_POST["senha"] . "<br>";

    if(isset($_POST["termo"]))
        echo "Termo aceito. <br/>" . $_POST["termo"];
?>