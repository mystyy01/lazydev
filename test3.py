import os

options = []
for script in os.listdir("scripts"):
    index = script.find(".")
    script = script[:index]
    script = script.replace("-", " ").title()
    options.append(script)
print(options)