// source: https://code.google.com/p/tinkerit/wiki/SecretThermometer

long readTemp() {
  long result;
  // Read temperature sensor against 1.1V reference
  ADMUX = _BV(REFS1) | _BV(REFS0) | _BV(MUX3);
  delay(2); // Wait for Vref to settle
  ADCSRA |= _BV(ADSC); // Convert
  while (bit_is_set(ADCSRA,ADSC));
  result = ADCL;
  result |= ADCH<<8;
  result = (result - 125) * 1075;
  return result;
}

void setup() {
  Serial.begin(115200);
}

int count = 0;

void loop() {
  //Serial.println( readTemp(), DEC );
  String s = String(count++, DEC) + ": " + String( readTemp(), DEC );
  for(int i=0; i < s.length(); i++ ){
    Serial.print( s.charAt(i) );
    delay( 200 );
  }
  Serial.println("");
  delay(1000);
}
