#include <SharpIR.h>
#include <OneWire.h>
#include <DallasTemperature.h>

#define IRPin A0
#define model 1080
#define ONE_WIRE_BUS 13

//preferences
int range = 3;
int P_RGB[] = {152, 251, 152};
int C_RGB[] = {255, 69, 0};
int des_temp = 25;
int H_RGB[] = {255, 0, 255};

int distance_cm;

int RELAY_PIN = 5;
int red_light_pin = 11;
int green_light_pin = 10;
int blue_light_pin = 9;
int mosPin = A2;

float Celcius = 0;
float Fahrenheit = 0;

SharpIR mySensor = SharpIR(IRPin, model);

OneWire oneWire(ONE_WIRE_BUS);

DallasTemperature sensors(&oneWire);

void setup() {
  Serial.begin(9600);
  pinMode(ONE_WIRE_BUS, INPUT_PULLUP);
  sensors.begin();
  pinMode(RELAY_PIN, OUTPUT);
  pinMode(red_light_pin, OUTPUT);
  pinMode(green_light_pin, OUTPUT);
  pinMode(blue_light_pin, OUTPUT);
  pinMode(mosPin, OUTPUT);
}

void loop() {
  distance_cm = mySensor.distance();
  Serial.print("Mean distance: ");
  Serial.print(distance_cm);
  Serial.println(" cm");

  sensors.requestTemperatures();
  Celcius = sensors.getTempCByIndex(0);
  Fahrenheit = sensors.toFahrenheit(Celcius);
  Serial.print(" C  ");
  Serial.print(Celcius);
  Serial.print(" F  ");
  Serial.println(Fahrenheit);
  Serial.println("");

  if (distance_cm <= 40) {
    if (Celcius + range < des_temp) {
      RGB_color(C_RGB[0], C_RGB[1], C_RGB[2]);
      Serial.println("COLD");
       digitalWrite(RELAY_PIN, LOW);
       turnOnHeat();
    }
    else if (Celcius - range > des_temp) {
      RGB_color(H_RGB[0], H_RGB[1], H_RGB[2]);
      Serial.println("HOT");
      digitalWrite(RELAY_PIN, HIGH);
      turnOnHeat();
    }
    else {
      RGB_color(P_RGB[0], P_RGB[1], P_RGB[2]);
      Serial.println("PERFECT");
       digitalWrite(RELAY_PIN, LOW);
       turnOnHeat();
    }
  }
  else {
    digitalWrite(RELAY_PIN, LOW);
    RGB_color(0, 0, 0);
    turnOffHeat();
  }
}

void RGB_color(int r, int g, int b)
{
  analogWrite(red_light_pin, r);
  analogWrite(green_light_pin, g);
  analogWrite(blue_light_pin, b);
}

void turnOnHeat(){
  analogWrite(mosPin, 255);
}

void turnOffHeat(){
  analogWrite(mosPin, 0);
}