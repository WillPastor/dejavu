#!/usr/bin/python
import os
import sys
import json
import warnings
import argparse
import dejavu

from argparse import RawTextHelpFormatter
from pydub import AudioSegment


warnings.filterwarnings("ignore")


DEFAULT_RECOGNITION_WAV_FILE = "recognize.this.wav"

WAV_Input = DEFAULT_RECOGNITION_WAV_FILE # Or the arg that may be passed in (once args are implimented)

wavRecSeg=AudioSegment.from_wav(WAV_Input)

#len(wavRecSeg / 1000.0)


for i, chunk in enumerate(wavRecSeg[::2500]):
	with open("samples/sample-%s.wav" % i, "wb") as f:
		#after 3 exported chunks, this loop should include code to compare the average certainty for each outcome, then output the most certain device/signal.    		
		chunk.export(f, format="wav")
		




dejavu.init()



