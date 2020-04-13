utils = require('./utils/utils')
u = require('util')
e = require('events')


utils.g()
utils.f()

emitter = new e.EventEmitter()
emitter.on('event-name-a', _ => console.log(_))
emitter.emit('event-name-a', 'event-a has emitted!')
emitter.emit('event-name-b', "event-b won't emit because there's no handler for it")

// events on nodes *********************************

Node = function(id, nature, type, description, status, exec_date){ 
    this.id = id
    this.nature = nature
    this.type = type
    this.description = description
    this.status = status
    this.exec_date = exec_date
}
// define events and event handlers on nodes
u.inherits(Node, e.EventEmitter) 

// define nodes
nodes = [
    new Node(1, 'exec', 'product', '', '', []),
    new Node(2, 'exec', 'feature', '', '', []),
    new Node(3, 'exec', 'story', '', '', []),
    new Node(4, 'exec', 'activity', '', '', []),
    new Node(5, 'exec', 'activity', '', '', []),
    new Node(6, 'exec', 'activity', '', '', []),
]
// define nodes get_nature handler
nodes.forEach(node =>
    node.on(
        'get_nature',
        node => console.log(`id: ${node.id}, nature: ${node.nature}`)
))
// trigger event get_nature
nodes.forEach(node => node.emit('get_nature', node))