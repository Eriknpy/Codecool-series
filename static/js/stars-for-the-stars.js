async function gettopten (genre){
    console.log('lajos')
    let formdata = new FormData()
    formdata.append('genre', genre)
    let response = await fetch('/api/genre', {
        method: "POST",
        body: formdata

    })

    return await response.json()
}

document.getElementById('spec-button').addEventListener("click", (e) => {
    e.preventDefault()
    console.log(gettopten("Action"))
    gettopten("Action")
})