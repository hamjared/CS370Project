import socket
import json

WeatherStationIP = findStationIP()
WeatherStationPort = 4210

def findStationIP():
    for i in range(1, len(u)-1):
     mac = re.search(r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", u[i]).groups()[0]
     if mac == 'bc:dd:c2:25:1b:24':
             return(u[i].split(' ')[0])


def sendData(message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode('utf-8'), (WeatherStationIP, WeatherStationPort))

def receiveData():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", WeatherStationPort))
    data, addr = sock.recvfrom(1024)
    return data, addr


def main():
    sendData("Hello from Pi")
    data, addr = receiveData()
    print(data)
    jsonData = json.loads(data)
    print(jsonData["temperature"])


if __name__ == "__main__":
    main()
