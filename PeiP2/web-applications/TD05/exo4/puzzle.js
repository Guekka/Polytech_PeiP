
window.onload = function () {
	function to_letter(digit) {
		console.assert(digit >= 1 && digit <= 26, "digit must be between 1 and 26");
		return 'abcdefghijklmnopqrstuvwxyz'[digit - 1];
	}

	function get_imgs() {
		return document.getElementById("puzzle").getElementsByTagName('img');
	}

	// pour stocker la première image cliquée
	let first_image;

	// traîte le clic sur une image
	function click_on() {
		if (first_image == null) {
			first_image = this;
			return;
		} if (first_image == this) {
			return;
		}

		// on swap les images
		[this.name, first_image.name] = [first_image.name, this.name];
		[this.src, first_image.src] = [first_image.src, this.src];

		first_image = null;

		if (is_finished()) {
			document.getElementById("result").style.visibility = "visible";
		}

	}

	// teste si le puzzle est terminé
	function is_finished() {
		let imgs = get_imgs();
		for (i = 0; i < imgs.length; i++) {
			if (imgs[i].name != to_letter(i + 1)) {
				return false;
			}
		}
		return true;
	}

	// ici, il faut relier la fonction "clic_on" à l'évènement "onclick"
	// sur toutes les images contenues dans l'élément d'id "puzzle"
	let imgs = get_imgs();
	for (let img of imgs) {
		img.onclick = click_on;
	}
};
