# npm create vite@latest
import os
import sys
from time import sleep
import requests

path = sys.argv[1].replace("'", "")
print("Project path is:", path)
project_name = sys.argv[2].replace("'", "")
print("Project name is:", project_name)


def pull_template(path, project_name):
    # make the folder for the project name under the path so its path/project_name
    complete_path = os.path.join(path, project_name)
    os.makedirs(complete_path, exist_ok=True)
    url = "https://api.github.com/repos/mystyy01/lazydev/contents/templates/vite-app"
    res = requests.get(url)
    if res.status_code == 200:
        for file in res.json():
            file_url = file['download_url']
            file_name = file['name']
            file_res = requests.get(file_url)
            if file_res.status_code == 200:
                with open(os.path.join(complete_path, file_name), 'wb') as f:
                    f.write(file_res.content)
                with open("logs.txt", "a") as log:
                    log.write(f"Downloaded {file_name}\n")
            else:
                with open("logs.txt", "a") as log:
                    log.write(f"Failed to download {file_name}\n")


pull_template(path, project_name)
