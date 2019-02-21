///joystick

#include  <SPI.h>
#include "nRF24L01.h"
#include "RF24.h"
int msg[1];
float mess;
float k1 = 0.17595;
float k2 = 0.09775;
RF24 radio(9,10);
const uint64_t pipe = 0xE8E8F0F0E1LL;

void setup(void){
 Serial.begin(9600);
 radio.begin();
 radio.openWritingPipe(pipe);}

void loop(void){
 msg[0] = analogRead(A1);
 mess = msg[0] * k2;
 msg[0] = mess;
 radio.write(msg, 1);
 Serial.println(msg[0]);
 }
