\## Docker Directory Task



This assignment will help you - how to use Python \& Docker to create directories and files inside a container.





\## What it Does

-> It creates 3 directories: "1", "2", "3"

-> Inside each directory:

&nbsp; - "1" -> '1.txt'

&nbsp; - "2" -> '1.txt', '2.txt'

&nbsp; - "3" -> '1.txt', '2.txt', '3.txt'



\## Files in this Repo

\- 'create\_dirs.py' -> Python script creates the directories \& files  

\- 'Dockerfile'-> Instructions for building a Docker image with Python and the script  

\- 'README.md' -> Notes of this assignment 



---



\## Steps followed



\## Write Python script

'''python

import os



for i in range(1, 4):

&nbsp;   os.makedirs(str(i), exist\_ok=True)

&nbsp;   for j in range(1, i + 1):

&nbsp;       with open(f"{i}/{j}.txt", "w") as f:

&nbsp;       f.write(f"This is file {j} inside directory {i}\\n")



\## create a Dockerfile

'''dockerfile

FROM python:3.10-slim

WORKDIR /app

COPY create\_dirs.py .

CMD \["python", "create\_dirs.py"]



Build Docker image

docker build -t dir-maker .



\## start the container

docker start 6337cb402dab



Note - Dirs \& files got created now









