#!/usr/bin/env python
# coding: utf-8

# In[1]:


import librosa
import soundfile as sf
import IPython.display as ipd
Original_Audio, sr = librosa.load('AI_VOICE.wav', sr=None)
Trimmed_Audio, _ = librosa.effects.trim(Original_Audio)
sf.write('AI_VOICE.wav', Trimmed_Audio, sr)
 
print("Original Audio:")
ipd.display(ipd.Audio(Original_Audio, rate=sr))
 
print("Trimmed Audio:")
ipd.display(ipd.Audio(Trimmed_Audio, rate=sr))


# In[3]:


import librosa
import soundfile as sf
import IPython.display as ipd
import matplotlib.pyplot as plt
 
Original_Audio, sr = librosa.load('AI_VOICE.wav', sr=None)
 
Trimmed_Audio, _ = librosa.effects.trim(Original_Audio)
 
sf.write('Trimmed_Audio.wav', Trimmed_Audio, sr)
def plot_waveform(audio, sr, title):
    plt.figure(figsize=(10, 4))
    plt.plot(audio)
    plt.title(title)
    plt.xlabel('Time (samples)')
    plt.ylabel('Amplitude')
    plt.show()
 
print("Original Audio:")
plot_waveform(Original_Audio, sr, "Original Audio")
ipd.display(ipd.Audio(Original_Audio, rate=sr))
 
print("Trimmed Audio:")
plot_waveform(Trimmed_Audio, sr, "Trimmed Audio")
ipd.display(ipd.Audio(Trimmed_Audio, rate=sr))


# In[ ]:




