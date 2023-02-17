function main() {
    const sendButton = document.querySelector('#send')
    sendButton.addEventListener('click', buildUnorderedList)
    starEffect()
}

function getGenre() {
    const genreInput = document.querySelector('#genre').value
    return fetchShowsByGenre(genreInput)
}

async function fetchShowsByGenre(genre) {
    const response = await fetch(`/api/get_genre?genre=${genre}`)
    return await response.json()
}

function buildUnorderedList() {
    const objectData = getGenre()
    let listRow = "";
    objectData.then((data) => {
        data.map((row) => {
            listRow += `<li>${row.title} ${row.starting_date} ${buildStars(row.rating)}</li>`
        })
        document.getElementById('unorderedList').innerHTML = listRow
    })
    function buildStars(rating) {
        const unfilled = 10 - rating
        return `${'<i class="fa-solid fa-star"></i>'.repeat(rating)}${'<i class="fa-regular fa-star"></i>'.repeat(unfilled)}`
    }
}

function starEffect() {
    document.addEventListener("mouseout", function ({target}) {
        if (target.matches('.fa-star')) {
            target.classList.remove('fa-solid');
            target.classList.add('fa-regular');
        }
    }, false);

    document.addEventListener("mouseover", function ({target}) {
        if (target.matches('.fa-star')) {
            addClassToPrevSiblings(target, 'fa-solid');
        }
    }, false);

    function addClassToPrevSiblings(elem, classToAdd) {
        while (elem) {
            if (elem.nodeType === 1) {
                elem.classList.add(classToAdd);
            }
            elem = elem.previousSibling;
        }
    }
}
main()