var osc =  require("osc"),
    http = require("http"),
    WebSocket = require("ws");




// Create an osc.js UDP Port listening on port 57121.
var udpPort = new osc.UDPPort({
    localAddress: "localhost",
    localPort: 9876,
    metadata: true
});
console.log("listening");


// Listen for incoming OSC bundles.
udpPort.on("message", function (msg, timeTag, info) {
    // console.log("An OSC bundle just arrived for time tag", timeTag, ":", msg);
    // console.log("Remote info is: ", info);
    printScore(80,4,msg.args[0].value,msg.args[1].value,msg.args[2]);
});

// Open the socket.
udpPort.open();



// When the port is read, send an OSC message to, say, SuperCollider
udpPort.on("ready", function () {
    udpPort.send({
        address: "/s_new",
        args: [
            {
                type: "s",
                value: "default"
            },
            {
                type: "i",
                value: 100
            }
        ]
    }, "127.0.0.1", 57110);
});


function printScore(columns, measures, freq, amp, count) {
    console.log(amp);
}



