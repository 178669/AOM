// Include the Arduino Stepper Library
#include <Stepper.h>

// Number of steps per output rotation
//400 steps for 2:1 gear rotation
//6 equal size steps of 334
const int stepsPerRevolution = 67;

// Create Instance of Stepper library
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);


void setup()
{
	// set the speed at 60 rpm:
	myStepper.setSpeed(120);
	// initialize the serial port:
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
      {//CCW when shaft pointing up
        Serial.println("CW Rotation 1: " + FromJetson);
        myStepper.step(stepsPerRevolution);
        delay(500);
      }

    if(FromJetson == "Clock2")
      {//CCW when shaft pointing up
        Serial.println("CW Rotation 2: " + FromJetson);
        myStepper.step(stepsPerRevolution*2);
        delay(500);
      }
    if(FromJetson == "Clock3")
      {
        Serial.println("CW Rotation 3: " + FromJetson);
        myStepper.step(stepsPerRevolution*3);
        delay(500);
      }
    
    if(FromJetson == "Counter1")
      {
        Serial.println("CCW Rotation 1: " + FromJetson);
        myStepper.step(-stepsPerRevolution*1);
        delay(500);
      }

    if(FromJetson == "Counter2")
      {
        Serial.println("CCW Rotation 1: " + FromJetson);
        myStepper.step(-stepsPerRevolution*2);
        delay(500);
      }

    if(FromJetson == "Counter3")
      {
        Serial.println("CCW Rotation 1: " + FromJetson);
        myStepper.step(-stepsPerRevolution*3);
        delay(500);
      }
     
     }
}
