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
    return v * sin_func(x)

def tolen(n,BPM,framerate):
    return int(n*60/BPM*framerate)

if __name__=="__main__":
    framerate = 44100
    BPM = 150
    hertz = 220
    total = 100

    """hight,len,start"""
    l =  int((total+1)*60/BPM*framerate)
    x = np.zeros(l)
    for i in range(total):
        start = int(i*60/BPM*framerate)
        for j in range(-10,10):
            h = j*12 + i%12
            s = create_sound(h,1,BPM,framerate,np.exp(-h*h / 2000))
            x[start:start+len(s)] += s

    m = np.max(abs(x))
    x = (x*30000/m).astype(np.int16)

    w = wave.Wave_write("inf.wav")
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(framerate)
    w.writeframes(x)
    w.close()