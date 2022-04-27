
// le nombre d'essais dans la partie courante
var essais = 0;
// le nombre total d'essais de toutes les parties
var nbEssais = 0;
// le nombre de paties jouées et terminées
var nbParties = 0;
// indique si on est en train de jouer une partie
var partieEnCours = true;
// le nombre à deviner
var secret = generer();
// le nombre d'essais du meilleur jeu
// Number.MAX_SAFE_INTEGER est la plus grande valeur
// entière possible
var meilleurJeu = Number.MAX_SAFE_INTEGER;

// vérifie la proposition de l'utilisateur et :
// - si la proposition est incorrecte, affiche la bonne
//   indication (trop petit ou trop grand)
// - sinon affiche le nombre d'essais qui ont été nécessaires
//   et mets à jour les statistiques
function verifier() {
    var proposition = document.getElementById("proposition").value;
    if (proposition != secret) {
        if (proposition < secret) {
            afficher("Trop petit", "red");
        } else {
            afficher("Trop grand", "red");
        }
    }
    else {
        afficher("Bravo !", "green");
        nbParties++;
        nbEssais += essais;
        if (essais < meilleurJeu) {
            meilleurJeu = essais;
        }
        document.getElementById("question").style.visibility = "visible";
        afficherStat();
    }
    essais++;
}

// si 'encore' est vrai, démarre une nouvelle partie
// sinon termine le jeu en affichant le message adéquat
function jouerEncore(encore) {
    partieEnCours = encore;
    if (encore) {
        essais = 0;
        secret = generer();
        afficher("Nouvel essai", "black");
    }
    else {
        afficher("Fin du jeu", "red");
    }
    document.getElementById("question").style.visibility = "hidden";
}

// affiche un message dans une couleur donnée
// dans l'élément prévu à cet effet
function afficher(message, couleur) {
    let display = document.getElementById("message");
    display.innerHTML = message;
    display.style.color = couleur;
}

// met à jour les statistiques
function afficherStat() {
    function show(id, val) {
        document.getElementById(id).innerHTML = val;
    }

    show("nbParties", nbParties);
    show("nbMoyenEssais", nbEssais / nbParties);
    show("meilleurJeu", meilleurJeu);
}

// retourne un nombre aléatoire dans l'intervalle [1, 100]
function generer() {
    return Math.floor(Math.random() * 100) + 1;
}
