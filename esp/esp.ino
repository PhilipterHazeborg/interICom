const int BTN = 13;
const int clk = 12;
int BTN_state = 0;
int last_state = 0;
unsigned long timestamp;
int clkState = 0;
int lastclkState = 0;
int counter = 0;
int buffer_array[4];
char str_buffer[4];

void setup() {
  setlocale(LC_ALL, "en_US.utf8");
  Serial.begin(9600);
  pinMode(BTN, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(clk, INPUT);
}

void loop() {
  BTN_state = digitalRead(BTN);
  clkState = digitalRead(clk);
  
  if(counter == 3){
    for(int i = 0; i = 3; i++){
      str_buffer[i] = /*(String)*/buffer_array[i];
      counter = 0;
    }
    Serial.println(str_buffer);
  }
  
  if(clkState != lastclkState) {
    if(clkState == HIGH){
      
      unsigned long current_time = millis();
      unsigned long duration = current_time - timestamp;
      timestamp = current_time;
      
      //Serial.println(duration);
      if(BTN_state == HIGH) {
        
        Serial.println("1");
        digitalWrite(LED_BUILTIN, HIGH);
        buffer_array[counter] = BTN_state;
      }else{
        
        Serial.println("0");
        digitalWrite(LED_BUILTIN, LOW);
        buffer_array[counter] = BTN_state;
      }
      counter++;
    }
  }
  lastclkState = clkState;
}
