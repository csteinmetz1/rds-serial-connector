# rds-serial-connector
Send serial messages over RS-232 to update DPS text from WSBF now playing

## Overview

WSBF uses the [Inovonics 730](http://www.inovonicsbroadcast.com/model/730) in order to transmit [Radio Data System (RDS)](https://en.wikipedia.org/wiki/Radio_Data_System) messages over our FM broadcast.  In addition to providing a static text message of the station ID and phone number, the system has the ability to display a scrolling message of the current playing track and artist. In order to update this text dynamically a serial connection (over RS-232) can be made between a computer and the 730. This allows for control over a number of system settings, including the Dynamic PS message (DPS). This program interfaces with the WSBF API to grab the current song title and artist that is being played and construct an appropriate serial message to be sent over a local COM port to the 730. 

Details about the operation of the 730 can be found in the [manual](http://www.inovonicsbroadcast.com/uploads/2017/04/03/730%20Manual%20Rev.%203%20(5.13.14).pdf).

## Install & Usage

Clone this repository.

```
git clone https://github.com/csteinmetz1/rds-serial-connector
```

Install requirements,
```
pip install -r requirements.txt
```

Make a connection from the PC to the 730 via RS-232 port. We are using this [interface](https://www.amazon.com/dp/B0007T27H8).

Start sending messages.
```
python connector.py
```