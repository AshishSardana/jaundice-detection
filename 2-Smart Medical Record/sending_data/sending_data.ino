#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9
 
MFRC522 rfid(SS_PIN, RST_PIN);

void setup() { 
  Serial.begin(9600);
  SPI.begin(); // Init SPI bus
  rfid.PCD_Init();
}

void loop() {

  // Look for new cards
  if ( ! rfid.PICC_IsNewCardPresent())
    return;

  // Verify if the NUID has been readed
  if ( ! rfid.PICC_ReadCardSerial())
    return;
   sendHex(rfid.uid.uidByte, rfid.uid.size);
   Serial.println();
    rfid.PICC_HaltA();
    rfid.PCD_StopCrypto1();    
}


void sendHex(byte *buffer, byte bufferSize)
{
  byte t[4][4] = {{150,83,190,147},{194,150,179,171},{186,77,173,181},{66,03,174,181}};
  byte temp[4];
  byte c=0,s=0;
  Serial.println(bufferSize);
  for (byte i = 0; i < bufferSize; i++) {
    Serial.print(buffer[i] < 0x10 ? " 0" : " ");
    Serial.println(buffer[i]);
    temp[i]=buffer[i];
  }

   for(byte j=0;j<4;j++)
   { 
    for(byte k=0;k<4;k++)
    {
      if(temp[k]==t[j][k])
      c++;
    }
    if(c==4) 
      s=j+1
    c=0;
    }
    Serial.println(s);
}

