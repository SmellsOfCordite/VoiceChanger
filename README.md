# VoiceChanger
A quick and light way of changing your voice, live.
Uses PyAudio as the workhorse.

Controller (..._Wrapper.py) -> Stream manager (voice_Change.py) -> JSON read/write (JSON...py)

## MVP: I want to sound like a space marine when I play warhammer40 space marine 2.
  For that, I need to:
    - [ ] Get audio streaming working
    - [ ] Add pitch shifting
    - [ ] Add reverb
    - [ ] Add anything else that sounds cool
    - [ ] Route the audio to my/a virtual mic so software can pick it up and use it

## Stretch
 - [ ] JSON config for choosing voice effect packs
   - [ ] JSON reading and writing
   - [ ] Be able to select effect packs to implement while running the voice changer live
   - [ ] Parameterised effect functions in a separate file
   - [ ] Have some component that interprets the JSON and calls the right effect functions with parameters
   - [ ] Create new voice effect options in the sw
