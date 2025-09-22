from picamera import PiCamera
from time import sleep
camera=PiCamera()
camera.start_preview(alpha=192)
sleep(5)
camera.capture("/home/smita/Desktop/pic1.jpg") # replace with a valid path 
camera.stop_preview()
