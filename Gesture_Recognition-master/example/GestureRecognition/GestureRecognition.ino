/*****************************************************************************/
//Introduction:this sketch can be used to test gesture recognition.3-Axis Digital 
//   Accelerometer(16g) is in need. Start to test, you should press the button and
//   draw your graphics in the air.Matching results will be seen in serial output.
//   Any problems, please feel free to contact me !
//   now we only support 15 kinds of gestures. It is as follow
//
/*********************************************************************************************************************************************
 *|   0   |   1   |   2	 |   3   |    4   |	5       |	6      |    7  |    8  |    9    |    10   |   11  |   12  |   13    |    14   |   15  |*
 *|   *   |   *   |  *   |   *   |  * * * |	      * |* * *   |*      | *     |* * * *  |  * * * *|    *  |*      |  *      |      *  |      *|*
 *|  ***  |   *   | *    |    *  | * *	  |	     *  |   * *  | *     |* * * *|      *  |  *      |* * * *|*      |* * *    |    * * *|      *|*
 *| * * * | * * * |******|****** |*   *	  | *   *   |  *   * |  *   *| *    *|      *  |  *      |*   *  |*   *  |  *      |      *  |  *   *|*
 *|   *   |  ***  | *    |    *  |     *  |  * *    | *      |   * * |      *|    * * *|* * *    |*      |* * * *|  *      |      *  |* * * *|*
 *|   *   |   *   |  *   |   *   |      * |   * * * |*       |* * *  |      *|      *  |  *      |*      |    *  |  * * * *|* * * *  |  *    |*
 *********************************************************************************************************************************************
//
//  Hardware:3-Axis Digital Accelerometer(16g)
//  Arduino IDE: Arduino-1.0
//  Author:lawliet.zou(lawliet.zou@gmail.com)		
//  Date: Dec 24,2013
//  Version: v1.0
//  by www.seeedstudio.com
//
//  This library is free software; you can redistribute it and/or
//  modify it under the terms of the GNU Lesser General Public
//  License as published by the Free Software Foundation; either
//  version 2.1 of the License, or (at your option) any later version.
//
//  This library is distributed in the hope that it will be useful,
//  but WITHOUT ANY WARRANTY; without even the implied warranty of
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
//  Lesser General Public License for more details.
//
//  You should have received a copy of the GNU Lesser General Public
//  License along with this library; if not, write to the Free Software
//  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
//
/*******************************************************************************/
#include <gesture.h>
#include <Wire.h>
#include <ADXL345.h>
#include <Process.h>
#include <Bridge.h>

const int BUTTON = 5;
const int MAX_NUM_SUPPORTED_GESTURES = 4;
Gesture gesture;

const String AWS_API_GATEWAY_URL = "https://q4ur7dt6q7.execute-api.us-west-2.amazonaws.com/beta";
const String PHILLIPS_HUE_IP_ADDRESS = "172.20.10.4";

void setup(){
    Bridge.begin();
    Serial.begin(9600);
    pinMode(BUTTON, INPUT);
    gesture.init();
}

String readProcessReturn(Process p) {
  String return_val = "";
    while (p.available()>0) {
      char c = p.read();
      return_val.concat(c);
      Serial.print(c);
    }
    Serial.flush();
    return return_val;
}

String callAWSLambda(int gesture_number) {
    String gesture_string = String(gesture_number);
    Process p;
    p.begin("curl");
    p.addParameter("-X");
    p.addParameter("POST");
    p.addParameter("-d");
    p.addParameter("{\"gesture\": \"" + gesture_string + "\"}");
    p.addParameter(AWS_API_GATEWAY_URL);
    p.run();

    String return_val = readProcessReturn(p);
    return return_val;
    
}

String turnHueLightOn(){
    Serial.println("turning light on");
    Process p;
    p.begin("curl");
    p.addParameter("-X");
    p.addParameter("PUT");
    p.addParameter("-d");
    p.addParameter("{\"on\":true}");
    p.addParameter("http://172.20.10.4/api/9EWT1X3Rtx9swhpulAo7SBMNML1uYpdWWnA0yumO/groups/1/action");
    p.run();

    String return_val = readProcessReturn(p);
    return return_val;
}

String turnHueLightOff(){
    Serial.println("Turning light off...");
    Process p;
    p.begin("curl");
    p.addParameter("-X");
    p.addParameter("PUT");
    p.addParameter("-d");
    p.addParameter("{\"on\":false}");
    p.addParameter("http://172.20.10.4/api/9EWT1X3Rtx9swhpulAo7SBMNML1uYpdWWnA0yumO/groups/1/action");
    p.run();
  
    String return_val = readProcessReturn(p);
    return return_val;
}

String getHueUsername() {
    Serial.println("Getting username...");
    Process p;
    p.begin("curl");
    p.addParameter("-X");
    p.addParameter("POST");
    p.addParameter("-d");
    p.addParameter("{\"devicetype\":\"Console\"}");
    p.addParameter("172.20.10.4/api");
    p.run();
    
    String return_val = readProcessReturn(p);
    return return_val;
}

String pressHueLinkButton() {
    Serial.println("Pressing Link Button...");
    Process p;
    p.begin("curl");
    p.addParameter("-X");
    p.addParameter("PUT");
    p.addParameter("-d");
    p.addParameter("{\"linkbutton\": true}");
    p.addParameter("http://172.20.10.4/api/9EWT1X3Rtx9swhpulAo7SBMNML1uYpdWWnA0yumO/config");
    p.run();
  
    String return_val = readProcessReturn(p);
    return return_val;
}

String setHueLightColor(int s, int h) {
    Serial.println("Changing hue light to random color...");
    String saturation = String(s);
    String hue = String(h);
    Process p;
    p.begin("curl");
    p.addParameter("-X");
    p.addParameter("PUT");
    p.addParameter("-d");
    p.addParameter("{\"on\":true, \"sat\":" + saturation + ", \"bri\":254,\"hue\":" + hue + "}");
    p.addParameter("http://172.20.10.4/api/9EWT1X3Rtx9swhpulAo7SBMNML1uYpdWWnA0yumO/lights/1/state");
    p.run();
    
    String return_val = readProcessReturn(p);
    return return_val;
}

void toggleHue(String command) {
    pressHueLinkButton();
    getHueUsername();
    if (command == "1") {
        turnHueLightOn();
    } else {
        turnHueLightOff();
    }
}


void loop(){
//    int gesture_result; 
//    if(HIGH == digitalRead(BUTTON)){
//      	delay(200);//debug
//      	if(!gesture.samplingAccelerateData){       
//      	    gesture.checkMoveStart();
//              }
//      	if(gesture.samplingAccelerateData){
//                  if(0 != gesture.getAccelerateData()){
//                      Serial.print("\r\n get accelerate data error.");
//                      gesture_result = -1; 
//                  }
//      	}
//      	if (gesture.calculatingAccelerateData){
//      	    gesture_result = gesture.calculateAccelerateData();
//            if (gesture_result >= 0 && gesture_result < MAX_NUM_SUPPORTED_GESTURES) {
//                String return_val = callAWSLambda(gesture_result);
//                if (gesture_result == 0) {
//                    // User trying to toggle Hue light
//                    toggleHue(return_val);
//                }
//                if (gesture_result == 2) {
//                    setHueLightColor(random(0, 256), random(0, 65535));
//                }
//            }
//        }
//    }
toggleHue("0");
Serial.println("here");
for(;;);
}
