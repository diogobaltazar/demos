
Node = mongoose.model('Node', schema = new mongoose.Schema({
    code: String,
    name: String, 
    nature: String, 
    type: String, 
    description: String, 
    status: String,
    edges_in: [],
    edges_out: [],
}))

module.exports = Node