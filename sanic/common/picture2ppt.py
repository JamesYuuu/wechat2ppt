import collections.abc
import pptx
import os
from PIL import Image
import requests
from io import BytesIO
import shutil

def make_ppt(link,width,ratio):
    ppt=pptx.Presentation()
    if ratio==0.5625:  # 16:9
        ppt.slide_height=6858000
        ppt.slide_width=12192000

    if os.path.exist('./image'):
        shutil.rmtree('./image')
    
    os.mkdir('./image')

    for data in link:
        if data['width']==width and data['ratio']==ratio:
            img_src=data['url']
            image=Image.open(BytesIO(requests.get(img_src).content))
            image.save('./image/'+str(data['id'])+'.png')
            slide = ppt.slides.add_slide(ppt.slide_layouts[3])
            slide.shapes.add_picture(f'.\image\{file}',0,0,ppt.slide_width,ppt.slide_height)

        slide=ppt.slide_layouts[6]
        slide.placeholders[1].insert_picture(f'./image/{i}.png')
    
    ppt.save('/image/输出.pptx')