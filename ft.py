import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt


frequency_1 = 440  # Hz
frequency_2 = 293.665  # Hz
frequency_3 = 349.228  # Hz
duration = 0.5  # seconds
sample_rate = 44100  # samples per second

t = np.linspace(0, duration, int(sample_rate * duration), False)
audio_1 = np.sin(2 * np.pi * frequency_1 * t)
audio_2 = np.sin(2 * np.pi * frequency_2 * t)
audio_3 = np.sin(2 * np.pi * frequency_3 * t)
audio = audio_1 + audio_2 + audio_3


# Play the sound
sd.play(audio, sample_rate)
sd.wait()


nyquist_frequency = sample_rate / 2
test_frequencies = np.linspace(0, 600, 1000)


def ft(t, audio, freq):
    dt = t[1] - t[0]
    return np.sum([a*np.e**(-2j*np.pi*freq*_t) for _t, a in zip(t, audio)]) * dt


ft_result = [ft(t, audio, freq) for freq in test_frequencies]
plt.figure(figsize=(12, 6))
plt.plot(test_frequencies, np.abs(ft_result))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('FFT of the Signal')
plt.xlim(0, 1000)
plt.grid(True)
plt.show()
