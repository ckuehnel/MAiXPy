# MAiX_Dock_Snapshots.py
# This sample program takes periodically shapshots from OV2640 camera
# and displays them on 2.4" LCD.
# The first 100 frames will be saved into file capture.avi.
# Source: https://maixpy.sipeed.com/en/libs/machine_vision/image.html#routine-2-display-fps
# Small adaptions: Claus Kuehnel 2019-04-09 info@ckuehnel.ch

print('MAiXPy Imaging Sample')
print('Initialization...')

import sensor
import image
import lcd
import clock, time
import video

lcd.init()
clock = clock.clock()

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
sensor.skip_frames(30)
v = video.open("/sd/capture.avi", record=1, interval=200000, quality=50)
i = 0

print('Initialization done.')
print('MAiXPy imaging app running...')

tim = time.ticks_ms()

while True:
  tim = time.ticks_ms()
  clock.tick()
  img = sensor.snapshot()
  fps = clock.fps()
  img.draw_string(2,2,'MAiXPy Real Time Imaging', color=(0, 255,0))
  img.draw_string(2,10,'Rate = {:2.1f} fps'.format(fps), color=(0,255,0))
  lcd.display(img)
  if i < 100:
    img_len = v.record(img)
    print("record",i, time.ticks_ms() - tim)
    i += 1
  if i == 100:
    print('Recording finished')
    v.record_finish()
    i = 200


