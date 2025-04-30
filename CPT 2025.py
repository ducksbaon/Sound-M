import streamlit as st
import sounddevice as sd
import soundfile as sf
import numpy as np
from PIL import Image 
from scipy.signal import resample
import os
file_path = os.path.join("assets", "quack.mp3")  # Example for organizing files in an "assets" folder
#importing dependencies



#initialize session state for sound_chosen. Streamlit re-runs the script on every interaction,
#so the sound_chosen variable is reset to "None" each time unless it is stored in a persistent state.
if "sound_chosen" not in st.session_state:
    st.session_state.sound_chosen = "None"
# Default sample rate
samplerate = 44100  


#functions for sounds to play and manipulate audio
def play_sound(file_path):
    try:
        data, samplerate = sf.read(file_path)  # Ensure the sound file is in the same directory
        sd.play(data, samplerate)
        sd.wait()  # Wait until the sound finishes playing
    except Exception as e:
        st.error("Error playing sound: {e}")


#----------------------------------------------------------------------------------------------------------

#duck

def decrease_samplerate():
    if st.session_state.sound_chosen == "duck":
        try:
            # Read the audio file
            data, samplerate = sf.read("quack.mp3")

            # Calculate the number of samples for the target sample rate
            target_samplerate = int(samplerate * 0.5)  # Quadrisect the sample rate
            num_samples = int(len(data) * target_samplerate / samplerate)

            # Resample the audio data
            resampled_data = resample(data, num_samples)

            # Play the resampled audio
            sd.play(resampled_data, target_samplerate)
            sd.wait()

            st.success(f"Played sound at reduced sample rate: {target_samplerate} Hz")
        except Exception as e:
            st.error(f"Error playing sound: {e}")

#clap
    if st.session_state.sound_chosen == "clap":
        try:
            # Read the audio file
            data, samplerate = sf.read("cheering.mp3")

            # Calculate the number of samples for the target sample rate
            target_samplerate = int(samplerate * 0.5)  # Quadrisect the sample rate
            num_samples = int(len(data) * target_samplerate / samplerate)

            # Resample the audio data
            resampled_data = resample(data, num_samples)

            # Play the resampled audio
            sd.play(resampled_data, target_samplerate)
            sd.wait()

            st.success(f"Played sound at reduced sample rate: {target_samplerate} Hz")
        except Exception as e:
            st.error(f"Error playing sound: {e}")

#sax
    if st.session_state.sound_chosen == "sax":
        try:
            # Read the audio file
            data, samplerate = sf.read("sax.mp3")

            # Calculate the number of samples for the target sample rate
            target_samplerate = int(samplerate * 0.5)  # Quadrisect the sample rate
            num_samples = int(len(data) * target_samplerate / samplerate)

            # Resample the audio data
            resampled_data = resample(data, num_samples)

            # Play the resampled audio
            sd.play(resampled_data, target_samplerate)
            sd.wait()

            st.success(f"Played sound at reduced sample rate: {target_samplerate} Hz")
        except Exception as e:
            st.error(f"Error playing sound: {e}")


#----------------------------------------------------------------------------------------------------------

#duck

def decrease2_samplerate():
    if st.session_state.sound_chosen == "duck":
        try:
            # Read the audio file
            data, samplerate = sf.read("quack.mp3")

            # Calculate the number of samples for the target sample rate
            target_samplerate = int(samplerate * 0.25)  # Quadrisect the sample rate
            num_samples = int(len(data) * target_samplerate / samplerate)

            # Resample the audio data
            resampled_data = resample(data, num_samples)

            # Play the resampled audio
            sd.play(resampled_data, target_samplerate)
            sd.wait()

            st.success(f"Played sound at reduced sample rate: {target_samplerate} Hz")
        except Exception as e:
            st.error(f"Error playing sound: {e}")

#clap
    if st.session_state.sound_chosen == "clap":
        try:
            # Read the audio file
            data, samplerate = sf.read("cheering.mp3")

            # Calculate the number of samples for the target sample rate
            target_samplerate = int(samplerate * 0.25)  # Quadrisect the sample rate
            num_samples = int(len(data) * target_samplerate / samplerate)

            # Resample the audio data
            resampled_data = resample(data, num_samples)

            # Play the resampled audio
            sd.play(resampled_data, target_samplerate)
            sd.wait()

            st.success(f"Played sound at reduced sample rate: {target_samplerate} Hz")
        except Exception as e:
            st.error(f"Error playing sound: {e}")

