#define REPORTING_PERIOD_MS    1000
int tsLastReport = 0;
// the setup routine runs once when you press reset:
void setup() {
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  if (millis() - tsLastReport > REPORTING_PERIOD_MS) {
    int sensorValue = analogRead(A0);  // Le o sinal na porta A0 e grava em sensorValue

    float voltage = sensorValue * (5.0 / 1023.0);  // Calcula a voltagem dividindo o sinal pela cxonstante 5.0 / 1023

    Serial.print(voltage);
    Serial.print("\n");

    tsLastReport = millis();
  }
}
