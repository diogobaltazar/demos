module.exports = app => {
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
}