import pyaudio
import numpy as np
from PyQt5 import QtCore
from scipy.io import wavfile
from music21 import*

class sound(QtCore.QObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=pyaudio.paInt16,
                                    channels=1,
                                    rate=44100,
                                    output=True)
        self.notes = ''
        self.dictionary_of_drums = self.generate_drums_sounds()
        self.dictionary_of_piano = self.generate_piano_sounds()
        self.dictionary_of_strings = self.generate_guitar_sounds()

    @QtCore.pyqtSlot(str)
    def play_drum(self, key):
        self.stream.write(1*self.dictionary_of_drums[key])

    @QtCore.pyqtSlot(str)
    def play_guitar(self, key):
        self.stream.write(1*self.dictionary_of_strings[key])

    @QtCore.pyqtSlot(str)
    def play_piano(self, key):
        self.stream.write(1*self.dictionary_of_piano[key])
        
    @QtCore.pyqtSlot(str)
    def piano(self,notes):    
        x = instrument.Piano()
        keyNote = note.Note(notes)
        keyNote.duration.quarterLength = 1
        keyNote.volume.velocity = 127 
        output_notes=[]
        output_notes.append(x)
        output_notes.append(keyNote)
        streamNote = stream.Stream(output_notes)
        midi.realtime.StreamPlayer(streamNote).play(playForMilliseconds=50, blocked=False)
        
    @QtCore.pyqtSlot(str)
    def guitar(self,notes):    
        x = instrument.Guitar()
        keyNote = note.Note(notes)
        keyNote.duration.quarterLength = 1
        keyNote.volume.velocity = 127 
        output_notes=[]
        output_notes.append(x)
        output_notes.append(keyNote)
        streamNote = stream.Stream(output_notes)
        midi.realtime.StreamPlayer(streamNote).play(playForMilliseconds=50, blocked=False)
    @QtCore.pyqtSlot(str)   
    def cymbals(self,notes):    
        x = instrument.Cymbals()
        keyNote = note.Note(notes)
        keyNote.duration.quarterLength = 1
        keyNote.volume.velocity = 127 
        output_notes=[]
        output_notes.append(x)
        output_notes.append(keyNote)
        streamNote = stream.Stream(output_notes)
        midi.realtime.StreamPlayer(streamNote).play(playForMilliseconds=50, blocked=False)
    
    @QtCore.pyqtSlot(str)  
    def Bongo(self):
            x = instrument.BongoDrums()
            keyNote = chord.Chord([5.5])
            keyNote.duration.quarterLength = 1
            keyNote.volume.velocity = 127
            output_notes = []
            output_notes.append(x)
            output_notes.append(keyNote)
            streamNote = stream.Stream(output_notes)
            midi.realtime.StreamPlayer(streamNote).play(playForMilliseconds=50, blocked=False)
            
    def generate_piano_sounds(self):
        dictionary_of_piano = {}
        piano_notes = ["C4", "C#", "D4", "D#", "E4",
                       "F4", "F#", "G4", "G#", "A4", "A#", "B4"]
        for note in piano_notes:
            sample_rate, data = wavfile.read(
                f"piano_notes/{note}.wav")
            if data.ndim == 1:
                main_graph_data = (data.tolist())
            else:
                main_graph_data = (data[:, 0].tolist())
            main_graph_data = np.array(main_graph_data)
            main_graph_data = main_graph_data.astype(np.int16)
            dictionary_of_piano[note] = main_graph_data
        return dictionary_of_piano

    def generate_drums_sounds(self):
        dictionary_of_drums = {}
        drums = ["d1", "d2", "d3", "d4"]
        for drum in drums:
            sample_rate, data = wavfile.read( f"drums/{drum}.wav")
            if data.ndim == 1:
                main_graph_data = (data.tolist())
            else:
                main_graph_data = (data[:, 0].tolist())
            main_graph_data = np.array(main_graph_data)
            main_graph_data = main_graph_data.astype(np.int16)
            dictionary_of_drums[drum] = main_graph_data
        return dictionary_of_drums

    def generate_guitar_sounds(self):
        dictionary_of_strings_sounds = {}
        guitar_strings = ["s1", "s2", "s3", "s4", "s5", "s6"]
        for string in guitar_strings:
            sample_rate, data = wavfile.read(
                f"guitar_strings/{string}.wav")
            if data.ndim == 1:
                main_graph_data = (data.tolist())
            else:
                main_graph_data = (data[:, 0].tolist())
            main_graph_data = np.array(main_graph_data)
            main_graph_data = main_graph_data.astype(np.int16)
            dictionary_of_strings_sounds[string] = main_graph_data
        return dictionary_of_strings_sounds
    
    @QtCore.pyqtSlot(np.ndarray)
    def play_modified_sound(self,sound):
        sound = np.array(sound)
        sound = sound.astype(np.int16)
        self.stream = self.audio.open(format=pyaudio.paInt16,
                                      channels=1,
                                      rate=48000,
                                      output=True)
        self.stream.write(1*sound)
