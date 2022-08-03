import collections.abc
import pptx
import os
from PIL import Image
import requests
from io import BytesIO
import shutil
import json

def make_ppt(width:str,ratio:str):

    with open('./image/link.json','r') as f:
        link=json.load(f)

    ppt=pptx.Presentation()
    # 默认比例为4:3，根据图片大小把ppt尺寸修改为16:9
    if ratio=='0.5625':
        ppt.slide_height=6858000
        ppt.slide_width=12192000

    if os.path.exists('./image'):
        shutil.rmtree('./image')
    os.mkdir('./image')

    for data in link:
        if data['width']==width and data['ratio']==ratio:
            img_src=data['url']
            image=Image.open(BytesIO(requests.get(img_src).content))
            image=image.resize((1920,1080),resample=Image.Resampling.BICUBIC)

            file='./image/'+str(data['id'])+'.png'
            image.save(file)
            slide = ppt.slides.add_slide(ppt.slide_layouts[3])
            slide.shapes.add_picture(file,0,0,ppt.slide_width,ppt.slide_height)

    ppt.save('./image/result.pptx')