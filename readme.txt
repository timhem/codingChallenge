How to run:

I am running arch linux as OS so these are linux commands

For the mosquitto docker container to first create the container I ran:
docker run -it -d -p 1883:1883 --name mosquitto  -v /etc/mosquitto/passwd:/mosquitto/config/passwd -v /etc/mosquitto/mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto

This creates the container with default mosquitto.conf mapping it from the system to the docker container.
Since in the hint no username and password was given I assumed for easyness "allow_anonymous true" in mosquitto.conf is ok.
Sidenote: The first mapping for password file then is not needed.

Afterwards the container can be run with
docker run mosquitto

For the python script running in a terminal:
activate the virtual enviroment (see zip file) if asyncio and gmqtt is not installed globally in your system or your
IDE does not create it do so with "source venv/bin/activate"
then run main.py with python3 main.py

if you now send a message via mosquitto_pub -h localhost -t "/event" -m '{"sensor_value":20.2}'
it should be shown in the terminal
If you send a burst of messages the program will print one message every 10 seconds (can be changed in main.py)

Dockerization did not work for me. Since I am not as much expierinced in creating docker images (only using),
the networking between the docker containers did not work.