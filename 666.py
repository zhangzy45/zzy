import streamlit as st
st.set_page_config(page_title='视频网站',page_icon='🎞')
videos = [
    {
        'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/25/47/808744725/808744725-1-208.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&platform=html5&uipk=5&trid=dffe19d76f784313a79ea00b6c2aa0dh&og=cos&deadline=1761305042&oi=771356656&mid=0&nbs=1&gen=playurlv3&os=cosovbv&upsig=7a84200daa703502a51c757355cf35d1&uparams=e,platform,uipk,trid,og,deadline,oi,mid,nbs,gen,os&bvc=vod&nettype=0&bw=479740&build=0&dl=0&f=h_0_0&agrr=1&buvid=&orderid=0,1',
        'title': '【驯龙高手】主题曲史诗级REMIX - Epic Orchestra Remix',
        'episode': '主题'
    },
    {
        'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/60/00/1135210060/1135210060-1-208.mp4?e=ig8euxZM2rNcNbhVhbdVhwdlhzdghwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&deadline=1761302451&nbs=1&os=cosovbv&mid=0&oi=771356656&uipk=5&platform=html5&trid=21dd36fe9a1043d59b1495bcd3d8cf4h&gen=playurlv3&og=hw&upsig=c9f272d6ab9f392b5312eda212c607e1&uparams=e,deadline,nbs,os,mid,oi,uipk,platform,trid,gen,og&bvc=vod&nettype=0&bw=2417062&agrr=1&buvid=&build=0&dl=0&f=h_0_0&orderid=0,1',
        'title': '猫抓老鼠',
        'episode': '治愈'
    },
    {
        'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/15/34/1285573415/1285573415-1-192.mp4?e=ig8euxZM2rNcNbRBhbdVhwdlhWUghwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&oi=771356656&mid=0&nbs=1&gen=playurlv3&og=hw&platform=html5&deadline=1761302717&trid=a029318ba79a480681a867610994c74h&os=cosovbv&uipk=5&upsig=16a3441f4be315a9c9cea9c8f7614064&uparams=e,oi,mid,nbs,gen,og,platform,deadline,trid,os,uipk&bvc=vod&nettype=0&bw=1221273&agrr=1&buvid=&build=0&dl=0&f=h_0_0&orderid=0,1',
        'title': '【时光音乐会】G.E.M.邓紫棋《唯一》',
        'episode': '演唱会'
    }
]

if 'ind' not in st.session_state:
    st.session_state['ind'] = 0
st.title( videos[st.session_state['ind']]['title']+'-第' + videos[st.session_state['ind']]['episode']+'片段')
# 显示视频介绍
st.write("**剧情介绍：**", videos[st.session_state['ind']]['title'])

st.video(videos[st.session_state['ind']]['url'])

c1, c2, c3 = st.columns(3)

def play(arg):
    st.session_state['ind'] = int(arg)

for i in range (len(videos)):
    st.button('第'+str(i+1)+'片段',use_container_width=True,on_click=play,args=([i]))
