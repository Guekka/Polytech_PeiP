
window.onload = function () {

	// affiche le nombre "t" dans le span "spanElt"
	// "t" a au plus deux chiffres
	function afficher(t, spanElt) {
		let children = spanElt.children;
		console.assert(children.length == 2);
		console.assert(t >= 0 && t <= 99);
		let unit = children[0];
		let dec = children[1];
		dec.src = "images/" + t % 10 + ".png";
		unit.src = "images/" + Math.floor(t / 10) + ".png";
	}

	// met à jour les images de l'horloge
	// à chaque seconde
	function tictac() {
		let now = new Date();

		let spans = document.getElementById("horloge").getElementsByTagName("span");
		console.assert(spans.length == 3);
		afficher(now.getHours(), spans[0]);
		afficher(now.getMinutes(), spans[1]);
		afficher(now.getSeconds(), spans[2]);
	}

	// ici, il faut lancer l'horloge
	setInterval(tictac, 500);
};
