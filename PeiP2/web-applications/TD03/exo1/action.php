<?php
session_start();

# retourne une chaîne de caractères indiquant
# le résultat, où '$x' et '$y' sont les nombres
# dont il fallait deviner la valeur du produit
# et '$user' la valeur proposée par l'utilisateur
function resultat($x, $y, $user)
{
	if ($user == $x * $y) {
		return "Bravo, vous avez trouvé le résultat !";
	} else {
		$ans = $x * $y;
		return "Désolé, la réponse était $ans, pas $user.";
	}
}
?>
<!DOCTYPE html>
<html lang="fr">

<head>
	<meta charset="utf-8">
	<title>TP 3 - Exo 1</title>
	<meta name="author" content="Marc Gaetano">
	<meta name="viewport" content="width=device-width; initial-scale=1.0">
	<link rel="stylesheet" href="../css/tp3.css">
	<link rel="stylesheet" href="style.css">
</head>

<body>
	<h1>TP 3 - Exo 1</h1>
	<hr>

	<h2>Multiplication</h2>
	<p>
		<?php
		$x = $_SESSION['x'];
		$y = $_SESSION['y'];
		$user = $_GET['utilisateur'];

		echo resultat($x, $y, $user);
		?>
	</p>
	<p>
		<a href="formulaire.php">Autre multiplication</a>
	</p>
</body>

</html>
