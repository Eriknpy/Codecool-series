function main(){
    buildTable()
}

async function fetchShowsMoreThan10ep(){
    const response = await fetch('/api/show_details')
    return await response.json()
}

function buildTable(){
    const data = fetchShowsMoreThan10ep()
    let tableBodyRow = "";
    data.then((response)=>{
        response.map((line)=>{
            tableBodyRow += `<tr>
                                <td>${parseHomePage(line.title,line.website)}</td>
                                <td>${line.genres}</td>
                                <td style="text-align: center">${line.number_of_season}</td>
                                <td style="text-align: center">${line.year}</td>
                            </tr>`
        })
        document.getElementById('tableBody').innerHTML = tableBodyRow
    })
    function parseHomePage(title,homepage){
        if(homepage == "No URL"){
            return `${title}`
        }
        else{
            return `<a href="${homepage}">${title}</a>`
        }
    }
}
main()
