// NON EXECUTABLE 
// TODO improve with visual data
function render_network(selection, props) {

    let { vertices, edges } = props

    
    const SVG_OFFSET_Y = 20
    const SVG_OFFSET_X = 20

    // group with groups of (vertice, text)
    vertices_group = selection.append('g').attr('class', 'vertices_group')
    vertice_group = vertices_group.selectAll("g.vertices_group").data(vertices)
        .enter()
        .append('g')
        .attr('class', 'vertice_group')
        .attr('transform', (_, i) => `translate(${SVG_OFFSET_X + i * 70}, ${SVG_OFFSET_Y})`)
    vertice_group.append('circle')
        .attr('class', 'vertice')
        .attr('r', 10)
        .attr('cx', 0)
        .attr('cy', 0)
    vertice_group.append('text')
        .text(d => d.name)
        .attr('class', 'vertice-text')
        .attr('transform', (_, i) => `translate(0, ${SVG_OFFSET_Y * 2})`)

    // group with groups of (edge, text)
    edges_group = selection.append('g').attr('class', 'edges_group')
    edge_group = edges_group.selectAll("g.edges_group").data(edges)
        .enter()
        .append('g')
        .attr('class', 'edge_group')
        .attr('transform', (_, i) => `translate(${SVG_OFFSET_X + i * 70}, ${SVG_OFFSET_Y * 4})`)
    edge_group.append('line')
        .attr('class', 'edge')
        .attr('x1', 10)
        .attr('y1', 10)
        .attr('x2', 100)
        .attr('y2', 100)
    edge_group.append('text')
        .text(d => `${d.source} - ${d.target}`)
        .attr('class', 'edge-text')
        .attr('transform', (_, i) => `translate(${SVG_OFFSET_X + i * 70}, ${SVG_OFFSET_Y * 6})`)

    // there are 4 data elements and 1 q.vertices_group, so only 3 will be apended
    // selectAll('g') would get all the groups (> data element ), and hence no data elem would be added
    selection.selectAll('g.vertices_group').data(vertices).enter().append('div')

    // select all g whithin the group, so 4
    // inside each of these, select all g, so 0
    // append 4 divs!
    vertices_group.selectAll('g').selectAll('g').data(vertices).enter().append('div')

    // all g in vertices, 1
    // all circle in g, 1
    // added div: 4 - 1
    vertices_group.selectAll('g').selectAll('circle').data(vertices).enter().append('div')

    // selecting all g
    // inside each pof these, select all g
    // bind with data
    // enter div for each data elem, so 4
    // each g.g will have 4 divs
    selection.selectAll('g').selectAll('g').data(vertices).enter().append('div')

    // select all g, 4
    // bind 4 - 4 elems
    vertices_group.selectAll('g').data(vertices).enter().apppend('div')
}