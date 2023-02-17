function main(){
    const card = document.querySelectorAll('#cardTemplate')
    let display_rating = []
    card.forEach((yolo)=>{
        console.log(card)
        yolo.addEventListener('click',(e)=>{
            e.currentTarget.style.backgroundColor = 'red'
            display_rating.push(e.currentTarget.children[1].innerHTML)

            if(display_rating.length == 3){
                let sum = 0
                sum += +display_rating[0]
                sum += +display_rating[1]
                sum += +display_rating[2]
                let result = (Math.round((sum/display_rating.length)*100))/100
                document.getElementById('result').innerHTML = `${result}`
            }
        })

    })
}
main()

async function fetchShowsByYear(){
    const response = await fetch('/api/shows_yearly_rating')
    return await response.json()
}

// function buildCards(card_details){
//     const cardsContainer = document.getElementById('cardsContainer')
//     let cardDiv = "";
//     card_details.then((object)=>{
//         let counter = 0
//         object.map((card)=>{
//             cardDiv += `
//                             <div class="details" id="year" data-id="${counter}">${card.year}</div>
//                             <div class="details" id="rating">${card.rating}</div>
//                             <div class="details" id="showCount">${card.count_shows}shows</div>
//                 `
//             counter++
//         })
//
//         cardsContainer.innerHTML = cardDiv
//     })
// }

// function multiSelect(){
//     console.log('HALÓ')
// }
