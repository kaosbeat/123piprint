var tracery = require('tracery-grammar');



var grammar = tracery.createGrammar({
    'animal': ['panda','fox','capybara','iguana'],
    'emotion': ['sad','happy','angry','jealous'],
    'origin':['I am #emotion.a# #animal#.'],
  });
   
grammar.addModifiers(tracery.baseEngModifiers); 
   
  
module.exports = {
    foo: function () {
      // whatever
    },
    buildWord: function(note, velocity){
        console.log(note,velocity);
    },
    model: grammar
  };



  



