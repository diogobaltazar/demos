http = require('http')
fs = require('fs')
express = require('express')
bp = require('body-parser')

app = express()
app.set('view engine', 'ejs')
app.use('/static', express.static('static'))

url_encoded_parser = bp.urlencoded({ extended: false })

// event handlers on routing
app.get('/', (req, res) => {
    res.render('index')
})
app.get('/node/:ids', (req, res) => {
    // middleware code here
    res.render('node', {ids: req.params.ids.split(',')})
})
app.post('/new', url_encoded_parser, (req, res) => {
    console.log(req.body)
    res.render('success', {data: JSON.stringify(req.body)})
})


app.listen(3000)
console.log(`listenning`)