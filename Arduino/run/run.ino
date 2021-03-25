const char* temperature; // "77"
const char* LED; // "Purple"

void setup() {
  Serial.begin(9600); // open the serial port at 9600 bps:
}

void loop() {
  Serial.print(temperature);
  Serial.print(LED);
}

void subroutinename() {}
