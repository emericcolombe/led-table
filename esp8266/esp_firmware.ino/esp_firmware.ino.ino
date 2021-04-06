#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <ArduinoOTA.h>
#include <WebSocketsServer.h>

// Create header file containing wifi credentials
//const char *ssid = "my_ssid";
//const char *password = "my_password";

#include "WiFiCredentials.h"

ESP8266WiFiMulti wifiMulti;       // Create an instance of the ESP8266WiFiMulti class, called 'wifiMulti'

WebSocketsServer webSocket(81);    // create a websocket server on port 81

const char *OTAName = "ESP8266";           // A name and a password for the OTA service
const char *OTAPassword = "esp8266";

void webSocketEvent(uint8_t num, WStype_t type, uint8_t * payload, size_t lenght) { // When a WebSocket message is received
    Serial.printf("[%u] Disconnected!\n", num);
    switch (type) {
        case WStype_DISCONNECTED:             // if the websocket is disconnected
            Serial.printf("[%u] Disconnected!\n", num);
            break;
        case WStype_CONNECTED: {              // if a new websocket connection is established
            IPAddress ip = webSocket.remoteIP(num);
            Serial.printf("[%u] Connected from %d.%d.%d.%d url: %s\n", num, ip[0], ip[1], ip[2], ip[3], payload);
            }
            break;
        case WStype_TEXT:                     // if new text data is received
            Serial.printf("[%u] get Text: %s\n", num, payload);
            break;
  }
}

void startWebSocket() { // Start a WebSocket server
  webSocket.begin();                          // start the websocket server
  webSocket.onEvent(webSocketEvent);          // if there's an incomming websocket message, go to function 'webSocketEvent'
  Serial.println("WebSocket server started.");
}

void startWifi() { // Start a WebSocket server
    // Initialize serial communication
    Serial.begin(115200);
    
    // Initalizing band strip
    //FastLED.addLeds<NEOPIXEL, LED_PIN>(leds, LED_NUM);
    
    // Connect to wifi
    Serial.print("Trying to connect to ");
    Serial.print(ssid);
    wifiMulti.addAP(ssid, password);

    while(wifiMulti.run() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }  

    Serial.println("");
    Serial.print("Connected to ");
    Serial.println(WiFi.SSID());
    Serial.print("IP address: ");
    Serial.println(WiFi.localIP());
}

void setup() {
  startWifi ();
  startWebSocket();

}

void loop() {
    webSocket.loop();   
}
