<?php
session_start();
// à compléter
// Dans cette partie, on teste le login et le mot de passe :
// - on teste si le login proposé existe bien
// - on teste si le mot de passe correspond
// En cas de succès :
// - si le paramètre "goto" existe, on redirige l'utilisateur vers le script
//   qui est la valeur de ce paramètre
// - sinon on redirige l'utilisateur vers "page1.php"
// En cas d'échec, on redirige l'utilisateur vers la page de login

$csv = file('users.csv');
$users = [];
foreach ($csv as $line) {
	$line = explode(',', trim($line));
	$users[$line[0]] = $line[1];
}

$login = $_POST['login'];
$password = md5($_POST['password']);

if (isset($users[$login]) && $users[$login] == $password) {
	$_SESSION['login'] = $login;
	$goto = $_GET['goto'] ?? 'page1.php';
} else {
	$goto = $_GET["goto"] ?? "";
	$goto = "signin.php?" . http_build_query(['goto' => $goto, 'badlogin' => true]);
}
header("Location: $goto");
