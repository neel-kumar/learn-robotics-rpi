import PiMotor
import time
import RPi.GPIO as GPIO
from ultrasonic_sensor import ultra
from gyro import go_straight
import config

ir1 = 1
ir2 = 14

GPIO.setup(ir1,GPIO.IN)
GPIO.setup(ir2,GPIO.IN)

m1 = PiMotor.Motor("MOTOR1",2) # Left Wheel
m2 = PiMotor.Motor("MOTOR2",1) # Right Wheel

ultra = ultra()
ultra_dist = config.read("ultra")
motor_cal = config.read("motor")

def turn_till_clear(ir1=ir1, ir2=ir2, ultra=ultra, speed=40, m1=m1, m2=m2, cal=motor_cal):
    m1.forward(speed+cal)
    m2.reverse(speed)
    while GPIO.input(ir1) == 0 or GPIO.input(ir2) == 0 or ultra.get_dist() < 5:
        time.sleep(0.01)
    m1.stop()
    m2.stop()

print("Press Control-C to end the program")

speed = 40
ultra.start()

# Wait for Ultrasonic sensor to measure first distance
while ultra.get_dist() == None:            #print(euler)
    time.sleep(0.01)

m1.forward(speed+motor_cal)
m2.forward(speed)

try:
    while True:
        if GPIO.input(ir1) == 0 or GPIO.input(ir2) == 0 or ultra.get_dist() < ultra_dist:
            m1.stop()
            m2.stop()
            turn_till_clear()
            m1.forward(speed+motor_cal)
            m2.forward(speed)
except Exception as e:
    print("FAILURE:", e)
except KeyboardInterrupt as ki:
    pass
finally:
    ultra.stop()
    GPIO.cleanup()

