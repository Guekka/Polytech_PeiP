<?php
include("exo6.inc.php");

$id = $_GET["id"];
$prenom = $_GET["prenom"];
$nom = $_GET["nom"];
$note1 = $_GET["note1"];
$note2 = $_GET["note2"];
$note3 = $_GET["note3"];

$students = student_array($STUDENT_FILE);
$scores = score_array($SCORE_FILE);

update_score_array($scores, $id, $note1, $note2, $note3);
update_student_array($students, $id, $prenom, $nom);

save_array($students, $STUDENT_FILE);
save_array($scores, $SCORE_FILE);
?>
<!DOCTYPE html>
<html lang="fr">

<head>
	<meta charset="utf-8">
	<title>TP 2 - Exo 6</title>
	<meta name="author" content="Marc Gaetano">
	<meta name="viewport" content="width=device-width; initial-scale=1.0">
	<link rel="stylesheet" type="text/css" href="css/tp2.css">
</head>

<body>
	<h1>TP 2 - Exo 6</h1>
	<hr>

	<h2>Modification(s) effectuée(s)</h2>
	<a class="bouton" href="exo6-formulaire.html">Nouvelle recherche</a>
</body>

</html>
