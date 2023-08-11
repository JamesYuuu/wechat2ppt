import streamlit as st
from common.wechatpicture import PictureSpider
from common.picture2ppt import ppt

def create_ppt(url):
    Spider=PictureSpider(url)
    link=Spider.get_pictures()

    width=[item['width'] for item in link]
    ratio=[item['ratio'] for item in link]

    most_width = max(width,key=width.count)
    most_ratio = max(ratio,key=ratio.count)

    pptx=ppt(link,most_width,most_ratio)
    pptx.make_ppt()

st.write('''
# 把微信公众号文章转换成PPT
''')

url = st.text_input("**请输入微信公众号文章链接**")

if st.button(label='开始转换'):
    try:
        with st.spinner("正在转换中..."):
            create_ppt(url)
        st.success("转换成功，请点击下方按钮下载")
        with open("./image/result.pptx","rb") as f:
            try:
                st.download_button(
                    label="下载PPT",
                    data=f,
                    file_name="result.pptx",
                    mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                )
            except Exception as e:
                st.error("下载失败，请重试")
    except Exception as e:
        st.error("转换失败，请检查链接是否正确")