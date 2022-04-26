<?php

?>
<!DOCTYPE html>
<html lang="fr">
	<head>
		<meta charset="utf-8">
		<title>TP 1 - Exo 11</title>
		<meta name="author" content="Marc Gaetano">
		<meta name="viewport" content="width=device-width; initial-scale=1.0">
		<link rel="stylesheet" href="css/tp1.css">
	</head>
	<body>
		<h1>TP 1 - Exo 11</h1>
		<hr>
		<p>
			<?php
$x = rand(2, 10);
$y = rand(2, 10);
echo "Le produit de $x et $y est ... ?<br>";
?>
		<form action="exo11-action.php" method="get">
			<input type="hidden" name="x" value=<?php echo $x; ?>>
			<input type="hidden" name="y" value=<?php echo $y; ?>>
			<p>
			<label for="user">Votre réponse</label>
			<input type="number" name="user" id="user" required>
			</p>
			<p>
			<input type="submit" value="Valider">
			</p>
		</form>

	</body>
</html>
