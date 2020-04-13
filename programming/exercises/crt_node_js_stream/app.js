http = require('http')
fs = require('fs')
http = require('http')




server = http.createServer((req, res) => {
    // res
    res.writeHeader(200, {'Content-Type': 'text/plain'})

    // read the file a chunk at a time until the buffer
    // is fill, and then send the data in the buffer to the
    // variable read_st.
    // createReadStream inherits from eventsEmitter. The
    // createReadStream has an event called 'data' when a new
    // chunk of data arrives at the stream. We can thus handle
    // that event in read_st.
    read_st = fs.createReadStream(`${__dirname}/data.txt`, 'utf-8')


    // write to file in server (with custom event handler)
    write_st = fs.createWriteStream(`${__dirname}/data-out.txt`, 'utf-8')
    read_st.on('data', chunk => {
        console.log(`received chunk with data:\n ${chunk}`)
        write_st.write(chunk)
    })

    // write to client
    read_st.pipe(res)
})

server.listen(port = 3000, host = 'localhost')
console.log(`listenning on ${host}:${port}`)

