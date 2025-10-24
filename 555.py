import streamlit as st

st.set_page_config(page_title="音乐播放器", page_icon='🎵')

music = [
    {
        'title': '我知道',
        'artist': 'BY2',
        'duration': '3:46',
        'audio_file': 'https://music.163.com/song/media/outer/url?id=2643537823.mp3',
        'photo': 'https://p1.music.126.net/icdfSZmawPHdYCkQB-E-RA==/109951163200171219.jpg'
    },
    {
        'title': '像晴天像雨天',
        'artist': '江苏泷',
        'duration': '3:11',
        'audio_file': 'https://music.163.com/song/media/outer/url?id=268458378.mp3',
        'photo': 'https://p2.music.126.net/gN6htv5E9WwyOoTASMuvDQ==/109951170483576228.jpg'
    },
    {
        'title': '有些',
        'artist': '粉笔',
        'duration': '2:18',
        'audio_file': 'https://music.163.com/song/media/outer/url?id=2604234517.mp3',
        'photo': 'https://p2.music.126.net/rs_lGvUgkttfbO1YsgsrVg==/109951169743264606.jpg'
    }
]

if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

def next_song():
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(music)

def prev_song():
    st.session_state['ind'] = (st.session_state['ind'] - 1) % len(music)

col1, col2 = st.columns([1, 2], gap='large')

with col1:
    st.image(
        music[st.session_state['ind']]['photo'],
        use_container_width=True,  # 修正参数
        caption=f"当前播放：{music[st.session_state['ind']]['title']}"
    )

with col2:
    st.subheader(music[st.session_state['ind']]['title'], divider='blue')
    st.write(f"歌手：{music[st.session_state['ind']]['artist']}")
    st.write(f"时长：{music[st.session_state['ind']]['duration']}")
    
    st.audio(
        music[st.session_state['ind']]['audio_file'],
        format='audio/mp3',
        autoplay=True
    )

btn_col1, btn_col2 = st.columns(2, gap='small')

with btn_col1:
    st.button(
        '上一首 ←',  # 简化符号
        on_click=prev_song,
        use_container_width=True
    )

with btn_col2:
    st.button(
        '下一首 →',  # 简化符号
        on_click=next_song,
        use_container_width=True
    )

st.caption('-----')
st.caption('本播放器仅用于学习交流，所有音乐版权归原作者所有')