#sax
    if st.session_state.sound_chosen == "sax":
        try:
            # Read the audio file
            data, samplerate = sf.read("sax.mp3")

            # Calculate the number of samples for the target sample rate
            target_samplerate = int(samplerate * 0.25)  # Quadrisect the sample rate
            num_samples = int(len(data) * target_samplerate / samplerate)

            # Resample the audio data
            resampled_data = resample(data, num_samples)

            # Play the resampled audio
            sd.play(resampled_data, target_samplerate)
            sd.wait()

            st.success(f"Played sound at reduced sample rate: {target_samplerate} Hz")
        except Exception as e:
            st.error(f"Error playing sound: {e}")

#----------------------------------------------------------------------------------------------------------

#duck

def decrease3_samplerate():
    if st.session_state.sound_chosen == "duck":
        try:
            # Read the audio file
            data, samplerate = sf.read("quack.mp3")

            # Calculate the number of samples for the target sample rate
            target_samplerate = int(samplerate * 0.125)  # Quadrisect the sample rate
            num_samples = int(len(data) * target_samplerate / samplerate)

            # Resample the audio data
            resampled_data = resample(data, num_samples)

            # Play the resampled audio
            sd.play(resampled_data, target_samplerate)
            sd.wait()

            st.success(f"Played sound at reduced sample rate: {target_samplerate} Hz")
        except Exception as e:
            st.error(f"Error playing sound: {e}")

#clap
    if st.session_state.sound_chosen == "clap":
        try:
            # Read the audio file
            data, samplerate = sf.read("cheering.mp3")

            # Calculate the number of samples for the target sample rate
            target_samplerate = int(samplerate * 0.125)  # Quadrisect the sample rate
            num_samples = int(len(data) * target_samplerate / samplerate)

            # Resample the audio data
            resampled_data = resample(data, num_samples)

            # Play the resampled audio
            sd.play(resampled_data, target_samplerate)
            sd.wait()

            st.success(f"Played sound at reduced sample rate: {target_samplerate} Hz")
        except Exception as e:
            st.error(f"Error playing sound: {e}")

#sax
    if st.session_state.sound_chosen == "sax":
        try:
            # Read the audio file
            data, samplerate = sf.read("sax.mp3")

            # Calculate the number of samples for the target sample rate
            target_samplerate = int(samplerate * 0.125)  # Quadrisect the sample rate
            num_samples = int(len(data) * target_samplerate / samplerate)

            # Resample the audio data
            resampled_data = resample(data, num_samples)

            # Play the resampled audio
            sd.play(resampled_data, target_samplerate)
            sd.wait()

            st.success(f"Played sound at reduced sample rate: {target_samplerate} Hz")
        except Exception as e:
            st.error(f"Error playing sound: {e}")

#----------------------------------------------------------------------------------------------------------

#bit depth functions

def bit_depth():

    #duck
    try:
        if st.session_state.sound_chosen == "duck":
            data, samplerate = sf.read("quack.mp3")
            
            if data.dtype == np.float32:
                max_val = 2 ** 15 - 1 # Maximum value for 16-bit audio
                data = np.clip(data * max_val, -max_val, max_val).astype(np.int16)
            # set audio data in the range of bit depth
            
            sd.play(data, samplerate)
            sd.wait()

            st.success("Played sound at 16-bit depth")
    except Exception as e:
        st.error(f"Error processing audio: {e}")   

    #clap
    try:
        if st.session_state.sound_chosen == "clap":
            data, samplerate = sf.read("cheering.mp3")
            
            if data.dtype == np.float32:
                max_val = 2 ** 15 - 1 # Maximum value for 16-bit audio
                data = np.clip(data * max_val, -max_val, max_val).astype(np.int16)
            # set audio data in the range of bit depth
            
            sd.play(data, samplerate)
            sd.wait()

            st.success("Played sound at 16-bit depth")
    except Exception as e:
        st.error(f"Error processing audio: {e}")  
    #sax
    try:
        if st.session_state.sound_chosen == "sax":
            data, samplerate = sf.read("sax.mp3")
            
            if data.dtype == np.float32:
                max_val = 2 ** 15 - 1 # Maximum value for 16-bit audio
                data = np.clip(data * max_val, -max_val, max_val).astype(np.int16)
            # set audio data in the range of bit depth
            
            sd.play(data, samplerate)
            sd.wait()

            st.success("Played sound at 16-bit depth")
    except Exception as e:
        st.error(f"Error processing audio: {e}")  

