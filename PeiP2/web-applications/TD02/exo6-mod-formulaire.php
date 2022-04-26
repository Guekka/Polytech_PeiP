<?php
include("exo6.inc.php");
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

	<form class="exo6" action="exo6-mod-action.php" method="get">
		<table>
			<tr>
				<th>ID</th>
				<th>Prénom</th>
				<th>Nom</th>
				<th>Trimestre 1</th>
				<th>Trimestre 2</th>
				<th>Trimestre 3</th>
				<th>Moyenne</th>
				<th>Validation</th>
			</tr>
			<?php
			$id = $_GET["id"];
			$students = student_array($STUDENT_FILE);
			$scores = score_array($SCORE_FILE);

			echo form_content($id, $students, $scores);
			?>
		</table>
	</form>
</body>

</html>
