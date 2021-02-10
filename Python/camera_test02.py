import time
import picamera

print("running pic 1")

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.image_effect = 'colorswap' #this is where you put the code for the effect   
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('test1.jpg')

print("done with pic 1")

print("running pic 2")

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.image_effect = 'pastel'
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('test2.jpg')

print("done with pic 2")

print("running pic 3")

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.image_effect = 'gpen'
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('test3.jpg')

print("done with pic 3")

print("running pic 4")

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.image_effect = 'solarize'
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('test4.jpg')

print("done with pic 4")

print("running pic 5")

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.image_effect = 'cartoon'
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('test5.jpg')

print("done with pic 5")
