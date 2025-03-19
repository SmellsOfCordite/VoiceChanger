import numpy as np
from scipy import signal

def pitch_shift(audio_array, shift_amount):
  audio_array = signal.resample(audio_array, int(len(audio_array) / shift_amount))
  return audio_array