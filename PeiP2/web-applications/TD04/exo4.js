"use strict";

function onlyLetters(str) {
    return /^[a-zA-Z]+$/.test(str);
}

// teste si les champs du formulaire sont corrects et :
// - si ils le sont, retourne 'true'
// - sinon, affiche le message d'erreur adéquat dans
//   l'emplacement prévu à cet effet, et retourne 'false'
function checkform() {
    let login = document.getElementById("log").value;
    let pass1 = document.getElementById("pass1").value;
    let pass2 = document.getElementById("pass2").value;

    if (login.length < 3) {
        errormsg("Le login doit comporter au moins 3 caractères");
        return false;
    }
    if (pass1.length < 4) {
        errormsg("Le mot de passe doit comporter au moins 4 caractères");
        return false;
    }
    if (!onlyLetters(login)) {
        errormsg("Le login ne doit contenir que des lettres");
        return false;
    }
    if (!onlyLetters(pass1)) {
        errormsg("Le mot de passe ne doit contenir que des lettres");
        return false;
    }
    if (pass1 !== pass2) {
        errormsg("Les mots de passe ne correspondent pas");
        return false;
    }
    return true;
}

// efface le contenu de l'élément où on affiche
// les messages d'erreur et cache cet élément
function resetform() {
    let display = document.getElementById("erreur");
    display.style.visibility = "hidden";
}

// écrit 'msg' dans l'élément où on affiche
// les messages d'erreur et montre cet élément
function errormsg(msg) {
    let display = document.getElementById("erreur");
    display.style.visibility = "visible";
    display.innerHTML = msg;
}
