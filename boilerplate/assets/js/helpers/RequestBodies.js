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