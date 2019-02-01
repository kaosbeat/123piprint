seqNotes =  [];
seqNotesOn =  [];
seqNotesOff =  [];
seqVelocityOn = [];
seqVelocityOff = [];
seqDeltaOn = [];
seqDeltaOff = [];
style = ""
level = ""

function resetSeqs(){
    seqNotes =  [];
    seqNotesOn =  [];
    seqNotesOff =  [];
    seqVelocityOn = [];
    seqVelocityOff = [];
    seqDeltaOn = [];
    seqDeltaOff = [];
}

module.exports = {


    addToSeqs: function (note, velocity, delta) {
        if (velocity != 0) {
            if (delta > 10) {
                resetSeqs();
            }
            seqNotes.push(note);
            seqNotesOn.push(note);
            seqVelocityOn.push(velocity);
            seqDeltaOn.push(delta);
        } else {
            seqNotes.push(note);
            seqNotesOff.push(note);
            seqVelocityOff.push(velocity);
            seqDeltaOff.push(delta);
        }

        // console.log(seqNotes);
    },
    calcStyle: function(){
        if (seqNotesOn.length > 2){
            console.log (seqNotesOn[seqNotesOn.length-1], seqNotesOn[seqNotesOn.length-2])
            if (seqNotesOn[seqNotesOn.length-1] == seqNotesOn[seqNotesOn.length-2]){
                style = "repetetive";
            }
            if (seqNotesOn[seqNotesOn.length-1] - seqNotesOn[seqNotesOn.length-2]  >  4 ){
                style = "extreme";
            }
            if (seqNotesOn[seqNotesOn.length-1] - seqNotesOn[seqNotesOn.length-2]  <=  4 ){
                style = "moderate";
            }
        }
        if (seqNotesOn[seqNotesOn.length-1] < 43) {
            level = "low";
        } else if (seqNotesOn[seqNotesOn.length-1] >= 43 && seqNotesOn[seqNotesOn.length-1] <= 86) {
            level = "medium";
        } else if (seqNotesOn[seqNotesOn.length-1] > 86) {
            level = "high";
        }
        console.log(style, " ", level)
    },
    buildWord: function(note, velocity){
        console.log(note,velocity);
    },
    model: "blah"
  };



