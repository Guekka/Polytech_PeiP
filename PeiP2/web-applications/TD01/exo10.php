<?php

# retourne le nom du jour de la semaine
# correspondant à '$week', le  numéro du
# jour de la semaine (0 -> dimanche, 1 -> lundi, ...)
function jour($week)
{
    $jours = array("Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi");
    return $jours[$week];
}

?>
<!DOCTYPE html>
<html lang="fr">
	<head>
		<meta charset="utf-8">
		<title>TP 1 - Exo 10</title>
		<meta name="author" content="Marc Gaetano">
		<meta name="viewport" content="width=device-width; initial-scale=1.0">
		<link rel="stylesheet" href="css/tp1.css">
	</head>
	<body>
		<h1>TP 1 - Exo 10</h1>
		<hr>
		<h2>
	<?php
$jour = $_GET['jour'];
$mois = $_GET['mois'];
$annee = $_GET['annee'];

$timestamp = mktime(0, 0, 0, $mois, $jour, $annee);

$day_idx = date("w", $timestamp);

echo jour($day_idx);
?>
	</h2>
	</body>
</html>
