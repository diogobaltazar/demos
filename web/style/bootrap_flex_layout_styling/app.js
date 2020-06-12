const express = require('express')
_ = require('lodash')
app = express()

// set public path
app.use('/public', express.static('public'))

// set views
app.set('view engine', 'ejs')

const main = require('./controllers/main')
main(app)

// run server
app.listen(port = 3002)
console.log(`listenning on 'localhost:${port}`)