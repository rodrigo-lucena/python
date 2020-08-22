import serial
import time
import keyboard
import matplotlib.pyplot as plt

conexao = serial.Serial('COM3',9600, timeout=1) #conexao = serial.Serial('COM3',9600)
line=conexao.readline()
to = time.time()
ta = time.time()
x=[]
t=[]

while True:
    
    line=conexao.readline()
    print(time.time()-ta)
    if keyboard.is_pressed("p"):
        print("pressionou p")
        break
    if time.time()-ta>=2:
        h=""
        line=conexao.readline()
        for i in line:
            h+=chr(i)
        dt=time.time()-to
        ta = time.time()
        x.append(float(h))
        t.append(round(dt,3))
        print(x)
        print(t)
        
lines=plt.plot(t,x)
plt.show()        
