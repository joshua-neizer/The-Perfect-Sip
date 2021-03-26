const String LED = "Lightning";
const int temperature = 7;
int ledPin = 13;
int blinkTime = 250;

void setup(){
  pinMode(ledPin, OUTPUT);
   // 5 is number of blinks, blinkTime is the milliseconds in each state from above: int blinkTime = 500;
}

void loop(){
  blinkyBlinky(temperature, blinkTime); // 5 is number of blinks, blinkTime is the milliseconds in each state from above: int blinkTime = 500;
  delay(2000);
}

void blinkyBlinky(int repeats, int time){
  for (int i = 0; i < repeats; i++){
    digitalWrite(ledPin, HIGH);
    delay(time);
    digitalWrite(ledPin, LOW);
    delay(time);
  }
}