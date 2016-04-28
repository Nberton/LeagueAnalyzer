d3.csv('test.csv', function(data) {

  var parcoords = d3.parcoords()("#para")
    .data(data)
    .render()
    .createAxes() 
    .alpha(0.35)
    .brushMode("1D-axes")  // enable brushing
  	.reorderable()

});