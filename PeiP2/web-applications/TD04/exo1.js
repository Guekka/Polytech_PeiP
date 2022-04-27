
// calcule le prix TTC à partir du prix hors-taxe
// et de la TVA
// affiche une alerte avec un message d'erreur si les
// valeurs fournies ne sont pas des nombres
function prixTTC() {
    let pht = document.getElementById("pht").value;
    let tva = document.getElementById("tva").value;

    if (isNaN(pht) || isNaN(tva)) {
        alert("Veuillez saisir des nombres");
        return;
    }

    let res = pht * (1 + tva / 100);

    let display = document.getElementById("resultat");
    display.style.visibility = "visible";
    let pttc = document.getElementById("pttc");
    pttc.innerHTML = res;
}
