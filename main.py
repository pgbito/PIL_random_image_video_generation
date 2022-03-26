import cv2
from PIL import Image, ImageDraw
import numpy as np
import io
import PIL.Image
import random
maxcolorview = 150


def rf(): 
    return (random.choice(list(range(0, maxcolorview))), random.choice(
    list(range(0, maxcolorview))), random.choice(list(range(0, maxcolorview))))


frames = []
fc = 1  # 3 mins
fps = 30
r = (1920, 1080)
fcd = round(fps*(fc*60))
left = fcd
for f in range(fcd):
    print(f'Frames left: {left}', end='\r')
    left = left - 1
    i = PIL.Image.new('RGB', r, rf())
    stream = io.BytesIO()
    i.save(stream, format='PNG')

    frames.append(stream)
    i.close()



fourcc = cv2.VideoWriter_fourcc(*'avc1')

video = cv2.VideoWriter("test.mp4", fourcc, fps, r)

for s in frames:
    i = PIL.Image.open(io.BytesIO(s.getvalue()))
    ic = i.copy()

    video.write(cv2.cvtColor(np.array(ic), cv2.COLOR_RGB2BGR))
video.release()
