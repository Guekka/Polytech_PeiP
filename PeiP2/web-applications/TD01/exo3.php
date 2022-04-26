<?php

# retourne le code HTML (une chaîne de caractères)
# d'une table contenant les diviseurs de '$N'
# (une seule ligne, autant de colonnes que de diviseurs)
function diviseurs($N)
{
    $html = "<table><tr>";
    for ($i = 1; $i <= $N; $i++) {
        if ($N % $i == 0) {
            $html .= "<td>$i</td>";
        }
    }
    $html .= "</tr>";
    $html .= "</table>";

    return $html;
}

?>
<!DOCTYPE html>
<html lang="fr">
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
		<title>TP 1 - Exo 3</title>
		<meta name="author" content="LP IMApp">
		<meta name="viewport" content="width=device-width; initial-scale=1.0">
		<link rel="stylesheet" href="css/tp1.css">
	</head>
	<body>
		<h1>TP 1 - Exo 3</h1>
		<hr>
		<h2>

		<?php
print "Les diviseurs de " . $_GET['n'] . " sont :" . diviseurs($_GET['n']);
?>
	</h2>
	</body>
</html>
