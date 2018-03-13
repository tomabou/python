import numpy as np
import wave

def sin_func(x):
    return np.sin(2*np.pi*x)

def san_func(x):
    return np.abs(x*4-2) - 1

def noko_func(x):
    return x*2-1

def create_sound(h,l,BPM,framerate):
    l = l*60/BPM*framerate
    x = np.arange(l)
    hertz = 442 * (2**(h/12))
    x = x/(framerate/hertz)
    x = x - np.floor(x)
    return noko_func(x)

def music_len(music,BPM,framerate):
    n = music[-1][2]+music[-1][1]
    return int(n*60/BPM*framerate)

if __name__=="__main__":
    framerate = 44100
    BPM = 50
    hertz = 442

    """hight,len,start"""
    music = [(0,1,0),(2,1,1),(4,0.2,2),(4,0.2,2.25),(4,0.2,2.5),(4,0.5,3), (2,0.5,3.5),(0,1,4)]
    music+= [(7,1,0),(5,1,1),(0,0.2,2),(0,0.2,2.25),(0,0.2,2.5),(-1,0.5,3.5),(-5,1,4)]
    music+= [(-8,1,0),(-15,1,1),(-17,1.5,2),(-17,0.5,3.5),(-8,1,4)]
    x = np.zeros(music_len(music,BPM,framerate))
    for note in music:
        start = int(note[2]*60/BPM*framerate)
        s = create_sound(note[0],note[1],BPM,framerate)
        x[start:start+len(s)] += s

    N = len(x)
    fc = 2000/framerate
    F = np.fft.fft(x)/(N/2)
    freq = np.fft.fftfreq(len(x))
    F[0] = F[0]/2
    F[(freq > fc)] = 0
    F[(freq < 0)] = 0
    x = np.fft.ifft(F)*(2*N/2)

    m = np.max(abs(x))
    x = (x*30000/m).astype(np.int16)

    w = wave.Wave_write("lowpath.wav")
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(framerate)
    w.writeframes(x)
    w.close()