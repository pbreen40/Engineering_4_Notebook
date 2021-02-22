from gpiozero import MotionSensor
from picamera import PiCamera
import datetime

pir = MotionSensor(4)# Sets the motion sensors pin to 4
camera = PiCamera()# makes pi camera be identifiable as camera
now = datetime.datetime.now()# sets up date as to be indentified by now
filename = "intruder_" + str(now).replace(" ", "_") + ".h264"# makes the file name change based of the date taken

while True:
	pir.wait_for_motion()# waits for motion detection with motion sensor
	print("Motion detected!")
	camera.start_recording(filename)# starts recording
	pir.wait_for_no_motion()# when motion stops
	camera.stop_preview()# ends recording
