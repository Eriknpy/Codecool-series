async function apiGet(url) {
    let response = await fetch(url, {
        method: "GET",
    });
    if (response.ok) {
        return await response.json();
    }
}

apiGet('/api/top15-shows').then((objectData)=>{
    let tableData = "";
    objectData.map((row)=>{
        tableData += `<tr>
                        <td><a href="">${row.title}</a></td>
                        <td>${row.year}</td>
                        <td style="text-align: center">${row.runtime}</td>
                        <td>${row.rating}</td>
                        <td>${row.genres}</td>
                        <td><a href="${row.trailer}" >${row.trailer}</a></td>
                        <td><a href="${row.homepage}" >${row.homepage}</a></td>
                     </tr>`
        document.querySelector('#tBody').innerHTML = tableData
    })
})

