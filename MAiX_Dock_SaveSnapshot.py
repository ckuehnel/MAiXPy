# MAiX_Dock_SaveSanpshot.py
# Source OpenMV Emboss Snapshot Example
# Some adaptions: Claus Kuehnel 2019-04.10 info@ckuehnel.ch

import sensor, image, time

print('MAiX Make a Snapshot running...')

sensor.reset() 
sensor.set_pixformat(sensor.RGB565) 
sensor.set_framesize(sensor.QVGA) 
sensor.run(1)
sensor.skip_frames(30) # Let new settings take affect.

for i in range (10):
  img = sensor.snapshot()
  img.draw_string(2,2,'Wait...{}'.format(10-i), color=(0, 255,0), scale = 1)
  if (i == 8):
     img.draw_string(2,20,'Cheese', color=(0, 255,0), scale = 2)
  lcd.display(img)
  time.sleep_ms(1000)

img = sensor.snapshot()
lcd.display(img)

img.save("example.jpg") 
print('Snapshot saved.')

