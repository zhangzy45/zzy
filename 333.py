import streamlit as st

st.set_page_config(page_title="快乐",page_icon="😊" )

images = [
{'url':'https://vip.123pan.cn/1821652950/123pan/123panlikebizhi/231223004004.jpg',
 'parm':'熊出没'},
{'url':'https://wenhui.whb.cn/u/cms/www/202011/19152600az6b.jpg',
 'parm':'猫和老鼠'},
{'url':'https://wallpaperaccess.com/full/36372.jpg',
 'parm':'洞庭湖边'},
{'url':'https://img.52desk.com/tp/2325053sNh5.jpg',
 'parm':'懒洋洋'}
]

if 'ind' not in st.session_state:
    st.session_state.ind = 0

def next_img():
    st.session_state.ind = (st.session_state.ind + 1) % len(images)

def prev_img():
    st.session_state.ind = (st.session_state.ind - 1) % len(images)


st.image(images[st.session_state['ind']]['url'],caption=images[st.session_state['ind']]['parm'])


c1, c2 = st.columns(2)
with c1:
    st.button("上一张", on_click=prev_img)
with c2:
    st.button("下一张", on_click=next_img)
