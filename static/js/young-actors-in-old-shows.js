function main(){
    const sendButton = document.querySelector('#send')
    sendButton.addEventListener('click',getActorsByYear)

}
function getActorsByYear(){
    const year = document.querySelector('#year').value
    const objectData = fetchActorsByYear(year)
    objectData.then((data)=>{
        data.map((record)=>{
            console.log(record)
        })
    })

}

async function fetchActorsByYear(year){
    const response = await fetch(`/api/actors_played_in_year?year=${year}`)
    return await response.json()
}

function buildOrderedList(year){


}
main()
