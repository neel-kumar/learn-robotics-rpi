import PiMotor
import time
import RPi.GPIO as GPIO
from gyro import go_straight, turn_by_angle
import config

left_wheel = PiMotor.Motor("MOTOR1",2)
right_wheel = PiMotor.Motor("MOTOR2",1)
motor_cal = config.read("motor")

try:
    while True:
        thing_2_do = input("Enter f/b/l/r to go forward/backward/left/right, anything else will end the program: ")
        if thing_2_do == 'f':
            forward_time = input("How long(in seconds): ")
            new_sensor, thread = go_straight(50, left_wheel, right_wheel, motor_cal)
            time.sleep(int(forward_time))
            thread.stop()
            sensor = new_sensor
        elif thing_2_do == 'b':
            backward_time = input("How long(in seconds): ")
            new_sensor, thread = go_straight(50, left_wheel, right_wheel, motor_cal, direc="backward")
            time.sleep(int(backward_time))
            thread.stop()
            sensor = new_sensor
        elif thing_2_do == 'l':
            angle = input("Angle: ")
            turn_by_angle('l', int(angle), left_wheel, right_wheel, motor_cal)
        elif thing_2_do == 'r':
            angle = input("Angle: ")
            turn_by_angle('r', int(angle), left_wheel, right_wheel, motor_cal)
        else:
            break
except Exception as e:
    print('ERROR:', e)
finally:
    left_wheel.stop()
    right_wheel.stop()
    GPIO.cleanup()

