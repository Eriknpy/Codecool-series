document.getElementById('submit').addEventListener('click',handleAddShow)

async function handleAddShow(){
    const title = document.getElementById('title')
    const year = document.getElementById('year')
    const rating = document.getElementById('rating')

    const response = await fetch('/api/shows',{
        method: 'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            title: title.value,
            year: year.value,
            rating: rating.value
        }),

    })
    console.log(response)
    const json = await response.json()
    console.log(json)

}
