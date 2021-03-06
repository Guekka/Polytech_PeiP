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
	$moyenne = average($score);
	$tr = "<tr>\n";
	$tr .= "<td>$id</td>\n";
	$tr .= "<td>$prenom</td>\n";
	$tr .= "<td>$nom</td>\n";
	foreach ($score as $note) {
		$tr .= "<td>$note</td>\n";
	}
	$tr .= "<td>$moyenne</td>\n";
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

$STUDENT_FILE = "exo5-6/students.csv";
$SCORE_FILE = "exo5-6/scores.csv";
