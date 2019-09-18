import os
import time
# import commands


# commands.getstatusoutput('ls -lt')
loop = 200
os.system("echo \"-->> start testing "+str(loop)+" times\"")
for i in range(loop):
    time.sleep(0.2)
    os.system('curl -F "file=@thai1.jpg" http://127.0.0.1:5005/stream_predict')