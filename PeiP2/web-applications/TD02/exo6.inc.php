<?php

// retiourne une chaîne de caractères identique
// à '$nom' mais avec tous les caractères en
// minuscule et avec la première lettre en majuscule
function normalize($nom)
{
	$nom = strtolower($nom);
	return ucfirst($nom);
}

// lit le fichier '$student_file' et retourne un tableau
// associatif de la forme [ ID => [ PRENOM , NOM ], ... ]
// où ID est l'identifiant, PRENOM le prénom et
// NOM le nom de l'étudiant
function student_array($student_file)
{
	$students = [];
	$csv = file($student_file);
	foreach ($csv as $line) {
		$line = trim($line);
		$line = explode(";", $line);
		$students[$line[0]] = array_slice($line, 1);
	}
	return $students;
}

// lit le fichier '$score_file' et retourne un tableau
// associatif de la forme [ ID => [ NOTE1, NOTE2, NOTE3 ], ... ]
// où ID est l'identifiant, et NOTE1, NOTE2 et NOTE3 les trois
// notes obtenues par l'étudiant
function score_array($score_file)
{
	$scores = [];
	$csv = file($score_file);
	foreach ($csv as $line) {
		$line = explode(";", $line);
		$scores[$line[0]] = array_slice($line, 1);
	}
	return $scores;
}

// retourne la moyenne des valeurs
// contenues dans le tableau '$tabnotes'
function average($tabnotes)
{
	return array_sum($tabnotes) / count($tabnotes);
}

// retourne le TR adéquat qui contient successivement dans
// les sept TD successifs l'identifiant, le prénom, le nom,
// les trois notes et la moyenne de ces notes
function student_score($id, $info, $score)
{
	$prenom = $info[0];
	$nom = $info[1];
	$moyenne = round(average($score), 2);
	$tr = "<tr>\n";
	$tr .= "<td>$id</td>\n";
	$tr .= "<td>$prenom</td>\n";
	$tr .= "<td>$nom</td>\n";
	foreach ($score as $note) {
		$tr .= "<td>$note</td>\n";
	}
	$tr .= "<td>$moyenne</td>\n";
	$tr .= "<td><a href='exo6-mod-formulaire.php?id=$id'>Modifier</a></td>\n";
	$tr .= "</tr>\n";
	return $tr;
}

// retourne les TR adéquats qui contiennent successivement
// les informations des étudiants sélectionnés suivant la
// valeur de '$name' :
// - si '$name' est le prénom de l'étudiant, l'étudiant est sélectionné
// - si '$name' est le nom de l'étudiant, l'étudiant est sélectionné
// - si '$name' est la chaîne vide, l'étudiant est sélectionné
function table_content($name, $students, $scores)
{
	$tr = "";
	foreach ($students as $id => $info) {
		if ($name == "" || $name == $info[0] || $name == $info[1]) {
			$tr .= student_score($id, $info, $scores[$id]);
		}
	}
	return $tr;
}

// retourne le contenu de l'élément HTML FORM
// pour comprendre ce que cette fonction doit générer
// regardez le code source HTML du fichier exemple fourni
function form_content($id, $students, $scores)
{
	$info = $students[$id];

	$prenom = $info[0];
	$nom = $info[1];
	$tr = "<tr>\n";
	$tr .= "<td>$id</td>\n";
	$tr .= "<td><input type='text' name='prenom' value='$prenom'></td>\n";
	$tr .= "<td><input type='text' name='nom' value='$nom'></td>\n";

	$score = $scores[$id];
	for ($i = 0; $i < 3; $i++) {
		$tr .= "<td><input type='number' step='0.01' name='note" . $i + 1 .
			"' value='" . floatval($score[$i]) . "'></td>\n";
	}
	$average = round(average($score), 2);
	$tr .= "<td>$average</td>\n";
	$tr .= "<td><input type='submit' name='submit' value='Valider'></td>\n";
	$tr .= "<td style='display:none;'><input type='hidden' name='id' value='$id'></td>\n";
	$tr .= "</tr>\n";
	return $tr;
}

// sauve le tableau associatif '$array' dans le
// fichier '$file' au format CSV. Le tableau est de
// la forme [ ID => INFO ] où INFO est un tableau de
// valeurs (associatif ou pas)
function save_array($array, $file)
{
	$csv = "";
	foreach ($array as $id => $info) {
		$csv .= $id . ";" . implode(";", $info) . "\n";
	}
	file_put_contents($file, $csv);
}

// modifie le contenu du tableau '$students' en associant les
// valeurs '$firstnme' et '$lastname' aux clefs 'prenom' et 'nom'
// pour la clef '$id'
function update_student_array(&$students, $id, $firstname, $lastname)
{
	$students[$id][0] = $firstname;
	$students[$id][1] = $lastname;
}

// modifie le contenu du tableau '$scores' en associant les
// valeurs '$score1', '$score2' et '$score3' à la clef '$id'
function update_score_array(&$scores, $id, $score1, $score2, $score3)
{
	$scores[$id] = [$score1, $score2, $score3];
}

$STUDENT_FILE = "exo5-6/students.csv";
$SCORE_FILE = "exo5-6/scores.csv";
