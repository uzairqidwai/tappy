/*
 * Write ID Number onto a MIFARE RFID card using a RFID-RC522 reader
 * -----------------------------------------------------------------------------------------
 * Developed by Uzair Qidwai
 */

#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN         9           // Set RST Pin
#define SS_PIN          10          // Set SS Pin 

MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance
const int buzzer = 9;               // Set Buzzer pin

void setup() {
  pinMode(buzzer, OUTPUT);   // Set buzzer pin to output
  Serial.begin(9600);        // Initialize serial communications with the PC
  SPI.begin();               // Init SPI bus
  mfrc522.PCD_Init();        // Init MFRC522 card
}


void loop() {
  Menu();
}


// Menu to put device in Read or Write mode
void Menu() {
    for (;;) {
        noTone(buzzer);                       
        switch (Serial.read()) {
            case 'R': read_card(); break;
            case 'W': write_card(); break;
            default: continue;  // includes the case 'no input'
        }
    }
}


// Function to read card
void read_card(){

// Prepare key - all keys are set to FFFFFFFFFFFFh at chip delivery from the factory.
  MFRC522::MIFARE_Key key;
  for (byte i = 0; i < 6; i++) key.keyByte[i] = 0xFF;

  // Setup variables we need
  byte block;
  byte len;
  MFRC522::StatusCode status;


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

  // Print ID Number to serial & enable buzzer
  for (uint8_t i = 0; i < 16; i++) {
    Serial.write(buffer2[i]);
  }
  
  Serial.write("\n"); //EOL 
  tone(buzzer, 700); // Send 1KHz sound signal...
  delay(300);      
  noTone(buzzer);     // Stop sound

  delay(1000); // Deley between readngs

  mfrc522.PICC_HaltA();
  mfrc522.PCD_StopCrypto1();

}


// Write Card
void write_card(){

    // Prepare key - all keys are set to FFFFFFFFFFFFh at chip delivery from the factory.
  MFRC522::MIFARE_Key key;
  for (byte i = 0; i < 6; i++) key.keyByte[i] = 0xFF;

  // Reset the loop if no new card present on the sensor/reader. This saves the entire process when idle.
  if ( ! mfrc522.PICC_IsNewCardPresent()) {
    return;
  }

  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()) {
    return;
  }

  Serial.print(F("Card UID:"));    //Print UID
  for (byte i = 0; i < mfrc522.uid.size; i++) {
    Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
    Serial.print(mfrc522.uid.uidByte[i], HEX);
  }
  Serial.print(F(" PICC type: "));   // Print PICC type
  MFRC522::PICC_Type piccType = mfrc522.PICC_GetType(mfrc522.uid.sak);
  Serial.println(mfrc522.PICC_GetTypeName(piccType));

  byte buffer[34];
  byte block;
  MFRC522::StatusCode status;
  byte len;

  Serial.setTimeout(20000L) ;     // Wait until 20 seconds for input from serial
  
  // Ask ID Number
  Serial.println(F("Type ID Number, ending with #"));
  len = Serial.readBytesUntil('#', (char *) buffer, 30) ; // Read ID Number from serial
  for (byte i = len; i < 30; i++) buffer[i] = ' ';     // Pad with spaces

  block = 1;
 
  status = mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, block, &key, &(mfrc522.uid));
  if (status != MFRC522::STATUS_OK) {
    Serial.print(F("PCD_Authenticate() failed: "));
    Serial.println(mfrc522.GetStatusCodeName(status));
    return;
  }
  else Serial.println(F("PCD_Authenticate() success: "));

  // Write block
  status = mfrc522.MIFARE_Write(block, buffer, 16);
  if (status != MFRC522::STATUS_OK) {
    Serial.print(F("MIFARE_Write() failed: "));
    Serial.println(mfrc522.GetStatusCodeName(status));
    return;
  }
  else Serial.println(F("MIFARE_Write() success: "));

  block = 2;

  status = mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, block, &key, &(mfrc522.uid));
  if (status != MFRC522::STATUS_OK) {
    Serial.print(F("PCD_Authenticate() failed: "));
    Serial.println(mfrc522.GetStatusCodeName(status));
    return;
  }

  // Write block
  status = mfrc522.MIFARE_Write(block, &buffer[16], 16);
  if (status != MFRC522::STATUS_OK) {
    Serial.print(F("MIFARE_Write() failed: "));
    Serial.println(mfrc522.GetStatusCodeName(status));
    return;
  }
  else {
    Serial.println(F("MIFARE_Write() success: "));
    tone(buzzer, 1000); // Send 1KHz sound signal...
    delay(300);        // ...for 
    noTone(buzzer);     // Stop sound...
  }

  Serial.println(" ");
  mfrc522.PICC_HaltA(); // Halt PICC
  mfrc522.PCD_StopCrypto1();  // Stop encryption on PCD
}
