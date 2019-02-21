#define enA 3
#define in1 4
#define in2 5

#include <SPI.h>
#include "nRF24L01.h"
#include "RF24.h"
#include <Servo.h>

float k ;
float mess;
int msg[1];
int num;
RF24 radio(9,10);
const uint64_t pipe = 0xE8E8F0F0E1LL;

void setup() {
  // put your setup code here, to run once:
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  digitalWrite(4,LOW);
  digitalWrite(5,LOW);
  Serial.begin(9600);
 radio.begin();
 radio.openReadingPipe(1,pipe);
 radio.startListening();
}

void loop() {
  // put your main code here, to run repeatedly:
  if (radio.available()){
   bool done = false;    
   while (!done){
    done = radio.read(msg, 1);
    Serial.println(msg[0]);
     if (msg[0] >= 55){
     analogWrite(enA, msg[0]);
     digitalWrite(in1,HIGH);
     digitalWrite(in2,LOW);
     }
     else if ((msg[0] <55) && (msg[0] > 45)){
     analogWrite(enA, 0);
     digitalWrite(in1,LOW);
     digitalWrite(in2,LOW);
     }
     else{
     num = 100 - msg[0];
     analogWrite(enA, num);
     digitalWrite(in1,LOW);
     digitalWrite(in2,HIGH);
     }}}
 else{Serial.println("No radio available");}}
