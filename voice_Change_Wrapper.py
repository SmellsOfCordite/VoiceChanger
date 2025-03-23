#imports of python libs
import pyaudio #main workhorse for audio stream management
import inquirer #Prettify user input list selection

#imports from this project
import voice_Change
from voice_Change import VoiceChanger as Vc

p = pyaudio.PyAudio()

#Get all audio devices on the user's machine and print them out. Good for debug.
def print_all_devices():
    for i in range(p.get_device_count()):
        print("\n" + str(p.get_device_info_by_index(i)))

#Give user a list of input devices to pick from
def get_input_device():
    #Get the device that the user would like to use as the mic input
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')

    devices = [p.get_device_info_by_host_api_device_index(0, i).get('name') for i in range(0 , numdevices) if p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels') > 0]

    questions = [
      inquirer.List('device',
                    message="Which INPUT device would you like to use?",
                    choices=devices,
                ),
    ]
    answers = inquirer.prompt(questions)
    #print(answers["device"])

    input_device_index = devices.index(answers["device"])
    #print(input_device_index)
    print("Selection: " + str(input_device_index))
    return input_device_index
    
# Give user a list of output devices to choose from    
def get_output_device():
    #output_device_index = p.get_default_output_device_info()
    info = p.get_host_api_info_by_index(2)
    numdevices = info.get('deviceCount')

    devices = [p.get_device_info_by_host_api_device_index(1, i).get('name') for i in range(0 , numdevices) if p.get_device_info_by_host_api_device_index(2, i).get('maxInputChannels') > 0]
    questions = [
      inquirer.List('device',
                    message="Which OUTPUT device would you like to use?",
                    choices=devices,
                ),
    ]
    answers = inquirer.prompt(questions)
    #print(answers["device"])

    output_device_index = devices.index(answers["device"])
    print("Selection: " + str(output_device_index))
    return output_device_index

######################
# MAIN WORKINGS HERE #
######################

#DEbug - List all devices:
#print_all_devices()

#Get user defined IO
input_device_index = get_input_device()
output_device_index = get_output_device() #Not currently using this; pyaudio doesn't seem to like it when I plumb this into the stream .open

# Create a voice changer instance
voice_changer = Vc(input_device_index, output_device_index)

# Start the voice changer
voice_changer.start()