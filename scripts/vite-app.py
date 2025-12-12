from time import sleep


sleep(1)

with open("logs.txt", "a") as f:
    f.write("vite is running\n")
print("200")

import sys
print("Argument List:", str(sys.argv))