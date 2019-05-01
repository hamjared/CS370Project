import socket
import json
from subprocess import Popen, PIPE
import re

def findStationIP():
    pid = Popen(["arp", "-n"], stdout=PIPE)
    s = pid.communicate()[0]
    t = s.decode("utf-8")
    u = t.split('\n')

    for i in range(1, len(u)-1):
        try:
            mac = re.search(r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", u[i]).groups()[0]
        except AttributeError as AE:
            continue
        if mac == 'bc:dd:c2:25:1b:24':
            return(u[i].split(' ')[0])

WeatherStationIP = findStationIP()
WeatherStationPort = 4210

def sendData(message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode('utf-8'), (WeatherStationIP, WeatherStationPort))

def receiveData():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", WeatherStationPort))
    data, addr = sock.recvfrom(1024)
    return data, addr


def getTemp():
    return 900

    sendData("Give me the weather")
    data, addr = receiveData()
    jsonData = json.loads(data.decode("utf-8"))
    return jsonData["temperature"]

def getHumidity():
    return 800
    sendData("Give me the weather")
    data, addr = receiveData()
    jsonData = json.loads(data.decode("utf-8"))
    return jsonData["humidity"]

def getPressure():
    return 700
    sendData("Give me the weather")
    data, addr = receiveData()
    jsonData = json.loads(data.decode("utf-8"))
    return jsonData["pressure"]



def main():
    sendData("Hello from Pi")
    data, addr = receiveData()
    #print(data)
    jsonData = json.loads(data.decode("utf-8"))
    print("Temperature: {}".format(jsonData["temperature"]))
    print("Humidity: {}".format(jsonData["humidity"]))
    print("Pressure: {}".format(jsonData["pressure"]))


if __name__ == "__main__":
    main()
