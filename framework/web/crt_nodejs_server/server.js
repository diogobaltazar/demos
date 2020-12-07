const http = require('http')
const port = process.env.PORT || 3000 // default
const { app } = require('./app')

server = http.createServer(app)
server.listen(port)