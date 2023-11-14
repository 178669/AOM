// Include the Arduino Stepper Library
#include <Stepper.h>

// Number of steps per output rotation
const int stepsPerRevolution = 200;

// Create Instance of Stepper library
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);


void setup()
{
	// set the speed at 60 rpm:
	myStepper.setSpeed(60);
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
    //Serial.print("Serial MSG: " + FromJetson);
    if(FromJetson == "Clock")
      {//CCW when shaft pointing up
        Serial.println("CW Rotation: " + FromJetson);
        myStepper.step(stepsPerRevolution);
        delay(5000);
      }
    if(FromJetson == "Counter")
      {
        Serial.println("CCW Rotation: " + FromJetson);
        myStepper.step(-stepsPerRevolution);
        delay(5000);
      }
    

  }
	// step one revolution in one direction:
	

	// step one revolution in the other direction:

}
