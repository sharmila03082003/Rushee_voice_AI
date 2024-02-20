import pyaudio
import sounddevice as sd
def mic_checking():
    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Get the number of available audio devices
    num_devices = audio.get_device_count()

    # Check if any microphone device is found and enabled
    is_microphone_connected = False
    is_microphone_enabled = False
    for i in range(num_devices):
        device_info = audio.get_device_info_by_index(i)
        if device_info["maxInputChannels"] > 0:
            is_microphone_connected = True
            # Check if the device is enabled using sounddevice
            try:
                with sd.InputStream(device=i):
                    pass
                is_microphone_enabled = True
            except sd.PortAudioError:
                pass
            break
 # Terminate PyAudio
    audio.terminate()
    # Print the microphone connection and enable status
    if is_microphone_connected:
        if is_microphone_enabled:
            #print("Microphone is connected and enabled.")
            return True
        else:
            #print("Microphone is connected but disabled.")
            return False
    else:
        #print("Microphone is not connected.")
        return False
