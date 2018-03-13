import numpy as np
import wave

def sin_func(x):
    return np.sin(2*np.pi*x)

def san_func(x):
    return np.abs(x*4-2) - 1

def noko_func(x):
    return x*2-1

def create_sound(h,l,BPM,framerate,v):
    l = l*60/BPM*framerate
    x = np.arange(l)
    hertz = 442 * (2**(h/12))
    x = x/(framerate/hertz)
    x = x - np.floor(x)
    return v * san_func(x)

def music_len(music,BPM,framerate):
    n = music[-1][2]+music[-1][1]
    return int(n*60/BPM*framerate)

def tolen(n,BPM,framerate):
    return int(n*60/BPM*framerate)

if __name__=="__main__":
    framerate = 44100
    BPM = 50
    hertz = 221

    """hight,len,start"""
    l =  int(25*60/BPM*framerate)
    x = np.zeros(l)
    for i in range(24):
        start = int(i*60/BPM*framerate)
        for j in range(-5,5):
            h = j*12 + i%12
            s = create_sound(h,1,BPM,framerate,1/(abs(h)+10))
            x[start:start+len(s)] += s

#    N = len(x)
#    fc = 2000/framerate
#    F = np.fft.fft(x)/(N/2)
#    freq = np.fft.fftfreq(len(x))
#    F[0] = F[0]/2
#    F[(freq > fc)] = 0
#    F[(freq < 0)] = 0
#    x = np.fft.ifft(F)*(2*N/2)

    m = np.max(abs(x))
    x = (x*30000/m).astype(np.int16)

    w = wave.Wave_write("inf.wav")
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(framerate)
    w.writeframes(x)
    w.close()