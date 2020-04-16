express = require('express')
_ = require('lodash')
app = express()
app.engine('.html', require('ejs').__express)
app.set('views', __dirname)
app.set('view engine', 'html')

// establish a connection to the database
mongoose = require('mongoose')
host = 'localhost'
port = 27017
database = 'node'
user = 'root'
pwd = 'root' // tmp
mongoose.connect(
    `mongodb://${user}:${pwd}@${host}:${port}/${database}`,
    {useUnifiedTopology: true, useNewUrlParser: true},
    (err, client) => {
    if (err){
        console.log(`> could not connect to database`)
        throw err
    }
})

// load model
Node = require('./model/node')

// load POST http request body parser
bp = require('body-parser')
url_encoded_parser = bp.urlencoded({ extended: false })

fixtureData = require('./fixture_data.json')
app.locals.barChartHelper = require('./bar_chart_helper')



// load controller
require('./controller/node')(app)

port = 3001
app.listen(port);
console.log(`listening on port ${port}`)
