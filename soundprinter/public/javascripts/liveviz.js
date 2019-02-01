var socket;
var w = 1920,h = 1080;
var svg;
var svgback;
var params = {
    impact: 10,
    duration: 1000,
    fattyness: 10
};
var deltaX = 0;
var deltaY = 0;
var dataSet1 =[];
var dataSet2 =[];
var datasource = "127.0.0.1"
    // init socket
    socket = io.connect(datasource);


$(function(){
    //init buttons
    var socket = io.connect('http://localhost');
    
    socket.on('news', function (data) {
      console.log(data);
      socket.emit('my other event', { my: 'data' });
    });
    socket.on('liveviz', onSocket);
    socket.on('components', onComponents);
    $('#button').click(function(){
        console.log("clickedy");
        $.post( '/buttondata', JSON.stringify({data:100, moredata:23}));
    });

	// listen to socket
    svgback = d3.select("body").append("svg")
    .attr("width", w)
    .attr("height", h)
    .attr('class','background');

	svg = d3.select("body").append("svg")
    .attr("width", w)
    .attr("height", h)
    .attr('class','foreground')
    .style("pointer-events", "all");

});



function onSocket(data){

    console.log(data.count.value);
    hit = {size:data.amp, ttl:data.freq, posmod:data.count.value%16 } 
    dataSet1.push(hit);
    // if (hit.posmod > 14) {
    //     deltaY = deltaY + 200;
    //     console.log("deltacheck: " + deltaX +" "+ deltaY)
    // }
    addDataPoint(dataSet1);
    if (data.amp > 100){
    dataSet1.push(data);
    addDataPoint(dataSet1);
    // console.log(dataSet1)
    }
    // if (data.amp < 10){
    // //dataSet2.push(data);
    // addCtlOut(data);
    // }
};

function addDataPoint(data){
    //console.log("deltacheck: " + deltaX +" "+ deltaY)
    if (data.posmod > 14) {
        deltaX = 0;
        deltaY = deltaY + 200;
        console.log("deltacheck: " + deltaX +" "+ deltaY)
        }
    if (deltaY > 1080) {
        deltaY = 0;
    }


    svgback.selectAll("circle")
        .data(data)
        .enter()
        .append("circle")
        .attr({
            cx: function(d,i){
                console.log(d);
                return d.posmod*1920/16
                // deltaX = deltaX + d.amp
                // return deltaX;
            },
            cy: function(d){return deltaY + d.ttl/10},
            r: function(d){return d.size/10;},
        })
        .style("stroke", '#000000')
        .style("fill", '#234565')
        .attr("fill-opacity", 0.5)
        .attr("stroke-opacity", 0)
    .transition()
        .duration(params.duration*5)
        .style("stroke", '#000000')
        .attr("fill-opacity", 0)
        .attr("stroke-opacity", 1);

};

function addCtlOut(data){
    svgback.selectAll('rect')
        .data(data)
        .enter()
        .append('rect')
        .attr({
            x: function(d,i){
                deltaX = deltaX + d.delta
                return deltaX*100;
            },
            y: function(d){return deltaY + d.data[2];},
            width: 10,
            height: 10,
        })
        .style("fill", '#234565')

};



function onComponents(data){
    dataSet2.push(data);
    addcomponentdata(dataSet2);
}

function addcomponentdata(data){
    // console.log(data);
    svgback.selectAll("rect")
    .data(data)
    .enter()
    ///rect1
    .append("rect")
    .attr({
        width: function(d){return d.c1.value},
        height: function(d){return d.c1.value},
        x: function(d,i){return i%64*1920/64;},
        y: function(d){return d.c0.value},
    })
    .attr('height', '45')
    .style("stroke", '#000000')
    .style("fill", '#354565')
    .attr("fill-opacity", 0.5)
    .attr("stroke-opacity", 0)
    .append("rect")
    .attr({
        width: function(d){return d.c3.value},
        height: function(d){return d.c3.value},
        x: function(d,i){return i%64*1920/64;},
        y: function(d){return d.c2.value},
    })
    .attr('height', '45')
    .style("stroke", '#000000')
    .style("fill", '#354565')
    .attr("fill-opacity", 0.5)
    .attr("stroke-opacity", 0)
.transition()
    .duration(params.duration*5)
    .style("stroke", '#000000')
    .attr("fill-opacity", 0)
    .attr("stroke-opacity", 1);
}