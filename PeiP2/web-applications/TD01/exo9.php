<?php

# retourne la chaîne '$s' normalisée
# (toutes les lettres en minuscule sauf la première)
function normalize($s)
{
    $s = strtolower($s);
    $s = ucfirst($s);
    return $s;
}

# Teste si les prénom et nom sont bien renseignés et
# retourne le tableau des messages d'erreurs
# (tableau vide s'il n'y a pas d'erreur)
function check_input()
{
    $errors = array();
    if (empty($_GET['prenom'])) {
        $errors[] = 'Veuillez renseigner votre prénom';
    }
    if (empty($_GET['nom'])) {
        $errors[] = 'Veuillez renseigner votre nom';
    }
    if (empty($_GET['civilite'])) {
        $errors[] = 'Veuillez renseigner votre civilité';
    }
    return $errors;
}

# retourne le code HTML (une chaîne de caractères)
# d'une liste "<ul><li>..</li>..</ul>", les
# éléments de liste contenant les erreurs
# contenues dans le tableau '$errors'
function display_errors($errors)
{
    if (empty($errors)) {
        return '';
    } else {
        $html = '<ul>';
        foreach ($errors as $error) {
            $html .= '<li>' . $error . '</li>';
        }
        $html .= '</ul>';
        return $html;
    }
}

# retourne le code HTML (une chaîne de caractères)
# d'un heading "<h2>...</h2>" contenant le message
# de bienvenu en anglais
function display_welcome($heure, $civilite, $prenom, $nom)
{
    if ($heure < 12) {
        $first = 'Good morning';
    } elseif ($heure < 18) {
        $first = 'Good afternoon';
    } else {
        $first = 'Good evening';
    }

    $second = $civilite;
    $third = normalize($prenom);
    $fourth = normalize($nom);

    $html = '<h2>' . $first . ' ' . $second . ' ' . $third . ' ' . $fourth . '</h2>';
    return $html;
}

?>
<!DOCTYPE html>
<html lang="fr">

<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
	<title>TP 1 - Exo 9</title>
	<meta name="author" content="Marc Gaetano">
	<meta name="viewport" content="width=device-width; initial-scale=1.0">
	<link rel="stylesheet" href="css/tp1.css">
</head>

<body>
	<h1>TP 1 - Exo 9</h1>
	<hr>
	<?php
$errors = check_input();
if (empty($errors)) {
    $heure = date('H');
    echo display_welcome($heure, $_GET['civilite'], $_GET['prenom'], $_GET['nom']);
} else {
    echo display_errors($errors);
}
?>
</body>

</html>
