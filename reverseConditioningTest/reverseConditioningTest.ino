#include <Servo.h>
int count = 0;
#define uv 5
#define led 7
#define shock 12

#define uvStrength 255


//DATA RECORDING


#define isRecording true
#define shockDuration 300
#define uvDuration 3000//for tail cond test:3000
#define recordDuration 5000 //duration of each recording in msec, for tail cond test: 14000
#define recordNum 20 //how many recordings 
#define waitMinute 2 //wait time between trials (in minutes)

void setup() {
  // put your setup code here, to run once:
  pinMode(uv, OUTPUT);
  pinMode(shock, OUTPUT);
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  delay(1000);


}

void loop() {
  // put your main code here, to run repeatedly:
Serial.println("START_RECORDING");
  delay(7000);
}
