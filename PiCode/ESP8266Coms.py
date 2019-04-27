import socket
import json

WeatherStationIP = "192.168.1.149"
WeatherStationPort = 4210

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
