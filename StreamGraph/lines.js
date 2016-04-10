/**
 * Created by Arion on 3/14/16.
 */
var colorrange = [];
var margin = {top: 20, right: 40, bottom: 30, left: 30};
var width = document.body.clientWidth - margin.left - margin.right;
var height = 400 - margin.top - margin.bottom;

colorrange = ["#B30000", "#E34A33", "#FC8D59", "#FDBB84", "#FDD49E", "#FEF0D9"];

var x = d3.scale.linear().range([0, width]);
var y = d3.scale.linear().range([height, 0]);
var z = d3.scale.ordinal().range(colorrange);

// Define the axes
var xAxis = d3.svg.axis().scale(x)
    .orient("bottom").ticks(1);

var yAxis = d3.svg.axis().scale(y)
    .orient("left").ticks(1);

var line = d3.svg.line()
    .interpolate("cardinal")
    .x(function (d) { return x(d.time); })
    .y(function (d) { return y(d.actions); });

var color = d3.scale.ordinal()
    .range(colorrange);

var svg = d3.select("body").append("svg")
    .attr("width",  width  + margin.left + margin.right)
    .attr("height", height + margin.top  + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");


d3.csv("collectedAPM.csv", function (data) {
    data.forEach(function(d) {
        d.time = +d.time;
        d.actions = +d.actions;
    });

    x.domain(d3.extent(data, function(d) { return d.time; }));
    y.domain([0, d3.max(data, function(d) { return d.actions; })]);

    var dataNest = d3.nest()
        .key(function(d) {return d.game;})
        .entries(data);

    dataNest.forEach(function(d) {
        svg.append("path")
            .attr("class", "line")
            .attr("d", line(d.values))
            .style("stroke", color(parseInt(d.key)))
            .style("stroke-width", "4px")
            .style("fill", "none");
    });

    // Add the X Axis
    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);

    // Add the Y Axis
    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis);
});