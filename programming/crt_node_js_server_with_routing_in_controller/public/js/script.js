// f = require('./utils')
// f()

// colors
GOOGLE_BLUE = '#4285F4'
GOOGLE_YELLOW = '#F4B400'
GOOGLE_RED = '#DB4437'
GOOGLE_GREEN = '#0F9D58'

var w = 1000,
    h = 1000,
    node_default_color = d3.rgb(GOOGLE_BLUE),
    fill = [
        node_default_color,
    ]

var nodes = 
    d3
    .range(211,261).map(i => { return {
        id: i,
        in: 0,
        out: 0,
        nature: 'exploratory',  // exp | exec
        type: 'activity',       // activity | story | feature | product
        description: '',
        status: '',
    }});

var vis = 
    d3
    .select("body")
    .append("svg:svg")
    .attr("width", w)
    .attr("height", h);

var links = [
    { source:27, target:28 },
	{ source:28, target:27 },
]

// init links
links.forEach((link, _) => {
  nodes[link.source].out++
  nodes[link.target].in++
})

// force
var force = 
    d3
    .layout.force()
    .charge(-200)       // how far apart the nodes are
    .linkDistance(100)  // default link distance
    .linkStrength(0.1)  // how tight nodes are pulled
    .size([w, h])
    .nodes(nodes)
    .links(links)
    .start()


var link = 
    vis
    .selectAll(".link")
    .data(links)
    .enter()
    .append("line")
    .attr("class", "link")


var node = 
    vis
    .selectAll("circle.node")
    .data(nodes)
    .enter()
    .append("svg:circle")
    .attr("class", "node")
    .attr("cx", d => { return d.x })
    .attr("cy", d => { return d.y })
    .attr("r", 20)
    .style("fill", (d, _) => {
      return fill[ parseInt( ++d.in / 3) ]
    })
    .call(force.drag)

// node
// .append("title")
// .text(d => { return "User " + d.id })

/* Start transition */
vis
.style("opacity", 1e-6)
.transition()
.duration(1000)
.style("opacity", 1)

//Forces in action
force.on("tick", function(e) {
    // Clustering: Push odd/even nodes up/down, something alike for left/right
    // var k = 6 * e.alpha
    // nodes.forEach((o, i) => {
    //     o.y += i & 1 ? k : -k
    //     o.x += i & 2 ? k : -k
    // }) 


    // Get items coords (then whole force's maths managed by D3)

    link
    .attr("x1", d => { return d.source.x })
    .attr("y1", d => { return d.source.y })
    .attr("x2", d => { return d.target.x })
    .attr("y2", d => { return d.target.y })

    node
    .attr("cx", d => { return d.x })
    .attr("cy", d => { return d.y })
})

/*  EVENTS

*/

// rearrange nodes positioning on body double-click
d3
.select("body")
.on("dblclick", _ => {
  nodes.forEach(function(o, _) {
    o.x += (Math.random() - .5) * 200
    o.y += (Math.random() - .5) * 200
  })

  force.resume()
})

// change node color with click
d3
.selectAll('.node')
.on('click', function(d, _) {
    var node = d3.select(this)

    if(node.style("fill") == GOOGLE_YELLOW)
        node.style('fill', GOOGLE_BLUE)

    else
        node.style("fill", GOOGLE_YELLOW)

    d3.event.stopPropagation()
})

// make node static with double click
d3
.selectAll(".node")
.on("dblclick", (d, i) => {
    d.fixed = !d.fixed
    d3.event.stopPropagation()
})

var div = d3.select("div.tooltip")

// shwo label
d3
.selectAll(".node")
.on("mouseover", (d, _) => {

    div
    .style("visibility", "visible")
    .transition()
    .duration(200)
    .style("opacity", .9)
    
    // label styling
    div
    .html(`id ${d.id}<br/>${d.in} in, ${d.in} out<br/>nature: ${d.nature}`)
    .style("left", `${d.x + 15}px`)
    .style("top", `${d.y - 30}px`)
    .style({
        'width': '200px', 
        'height': '50px',
        'border-radius': '1px',
        'background-color': GOOGLE_GREEN,
        'text-align': 'left',
    })

})
.on("mouseout", (d, i) => {
    div
    .transition()
    .duration(500)
    .style("opacity", 0)
    .each("end", _ => div.style("visibility", "hidden"))
})



