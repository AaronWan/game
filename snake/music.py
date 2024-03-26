import wave
import numpy as np
import pyaudio
# brew install portaudio (mac)
# 设置音频参数
sample_rate = 44100
duration = 5
frequency = 440

# 生成音频数据
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
audio_data = np.sin(2 * np.pi * frequency * t)

# 将音频数据写入wav文件
with wave.open("generated_audio.wav", "wb") as wf:
    wf.setnchannels(2)
    wf.setsampwidth(2)
    wf.setframerate(sample_rate)
    wf.writeframes((audio_data * 32767).astype(np.int16).tobytes())

# 播放生成的音频数据
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=sample_rate, output=True)
stream.write((audio_data * 32767).astype(np.int16).tobytes())
stream.stop_stream()
stream.close()
p.terminate()