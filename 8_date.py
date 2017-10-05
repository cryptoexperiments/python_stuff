import time
import os

while True:
    timestr = time.strftime("%Y%m%d-%H%M%S")
    print(timestr)
    file = open("/home/pi/GIT/python_stuff/date_files/file_" +  timestr, "w")
    file.write("Hello World " + os.getcwd())
    file.close()
    time.sleep(5)
