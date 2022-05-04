
window.onload = function () {

	// le "handler" du setTimeout
	let chrono = null;

	// si 'ok' est 'true', alors l'utilisateur
	// a choisi la bonne réponse
	let ok = false;

	// affiche le message 'm' avec la couleur 'c'
	// dans l'élément prévu à cet effet
	function msg(m, c) {
		var mess = document.getElementById("message");
		mess.innerHTML = m;
		mess.style.color = c;
	}

	// cette fonction est appelée à l'issue
	// du setTimeout
	function stop() {
		// on affiche le message
		msg("Vous avez " + (ok ? "bien" : "mal") + " répondu",
			ok ? "green" : "red");


		for (let radio of document.getElementsByName("reponse")) {
			radio.onclick = null;
		}
	}

	// traite le "clic" sur un bouton radio
	function verifier() {
		if (this.getAttribute("data-ok") != null) {
			msg("Bonne réponse", "green");
			ok = true;
		} else {
			msg("Mauvaise réponse", "red");
			ok = false;
		}
	}

	// ici, on lance le setTimeout et stocke
	// le "handler" dans la variable 'chrono'
	chrono = setTimeout(stop, 5000);

	for (let radio of document.getElementsByName("reponse")) {
		radio.onclick = verifier;
	}
};
