#include <SharpIR.h>
#include <OneWire.h>
#include <DallasTemperature.h>

#define IRPin A0
#define model 1080
#define ONE_WIRE_BUS 13

//preferences
int range = 3;
int desireTemp = 25;
int hotColour[] = {255, 0, 0};
int coldColour[] = {0, 0, 255};
int perfectColour[] = {0, 255, 0};

int distance_cm;

int RELAY_PIN = 5;
int red_light_pin = 11;
int green_light_pin = 10;
int blue_light_pin = 9;

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
    if (Celcius + range < desireTemp) {
      RGB_color(coldColour[0], coldColour[1], coldColour[2]);
      Serial.println("COLD");
       digitalWrite(RELAY_PIN, LOW);
    }
    else if (Celcius - range > desireTemp) {
      RGB_color(hotColour[0], hotColour[1], hotColour[2]);
      Serial.println("HOT");
      digitalWrite(RELAY_PIN, HIGH);
    }
    else {
      RGB_color(perfectColour[0], perfectColour[1], perfectColour[2]);
      Serial.println("PERFECT");
       digitalWrite(RELAY_PIN, LOW);
    }
  }
  else {
    digitalWrite(RELAY_PIN, LOW);
    RGB_color(0, 0, 0);
  }
}

void RGB_color(int r, int g, int b)
{
  analogWrite(red_light_pin, r);
  analogWrite(green_light_pin, g);
  analogWrite(blue_light_pin, b);
}
