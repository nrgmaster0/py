import time

x = 1000

while True:
    if x.endswith("0"):
        print("yes")
    time.sleep(0.1)
    x += 1
    print(x)