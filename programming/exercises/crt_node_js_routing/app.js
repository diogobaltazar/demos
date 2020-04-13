http = require('http')

server = http.createServer((req, res) => {
    
    if ('/home'.includes(req.url)){
        res.writeHead(statusCode = 200, headers = { 'Content-Type': 'text/html' })
        res.end('200: OK')
    } else {
        res.writeHead(statusCode = 404, headers = { 'Content-Type': 'text/plain' })
        res.end('404: page not found')
    }

})
server.listen(3000, 'localhost')