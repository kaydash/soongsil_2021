title "(Docker)Jupyter:8888[mount Point: /data -> /home/jovyan/ ]"
color E
wsl -e docker run -it -v /data:/home/jovyan/ -p 8888:8888 jupyter/all-spark-notebook