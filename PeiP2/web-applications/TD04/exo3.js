"use strict";

var x; // le premier nombre de la multiplication
var y; // le deuxième nombre de la multiplication

// donne le rôle du bouton :
// si 'verifier' est 'true' alors le prochain clic sur le bouton
// est destiné à vérifier la réponse de l'utilisateur, sinon,
// le clic est destiné à proposer une nouvelle multiplication
var verifier = true;

// génére une nouvelle multiplication, autrement dit :
// - génère deux entiers au hasard dans l'intervalle [1,9]
// - les affiche dans les bons éléments HTML
function nouvelle() {
    x = Math.floor(Math.random() * 9) + 1;
    y = Math.floor(Math.random() * 9) + 1;

    function show(id, val) {
        document.getElementById(id).innerHTML = val;
    }

    show("nombre1", x);
    show("nombre2", y);
}

// cette fonction est appelée quand l'utilisateur clique
// sur le bouton. La fonction a deux rôles alternatifs :
// - vérifier que la proposition de l'utilisateur est correcte
// - générer une nouvelle multiplication
// Cette alternance est gérée à l'aide de la variable 'verifier'
function valider() {
    let proposition = document.getElementById("proposition").value;

    let resultat = document.getElementById("resultat");
    let bouton = document.getElementById("bouton");

    if (verifier) {
        resultat.style.visibility = "visible";
        if (proposition == x * y) {
            resultat.innerHTML = "Bravo, vous avez trouvé !";
        } else {
            resultat.innerHTML = "Désolé, la réponse était " + x * y;
        }

        bouton.value = "Continuer";

    } else {
        resultat.style.visibility = "hidden";
        bouton.value = "Vérifier";
        nouvelle();

    }

    verifier = !verifier;
}


