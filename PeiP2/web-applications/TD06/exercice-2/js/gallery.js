
window.onload = function () {
	// l'élément d'id 'info' qui contient les
	// informations pour un personnage donné
	let info = document.getElementById('info');

	// cette fonction place les données regroupées
	// dans le JSON 'data' dans les éléments adéquats, ainsi
	// que le 'src' comme valeur de l'attribut 'src' de
	// l'image adéquate
	function update(data, src) {
		info.style.visibility = "visible";
		document.getElementById('nom').innerHTML = data.nom;
		document.getElementById('prenom').innerHTML = data.prenom;
		document.getElementById('sexe').innerHTML = data.sexe;
		document.getElementById('age').innerHTML = data.age;
		document.getElementById('activite').innerHTML = data.activite;

		info.getElementsByTagName('img')[0].src = src;
	}

	// cette fonction est appelée lorsqu'on clique sur une image.
	// Elle récupère la valeur de l'attribut 'id' et effectue une
	// requête AJAX au script 'info.php' avec cette valeur en paramètre.
	// Elle mets à jour le contenu des éléments adéquat avec les valeurs
	// retournées par le script.
	function showinfo() {
		let id = this.getAttribute('id');
		let success = (response) => {
			update(JSON.parse(response.response), this.getAttribute('src'));
		}

		simpleAjax('info.php', 'get', 'id=' + id, success);
	}

	// ici, on ajoute l'évènement 'onclick' sur toutes les images
	// et on lie la fonction 'showInfo' à cet évènement
	for (let img of document.getElementsByTagName("img")) {
		img.onclick = showinfo;
	};

	// ici, on ajoute l'évènement 'onclick' sur l'élément
	// d'id 'info' et on lie à cet évènement la fonction
	// qui cache cet élément
	info.onclick = function () {
		info.style.visibility = "hidden";
	};
};
