import config
import PiMotor
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Right Motor
if config.read("rightrev")[0] == "f":
    m2 = PiMotor.Motor("MOTOR2",1)
else:
    m2 = PiMotor.Motor("MOTOR2",2)

# Left Motor
if config.read("leftrev")[0] == "f":
    m1 = PiMotor.Motor("MOTOR1",1)
else:
    m1 = PiMotor.Motor("MOTOR1",2)


m1.forward(40)
m2.reverse(40)
direc = input("The robot should turn be turning right. Enter the direction it's turning: ")
m1.stop()
m2.stop()

if direc == "right":
    config.write("leftrev", "f")
    config.write("rightrev", "f")
elif direc == "left":
    config.write("leftrev", "t")
    config.write("rightrev", "t")
elif direc == "forward":
    config.write("leftrev", "f")
    config.write("rightrev", "t")
elif direc == "backward":
    config.write("leftrev", "f")
    config.write("rightrev", "t")
