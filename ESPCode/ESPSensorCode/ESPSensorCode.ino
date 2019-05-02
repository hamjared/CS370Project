#include <ArduinoJson.h>

#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>


#define BME_CS 15 //chip select pin

#define SEALEVELPRESSURE_HPA (1013.25)

#ifndef STASSID
#define STASSID "ssid"
#define STAPSK  "password"
#endif

const char* ssid = STASSID;
const char* password = STAPSK;

WiFiUDP Udp;
unsigned int localUdpPort = 4210;
char incomingPacket[256];


Adafruit_BME280 bme(BME_CS); //hardware spi for the pressure, humidty, temperature sensor
bool status; //boolean to hold status of successfull connection to temp sensor

//Arduino JSON data structure
StaticJsonDocument<250> sensorData;


void setup()
{
    Serial.begin(115200);
    Serial.println();

    Serial.printf("Connecting to %s ", ssid);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }
    Serial.println(" connected");

    Udp.begin(localUdpPort);
    Serial.printf("Now listening at IP %s, UDP port %d\n", WiFi.localIP().toString().c_str(), localUdpPort);

    //initialize temperature, pressure, humidity sensor
    status = bme.begin();
    if (!status) {
        Serial.println("Could not find a valid BME280 sensor, check wiring!");
        while (1); //don't advance if connection was not made to sensor.
    }
}


void loop()
{




    int packetSize = Udp.parsePacket();
    if (packetSize)
    {
        char replyPacket[256] = "";
        sensorData["temperature"] = bme.readTemperature()*1.8 + 32;
        sensorData["humidity"] = bme.readHumidity();
        sensorData["pressure"] = bme.readPressure();
        int sunlight = analogRead(A0);
        char sun [32] = "";
        if (sunlight >= 0 && sunlight <=5){
          strcat(sun, "No sun");
        }
        else if (sunlight >=6 && sunlight <= 100){
          strcat(sun, "Cloudy");
        }
        else{
          strcat(sun, "Sunny");
        }
        sensorData["Sunlight"] = sun;
        serializeJson(sensorData, replyPacket, 256);
        // receive incoming UDP packets
        Serial.printf("Received %d bytes from %s, port %d\n", packetSize, Udp.remoteIP().toString().c_str(), Udp.remotePort());
        int len = Udp.read(incomingPacket, 255);
        if (len > 0)
        {
            incomingPacket[len] = 0;
        }
        Serial.printf("UDP packet contents: %s\n", incomingPacket);

        // send back a reply, to the IP address and port we got the packet from
        Udp.beginPacket(Udp.remoteIP(), 4210);
        Udp.write(replyPacket);
        Udp.endPacket();
    }
}
