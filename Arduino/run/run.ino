const int temperature = 3;
const int RGB[] = {218, 165, 32};
const int redPin = 11;
const int greenPin = 10;
const int bluePin = 9;
int blinkTime = 250;

void setup() {
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}

void loop() {
  blinkyBlinky(temperature, blinkTime);
  delay(2000);
}

void blinkyBlinky(int repeats, int time) {
  for (int i = 0; i < repeats; i++) {
    analogWrite(redPin, RGB[0]);
    analogWrite(greenPin, RGB[1]);
    analogWrite(bluePin, RGB[2]);
    delay(time);
    analogWrite(redPin, 0);
    analogWrite(greenPin, 0);
    analogWrite(bluePin, 0);
    delay(time);
  }
}