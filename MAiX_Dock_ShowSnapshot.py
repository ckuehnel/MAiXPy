# MAiX_Dock_ShowSnapshot.py
# Source: OpenMV copy2fb.py
# Some adaptions: Claus Kuehnel 2019-04.10 info@ckuehnel.ch

import image
import lcd

print('MAiX Show Snapshot')

lcd.init()

img = image.Image("/sd/example.jpg", copy_to_fb=True)

lcd.display(img)