#----------------------------------------------------------------------------------------------------------

def bit_depth2():
    try:
        if st.session_state.sound_chosen:
            # Map sound file based on the chosen sound
            file_map = {
                "duck": "quack.mp3",
                "clap": "cheering.mp3",
                "sax": "sax.mp3"
            }
            file_path = file_map.get(st.session_state.sound_chosen)

            # Read the audio file
            data, samplerate = sf.read(file_path)

            # Check if the data is in float32 format
            if data.dtype == np.float32:
                max_val = 2 ** 7 - 1  # Maximum value for 8-bit audio
                # Scale and quantize to 8-bit
                data = np.clip(data * max_val, -max_val, max_val).astype(np.int8)
                # Add quantization noise
                data = data + np.random.randint(-1, 2, size=data.shape, dtype=np.int8)
                # Scale back to float32 for playback
                data = data / max_val

            # Play the quantized audio
            sd.play(data, samplerate)
            sd.wait()

            st.success("Played sound at 8-bit depth")
        else:
            st.warning("Please select a sound to apply bit depth changes.")
    except Exception as e:
        st.error(f"Error processing audio: {e}")

#-----------------------------------------------------------------------------------------------------------

def bit_depth3():

    #duck
    try:
        if st.session_state.sound_chosen == "duck":
            data, samplerate = sf.read("quack.mp3")
            
            if data.dtype == np.float32:
                max_val = 2 ** 4 - 1  # Maximum value for unsigned 4-bit (15)
                data = np.clip((data + 1.0) * (max_val / 2), 0, max_val)  # Scale to [0, 15]
                data = np.round(data).astype(np.int8)  # Quantize and store in int8
                data = (data / (max_val / 2)) - 1.0  # Normalize back to [-1.0, 1.0]
            
            sd.play(data, samplerate)
            sd.wait()

            st.success("Played sound at 4-bit depth")
    except Exception as e:
        st.error(f"Error processing audio: {e}")   

    #clap
    try:
        if st.session_state.sound_chosen == "clap":
            data, samplerate = sf.read("cheering.mp3")
            
            if data.dtype == np.float32:
                max_val = 2 ** 4 - 1  # Maximum value for unsigned 4-bit (15)
                data = np.clip((data + 1.0) * (max_val / 2), 0, max_val)  # Scale to [0, 15]
                data = np.round(data).astype(np.int8)  # Quantize and store in int8
                data = (data / (max_val / 2)) - 1.0  # Normalize back to [-1.0, 1.0]
            
            sd.play(data, samplerate)
            sd.wait()

            st.success("Played sound at 4-bit depth")
    except Exception as e:
        st.error(f"Error processing audio: {e}")  
    #sax
    try:
        if st.session_state.sound_chosen == "sax":
            data, samplerate = sf.read("sax.mp3")
            
            if data.dtype == np.float32:
                max_val = 2 ** 4 - 1  # Maximum value for unsigned 4-bit (15)
                data = np.clip((data + 1.0) * (max_val / 2), 0, max_val)  # Scale to [0, 15]
                data = np.round(data).astype(np.int8)  # Quantize and store in int8
                data = (data / (max_val / 2)) - 1.0  # Normalize back to [-1.0, 1.0]
            
            sd.play(data, samplerate)
            sd.wait()

            st.success("Played sound at 4-bit depth")
    except Exception as e:
        st.error(f"Error processing audio: {e}")
#-----------------------------------------------------------------------------------------------------------

#list for sampling rates to be used in the buttons

sampling_rates = [
    {"label": "Decrease to 22050 Hz", "function": decrease_samplerate},
    {"label": "Decrease to 11025 Hz", "function": decrease2_samplerate},
    {"label": "Decrease to 5512 Hz", "function": decrease3_samplerate}
]

