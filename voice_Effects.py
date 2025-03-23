import numpy as np
from scipy import signal

import math #reverb

def mute(audio_array):
  return np.zeros(len(audio_array))

#Take an audio array and shift it by a % amount
#  just a few percent is normally more than enough
def pitch_shift(audio_array, shift_amount):
  return signal.resample(audio_array, int(len(audio_array) / shift_amount))

#Take audio array and historic audio, generate reverb from history.
def reverb(audio_array, historic_audio, delay_cycles):
  for cycle in range(delay_cycles):
    delay_amplitude = 1 / math.pow(cycle + 1, 1.2) #Exponentially decrease the amplitude of historic audio we're adding over time
    if len(historic_audio) >= cycle: #If we have enough history
      delay_vector_add = historic_audio[len(historic_audio) - cycle - 1] * delay_amplitude
      audio_array = audio_array + delay_vector_add
    else: #If there's not enough history to generate more reverb, just return
      break
  return audio_array