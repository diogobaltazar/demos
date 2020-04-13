http = require('http')
fs = require('fs')
express = require('express')

app = express()
app.set('view engine', 'ejs')


app.get('/', (req, res) => {
    res.sendFile(`${__dirname}/index.html`)
})
app.get('/node/:ids', (req, res) => {
    res.render('node', {ids: req.params.ids.split(',')})
})

app.listen(3000)
console.log(`listenning`)