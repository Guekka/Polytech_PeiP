<?php

function not_first_time()
{
    return !empty($_GET['guess_count']);
}

if (not_first_time()) {
    $guess = $_GET['guess'];
    $guess_count = $_GET['guess_count'];
    $answer = $_GET['answer'];
    $win = $guess == $answer;
} else {
    $guess_count = 0;
    $answer = rand(1, 100);
    $guess = null;
    $win = false;
}

?>
<!DOCTYPE html>
<html lang="fr">

<head>
	<meta charset="utf-8">
	<title>TP 1 - Exo 12</title>
	<meta name="author" content="Marc Gaetano">
	<meta name="viewport" content="width=device-width; initial-scale=1.0">
	<link rel="stylesheet" href="css/tp1.css">
</head>

<body>
	<h1>TP 1 - Exo 12</h1>
	<hr>
	<?php
if (not_first_time()) {
    echo "Vous avez proposé $guess";
} else {
    echo "Je pense à un nombre compris entre 1 et 100... à vous de le deviner !";
}

echo "<br>";

if ($win) {
    echo "Bravo, vous avez trouvé en " . $guess_count . " essais !";
    echo "<br>";
    echo "<a class='bouton' href='exo12.php'>Autre partie</a>";
} else {
    if (not_first_time()) {
        if ($guess < $answer) {
            echo "<h3>Trop petit, essayez encore...</h3>";
        } else {
            echo "<h3>Trop grand, essayez encore...</h3>";
        }
    }

    echo "<br><br>";
    echo "<form class='exo10' method='get'>
		Votre proposition : <input type='text' name='guess'>
		<input type='hidden' name='guess_count' value='" . (intval($guess_count) + 1) . "'>
		<input type='hidden' name='answer' value='" . $answer . "'>
		<input type='submit' value='Vérifier'>
	</form>";
}

?>
</body>

</html>
