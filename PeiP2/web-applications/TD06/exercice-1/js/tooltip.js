window.onload = function () {

	// place un message d'erreur comme contenu de l'élément
	// d'id 'tooltip' et rend cet élément visible
	function on_failure(request) {
		let tooltip = document.getElementById('tooltip');
		tooltip.innerHTML = "Erreur : "
			+ request.status + " " + request.statusText;
		tooltip.style.visibility = "visible";
	}

	// place la réponse du serveur (request.responseText)
	// comme contenu de l'élément d'id 'tooltip' et rend
	// cet élément visible
	function on_success(request) {
		let tooltip = document.getElementById('tooltip');
		tooltip.innerHTML = request.responseText;
		tooltip.style.visibility = "visible";
	}

	// supprime le contenu de l'élément d'id 'tooltip'
	// et rend cet élément caché
	function tooltip_hide() {
		let tooltip = document.getElementById('tooltip');
		tooltip.innerHTML = "";
		tooltip.style.visibility = "hidden";
	}

	// effectue la requête Ajax sur le script 'dico.php'
	// avec, comme paramètre 'word', le mot sélectionné
	// sur le double-clic et :
	//   * appelle la fonction 'on_success' en cas de succès
	//   * appelle la fonction 'on_failure' en cas d'échec
	function tooltip_show() {
		let word = window.getSelection().getRangeAt(0);
		simpleAjax('dico.php', 'get', 'word=' + word, on_success, on_failure);
	}

	// ici, il faut créer un nouvel élément 'div' avec
	// l'attribut 'id' ayant pour valeur 'tooltip', et
	// avec l'évènement 'onclick' lié à la fonction
	// 'tooltip_hide', et il faut ajouter ce nouvel élément
	// comme dernier fils de l'élément 'body'
	let tooltip = document.createElement('div');
	tooltip.id = 'tooltip';
	tooltip.style.visibility = 'hidden';
	tooltip.onclick = tooltip_hide;
	document.body.appendChild(tooltip);


	// ici, il faut ajouter l'évènement 'ondblclick' sur
	// l'élément 'body' et le ier à la fonction 'tooltip_show'
	document.body.ondblclick = tooltip_show;
};
