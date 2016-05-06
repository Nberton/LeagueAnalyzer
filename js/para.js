
var colors = d3.scale.category20b();

d3.csv('test.csv', function(data) {

	   //color on champ type
  var colorgen = d3.scale.ordinal()
    .range(["#a6cee3","#1f78b4","#b2df8a","#33a02c",
            "#fb9a99","#e31a1c","#fdbf6f","#ff7f00",
            "#cab2d6","#6a3d9a","#ffff99","#b15928"]);

  var blue_to_brown = d3.scale.linear()
  .domain([0, 170])
  .range(["steelblue", "red"])
  .interpolate(d3.interpolateLab);

  var colorC = function(d) { return colorgen(d.Champion); };
  var colorL = function(d){return colorgen(d.Lane)}
  // function(d) { return blue_to_brown(d['economy (mpg)']);
  var colorU = function(d){return blue_to_brown(d.R);}

  var parcoords = d3.parcoords()("#para")
    .data(data)
    .alpha(0.6) 
    .color(colorC)
    .alphaOnBrushed(0.15)
    .render()
    .createAxes()
    .reorderable()
    .brushMode("1D-axes");  // enable brushing

  $("#champ").click(function(){
     parcoords.color(colorC)
    .render();
  });

  $("#lane").click(function(){
    parcoords.color(colorL)
    .render();
  });

  $("#ult").click(function(){
    parcoords.color(colorU)
    .render();
  });

  d3.selectAll(".parcoords .label").attr("y", -5); //make title sit a little 
  	    // .shadows()
});

$(document).ready(function(){

  var colorgen = d3.scale.ordinal()
    .range(["#a6cee3","#1f78b4","#b2df8a","#33a02c",
            "#fb9a99","#e31a1c","#fdbf6f","#ff7f00",
            "#cab2d6","#6a3d9a","#ffff99","#b15928"]);

  var colorC = function(d) { return colorgen(d.Champion); };


});