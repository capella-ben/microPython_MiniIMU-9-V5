# MinIMU-9-v5 MicroPython library for Raspberry Pi Pico

This is a port from [https://github.com/DarkSparkAg/MinIMU-9-v5](https://github.com/DarkSparkAg/MinIMU-9-v5)


## Summary

This is a library for the Raspberry Pi that helps interface with Pololu's [MinIMU-9 v5 Gyro, Accelerometer, and Compass (LSM6DS33 and LIS3MDL Carrier)](https://www.pololu.com/product/2738/resources). The library configures the LSM6DS33 and LIS3MDL chips and makes it simple to read the raw accelerometer, gyro, and magnetometer data through I&sup2;C.  The library is also capable of tracking yaw and angle in the background with multi-threading.

## Supported platforms

This library is designed to work with the Raspberry Pi Pico; I have not tested it with other versions.

## Getting started

### Hardware

Make the following connections between the Raspberry Pi Pico and the MinIMU-9 v5 board:

         Pico   MiniIMU-9-v5
         ----   ------------
          3V3 - VIN
          GND - GND
          SDA - SDA
          SCL - SCL

### Software

1. Download the lastest version of this software from github.
2. Copy the MinIMU_v5.py file to your pico.

