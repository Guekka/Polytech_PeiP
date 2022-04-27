<?php


// Etant donnés la langue ($lang qui vaut "fr", "en" ou "it")
// et la page ($page qui vaut "index", "products" ou "contact")
// cette fonction retourne un tableau associatif contenant tous
// les couples (clef,information) contenus dans le fichier
// correspondant
function get_content($lang, $page)
{
	$csv = file("$lang/$page.txt");
	$content = [];
	foreach ($csv as $line) {
		$line = explode("#", trim($line));
		if ($line[0] == "productlist") // special case
			$line[1] = explode(";", $line[1]);

		$content[$line[0]] = $line[1];
	}
	return $content;
}

// à compléter
// Dans cette partie, il faut
// - démarrer/reprendre une session
// - stocker dans le tableau $_SESSION
//   la langue
// Par défaut, la langue est le français

session_start();
$_SESSION["lang"] = $_GET["lang"] ?? $_SESSION["lang"]  ?? "fr";
