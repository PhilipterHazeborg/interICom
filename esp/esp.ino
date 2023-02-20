const int BTN = 13;
const int clk = 12;
int BTN_state = 0;
int last_state = 0;
unsigned long timestamp;
int clkState = 0;
int lastclkState = 0;
int counter = 0;
char* buffer_array[5];
char str_buffer[4];
char* new_str;
char buffer_str;

void setup() {
  setlocale(LC_ALL, "en_US.utf8");
  Serial.begin(9600);
  pinMode(BTN, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(clk, INPUT);
}

void loop() {
  //Serial.println(counter);
  yield();
  BTN_state = digitalRead(BTN);
  clkState = digitalRead(clk);
  
  if(counter == 4){
    counter = 0;
    buffer_array[4] = "\0";
    String s = buffer_array;
    Serial.println(s);

    Serial.println("-----");
  }
  
  if(clkState != lastclkState) {
    if(clkState == HIGH){
      /*
      unsigned long current_time = millis();
      unsigned long duration = current_time - timestamp;
      timestamp = current_time;
      */
      //Serial.println(duration);
      if(BTN_state == HIGH) {
        
        Serial.println("1");
        digitalWrite(LED_BUILTIN, HIGH);
        buffer_array[counter] = (char*)BTN_state;
      }else{
        
        Serial.println("0");
        digitalWrite(LED_BUILTIN, LOW);
        buffer_array[counter] = (char*)BTN_state;
      }
      counter++;
    }
  }
  lastclkState = clkState;
}