bit_depth = [
    {"label": "16-bit", "function": bit_depth},
    {"label": "8-bit", "function": bit_depth2},
    {"label": "4-bit", "function": bit_depth3}
]

#-----------------------------------------------------------------------------------------------------------


#Title, explaining sound manipulation

st.title("Basics of Sound Manipulation")

st.write("Turn on Audio!", icon="🔊")

st.write("This is a demonstration of how sound manipulation works within digital audio. There are many different ways that sound can be manipulated for different effects and purposes, and in these examples, we will be focus on sample rate and audio bit depth. ")


#if statements for clicking the buttons
left, middle, right = st.columns(3)
if left.button("Cheering", icon="👏", use_container_width=True):
    left.markdown("Cheering Sound Effect")
    st.session_state.sound_chosen = "clap"
    play_sound("cheering.mp3")

if middle.button("Quack", icon="🦆", use_container_width=True):
    middle.markdown("Duck Sound Effect")
    st.session_state.sound_chosen = "duck"
    play_sound("quack.mp3")

if right.button("Saxophone Lick", icon="🎷", use_container_width=True):
    right.markdown("Sax Lick")
    st.session_state.sound_chosen = "sax"
    play_sound("sax.mp3")

#-----------------------------------------------------------------------------------------------------------

#subtitle to divide buttons to play sound and manipulate sampling rate buttons

st.subheader("_Sampling Rate Buttons_", divider="gray")
st.write("Changing the sample rate of audio is one of the most commonly used techniques in sound manipulation. The sample rate is the number of samples taken per second of audio waveforms to create digital signals. Specifically, the sample rate represents the highest possible frequency that can be played.")
st.write("The following buttons will manipulate the sampling rate of one of the sounds. First, click on one of the sounds, then click on the sampling rate you want to decrease to. The default sound you are hearing is 44.1 kHz, and these buttons go down by half each time.")

# Buttons to manipulate sampling rates
for rate in sampling_rates:
    if st.button(rate["label"], use_container_width=True):
        st.markdown("Converting audio...")
        rate["function"]()

st.write("As you can hear, the lower the sampling rate, the lower the audio quality becomes.")
st.write("You might think that this is directly correlated to the number passed, and how often the audio is read. However, it more relies on what I explained above. The sample rate "
"takes into account the highest frequency that can be processed within a file. However, whenever that threshold is higher than what audio is given, it misinterprets it as lower signals and starts to produce that fuzzy sound, known as aliasing.")
st.image("soundgraph.png")
st.write("_Each line represents a different sample rate, and how they cut into the overall given sound._")
st.write("Lower sample rates are used to cut down on file space. A good example of when you use a lower sample rate would be with the duck sound, as there is not a major difference in sound between all three sample rates.")
st.write("Overall, however, the sounds don't have any noticable distorion with 22050 kHz, so that would be best to use if you were to use all 3 sound files.")

#-----------------------------------------------------------------------------------------------------------

#subtitle to divide buttons for bit depth

st.subheader("_Bit Depth Buttons_", divider="gray")
st.write("Bit depth is another way that audio can be manipulated. The bit depth is the amount of discrete amplitude values that are available per sample. Again, however - the bit depth ties into a specific reason as to why it changes sound quality, as it determines the noise floor of your sound.")
st.write("Unfortunately, the audio given in the examples cannot be manipulated, as they have to small of dynamic contrast. Maybe you can try hearing the differences in the buttons, but I certainly can't...")

#buttons to manipulate bit depth
for rate in bit_depth:
    if st.button(rate["label"], use_container_width=True):
        st.markdown("Converting audio...")
        rate["function"]()

st.write("Anyways, bit depth is the amount of bits that are used to represent each sample. The higher the bit depth, the more signals you can have. However, when you have lower signals than what your audio calls for, the audio waves will push them to the max / min of their range. This causes a fuzzy noise and noise distortion. The process of this is known as quantization.")
st.write("The range of bit depth is calculated by 2^b, where b is the bit depth. For instance, 2^16 is 65,536, which makes the minimum -32,768, and the maximum 32768.")
st.image("bitdepth.png")
st.write("_The image above shows the sound waves mapped out on the bit depth of a graph, and it also shows where the cuts are made to squish the values into certain bit depths._")