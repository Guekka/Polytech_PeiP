window.onload = function () {

	// les noms des fichiers images
	var sources = ["paysage-1.jpg", "paysage-2.jpg", "paysage-3.jpg",
		"paysage-4.jpg", "paysage-5.jpg", "paysage-6.jpg",
		"paysage-7.jpg", "paysage-8.jpg", "paysage-9.jpg"];

	// l'indice de l'image actuellement visible
	var indice = 0;

	// affiche l'image suivante
	function next() {
		indice = (indice + 1) % sources.length;
		document.getElementById('show').src = 'images/' + sources[indice];
	}

	// affiche l'image précédente
	function previous() {
		indice = (indice - 1) % sources.length;
		if (indice < 0)
			indice = sources.length - 1
		document.getElementById('show').src = 'images/' + sources[indice];
	}

	// ici, il faut relier le JS à l'évènement "onclick" sur
	// les deux "flèches" (les images)
	let fleches = document.getElementsByClassName('arrow');
	for (let fleche of fleches) {
		var imgName = fleche.getAttribute('src');
		if (imgName == "images/arrow-left.jpg") {
			fleche.onclick = previous;
		}
		else if (imgName == "images/arrow-right.jpg") {
			fleche.onclick = next;
		}
	};
};
