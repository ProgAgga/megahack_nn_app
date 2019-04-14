export const ADD_NEW_SOURCE_BODY = (details) => ({
    method: "POST",
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        name: details.name,
        host: details.host,
        port: details.port,
        username: details.username,
        password: details.password,
        type: details.type,
        database: details.database,
    })
});

export const ADD_NEW_OFFER_BODY = (details) =>{
    let options = [];
    Object.entries(details.options).map(elem => {if (elem[1]) options.push(parseInt(elem[0]))});
    let dealers = [];
    Object.entries(details.options).map(elem => {if (elem[1]) dealers.push(parseInt(elem[0]))});
    return {
    method: "POST",
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        name: details.name,
        due_date: details.due_date+"T00:00",
        options: options,
        dealers: dealers
    })

    }

}