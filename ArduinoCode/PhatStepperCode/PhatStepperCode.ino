// Include the Arduino Stepper Library
#include <Stepper.h>

// Number of steps per output rotation
//400 steps for 10:1 gear rotation
//6 equal size steps of 334

//1000 steps for 5:1 gear rotation
//5 equal size steps of 200
const int steps = 200;
const int stepPin = 2; //X.STEP
const int dirPin = 5; // X.DIR

// Create Instance of Stepper library

void setup()
{
	// set the speed at 60 rpm:
  pinMode(stepPin,OUTPUT); 
  pinMode(dirPin,OUTPUT);	// initialize the serial port:
	Serial.begin(9600);
  while (!Serial){
  ;//waiting for serial connection
 }
 
}
const char TERMINATOR = '|';

void loop() 
{
  if(Serial.available() > 0)
  {
    String FromJetson = Serial.readStringUntil(TERMINATOR);
    Serial.print("Serial MSG: " + FromJetson);
    if(FromJetson == "Clock1")
    digitalWrite(dirPin,HIGH)
      {//CCW when shaft pointing up
        Serial.println("CW Rotation 1: " + FromJetson);
        //clockwise rotation when shaft facing downwards:
        for(int x = 0; x < steps; x++) 
          {
            digitalWrite(stepPin,HIGH); 
            delayMicroseconds(1000); 
            digitalWrite(stepPin,LOW); 
            delayMicroseconds(1000);       
          }
      }
    if(FromJetson == "Clock2")
      {//CCW when shaft pointing up
        digitalWrite(dirPin,HIGH)
        Serial.println("CW Rotation 2: " + FromJetson);
        for(int x = 0; x < steps*2; x++) 
          {
            digitalWrite(stepPin,HIGH); 
            delayMicroseconds(1000); 
            digitalWrite(stepPin,LOW); 
            delayMicroseconds(1000); 
          }
      }
    if(FromJetson == "Clock3")
      {
        digitalWrite(dirPin,HIGH)
        Serial.println("CW Rotation 3: " + FromJetson);
        for(int x = 0; x < steps*3; x++) 
          {
            digitalWrite(stepPin,HIGH); 
            delayMicroseconds(1000); 
            digitalWrite(stepPin,LOW); 
            delayMicroseconds(1000); 
          }
      }
    if(FromJetson == "Counter1")
      {
        digitalWrite(dirPin,LOW)
        Serial.println("CCW Rotation 1: " + FromJetson);
        for(int x = 0; x < 200; x++) 
          {
            digitalWrite(stepPin,HIGH);
            delayMicroseconds(1000);
            digitalWrite(stepPin,LOW);
            delayMicroseconds(1000);
          }
      }
    if(FromJetson == "Counter2")
      {
        digitalWrite(dirPin,LOW)
        Serial.println("CCW Rotation 1: " + FromJetson);
        for(int x = 0; x < 200*2; x++) 
          {
            digitalWrite(stepPin,HIGH);
            delayMicroseconds(1000);
            digitalWrite(stepPin,LOW);
            delayMicroseconds(1000);
          }
      }

    if(FromJetson == "Counter3")
      {
        digitalWrite(dirPin,LOW)
        for(int x = 0; x < 200*3; x++) 
          {
            digitalWrite(stepPin,HIGH);
            delayMicroseconds(1000);
            digitalWrite(stepPin,LOW);
            delayMicroseconds(1000);
          }
      }
     
     }
}
