import requests
import os
import time

path = "/home/jules/repo/themes/"
start_time = time.time()

i = 0
for path, subdirs, files in os.walk(path):
    i += 1
    for name in files:
        if os.path.isfile(os.path.join(path, name)):
            with open(os.path.join(path, name), 'r') as f:
                r = requests.post('http://127.0.0.1:5000/file-upload', files={'file': os.path.join(path, name)})
                print(r, r.text)
print("%s fichiers traités" % i)
print("--- %s seconds ---" % (time.time() - start_time))
