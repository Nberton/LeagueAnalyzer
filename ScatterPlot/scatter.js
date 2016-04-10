$(function () {



    Highcharts.theme = {
        colors: ['#d73027','#f46d43','#fdae61','#fee08b','#ffffbf','#d9ef8b','#a6d96a','#66bd63','#1a9850'],
        chart: {
            backgroundColor: {
                linearGradient: { x1: 0, y1: 0, x2: 1, y2: 1 },
                stops: [
                    [0, '#2a2a2b'],
                    [1, '#3e3e40']
                ]
            },
        }
    };
    Highcharts.setOptions(Highcharts.theme);

    // Give the points a 3D feel by adding a radial gradient
    Highcharts.getOptions().colors = $.map(Highcharts.getOptions().colors, function (color) {
        return {
            radialGradient: {
                cx: 0.4,
                cy: 0.3,
                r: 0.5
            },
            stops: [
                [0, color],
                [1, Highcharts.Color(color).brighten(-0.2).get('rgb')]
            ]
        };
    });

    var options = {
        chart: {
            renderTo: 'container',
            margin: 100,
            type: 'scatter',
            options3d: {
                enabled: true,
                alpha: 10,
                beta: 30,
                depth: 250,
                viewDistance: 5,
                fitToPlot: false,
                frame: {
                    bottom: { size: 1, color: 'rgba(0,0,0,0.02)' },
                    back: { size: 1, color: 'rgba(0,0,0,0.04)' }
                }
            }
        },
        title: {
            text: 'Draggable box'
        },
        subtitle: {
            text: 'Click and drag the plot area to rotate in space'
        },
        plotOptions: {
            scatter: {
                width: 10,
                height: 10,
                depth: 10,
                radius: 1
            }
        },
        yAxis: {
            min: -1080,
            max: 0,
            //maxPadding: 20,
            tickInterval: 100,
            title: null
        },
        xAxis: {
            min: 0,
            max: null,
            gridLineWidth: 1
        },
        zAxis: {
            min: -1920,
            max: 0,
            tickInterval: 200
        },
        legend: {
            enabled: false
        },
        series: [{
            name: 'Clicks',
            turboThreshold: 0,
            colorByPoint: true,
            data: []
        }]
    };

    // Set up the chart
    //alert(options.series[0].data);
    var chart = new Highcharts.Chart(options);
    var fileName = "";

    $('#gameID').change(function() {
        fileName = $('#gameID').val();
        fileName = fileName + "/mouselogs_parse.txt";
        UpdateGraph();
    });


    function UpdateGraph() {
        $.get(fileName, function (data) {
            //alert(data);
            var lines = data.split('\n');
            var linesJSON = [];
            for (var i in lines) {
                var obj = JSON.parse(lines[i]);
                //console.log(i + obj);
                linesJSON.push(obj);
            }
            //alert(linesJSON);
            chart.series[0].setData(linesJSON);
            //chart.series[0].addPoint({x: 0, y: 0, z: 0, fillColor: "Green"}, true);
            //chart.series[0].addPoint({x: 0, y: -1080, z: 0, fillColor: "Green"}, true);
            //chart.series[0].addPoint({x: 0, y: -1080, z: -1980, fillColor: "Green"}, true);
            //
        });
    }

    // Kept from source code to keep box draggable.
    // Source code from http://www.highcharts.com/demo/3d-scatter-draggable
    // Add mouse events for rotation
    $(chart.container).bind('mousedown.hc touchstart.hc', function (eStart) {
        eStart = chart.pointer.normalize(eStart);

        var posX = eStart.pageX,
            posY = eStart.pageY,
            alpha = chart.options.chart.options3d.alpha,
            beta = chart.options.chart.options3d.beta,
            newAlpha,
            newBeta,
            sensitivity = 5; // lower is more sensitive

        $(document).bind({
            'mousemove.hc touchdrag.hc': function (e) {
                // Run beta
                newBeta = beta + (posX - e.pageX) / sensitivity;
                chart.options.chart.options3d.beta = newBeta;

                // Run alpha
                newAlpha = alpha + (e.pageY - posY) / sensitivity;
                chart.options.chart.options3d.alpha = newAlpha;

                chart.redraw(false);
            },
            'mouseup touchend': function () {
                $(document).unbind('.hc');
            }
        });
    });

});