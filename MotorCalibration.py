import PiMotor
import RPi.GPIO as GPIO
import config

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

left_motor = PiMotor.Motor("MOTOR1",2)
right_motor = PiMotor.Motor("MOTOR2",1)
cal = config.read("motor")

input("Find a long space to calibrate the motors. When you press enter the calibration will commence.")

while True:
    left_motor.forward(40 + cal)
    right_motor.forward(40)
    drift_direc = input("Write the direction the robot is drifting in or press enter when the drift is negligible. ")
    left_motor.stop()
    right_motor.stop()
    if drift_direc != "right" and drift_direc != "left":
        break
    else:
        scale = input("On a scale of 1-10 how much is it drifting: ")
        if drift_direc == "right":
            cal -= int(scale)
        else:
            cal += int(scale)
        input("To make sure the motors have been adjusted properly, and allow for further adjustment, the test will be run again after you press enter.")

print("Calibration finished, Offset for left motor is:", cal)
config.write("motor", cal)
GPIO.cleanup()

