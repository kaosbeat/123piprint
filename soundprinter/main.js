var osc = require("osc");
var midi = require('midi');
var words = require('./words') 
var musicconcepts = require('./musicconcepts')




// var easymidi = require('easymidi');
// var midiparser = require("midiparser");
// var midiin = new midi.input();

// console.log(easymidi.getInputs());
// console.log(easymidi.getOutputs());

// var midiin = new easymidi.Input('Network Session 1');

// var app = require('express')();
const express = require('express')
const app = express()
var server = require('http').Server(app);
var routes = require('./routes');
var io = require('socket.io')(server);
server.listen(80);
app.use(express.json());
app.use("/", express.static(__dirname + "/public"));
app.get('/', routes.index);
app.set('views', __dirname + '/views');
app.set('view engine', 'pug');
// app.get('/users', user.list);
app.get('/start', function (req, res){
	res.json("OK");
	io.sockets.emit('liveviz', {data:100});
});
app.post('/buttondata', function (req, res){
	console.log("received update: "+req);
  // var data = req.body;
  console.log(req.body);
	res.sendStatus(200);
	// io.sockets.emit('liveviz', {value: data});

});

// //midi listener
// // Count the available input ports.
// // console.log("midicount" + midiin.getPortCount() +" " + midiin.getPortName(2));
// midiin.on('noteon', function (msg) {
//   // do something with msg
//   console.log(msg);
// });


var midi = require('midi');

// Set up a new input.
var input = new midi.input();

// Count the available input ports.
input.getPortCount();

// Get the name of a specified input port.
input.getPortName(0);
console.log("midicount" + input.getPortCount() +" " + input.getPortName(1));

// Configure a callback.
input.on('message', function(deltaTime, message) {
  // The message is an array of numbers corresponding to the MIDI bytes:
  //   [status, data1, data2]
  // https://www.cs.cf.ac.uk/Dave/Multimedia/node158.html has some helpful
  // information interpreting the messages.
  console.log('m:' + message + ' d:' + deltaTime);
  // console.log(grammar.flatten('#origin#'));
  musicconcepts.addToSeqs(ParseMIDI(message).note,ParseMIDI(message).velocity, deltaTime );
  musicconcepts.calcStyle();
  // console.log(ParseMIDI(message).note)
});

// Open the first available input port.
input.openPort(1);

///create OSC server
// Create an osc.js UDP Port listening on port 57121.
var udpPort = new osc.UDPPort({
  localAddress: "localhost",
  localPort: 9876,
  metadata: true
});
console.log("listening for OSC");

// Listen for incoming OSC msgs.
udpPort.on("message", function (msg, timeTag, info) {
  console.log("An OSC bundle just arrived for time tag", timeTag, ":", msg);
  console.log("Remote info is: ", info);
  if (msg.address == "/ch1"){
    printScore(80,4,msg.args[0].value,msg.args[1].value,msg.args[2]);
  }
  if (msg.address == "/components"){
    // io.sockets.emit('components', {'c0':msg.args[0].value, 'c1':msg.args[1].value, 'c2':msg.args[2],'c3':msg.args[3].value, 'c4':msg.args[4].value,'c5':msg.args[5]});
    io.sockets.emit('components', {c0:msg.args[0].value, c1:msg.args[1].value, c2:msg.args[2],c3:msg.args[3].value, c4:msg.args[4].value,c5:msg.args[5]});

  } 
});

udpPort.open();


// io.set('log level', 1); // geen socket.io debug info, thx!
io.on('connection', function (socket) {
  socket.emit('news', { hello: 'world' });
  socket.on('my other event', function (data) {
    console.log(data);
  });
});
    




function printScore(columns, measures, freq, amp, count) {
  console.log(amp);
  io.sockets.emit('liveviz', {freq:freq, amp:amp, count:count});
}



function ParseMIDI(msg){   //// from https://github.com/pwhelan/node-midiosc-bridge/blob/master/main.js
		var cmd = msg[0] & 0xf0;
		var chan = (msg[0] & 0x0f) + 1;
		var _msg = {
			command:	cmd,
			channel:	chan,
			parameters:	msg.slice(1)
    };
    //console.log (_msg)
    var _midi = {
      note: function(on, channel) {
        return (on ? 0x90 : 0x80) | ((channel-1) & 0x0f);
      },
      noteOn: function(channel) {
        return 0x90 | ((channel-1) & 0x0f);
      },
      noteOff: function(channel) {
        return 0x80 | ((channel-1) & 0x0f);
      },
      afterTouch: function(channel) {
        return 0xa0 | ((channel-1) & 0x0f);
      },
      continuousController: function(channel) {
        return 0xb0 | ((channel-1) & 0x0f);
      },
      cc: function(channel) {
        return 0xb0 | ((channel-1) & 0x0f);
      },
      patchChange: function(channel) {
        return 0xc0 | ((channel-1) & 0x0f);
      },
      channelPressure: function(channel) {
        return 0xd0 | ((channel-1) & 0x0f);
      },
      pitchBend: function(channel) {
        return 0xe0 | ((channel-1) & 0x0f);
      },
      systemExclusive: function(command) {
        return 0xf0 | (command & 0x0f);
      },
      floatTo7bit: function(value) {
        return (127.0 * value).toFixed(0);
      },
      floatToPitch: function(value) {
        var pitch = 0x3FFF * value;
        var lsb = (pitch & 0x7F);
        var msb = (pitch >> 7);
        
        return {lsb: lsb, msb: msb};
      },
      commandName: function(command) {
        switch(msg.command) {
          case 0x80: return "noteoff";
          case 0x90: return "noteon";
          case 0xa0: return "aftertouch";
          case 0xb0: return "continuouscontroller";
          case 0xc0: return "patchchange";
          case 0xd0: return "channelpressure";
          case 0xe0: return "pitchbend";
          case 0xf0: return "systemexclusive";
        }	
      }
    };
		_msg.commandname = _midi.commandName(_msg.command);
		
		
		switch(_msg.command) {
			case 0x90:
			case 0x80:
				_msg.note = msg[1];
				_msg.velocity = msg[2];
				break;
			case 0xa0:
				_msg.note = msg[1];
				_msg.touch = msg[2];
				break;
			case 0xb0:
				_msg.controller = msg[1];
				_msg.value = msg[2];
				break;
			case 0xc0:
				_msg.patch = msg[1];
				break;
			case 0xd0:
				_msg.pressure = msg[1];
				break;
			case 0xe0:
				_msg.lsb = msg[1];
				_msg.msb = msg[2];
				// TODO: get this working...
				//_midi.pitch = (msg[2] << 7 | msg[1]);
				break;
			case 0xf0:
				// TODO: Sysex/MMC
				break;
		}
		
		try {
			return(_msg);
		}
		catch (err) {
			console.error(err);
		}

  

};



console.log(words.model)
console.log(words.buildWord("3","3"))




////dump all input to the musicconcept input handler

///request current model from musicconcept

///reset musicconcept at some point


