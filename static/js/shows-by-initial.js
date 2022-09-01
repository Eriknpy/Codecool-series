function main(){
    const letters = document.querySelectorAll('#letter')
    letters.forEach((letter)=>{
        letter.addEventListener('click',(e)=>{
            const initial = e.currentTarget.innerHTML
            buildTable(fetchShowsByInitial(initial))
        })
    })
}

async function fetchShowsByInitial(letter){
    const response = await fetch(`/api/shows_details_by_initial?letter=${letter}`)
    return await response.json()
}

function buildTable(initial){
    const tableBody = document.querySelector('#tableBody')
    const tableDiv = document.querySelector('#tableDiv')
    initial.then((shows)=>{
        let table = "";
        shows.map((details)=>{

            table +=    `<tr>
                            <td >${details.title}</td>
                            <td>${details.year}</td>
                            <td style="text-align: center">${details.episode_count}</td>
                            <td style="text-align: center">${details.actor_count}</td>
                        </tr>`
        })
        tableDiv.className = 'card'
        tableBody.innerHTML = table
    })

}
main()