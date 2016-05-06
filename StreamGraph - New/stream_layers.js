/**
 * Created by Arion on 5/5/16.
 */


/* Inspired by Lee Byron's test data generator. */
// function stream_layers(n, m, o) {
//     if (arguments.length < 3) o = 0;
//     function bump(a) {
//         var x = 1 / (.1 + Math.random()),
//             y = 2 * Math.random() - .5,
//             z = 10 / (.1 + Math.random());
//         for (var i = 0; i < m; i++) {
//             var w = (i / m - y) * z;
//             a[i] += x * Math.exp(-w * w);
//         }
//     }
//     var result = d3.range(n).map(function() {
//         var a = [], i;
//         for (i = 0; i < m; i++) a[i] = o + o * Math.random();
//         for (i = 0; i < 5; i++) bump(a);
//         return a.map(stream_index);
//     });
//
//     var stack = d3.layout.stack()
//         .offset("silhouette")
//         .values(function(d) { return d.values; })
//         .x(function(d) { return d.time; })
//         .y(function(d) { return d.actions; });
//
//     var nest = d3.nest()
//         .key(function(d) { return d.game; })
//         .key(function(d) { return d.time; });
//
//     return result;
// }
//
function stream_layers() {
    var games = [ ];
    var gameNest = null;
    d3.csv("collectedAPM.csv", function(data) {
       data.forEach(function(d) {
           d.game = +d.game;
           d.y = +d.actions;
           d.x = +d.time;

           games.push(d);
       });

        //var layers = stack(nest.entries(data));

        var gamelayers = d3.nest()
            .key(function(d) {return d.game })
            .entries(games);
        gameNest = gamelayers.map(function(d) {
            return d.values;
        });
        takeData(gameNest);

    });
}

/* Another layer generator using gamma distributions. */
function stream_waves(n, m) {
    return d3.range(n).map(function(i) {
        return d3.range(m).map(function(j) {
            var x = 20 * j / m - i / 3;
            return 2 * x * Math.exp(-.5 * x);
        }).map(stream_index);
    });
}

function stream_index(d, i) {
    return {x: i, y: Math.max(0, d)};
}