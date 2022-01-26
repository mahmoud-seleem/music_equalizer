from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QFileDialog, QGraphicsView
import sys
from PyQt5.uic.properties import QtCore
from PyQt5.QtCore import pyqtSignal
import numpy as np
from pylab import plot, show, axis
from pyqtgraph import PlotWidget, plot
import pandas as pd
from scipy import signal
import os
import scipy.io.wavfile
# import librosa.display
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtCore import Qt, QUrl
import logging
import pyqtgraph as pg

import matplotlib
from datetime import datetime
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable

matplotlib.use('Qt5Agg')
from PyQt5 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import logging
import math
import wave
import random
from music21 import*


def keyPressEvent(self, event):
        # ===============================================Xylophone=========================#
    def Xylophone(): 
        x = instrument.Xylophone()
        keyNote = note.Note(notes)
        keyNote.duration.quarterLength = 1
        keyNote.volume.velocity = 127 
        output_notes=[]
        output_notes.append(x)
        output_notes.append(keyNote)
        streamNote = stream.Stream(output_notes)
        midi.realtime.StreamPlayer(streamNote).play(playForMilliseconds=50, blocked=False)

    if event.key() == QtCore.Qt.Key_1:
            notes = 'A#'
            Xylophone()
            logging.info('User is playing Xylophone and pressed 1')

    if event.key() == QtCore.Qt.Key_2:
        notes = 'B#'
        Xylophone()
        logging.info('User is playing Xylophone and pressed 2')

    if event.key() == QtCore.Qt.Key_3:
        notes = 'C#'
        Xylophone()
        logging.info('This is information message and pressed 3')

    if event.key() == QtCore.Qt.Key_4:
        notes = 'D#'
        Xylophone()
        logging.info('User is playing Xylophone and pressed 4')

    if event.key() == QtCore.Qt.Key_5:
        notes = 'E#'
        Xylophone()
        logging.info('User is playing Xylophone and pressed 5')

    if event.key() == QtCore.Qt.Key_6:
        notes = 'F#'
        Xylophone()
        logging.info('User is playing Xylophone and pressed 6')

    if event.key() == QtCore.Qt.Key_7:
        notes = 'A3'
        Xylophone()
        logging.info('User is playing Xylophone and pressed 7')

    if event.key() == QtCore.Qt.Key_8:
        notes = 'B3'
        Xylophone()
        logging.info('User is playing Xylophone and pressed 8')
        
    if event.key() == QtCore.Qt.Key_9:
        notes = 'C3'
        Xylophone()
        logging.info('User is playing Xylophone and pressed 9')
        
    if event.key() == QtCore.Qt.Key_0:
        notes = 'D3'
        Xylophone()
        logging.info('User is playing Xylophone and pressed 0')            

            
        # ===============================================Bongo===============================================#
        
    def Bongo():    
        x = instrument.BongoDrums()
        keyNote = note.Note(notes)
        keyNote.duration.quarterLength = 1
        keyNote.volume.velocity = 127 
        output_notes=[]
        output_notes.append(x)
        output_notes.append(keyNote)
        streamNote = stream.Stream(output_notes)
        midi.realtime.StreamPlayer(streamNote).play(playForMilliseconds=50, blocked=False)
        
    if event.key() == QtCore.Qt.Key_B:
        logging.info('User is playing Bongo and pressed B')
        notes = 'A2'
        Bongo()
    if event.key() == QtCore.Qt.Key_N:
        logging.info('User is playing Bongo and pressed N')
        notes = 'E2'
        Bongo()
    
 
        # ===============================================Piano================================================#
    def piano():    
        x = instrument.Piano()
        keyNote = note.Note(notes)
        keyNote.duration.quarterLength = 1
        keyNote.volume.velocity = 127 
        output_notes=[]
        output_notes.append(x)
        output_notes.append(keyNote)
        streamNote = stream.Stream(output_notes)
        midi.realtime.StreamPlayer(streamNote).play(playForMilliseconds=50, blocked=False)
        
            
    if event.key() == QtCore.Qt.Key_Q:
        logging.info('User is playing Flute and pressed Q')
        notes = 'F'
        piano()
    if event.key() == QtCore.Qt.Key_W:
        logging.info('User is playing Flute and pressed W')
        notes = 'G'
        piano()
    if event.key() == QtCore.Qt.Key_E:
        logging.info('User is playing Flute and pressed E')
        notes = 'A'
        piano()
    if event.key() == QtCore.Qt.Key_R:
        logging.info('User is playing Flute and pressed R')
        notes = 'B'
        piano()
    if event.key() == QtCore.Qt.Key_T:
        logging.info('User is playing Flute and pressed T')
        notes = 'C'
        piano()
    if event.key() == QtCore.Qt.Key_Y:
        logging.info('User is playing Flute and pressed W')
        notes = 'D'
        piano()
    if event.key() == QtCore.Qt.Key_I:
        logging.info('User is playing Flute and pressed E')
        notes = 'E'
        piano()
    if event.key() == QtCore.Qt.Key_O:
        logging.info('User is playing Flute and pressed R')
        notes = 'F'
        piano()
    if event.key() == QtCore.Qt.Key_P:
        logging.info('User is playing Flute and pressed T')
        notes = 'G'
        piano()
        
    if event.key() == QtCore.Qt.Key_S:
        logging.info('User is playing Flute and pressed T')
        notes = 'F#'
        piano()                
    if event.key() == QtCore.Qt.Key_D:
        logging.info('User is playing Flute and pressed T')
        notes = 'G#'
        piano()        
    if event.key() == QtCore.Qt.Key_G:
        logging.info('User is playing Flute and pressed T')
        notes = 'A#'
        piano()          
    if event.key() == QtCore.Qt.Key_H:
        logging.info('User is playing Flute and pressed T')
        notes = 'C#'
        piano()          
    if event.key() == QtCore.Qt.Key_J:
        logging.info('User is playing Flute and pressed T')
        notes = 'D#'
        piano()          
    if event.key() == QtCore.Qt.Key_K:
        logging.info('User is playing Flute and pressed T')
        notes = 'F#'
        piano()   
    if event.key() == QtCore.Qt.Key_L:
        logging.info('User is playing Flute and pressed T')
        notes = 'G#'
        piano()      

