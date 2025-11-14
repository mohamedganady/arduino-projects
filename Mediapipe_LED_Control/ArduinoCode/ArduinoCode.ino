int led_index = 2;
int led_middle = 3;
int led_ring = 4;
int led_pinky = 5;
int led_thumb = 6;
String command = "";

void setup() {
  Serial.begin(9600);
  pinMode(led_index, OUTPUT);
  pinMode(led_middle, OUTPUT);
  pinMode(led_ring, OUTPUT);
  pinMode(led_pinky, OUTPUT);
  pinMode(led_thumb, OUTPUT);

}

void loop() {
  if (Serial.available() > 0) {
    command = Serial.readStringUntil('\n');
    command.trim();  // Remove whitespace or newline

    if (command == "index_open") {
      digitalWrite(led_index, HIGH);
    } else if (command == "index_close") {
      digitalWrite(led_index, LOW);
    }
    if (command == "middle_open") {
      digitalWrite(led_middle, HIGH);
    } else if (command == "middle_close") {
      digitalWrite(led_middle, LOW);
    }
    if (command == "ring_open") {
      digitalWrite(led_ring, HIGH);
    } else if (command == "ring_close") {
      digitalWrite(led_ring, LOW);
    }
    if (command == "pinky_open") {
      digitalWrite(led_pinky, HIGH);
    } else if (command == "pinky_close") {
      digitalWrite(led_pinky, LOW);
    }
    if (command == "thumb_open") {
      digitalWrite(led_thumb, HIGH);
    } else if (command == "thumb_close") {
      digitalWrite(led_thumb, LOW);
    }
  
  } 
}