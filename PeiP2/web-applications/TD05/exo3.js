
window.onload = function () {

	function show() {
		document.getElementById("realsize").src = this.src;
		document.getElementById("legend").innerHTML = this.title;

	}

	// ici, il faut relier la fonction "show" à l'évènement "onmouseover"
	// sur toutes les images ayant la classe "miniature"
	let mins = document.getElementsByClassName('miniature');
	for (let min of mins) {
		min.onmouseover = show;
	}

};
