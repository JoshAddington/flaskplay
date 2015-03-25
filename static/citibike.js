mapboxgl.accessToken = 'pk.eyJ1Ijoiam9zaGFkZGluZ3RvbiIsImEiOiI3YkZxMFJnIn0.iVv6sgsySboP3BaH8KqGbA';
// Create a map in the div #mapbox
var width = 600;
var height = 550;




var map = new mapboxgl.Map({
  container: 'map',
  center: [40.72294999, -73.97100056],
  zoom: 11.8,
  style: 'https://www.mapbox.com/mapbox-gl-styles/styles/basic-v7.json'
});


var svg = d3.select("map").append("svg")
    .attr("width", width)
    .attr("height", height);

  d3.json('/boroughs', function(error, data) {

        console.log(data);

    var projection = d3.geo.mercator()
                                        .center([-73.97100056, 40.72294999])
                                        .scale(90000)
                                        .translate([(width) / 2, (height)/2]);

        var path = d3.geo.path()
                        .projection(projection);

        var g = svg.append("g");

        g.append("g")
                .attr("id", "boroughs")
                .selectAll(".state")
                .data(data.features)
                .enter().append("path")
                .attr("class", function(d){ return d.properties.name; })
                .attr("d", path);

        });
