from MinIMU_v5 import MinIMU_v5
import time
            


IMU = MinIMU_v5(i2cBusNum = 0, aFullScale = 4, gFullScale = 2000, mFullScale = 16,
        gOdr = 8, aOdr = 8, mOdr = 7)



print(IMU.gScale)


while True:
    print(IMU.gyroAngle()[2])
    time.sleep_ms(50)