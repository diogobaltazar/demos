// launch server with `npm app` and make a request with `127.0.0.1:3000`
http = require('http')

// create server and define request response function
server = http.createServer((client_request, server_response) => {

    // response header
    server_response.writeHead(statusCode = 200, headers = { 'Content-Type': 'text/plain' })
    server_response.end(`have received request ${client_request.url}`)
})

// define listenning port
server.listen(port = 3000, host = '127.0.0.1')

console.log(`listenning on ${port}`)