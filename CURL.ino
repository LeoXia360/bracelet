#include <Process.h>
#include <Bridge.h>
#include <BridgeClient.h>

void setup() {
  Bridge.begin();
  Serial.begin(9600);
  
}

void runCurl() {
  Process p;
  p.begin("curl");
  p.addParameter("-X");
  p.addParameter("POST");
  p.addParameter("https://q4ur7dt6q7.execute-api.us-west-2.amazonaws.com/beta");
  p.run();
  Serial.println("POST request sent");
  char c = p.read();
  Serial.println(c);
  //Serial.println("Return Code: " + c);
  Serial.flush();
}

void loop() {
  Serial.println("Running Curl");
  runCurl();
  Serial.println("Process Completed");
  for(;;);

}
