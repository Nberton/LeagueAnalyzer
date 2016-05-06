/**
 * Created by Arion on 5/3/16.
 */

var game = 1;
var filename = "../Data/Game" + game + "/Parsed Data/mouseParse - Scatter.txt";

var trace1 = {
    x: [ ],
    y: [ ],
    z: [ ],
    mode: 'markers',
    name: 'Left Click',
    marker: {
        size: 5,
        line: {
            color: 'rgba(217, 217, 217, 0.14)',
            width: 0.5
        },
        opacity: 0.8
    },
    type: 'scatter3d'
};
var trace2 = {
    x: [ ],
    y: [ ],
    z: [ ],
    mode: 'markers',
    name: 'Right Click',
    marker: {
        color: 'rgb(127, 127, 127)',
        size: 5,
        symbol: 'circle',
        line: {
            color: 'rgb(204, 204, 204)',
            width: 1
        },
        opacity: 0.9
    },
    type: 'scatter3d'
};
populateGraph();

function handleFiles() {
    game += 1;
    filename = "../Data/Game" + game + "/Parsed Data/mouseParse - Scatter.txt";

    trace1.x = [ ];
    trace1.y = [ ];
    trace1.z = [ ];

    trace2.x = [ ];
    trace2.y = [ ];
    trace2.z = [ ];

    populateGraph()

    return;
};

function populateGraph() {
    d3.csv(filename, function (data) {
        data.forEach(function (d) {
            d.x = +d.x;
            d.y = +d.y;
            d.z = +d.z;

            if (d.button == 'right') {
                trace1.x.push(-d.x);
                trace1.y.push(d.y);
                trace1.z.push(d.z);
            }
            else {
                trace2.x.push(-d.x);
                trace2.y.push(d.y);
                trace2.z.push(d.z);
            }

        });

        var data = [trace1, trace2];

        var layout = {
            title: '3D Graph of clicks in a game of LoL',
            scene: {
                xaxis: {title: 'X axis in px', mirror: false},
                yaxis: {title: 'Y axis in px', mirror: false},
                zaxis: {title: 'Time in seconds', autorange: "reversed", rangemode: "nonnegative"},
                camera: {
                    up: {x: 0, y: 1, z: 0},
                    center: {x: 0, y: 0, z: 0},
                    eye: {x: .1, y: .1, z: -2}
                },
                //aspectratio: {x: 2, y: 1, z: 2.5}
            }
        };

        Plotly.newPlot('myDiv', data, layout);
    });
}

