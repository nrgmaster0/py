# py
python
x = 1000
import time

while True:
    time.sleep(0.1)
    x += 1
    if x.endswith("0"):
        print("yes")
    else:
        print("no")
