"use script";

// étant donnée la moyenne 'm'
// retourne l'appréciation correspondante
// (une chaîne de caractères)
/*

    "très insuffisant" si la moyenne est strictement inférieure à 6
    "insuffisant" si la moyenne est supérieure ou égale à 6 et strictement inférieure à 10
    "moyen" si la moyenne est supérieure ou égale à 10 et strictement inférieure à 13
    "bien" si la moyenne est supérieure ou égale à 13 et strictement inférieure à 16
    "très bien" si la moyenne est supérieure ou égale à 16 et strictement inférieure à 19
    "excellent" si la moyenne est supérieure ou égale à 19
*/
function appreciation(m) {
    if (m < 6) {
        return "très insuffisant";
    } if (m < 10) {
        return "insuffisant";
    } if (m < 13) {
        return "moyen";
    } if (m < 16) {
        return "bien";
    } if (m < 19) {
        return "très bien";
    }
    return "excellent";
}

// calcule la moyenne à partir des trois notes
// et affiche la mmoyenne et l'appréciation correspondante
function calculer() {
    let n1 = document.getElementById("note1").value;
    let n2 = document.getElementById("note2").value;
    let n3 = document.getElementById("note3").value;

    // Sanity check
    if (isNaN(n1) || isNaN(n2) || isNaN(n3)) {
        alert("Veuillez saisir des nombres");
        return;
    }

    // Calculate
    let moyenne = (Number(n1) + Number(n2) + Number(n3)) / 3;

    // Show display
    let display = document.getElementById("resultat");
    display.style.visibility = "visible";

    let moyenneDisplay = document.getElementById("moyenne");
    moyenneDisplay.innerHTML = moyenne.toFixed(2);

    let appreciationDisplay = document.getElementById("appreciation");
    appreciationDisplay.innerHTML = appreciation(moyenne);
}
