/*
 * Read ID Number from a MIFARE RFID card using a RFID-RC522 reader
 * -----------------------------------------------------------------------------------------
 * Developed by Uzair Qidwai
 */
 
#include <SPI.h>
#include <MFRC522.h>
#include <Keyboard.h>

#define RST_PIN         9          
#define SS_PIN          10          

MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance
const int buzzer = 9;


void setup() {
  pinMode(buzzer, OUTPUT);
  Serial.begin(9600);                                           // Initialize serial communications with the PC
  SPI.begin();                                                  // Init SPI bus
  mfrc522.PCD_Init();                                           // Init MFRC522 card
  Keyboard.begin();
  delay(500);
}


void loop() {
  delay(200);
  noTone(buzzer);
  // Prepare key - all keys are set to FFFFFFFFFFFFh at chip delivery from the factory.
  MFRC522::MIFARE_Key key;
  for (byte i = 0; i < 6; i++) key.keyByte[i] = 0xFF;

  //some variables we need
  byte block;
  byte len;
  MFRC522::StatusCode status;

  mfrc522.PCD_StopCrypto1();

  // Reset the loop if no new card present on the sensor/reader. This saves the entire process when idle.
  if ( ! mfrc522.PICC_IsNewCardPresent()) {
    return;
  }

  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()) {
    return;
  }

  byte buffer1[18];

  block = 4;
  len = 18;

  // Get ID Number
  byte buffer2[18];
  block = 1;

  status = mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, 1, &key, &(mfrc522.uid)); //line 834
  if (status != MFRC522::STATUS_OK) {
    //Serial.print(F("Authentication failed: "));
    //Serial.println(mfrc522.GetStatusCodeName(status));
    return;
  }

  status = mfrc522.MIFARE_Read(block, buffer2, &len);
  if (status != MFRC522::STATUS_OK) {
    //Serial.print(F("Reading failed: "));
    //Serial.println(mfrc522.GetStatusCodeName(status));
    return;
  }

  //Print ID Number to serial & HID & buzzer
  for (uint8_t i = 0; i < 16; i++) {
    Serial.write(buffer2[i]);
    Keyboard.write(buffer2[i]);
  }
  typeKey(KEY_RETURN);

  tone(buzzer, 700); // Send 700Hz sound signal...
  delay(300);        
  noTone(buzzer);     // Stop sound
  

  mfrc522.PICC_HaltA();
  mfrc522.PCD_StopCrypto1();


  delay(1000); //Delay between readings

}

void typeKey(int key)
{
  Keyboard.press(key);
  delay(50);
  Keyboard.release(key);;
}
