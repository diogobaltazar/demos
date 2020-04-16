node_ctrl = require('./controllers/node')

http = require('http')
fs = require('fs')
express = require('express')
bp = require('body-parser')

app = express()
app.set('view engine', 'ejs')
app.use('/public', express.static('public'))
url_encoded_parser = bp.urlencoded({ extended: false })

// trigger controllers
node_ctrl(app)

app.listen(3000)
console.log(`listenning`)