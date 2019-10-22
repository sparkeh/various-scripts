import RPi.GPIO as GPIO
import time

pins = [8, 10, 12, 16, 18, 22, 24, 26]
pinsv2 = [10, 8, 16, 12, 22, 18, 26, 24]

def setup():
	GPIO.setmode(GPIO.BOARD)
	for pin in pins:
		GPIO.setup(pin, GPIO.OUT)
		GPIO.output(pin, GPIO.HIGH)

def loop():
	while True:
		for pin in pins:
			GPIO.output(pin, GPIO.LOW)
			time.sleep(0.1)
			GPIO.output(pin, GPIO.HIGH)
		for pin in reversed(pins):
			GPIO.output(pin, GPIO.LOW)
			time.sleep(0.1)
			GPIO.output(pin, GPIO.HIGH)
		for pin in pins:
                        GPIO.output(8, GPIO.LOW)
                        GPIO.output(26, GPIO.LOW)
                        time.sleep(0.1)
                        GPIO.output(10, GPIO.LOW)
                        GPIO.output(24, GPIO.LOW)
                        time.sleep(0.1)
                        GPIO.output(12, GPIO.LOW)
                        GPIO.output(22, GPIO.LOW)
                        time.sleep(0.1)
                        GPIO.output(16, GPIO.LOW)
                        GPIO.output(18, GPIO.LOW)
                        time.sleep(0.1)
			GPIO.output(pins, GPIO.HIGH)
               # for pin in pins:
                        GPIO.output(8, GPIO.HIGH)
                        GPIO.output(10, GPIO.HIGH)
                        GPIO.output(12, GPIO.HIGH)
                        GPIO.output(16, GPIO.HIGH)
                        GPIO.output(18, GPIO.HIGH)
                        GPIO.output(22, GPIO.HIGH)
                        GPIO.output(24, GPIO.HIGH)
                        GPIO.output(26, GPIO.HIGH)
			time.sleep(0.1)
                        GPIO.output(8, GPIO.LOW)
                        GPIO.output(10, GPIO.LOW)
                        GPIO.output(12, GPIO.LOW)
                        GPIO.output(16, GPIO.LOW)
                        GPIO.output(18, GPIO.LOW)
                        GPIO.output(22, GPIO.LOW)
                        GPIO.output(24, GPIO.LOW)
                        GPIO.output(26, GPIO.LOW)
			time.sleep(0.1)
                        GPIO.output(8, GPIO.HIGH)
                        GPIO.output(10, GPIO.HIGH)
                        GPIO.output(12, GPIO.HIGH)
                        GPIO.output(16, GPIO.HIGH)
                        GPIO.output(18, GPIO.HIGH)
                        GPIO.output(22, GPIO.HIGH)
                        GPIO.output(24, GPIO.HIGH)
                        GPIO.output(26, GPIO.HIGH)
                        time.sleep(0.1)
                        GPIO.output(8, GPIO.LOW)
                        GPIO.output(10, GPIO.LOW)
                        GPIO.output(12, GPIO.LOW)
                        GPIO.output(16, GPIO.LOW)
                        GPIO.output(18, GPIO.LOW)
                        GPIO.output(22, GPIO.LOW)
                        GPIO.output(24, GPIO.LOW)
                        GPIO.output(26, GPIO.LOW)
                        time.sleep(0.1)
                        GPIO.output(16, GPIO.HIGH)
                        GPIO.output(18, GPIO.HIGH)
                        time.sleep(0.1)
                        GPIO.output(22, GPIO.HIGH)
                        GPIO.output(12, GPIO.HIGH)
                        time.sleep(0.1)
                        GPIO.output(24, GPIO.HIGH)
                        GPIO.output(10, GPIO.HIGH)
                        time.sleep(0.1)
                        GPIO.output(8, GPIO.HIGH)
                        GPIO.output(26, GPIO.HIGH)
                        time.sleep(0.1)
                        GPIO.output(pin, GPIO.HIGH)
def destroy():
	for pin in pins:
		GPIO.output(pin, GPIO.HIGH)
	GPIO.cleanup()

if __name__ == '__main__':
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
