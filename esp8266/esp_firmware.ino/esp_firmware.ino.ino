#define FASTLED_ESP8266_RAW_PIN_ORDER
#include <FastLED.h>

#include <ESPAsyncTCP.h>
#include <ESPAsyncWebServer.h>
#include <WebSerial.h>

#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <ArduinoOTA.h>
#include <WebSocketsServer.h>

// Create header file containing wifi credentials
//const char *ssid = "my_ssid";
//const char *password = "my_password";

#include "WiFiCredentials.h"

#define LED_NUM 100
#define LED_PIN 2
CRGB leds[LED_NUM];

ESP8266WiFiMulti wifiMulti;       // Create an instance of the ESP8266WiFiMulti class, called 'wifiMulti'

AsyncWebServer server(80); // Create web server for serial
WebSocketsServer webSocket(81);    // create a websocket server on port 81

const char *OTAName = "ESP8266";           // A name and a password for the OTA service
const char *OTAPassword = "esp8266";

WiFiClient client;

void all(int new_color);

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
            WebSerial.println("read something on socket");
            break;
  }
}

void setupWebSocket() { // Start a WebSocket server
  webSocket.begin();                          // start the websocket server
  webSocket.onEvent(webSocketEvent);          // if there's an incomming websocket message, go to function 'webSocketEvent'
  Serial.println("WebSocket server started.");
}

void setupWifi() { // Start a WebSocket server
    // Initialize serial communication
    Serial.begin(115200);

    // Connect to wifi
    Serial.print("Trying to connect to ");
    Serial.print(ssid);
    wifiMulti.addAP(ssid, password);

    all(CRGB::Red);
    while(wifiMulti.run() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }  

    all(CRGB::Green);
    delay(1000);
    all(CRGB::Black);

    Serial.println("");
    Serial.print("Connected to ");
    Serial.println(WiFi.SSID());
    Serial.print("IP address: ");
    Serial.println(WiFi.localIP());
}

void setupOTA() {
    ArduinoOTA.setHostname(OTAName);
    ArduinoOTA.setPassword(OTAPassword);

    ArduinoOTA.onStart([]() {
        Serial.println("Start");
        all(CRGB::LightPink);
    });
    ArduinoOTA.onEnd([]() {
        Serial.println("\r\nEnd");
        all(CRGB::Gold);
    });
    ArduinoOTA.onProgress([](unsigned int progress, unsigned int total) {
        int percentage = progress / (total / 100);
        WebSerial.println(percentage);
        leds[percentage] = CRGB::Green;
        FastLED.show();
    });
    ArduinoOTA.onError([](ota_error_t error) {
        Serial.printf("Error[%u]: ", error);
        if (error == OTA_AUTH_ERROR) Serial.println("Auth Failed");
        else if (error == OTA_BEGIN_ERROR) Serial.println("Begin Failed");
        else if (error == OTA_CONNECT_ERROR) Serial.println("Connect Failed");
        else if (error == OTA_RECEIVE_ERROR) Serial.println("Receive Failed");
        else if (error == OTA_END_ERROR) Serial.println("End Failed");
    });
    ArduinoOTA.begin();
    Serial.println("OTA ready\r\n");
}

void setupWebSerial() {
    WebSerial.begin(&server);
    WebSerial.msgCallback([](uint8_t *data, size_t len){
        WebSerial.println("Received Data...");
        String d = "";
        for(int i=0; i < len; i++){
            d += char(data[i]);
        }
        WebSerial.println(d);});
    server.begin();
}

void setupLeds() {
    // Initalizing band strip
    FastLED.addLeds<NEOPIXEL, LED_PIN>(leds, LED_NUM);
}

void all(int new_color) {
    for (int i = 0; i < LED_NUM; i++) {
        leds[i] = new_color;
    }
    FastLED.show();
}

void setup() {
    setupLeds();
    setupWifi ();
    setupWebSerial();
    setupOTA();
    setupWebSocket();
}

void loop() {
    webSocket.loop();
    ArduinoOTA.handle();

    for (int j = 0; j < 255; j++) {
        for (int i = 0; i < LED_NUM; i++) {
            leds[i] = CHSV(i - (j * 2), 255, 255); /* The higher the value 4 the less fade there is and vice versa */ 
        }
        FastLED.show();
        ArduinoOTA.handle();
        delay(10); /* Change this to your hearts desire, the lower the value the faster your colors move (and vice versa) */
    }
}
