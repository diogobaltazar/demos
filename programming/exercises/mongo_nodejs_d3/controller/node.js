Node = require('../model/node')

module.exports = app => {
    app.get('/', function(req, res) {
        console.log(`DATA: ${fixtureData}`)
        res.render('index', { data: fixtureData })
      })

    app.get('/all', (req, res) => {

        Node.find({}, (err, data) => {
            if (err) throw err

            res.render('index', {
                data: _.map(
                    data,
                    (whatnot, index) => { return { name: `${index}`, count: Math.floor(Math.random() * 100) }}
                )
            })
        })
    })
}