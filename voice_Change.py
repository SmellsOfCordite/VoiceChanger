import pyaudio
import numpy as np
from scipy import signal
import math

import voice_Effects
from voice_Effects import pitch_shift
from voice_Effects import reverb

class VoiceChanger:
    """
    Class to create a voice changer using PyAudio library.

    Attributes:
    - rate: int
        The sampling rate of the audio.
    - chunk_size: int
        The number of audio frames per buffer.
    - stream: pyaudio.Stream
        The audio stream used for recording and playback.
    """

    def __init__(self, input_device_index, output_device_index, rate=44100, chunk_size=1024):
        """
        Constructor to instantiate the VoiceChanger class.

        Parameters:
        - rate: int, optional
            The sampling rate of the audio. Default is 44100.
        - chunk_size: int, optional
            The number of audio frames per buffer. Default is 1024.
        """

        self.rate = rate
        self.chunk_size = chunk_size
        self.stream = None

        self.input_device_index = input_device_index
        self.output_device_index = output_device_index
        self.historic_audio = []
        self.historic_audio_max = 10

    def start(self):
        """
        Starts the voice changer by initializing the PyAudio stream for recording and playback.
        """
        p = pyaudio.PyAudio()

        # Open audio stream for recording and playback
        self.stream = p.open(format=pyaudio.paInt16,
                             channels=2,
                             rate=self.rate,
                             input=True,
                             input_device_index = self.input_device_index,
                             output=True,
                             #output_device_index = self.output_device_index, #Commented out because it breaks everything with a channel error (invalid number of channels)
                             frames_per_buffer=self.chunk_size)

        # Start recording and playback
        print("Applying voice effects.")

        try:
            while True:
                # Read audio data from input stream
                data = self.stream.read(self.chunk_size)

                # Process the audio data (e.g., apply voice changing effects)
                processed_data = self.process_audio(data)

                # Write the processed audio data to output stream
                self.stream.write(processed_data)

        except KeyboardInterrupt:
            # Stop recording and playback
            print("Voice changer stopped.")

        # Close the audio stream
        self.stream.stop_stream()
        self.stream.close()
        p.terminate()

    def process_audio(self, data):
        """
        Process the audio data by applying voice changing effects.

        Parameters:
        - data: bytes
            The audio data to be processed.

        Returns:
        - bytes
            The processed audio data.
        """

        # Convert the audio data to numpy array
        audio_array = np.frombuffer(data, dtype=np.int16)

        # Apply voice changing effects (e.g., pitch shifting, time stretching, etc.)

        #Throw this latest bit of audio into a buffer so we can reference it for effects 
        #The element at [0] is the oldest element
        if len(self.historic_audio) >= self.historic_audio_max: #If buffer is too big, trim it
            del self.historic_audio[0]
        self.historic_audio.append(audio_array)

        audio_array = reverb(audio_array, self.historic_audio, delay_cycles = 5)
        audio_array = pitch_shift(audio_array, shift_amount = 0.98)

        # Convert the processed audio array back to bytes to return
        processed_data = audio_array.astype(np.int16).tobytes()
        return processed_data