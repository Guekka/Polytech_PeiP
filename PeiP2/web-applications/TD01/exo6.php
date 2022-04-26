<?php

# retourne le code HTML (une chaîne de caractères)
# d'une table '$n'x'$n' représentant un échiquier
# alternant cases blanches et noires
function table($n)
{
    $html = "<table>";
    for ($i = 1; $i <= $n; $i++) {
        $html .= "<tr>";
        for ($j = 1; $j <= $n; $j++) {
            if ($i % 2 == 0) {
                if ($j % 2 == 0) {
                    $html .= "<td class='blanc'>&nbsp;</td>";
                } else {
                    $html .= "<td class='noir'>&nbsp;</td>";
                }
            } else {
                if ($j % 2 == 0) {
                    $html .= "<td class='noir'>&nbsp;</td>";
                } else {
                    $html .= "<td class='blanc'>&nbsp;</td>";
                }
            }
        }
        $html .= "</tr>";
    }
    $html .= "</table>";

    return $html;

}

?>
<!DOCTYPE html>
<html lang="fr">
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
		<title>TP 1 - Exo 6</title>
		<meta name="author" content="Marc Gaetano">
		<meta name="viewport" content="width=device-width; initial-scale=1.0">
		<link rel="stylesheet" href="css/tp1.css">
	</head>
	<body>
		<h1>TP 1 - Exo 6</h1>
		<hr>
		<h2> </h2>
	<?php

# check for parameter "taille" in url
if (isset($_GET['taille'])) {
    echo table($_GET['taille']);
} else {
    echo table(8);
}

?>

	</body>
</html>
