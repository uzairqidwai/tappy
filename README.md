<p align="center"><img src="https://raw.githubusercontent.com/uzairqidwai/tappy/main/tappy_media/tappy_logo.png" width="400"></p>

<hr/>
<p align="center">
<img src="https://img.shields.io/github/last-commit/uzairqidwai/tappy?style=for-the-badge" />
&nbsp;
<img src="https://img.shields.io/github/workflow/status/ayushsharma82/ElegantOTA/Arduino%20Library%20CI/master?style=for-the-badge" />
&nbsp;
<img src="https://img.shields.io/github/license/ayushsharma82/ElegantOTA.svg?style=for-the-badge" />
&nbsp;

</p>
<hr/>


<p align="center">Read & Write to NFC/RFID Cards Elegantly! </p>
<p align="center">
Tappy provides a simple interface to read/write to Mifare Classic cards through a windows machine with a device built using an Arduino & RC522 reader. It also comes with a firmware to use the device in a "dumb" mode where it simply outputs the data on the card through the USB port (Emulates a HID)
</p>

<br>

<h2>How to Install</h2>


###### Arduino tappy Reader Sketch
If you want to install the tappy reader sketch, Go to tappy_reader and download tappy_reader.ino.
Go to Sketch > Include Library > Library Manager > Search for "RC522" > Install (to install the RC522 Library).
Upload this sketch to the Arduino using the Arduino or your prefered IDE


###### Arduino tappy App Sketch
If you want to install the tappy app sketch (to use the reader with the desktop app), Go to tappy_app > tappy_app_arduino and download tappy_app.ino.
Go to Sketch > Include Library > Library Manager > Search for "RC522" > Install (to install the RC522 Library).
Upload this sketch to the Arduino using the Arduino or your prefered IDE




###### Windows tappy App

For Windows: First, download the [Arduino IDE](https://www.arduino.cc/en/software) and install it. Then, download [tappy_app.exe](https://github.com/uzairqidwai/tappy/raw/main/tappy_app/tappy_app_windows/tappy_app.exe) and run it. Be sure to plug in the reader before you run the software. (The arduino has to be programmed with tappy_app.ino for the desktop app to work)


###### Debug Windows tappy App

Download [tappy_app_debug.exe](https://github.com/uzairqidwai/tappy/raw/main/tappy_app/tappy_app_windows/tappy_app_debug.exe) and run. This will run the app with console so you can see what errors are being thrown by the software. Feel free to raise an issue if you can't figure it out!

<br>
<br>

<h2>Usage</h2>


###### Arduino tappy Reader Sketch
To use tappy in reader mode, ensure you have tappy_reader.ino programmed on the device. Once it is programmed, you should be able to tap any programmed NFC/RFID card on the reader and have the data output via USB. When plugged into a device (Android, Windows, etc.), the device is recognized as a keyboard and the data from the card is "typed" out. A buzzer will sound when the card is read.


###### Windows tappy App
To use the tappy Windows app, ensure you have tappy_app.ino programmed on the device, and tappy_app.exe downloaded. 
Plug the device into the computer and then run tappy_app.exe. Place the card on the reader and enter the data you want to write and press program. You should hear the buzzer when the card is programmed (leave the card on the reader while programming). 
To read the card, place it on the reader and press the read button. The data on the card will be output.

<b>YOU HAVE TO LIFT THE CARD OFF THE READER AND PUT IT BACK ON BETWEEN FUNCTIONS (IE. READ OR WRITE). IF YOU DO NOT DO THIS, THE APP WILL CRASH AND YOU WILL HAVE TO RECONNECT THE READER</b>


###### Crashes
If the tappy app crashes, unplug the device, and close the app. Plug the device back in, and run the app again.

If you want to debug the issue, download and run tappy_app_debug.exe. This will open the console and you can see the error that is thrown by the app.
 
<br>
<br>

<h2>Device (Under Development)</h2>

###### Parts for Device

[Arduino Pro Micro](https://www.amazon.com/gp/product/B09TKMM8N5/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)

[RC522 RFID Reader](https://www.amazon.com/gp/product/B07QBPGYBF/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)

[Buzzer](https://www.digikey.com/en/products/detail/tdk-corporation/PS1240P02CT3/2179628)


<br>

###### Additional Parts

[Mifare Classic 1k Cards](https://www.amazon.com/gp/product/B09BD9V8NM/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)

[PCB](https://github.com/uzairqidwai/tappy/raw/main/tappy_PCB_gerber.zip)

<br>

###### Schematic
<p align="left"><img src="https://raw.githubusercontent.com/uzairqidwai/tappy/main/tappy_schematic.svg" height="400" ></p>


<br>

###### PCB
[Gerber Files](https://github.com/uzairqidwai/tappy/raw/main/tappy_PCB_gerber.zip)
<p align="left"><img src="https://raw.githubusercontent.com/uzairqidwai/tappy/main/tappy_media/PCB_top.png" height="300" ></p>

<p align="left"><img src="https://raw.githubusercontent.com/uzairqidwai/tappy/main/tappy_media/PCB_bottom.png" height="300" ></p>


<br>

###### Case
 
 
 
<br>

<br/>
<br/>


<h2>License</h2>
tappy is licensed under The MIT License ( MIT ).
<br/>
<br/>
<img src="https://img.shields.io/github/license/ayushsharma82/ElegantOTA.svg?style=for-the-badge" />
</div>
