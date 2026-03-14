#include <ESP8266WiFi.h> 
#include <ESP8266WebServer.h> 
#include <ESP8266mDNS.h> 

const char* ssid = "ALEXSSANDRA"; 
const char* password = "A24038712d"; 
ESP8266WebServer server(80); 

/*
Nome	GPIO
D1	5
D2	4
D5	14
D6	12
D7	13
*/

int relay = LED_BUILTIN;  // pino do relé 
int button = 4;

void tocarAlarme() { 
  digitalWrite(relay, HIGH); 
  delay(5000); 
  digitalWrite(relay, LOW); 
  server.send(200, "text/plain", "Alarme acionado"); 
} 
  
void setup() { 
  pinMode(relay, OUTPUT);
  pinMode(button, INPUT);

  digitalWrite(relay, LOW);

  Serial.begin(115200); 
  WiFi.begin(ssid, password); 
  Serial.print("Conectando ao WiFi"); 
  while (WiFi.status() != WL_CONNECTED) { 
    delay(500); Serial.print("."); 
  } 
  
  Serial.println(""); 
  Serial.println("WiFi conectado"); 
  Serial.println(WiFi.localIP()); 
  
  if (MDNS.begin("alarme")) { 
    Serial.println("mDNS iniciado: http://alarme.local"); 
  } 
  server.on("/alarme", tocarAlarme); 
  server.begin(); Serial.println("Servidor iniciado"); 
} 

void loop() {
  if(button == HIGH){
    digitalWrite(relay,HIGH);
  }

  MDNS.update();
  server.handleClient(); 
}
