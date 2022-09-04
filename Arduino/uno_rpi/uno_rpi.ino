
String command;
//#define ldr A0
#define l1 8
#define l2 9
#define l3 10
 
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(l1,OUTPUT);
  pinMode(l2,OUTPUT);
  pinMode(l3,OUTPUT);
  
}

void loop() {
 // put your main code here, to run repeatedly:
 // int reading=analogRead(ldr);
 // Serial.println(reading);
  

  if(Serial.available()){
    command=Serial.readStringUntil('\n');
    command.trim();
    if(command.equals("left")){
      digitalWrite(l1,LOW);
      digitalWrite(l2,LOW);
      digitalWrite(l3,HIGH);
    }
    else if(command.equals("right")){
      digitalWrite(l1,LOW);
      digitalWrite(l2,HIGH);
      digitalWrite(l3,LOW);
    }
    else if(command.equals("center")){
      digitalWrite(l1,HIGH);
      digitalWrite(l2,LOW);
      digitalWrite(l3,LOW);
    }
    else{
      digitalWrite(l1,HIGH);
      digitalWrite(l2,HIGH);
      digitalWrite(l3,HIGH);
    }
    
  }
  delay(1000);
}
