const titleInput = document.querySelector('#id_username');
const slugInput = document.querySelector('#id_slug');

const slugify = (slug) => {
    return slug.toString().toLowerCase().trim()
        .replace(/&/g, '-and-') // replace & with '-and'
        .replace(/[\s\W-]+/g, '-') // replace spaces , non word chars and dashes with single dash
}
const getTitle = (e) => {
    slugInput.setAttribute('value', slugify(titleInput.value));
}
slugify(getTitle);
titleInput.addEventListener('keyup', getTitle);

