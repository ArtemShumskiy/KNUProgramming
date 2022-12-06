import os
import time

dir = 'your directory'

for dirpath, dirnames, filenames in os.walk(dir):
    for file in filenames:
        if os.path.splitext(file)[1] == '.log' or os.path.splitext(file)[1] == '.tar.gz':
            ctime = os.path.getctime(os.path.join(dirpath, file))
            if (time.time() - ctime) / 60 > 1:
                print("successfully deleted a file")
                os.remove(os.path.join(dirpath, file))
