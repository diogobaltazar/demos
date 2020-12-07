function f(){
    setTimeout(_ => console.log('once after 3 seconds'), 3000)
    setInterval(_ => console.log('every 2 seconds'), 2000)
    counter = 0
    interval = setInterval(_ => {
        console.log(`every 2 seconds for the first 6 seconds: ${counter += 2}`)
        if (counter == 6) clearInterval(interval)

    }, 2000)
}


function g(){ console.log(__filename) }

// module.exports.f = f
// module.exports.g = g
module.exports = { f, g }