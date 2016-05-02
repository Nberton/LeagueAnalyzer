
var colors = d3.scale.category20b();

d3.csv('test.csv', function(data) {

	   //color on champ type
  var colorgen = d3.scale.ordinal()
    .range(["#a6cee3","#1f78b4","#b2df8a","#33a02c",
            "#fb9a99","#e31a1c","#fdbf6f","#ff7f00",
            "#cab2d6","#6a3d9a","#ffff99","#b15928"]);

  var color = function(d) { return colorgen(d.Champion); };

  var parcoords = d3.parcoords()("#para")
    .data(data)
    .alpha(0.6) 
    .color(color)
    .alphaOnBrushed(0.15)
    .render()
    .createAxes()
    .reorderable()
    .brushMode("1D-axes")  // enable brushing



  d3.selectAll(".parcoords .label").attr("y", -5); //make title sit a little 
  	    // .shadows()


});