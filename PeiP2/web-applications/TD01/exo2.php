<?php

# retourne le nom du jour de la semaine
# correspondant à '$week', le  numéro du
# jour de la semaine (0 -> dimanche, 1 -> lundi, ...)
function jour($week)
{
    switch ($week) {
        case 0:
            return "Dimanche";
            break;
        case 1:
            return "Lundi";
            break;
        case 2:
            return "Mardi";
            break;
        case 3:
            return "Mercredi";
            break;
        case 4:
            return "Jeudi";
            break;
        case 5:
            return "Vendredi";
            break;
        case 6:
            return "Samedi";
            break;

        default:
            return "Erreur";
            break;
    }
}

# retourne le nom du mois correspondant à '$month',
# le  numéro du mois (1 -> janvier, 2 -> février, ...)
function mois($month)
{
    switch ($month) {
        case 1:
            return "Janvier";
            break;
        case 2:
            return "Février";
            break;
        case 3:
            return "Mars";
            break;
        case 4:
            return "Avril";
            break;
        case 5:
            return "Mai";
            break;
        case 6:
            return "Juin";
            break;
        case 7:
            return "Juillet";
            break;
        case 8:
            return "Août";
            break;
        case 9:
            return "Septembre";
            break;
        case 10:
            return "Octobre";
            break;
        case 11:
            return "Novembre";
            break;
        case 12:
            return "Décembre";
            break;
        default:
            return "Erreur";
            break;
    }
}

# print date as day/month

?>
<!DOCTYPE html>
<html lang="fr">
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
		<title>TP 1 - Exo 2</title>
		<meta name="author" content="Marc Gaetano">
		<meta name="viewport" content="width=device-width; initial-scale=1.0">
		<link rel="stylesheet" href="css/tp1.css">
	</head>
	<body>
		<h1>TP 1 - Exo 2</h1>
		<hr>
		<h2>
	<?php
$jour = jour(date("w"));
$mois = mois(date("n"));
$jour_date = date("j");
$annee_date = date("Y");
echo "$jour $jour_date $mois $annee_date";
?>
		</h2>
	</body>
</html>
