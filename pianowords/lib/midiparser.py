import mido
import musicconcepts as mc

print("getting input ports")
print(mido.get_input_names())

inport = mido.open_input('MidiSport 1x1:MidiSport 1x1 MIDI 1 20:0')
inport.callback = mc.dostuff

