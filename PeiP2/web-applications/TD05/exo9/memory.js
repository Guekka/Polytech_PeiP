// première image cliquée
let first_image = null;
// le nombre total de paires de clics
let clicks_number = 0;
// nombre de paires de clics réussis
let good_clicks_number = 0;
// en attente de timeout
let waiting = false;

class ImageState {
    // Create new instances of the same class as static attributes
    static Hidden = new ImageState("hidden");
    static Revealed = new ImageState("revealed");
    static Selected = new ImageState("selected");

    constructor(name) {
        this.name = name
    }
}

function is_ignored_click(img) {
    if (waiting === true)
        return true;
    if (img === first_image)
        return true;
    if (img.name === img.getAttribute('src')) // relative path
        return true; // already revealed
    return false;
}

function set_state(state, ...imgs) {
    const question_image = "images/question-mark.png";

    for (let img of imgs) {
        if (state === ImageState.Hidden) {
            img.src = question_image;
            img.style.border = "";
        } else if (state === ImageState.Revealed) {
            img.src = img.name;
            img.style.border = "";
        } else if (state === ImageState.Selected) {
            img.src = question_image;
            img.style.border = "2px solid red";
        }
    }
}

function second_click(image1, image2) {
    clicks_number++;
    // Dans tous les cas, on révèle les images
    set_state(ImageState.Revealed, image1, image2);

    if (image1.name === image2.name) {
        good_clicks_number++;
        first_image = null;
    } else {
        waiting = true;
        setTimeout(() => {
            set_state(ImageState.Hidden, image1, image2);
            first_image = null;
            waiting = false;
        }, 1000);
    }
}

function handle_victory() {
    if (good_clicks_number === 8) {
        let display = document.getElementById("result");
        result.innerHTML = "Bravo, vous avez gagné !";
        result.style.visibility = "visible";
    }
}

// gère le clic sur l'image
function click_image() {
    if (is_ignored_click(this))
        return;

    if (first_image === null) {
        first_image = this;
        set_state(ImageState.Selected, this);
        return;
    }

    second_click(first_image, this);
    handle_victory();
}

window.onload = function () {
    imgs = document.getElementById("grid").getElementsByTagName('img');
    for (let img of imgs) {
        img.onclick = click_image;
    }
};
