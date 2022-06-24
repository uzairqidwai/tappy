<p align="center"><img src="https://raw.githubusercontent.com/uzairqidwai/tappy/main/tappy_media/tapy_logo.png" width="400"></p>

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
Tappy provides a simple interface to read/write to Mifare Classic cards through a windows machine with a device built using an Arduino & RC522 reader. It also comes with a firmware to use the device in a "dumb" mode where it simply outputs whatever is read through the USB port (Emulates a HID)
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

For Windows: Download [tappy_app.exe](https://github.com/uzairqidwai/tappy/raw/main/tappy_app/tappy_app_windows/tappy_app.exe) and run. Be sure to plug in the reader before you run the software. (The arduino has to be programmed with tappy_app.ino for the desktop app to work)


###### Debug Windows tappy App

Download [tappy_app_debug.exe](https://github.com/uzairqidwai/tappy/raw/main/tappy_app/tappy_app_windows/tappy_app_debug.exe) and run. This will run the app with console so you can see what errors are being thrown by the software. Feel free to raise an issue if you can't figure it out!

<br>
<br>

<h2>Usage</h2>
<p>ElegantOTA is a dead simple library which does your work in just 1 Line. Honestly, It's just a wrapper library which injects it's own elegant webpage instead of the ugly upload page which comes by default in Arduino Library.</p>

 Include ElegantOTA Library `#include <ElegantOTA.h>` at top of your Arduino Code.
 
 Paste this - `ElegantOTA.begin(&server);`  line above your `server.begin();`
 
 That's all!

<hr/>

Now copy the IPAddress displayed over your Serial Monitor and go to `http://<IPAddress>/update` in browser. ( where `<IPAddress>` is the IP of your ESP Module)

<hr/>

By default, ElegantOTA uses your chip id as a unique id for your esp chip on webpage. If you want to set a custom id, then you can set it via `ElegantOTA.setID("abcd123");`. Best to place it above `ElegantOTA.begin` function.

 
<br>

<br/>
<br/>


<h2>License</h2>
ElegantOTA is licensed under The MIT License ( MIT ).
<br/>
<br/>
<img src="https://img.shields.io/github/license/ayushsharma82/ElegantOTA.svg?style=for-the-badge" />
</div>
