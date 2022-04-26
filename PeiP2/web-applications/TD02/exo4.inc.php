<?php

// remplit les tableaux '$day', '$month' et '$lang'
// à partir des informations contenues dans les fichiers
// '*.txt' contenus dans le répertoire '$folderpath'
function fillArrays($folderpath, &$day, &$month, &$lang)
{
    $files = glob("$folderpath/*.csv");
    foreach ($files as $file) {
        $csv = file($file);
        $langue = basename($file, ".csv");
        $day[$langue] = explode(",", $csv[1]);
        $month[$langue] = explode(",", $csv[2]);
        $lang[$langue] = $csv[0];
    }
}

// pour comprendre ce que cette fonction doit générer
// regardez le code source HTML du fichier exemple fourni
function makeRadio($keyvalue, $name)
{
    $radio = "<div>\n";

    foreach ($keyvalue as $value => $lang) {
        $radio .= <<<EOD
        <fieldset>
        <input type='radio' name='$name' value='$value'> $lang
        </fieldset>
        EOD;
    }

    $radio .= "</div>";
    return $radio;
}

// retourne une chaîne de caractères qui donne
// la date dans la langue déterminée par le code '$langue'
function makeDate($langue, $jour, $mois)
{
    $jour_num = date("w");
    $mois_num = date("n");

    $jour_nom = $jour[$langue][$jour_num];
    $mois_nom = $mois[$langue][$mois_num - 1];

    return $jour_nom . " " . date("d") . " " . $mois_nom . " " . date("Y");
}

$LANGUE = [];
$JOUR = [];
$MOIS = [];

fillArrays("exo4", $JOUR, $MOIS, $LANGUE);
