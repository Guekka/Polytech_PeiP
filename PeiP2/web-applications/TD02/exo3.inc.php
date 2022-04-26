<?php
$csv = file("exo2-3/data.csv");
$INFO = [];
foreach ($csv as $line) {
	$line = explode(",", $line);
	$INFO[$line[0]] = $line;
}

// pour comprendre ce que cette fonction doit générer
// regardez le code source HTML du fichier exemple fourni
function makeRadio($info, $name)
{
	$radio = "<div>\n";

	foreach ($info as $value => $array) {
		$radio .= <<<EOD
        <fieldset>
        <input type='radio' name='$name' value='$value'> $array[0]
        </fieldset>
        EOD;
	}

	$radio .= "</div>";
	return $radio;
}

// retourne le nom du pays de clef '$key'
// '$key' est la clef dp nt la valeur est
// l'information dans le tableau associatif '$info'
function getCountryName($key, $info)
{
	return $info[$key][0];
}

// retourne le nom de la capitale de clef '$key'
// '$key' est la clef dp nt la valeur est
// l'information dans le tableau associatif '$info'
function getCapitalName($key, $info)
{
	return $info[$key][2];
}

// retourne l'élément HTML IMG qui est l'image
// du pays de clef '$key'
// '$key' est la clef dp nt la valeur est
// l'information dans le tableau associatif '$info'
function getCountryImage($key, $info)
{
	$pays = $info[$key];
	$name = $pays[0];

	return "<img class='exo2-3' src='exo2-3/$pays[1]' alt='$name' title='$name'>";
}

// retourne l'élément HTML IMG qui est l'image
// de la capitale de clef '$key'
// '$key' est la clef dp nt la valeur est
// l'information dans le tableau associatif '$info'
function getCapitalImage($key, $info)
{
	$pays = $info[$key];
	$name = $pays[2];

	return "<img class='exo2-3' src='exo2-3/$pays[3]' alt='$name' title='$name'>";
}
