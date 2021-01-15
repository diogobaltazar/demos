/**************************************************************************
    Render homepage

*/
module.exports = app => {
    app.get('/', (_, res) => { res.render('index') })
    app.get('/direction', (_, res) => { res.render('direction') })
    app.get('/align_content', (_, res) => { res.render('align_content') })
    app.get('/align_items', (_, res) => { res.render('align_items') })
    app.get('/align_self', (_, res) => { res.render('align_self') })
    app.get('/auto_margins', (_, res) => { res.render('auto_margins') })
    app.get('/fill', (_, res) => { res.render('fill') })
    app.get('/grow_shrink', (_, res) => { res.render('grow_shrink') })
    app.get('/justify_content', (_, res) => { res.render('justify_content') })
    app.get('/order', (_, res) => { res.render('order') })
    app.get('/wrap', (_, res) => { res.render('wrap') })
    app.get('/navbar', (_, res) => { res.render('navbar') })
    app.get('/container', (_, res) => { res.render('container') })
}