/*
* sensor.cpp
*
* Created on: Nov 20, 2019
* Author: Team_5
*/
#include<string>
#include"sensor.h"
#include<math.h>
int extInraRedSensor = 0;
int setSensor(){
  //Input port need to update
  //IN_1 = front sonar
  //IN_2 = light sensor
  setAllSensorMode(NXT_IR_SEEKER,COL_COLOR,NXT_IR_SEEKER,GYRO_ANG);
  setAllSensorMode(NXT_IR_SEEKER,COL_COLOR,NXT_IR_SEEKER,GYRO_RATE);
  setAllSensorMode(NXT_IR_SEEKER,COL_COLOR,NXT_IR_SEEKER,GYRO_ANG);
  setAllSensorMode(NXT_IR_SEEKER,COL_COLOR,NXT_IR_SEEKER,GYRO_RATE);
  setAllSensorMode(NXT_IR_SEEKER,COL_COLOR,NXT_IR_SEEKER,GYRO_ANG);
  setAllSensorMode(NXT_IR_SEEKER,COL_COLOR,NXT_IR_SEEKER,GYRO_RATE);
  return setAllSensorMode(NXT_IR_SEEKER,COL_COLOR,NXT_IR_SEEKER,GYRO_ANG);
}

int ReadInfraRedSensor(){
  char buffer[5];
  std::string greeting("Infra Red sensor init!");
  LcdPrintf(1, "%s\n", greeting.c_str());
  Wait(2);
  while(true){
    if(!ButtonIsUp(BTNUP)){
      FreeEV3();
      break;
    }
    //IN_2 will update according to final design
    extInraRedSensor = readSensor(IN_1);
  }
  return extInraRedSensor;
}