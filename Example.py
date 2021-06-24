
from MinIMU_v5 import MinIMU_v5
import time
            


IMU = MinIMU_v5(i2cBusNum = 0, aFullScale = 4, gFullScale = 1000, mFullScale = 16,
        gOdr = 8, aOdr = 8, mOdr = 7)

while True:
        print(IMU.angle())
        time.sleep_ms(50) 




