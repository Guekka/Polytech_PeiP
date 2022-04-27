<?php
// à compléter
// Ce script vérifie les paramètres envoyés par l'utilisateur
// et, si ces paramètres sont corrects, réalise le signup puis
// redirige l'utilisateur vers le script "signin.php",
// sinon, redirige directement l'utilisateur vers le script
// "signin.php" avec le bon message d'erreur en paramètre

// on récupère les paramètres
$login = $_POST['login'];
$password = $_POST['password1'];
$password2 = $_POST['password2'];

// on vérifie que les paramètres sont corrects
// seulement des lettres dans le login
if (!ctype_alpha($login)) {
    header('Location: signup.php?badsignup=1');
    exit;
}
// le login doit être unique
$csv = file('users.csv');
$users = [];
foreach ($csv as $line) {
    $line = explode(',', trim($line));
    $users[$line[0]] = $line[1];
}
if (isset($users[$login])) {
    header('Location: signup.php?badsignup=2');
    exit;
}
// le mot de passe doit contenir 4 caractères minimum
if (strlen($password) < 4) {
    header('Location: signup.php?badsignup=3');
    exit;
}
// les mots de passe doivent être identiques
if ($password != $password2) {
    header('Location: signup.php?badsignup=4');
    exit;
}

// on réalise le signup
$users[$login] = md5($password);

// on écrit les données dans le fichier
function save_array($array, $file)
{
    $csv = "";
    foreach ($array as $id => $pass) {
        $csv .= "$id,$pass\n";
    }
    file_put_contents($file, $csv);
}
save_array($users, 'users.csv');

// on redirige l'utilisateur vers le script "signin.php"
header("Location: signin.php");
