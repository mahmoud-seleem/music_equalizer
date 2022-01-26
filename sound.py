import pyaudio
import numpy as np
from Guitar import Guitar
from PyQt5 import QtCore
from music21 import instrument, note, stream, midi, chord

class sound(QtCore.QObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.audio = pyaudio.PyAudio()
        self.guitar_instrument = Guitar()
        self.piano_instrument= instrument.Piano()
        self.stream = self.audio.open(format=pyaudio.paInt16,
                                    channels=1,
                                    rate=44100,
                                    output=True)
        self.notes = ''
    @QtCore.pyqtSlot(str)
    def piano(self,notes):
        keyNote = note.Note(notes)
        keyNote.duration.quarterLength = 1
        keyNote.volume.velocity = 127
        output_notes=[]
        output_notes.append(self.piano_instrument)
        output_notes.append(keyNote)
        streamNote = stream.Stream(output_notes)
        print(streamNote)
        print(type(streamNote))
        midi.realtime.StreamPlayer(streamNote).play(playForMilliseconds=50, blocked=False)
        
    # @QtCore.pyqtSlot(str)
    # def guitar(self,notes):    
    #     x = instrument.Guitar()
    #     keyNote = note.Note(notes)
    #     keyNote.duration.quarterLength = 1
    #     keyNote.volume.velocity = 127 
    #     output_notes=[]
    #     output_notes.append(x)
    #     output_notes.append(keyNote)
    #     streamNote = stream.Stream(output_notes)
    #     midi.realtime.StreamPlayer(streamNote).play(playForMilliseconds=50, blocked=False)
    # @QtCore.pyqtSlot(str)   
    # def cymbals(self,notes):    
    #     x = instrument.Cymbals()
    #     keyNote = note.Note(notes)
    #     keyNote.duration.quarterLength = 1
    #     keyNote.volume.velocity = 127 
    #     output_notes=[]
    #     output_notes.append(x)
    #     output_notes.append(keyNote)
    #     streamNote = stream.Stream(output_notes)
    #     midi.realtime.StreamPlayer(streamNote).play(playForMilliseconds=50, blocked=False)
    
    # @QtCore.pyqtSlot(str)  
    # def Bongo(self):
    #         x = instrument.BongoDrums()
    #         keyNote = chord.Chord([5.5])
    #         keyNote.duration.quarterLength = 1
    #         keyNote.volume.velocity = 127
    #         output_notes = []
    #         output_notes.append(x)
    #         output_notes.append(keyNote)
    #         streamNote = stream.Stream(output_notes)
    #         midi.realtime.StreamPlayer(streamNote).play(playForMilliseconds=50, blocked=False)
    # def generate_piano_sounds(self):
    #     dictionary_of_piano = {}
    #     piano_notes = ["C4", "C#", "D4", "D#", "E4",
    #                 "F4", "F#", "G4", "G#", "A4", "A#", "B4"]
    #     for note in piano_notes:
    #         sample_rate, data = wavfile.read(
    #             f"piano_notes/{note}.wav")
    #         if data.ndim == 1:
    #             main_graph_data = (data.tolist())
    #         else:
    #             main_graph_data = (data[:, 0].tolist())
    #         main_graph_data = np.array(main_graph_data)
    #         main_graph_data = main_graph_data.astype(np.int16)
    #         dictionary_of_piano[note] = main_graph_data
    #     return dictionary_of_piano

    # def generate_drums_sounds(self):
    #     dictionary_of_drums = {}
    #     drums = ["d1", "d2", "d3", "d4"]
    #     for drum in drums:
    #         sample_rate, data = wavfile.read( f"drums/{drum}.wav")
    #         if data.ndim == 1:
    #             main_graph_data = (data.tolist())
    #         else:
    #             main_graph_data = (data[:, 0].tolist())
    #         main_graph_data = np.array(main_graph_data)
    #         main_graph_data = main_graph_data.astype(np.int16)
    #         dictionary_of_drums[drum] = main_graph_data
    #     return dictionary_of_drums

    @QtCore.pyqtSlot(str)
    def guitar(self, note):
        self.guitar_instrument.play(note)

    @QtCore.pyqtSlot(int)
    def guitar_multiply_freqs(self, factor):
        print(factor)
        self.guitar_instrument.multiply_freqs(factor)

    @QtCore.pyqtSlot(str)
    def cymbals(self, notes):
        x = instrument.Cymbals()
        keyNote = note.Note(notes)
        keyNote.duration.quarterLength = 1
        keyNote.volume.velocity = 127
        output_notes=[]
        output_notes.append(x)
        output_notes.append(keyNote)
        streamNote = stream.Stream(output_notes)
        midi.realtime.StreamPlayer(streamNote).play(playForMilliseconds=50, blocked=False)

    @QtCore.pyqtSlot(np.ndarray)
    def play_modified_sound(self,sound):
        sound = np.array(sound)
        sound = sound.astype(np.int16)
        self.stream = self.audio.open(format=pyaudio.paInt16,
                                    channels=1,
                                    rate=48000,
                                    output=True)
        self.stream.write(1*sound)
