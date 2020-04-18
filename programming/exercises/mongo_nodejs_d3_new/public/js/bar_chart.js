var d3 = require('d3')

var barChart = module.exports = () => {

  var data = []

  // defaults
  var width = 400
  var height = 300
  var margin = {
    top: 10,
    right: 10,
    bottom: 40,
    left: 40
  }
  var xAxisLabel = 'Categories'
  var yAxisLabel = 'Count'


  chart = function(container) {

    setDimensions()
    setupXAxis()
    setupYAxis()
    setupBarChartLayout()
    addBackground()
    addXAxisLabel()
    addYAxisLabel()
    addBarChartData()

    var xScale, xAxis, xAxisCssClass, axisLabelMargin, yScale, yAxis, g, bar;

    function setDimensions() {
        axisLabelMargin = 10
    }

    function setupXAxis() {

      xScale =
        d3
        .scale
        .ordinal()
        .domain(_.map(data, 'name'))
        .rangeRoundBands(
            [0, width - axisLabelMargin - margin.left - margin.right],
            0.25
        )
        
    xAxisCssClass = (data.length > 12 && width < 500) ?
        'axis-font-small'
        : ''

      xAxis = 
        d3
        .svg
        .axis()
        .scale(xScale)
        .innerTickSize(0)
        .outerTickSize(0)
        .orient('bottom')

    }

    function setupYAxis() {

      yScale =
        d3
        .scale.linear()
        .domain(
            [0, d3.max(data, d => { return d.count })]
        )
        .range(
            [height - axisLabelMargin - margin.top - margin.bottom, 0]
        )

      yAxis =
        d3
        .svg
        .axis()
        .ticks(5)
        .tickFormat(d3.format('s'))
        .innerTickSize(
            -width + axisLabelMargin + margin.left + margin.right
        )
        .outerTickSize(0)
        .scale(yScale)
        .orient('left')

    }

    function setupBarChartLayout() {

      g =
        container
        .append('svg')
        .attr('class', 'svg-chart')
        .attr('width', width)
        .attr('height', height)
        .append('g')
        .attr(
            'transform',
            `translate(${margin.left}, ${margin.top})`
        )

    }




    function addXAxisLabel() {

        g
        .append('g')
        .attr('class', `x axis ${xAxisCssClass}`)
        .attr(
            'transform', 
            `translate(${axisLabelMargin}, ${
                height - axisLabelMargin - margin.top - margin.bottom
            })xAxisCssClass`
        )
        .call(xAxis)
        .append('text')
        .attr('class', 'axis-label')
        .attr('x', (width - margin.left - margin.right - axisLabelMargin) / 2)
        .attr('y', margin.left)
        .style('text-anchor', 'middle')
        .text(xAxisLabel)

    }




    function addYAxisLabel() {

      g.append('g')
        .attr('class', 'y axis')
        .attr('transform', 'translate(' + axisLabelMargin + ', 0)')
        .call(yAxis)
        .append('text')
        .attr('class', 'axis-label')
        .attr('transform', 'rotate(-90)')
        .attr('y', -margin.left)
        .attr('x', -(height - margin.top - margin.bottom - axisLabelMargin) / 2)
        .style('text-anchor', 'middle')
        .text(yAxisLabel)

    }




    function addBackground() {

      g.append('rect')
        .attr('class', 'background')
        .attr('x', axisLabelMargin)
        .attr('y', -axisLabelMargin)
        .attr('width', width - axisLabelMargin - margin.left - margin.right)
        .attr('height', height - margin.top - margin.bottom)

    }

    function addBarChartData() {

      bar =
        g
        .selectAll('.bar')
        .data(data)
        .enter().append('rect')
        .attr('class', 'bar')
        .attr('x', d => { return xScale(d.name) + axisLabelMargin })
        .attr('y', d => { return yScale(d.count) })
        .attr('width', xScale.rangeBand())
        .attr('height', d => {
            return height - margin.top - margin.bottom - yScale(d.count) - axisLabelMargin
        })
    }


  }




  chart.data = value => {
    if (!arguments.length) return data
    data = value
    return chart
  }

  chart.width = value => {
    if (!arguments.length) return width
    width = value
    return chart
  }

  chart.height = value => {
    if (!arguments.length) return height
    height = value
    return chart
  }

  chart.margin = value => {
    if (!arguments.length) return margin
    margin = value
    return chart
  }

  chart.xAxisLabel = value => {
    if (!arguments.length) return xAxisLabel
    xAxisLabel = value
    return chart
  }

  chart.yAxisLabel = value => {
    if (!arguments.length) return yAxisLabel
    yAxisLabel = value
    return chart
  }

  return chart
}
