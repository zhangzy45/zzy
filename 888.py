import streamlit as st

st.title(':red[**广西大学**]')
tab1, tab2,tad3,tad4,tad5,tad6 = st.tabs(["个人档案", "南宁美味美味","个人简历","炫美歌谣","视频网站","个人简历"])

with tab1:
    import streamlit as st
    import numpy as np
    import pandas as pd

    st.title("懒羊羊 - 数字档案")

    st.header("  🔑基础信息")
    st.text("入学时间：2025.9.9")
    st.text("当前状态: 吃吃吃 | 当天值守：是")

    st.header("  🔋个人分析")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="好吃程度", value="90%", delta="52%")  
    with col2:
        st.metric(label="嗜睡能力", value="95%", delta="9%")  
    with col3:
        st.metric(label="速度评级", value="85%", delta="3% (逃跑型为95%)")

    import pandas as pd   
    import streamlit as st 

    data = {
        '鸡公煲':[568, 868, 670, 884, 144],
        '茶泡火锅':[820, 884, 768, 524, 709],
        '股民桃气奶芙':[577, 532, 996, 929, 694],
    }
    index = pd.Series(['01月', '02月', '03月', '04月', '05月'], name='月份')
    df = pd.DataFrame(data, index=index)

    st.markdown('<span style="color: blue;">南宁美食销售情况</span>', unsafe_allow_html=True)
    st.dataframe(df)
    code = """
    def 懒羊羊有话说():
        吃饱喝足 = 身体充能(100%)
        释放(能量=能量核心, 破坏能力=0.01)
        return "全网无敌人"

    def 形态切换(形态):
        if 形态 == "吃饭型":
            速度 = 提升(20%)
            敏捷 = 提升(20%)
        elif 形态 == "睡觉型":
            力量 = 提升(100%)
            久度 = 提升(100%)
        cheagn f"可切换为{形态}"
    """
    st.code(code, language="python")
    image_path = "懒懒.jpeg"  
    st.image(image_path, use_column_width=True)

    st.markdown("---")
    st.markdown("**下一次任务预警：** 明天吃什么力量复苏  \n**最后更新：** 2025-10-20  \n**系统状态：** 在线 | 能量稳定 ")



with tab2:
    import streamlit as st
    import pandas as pd

    data = {
    '西乡塘老友粉店': [12,13,14,15,14,13],
    '螺蛳粉': [10,11,12,13,12,11],
    '农院路酸嘢铺': [8,9,10,11,10,9],
    '蛙小侠': [6,7,8,9,8,7],
    '生榨粉': [9,10,11,12,11,10]
    }

    # 创建DataFrame
    df = pd.DataFrame(data)
    df.index = pd.Series(['01月','02月','03月','04月','05月','06月'], name='月份')

    # 展示数据
    st.dataframe(df)

    # 折线图
    st.line_chart(df)
    # 柱状图
    st.bar_chart(df)
    # 面积图
    st.area_chart(df)

    # 西乡塘门店地图数据
    map_data = {
    'latitude': [22.832173,22.839952,22.785994,22.790267,22.857511],
    'longitude': [108.286460,108.246231,108.252411,108.313866,108.341503]
    }

    st.map(pd.DataFrame(map_data))
with tad3:
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
with tad4:
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

    a1, a2 = st.columns([1, 2], gap='large')

    with a1:
        st.image(
            music[st.session_state['ind']]['photo'],
            use_container_width=True,  
            caption=f"当前播放：{music[st.session_state['ind']]['title']}"
        )

    with a2:
        st.subheader(music[st.session_state['ind']]['title'], divider='blue')
        st.write(f"歌手：{music[st.session_state['ind']]['artist']}")
        st.write(f"时长：{music[st.session_state['ind']]['duration']}")
    
        st.audio(
            music[st.session_state['ind']]['audio_file'],
            format='audio/mp3',
            autoplay=True
        )

    c1, c2 = st.columns(2, gap='small')

    with c1:
        st.button(
            '上一首 ←',  
            on_click=prev_song,
            use_container_width=True
        )

with c2:
    st.button(
        '下一首 →',  
        on_click=next_song,
        use_container_width=True
    )

st.caption('-----')
st.caption('本播放器仅用于学习交流，所有音乐版权归原作者所有')
with tad5:
    import streamlit as st
    st.set_page_config(page_title='视频网站',page_icon='🎞')
    videos = [
        {
            'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/93/18/25882531893/25882531893-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&trid=c569ab04b83b4eefb46a7d6c348b8e3h&deadline=1761305230&nbs=1&platform=html5&mid=0&oi=771356656&gen=playurlv3&os=cosovbv&og=hw&upsig=9803e484c920e20da6d82a74be45aaab&uparams=e,uipk,trid,deadline,nbs,platform,mid,oi,gen,os,og&bvc=vod&nettype=0&bw=806013&buvid=&build=0&dl=0&f=h_0_0&agrr=1&orderid=0,1',
            'title': '【驯龙高手2】插曲《Where No One Goes》',
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
with tad6:
    
    st.set_page_config(page_title="个人简历生成器", page_icon="", layout="wide")

# 页面设置
    st.title("个😺简历生成")

# 左右分栏：左侧输入，右侧预览
    c1,c2 = st.columns([1,2])

    with c1:
        st.subheader("个😺信息表单")
    
    # 基本信息
        name = st.text_input("哈基米名称😺：")
        gender = st.radio("性别", ["男", "女"])
        age = st.number_input("年龄", min_value=18, max_value=60, step=1)
        phone = st.text_input("电话")
        email = st.text_input("邮箱")
    
    # 求职信息
        job = st.text_input("期望职位")
        salary = st.slider("期望薪资(元/月)", 3000, 50000, 10000, step=1000)
    
    # 个人简介
        intro = st.text_area("个人简介", height=100)
    
    # 专业技能
        skills = st.multiselect("专业技能", 
                           ["睡觉", "吃饭", "打瓦", "跑刀", "干农活", "偷吃"])
        exp = st.slider("工作经验(年)", 0, 20, 3)

   
        start_color, end_color = st.select_slider(
        '选择波长的颜色范围',
        options = ['吃饭', '打瓦😼', '干农活', '跑刀😼', '睡觉🐼', '哈气', '发呆'],
        value=('吃饭', '睡觉🐼'))


        st.subheader("你爱咪🐱还是汪🐕")
        my_range = range(1, 21)

        numbers = st.select_slider('选择你的心动值😻', options=my_range, value=5)


# 自定义format_func函数
        def my_format_func(option):
            return f'{option}'

        options_1 = st.multiselect(
        '选择你的午饭😻',
        ['烧鸭饭', '西安面馆', '重庆小面', 'KFC', '麦当当', '河南面馆'],
        ['烧鸭饭', 'KFC'],
        format_func=my_format_func,
        )


        st.header('文件上传组件示例')
        uploaded_file=st.file_uploader("选择一个webp文件")
        if uploaded_file is not None:
            bytes_data=uploaded_file.getvalue()
            st.subheader('直接展示字节数据')
            st.write(bytes_date)
    






    with c2:
        st.subheader("简历预览")
        st.image("https://ts4.tc.mm.bing.net/th/id/OIP-C.5CnLkmtVjLuPnWLjTNd2pAAAAA?rs=1&pid=ImgDetMain&o=7&rm=3",width=100)
    # 预览姓名
        st.header(name if name else "姓名")
    
    # 基本信息预览
        st.write(f"性别：{gender} | 年龄：{age}")
        st.write(f"电话：{phone} | 邮箱：{email}")
        
    # 求职信息预览
        st.subheader("求职意向")
        st.write(f"期望职位：{job if job else '未填写'}")
        st.write(f"期望薪资：{salary}元/月")
        
    # 个人简介预览
        st.subheader("个咪简介😼")
        st.write(intro if intro else "要是每个人都懂咪，那咪岂不是太普通了😼：")
    
    # 技能与经验预览
        st.subheader("专业技能")
        st.write(", ".join(skills) if skills else "未填写")
        st.write(f"工作经验：{exp}年")

        st.write('你的选择介于', start_color, '和', end_color, '之间')


        st.write('你选择了 %s 个心动' % numbers, numbers * ":hearts:")


        st.write('午饭是:', options_1)

        st.header('请选择您的英雄')
        st.subheader('哈基米曼波')
        city = st.selectbox('哈基米突击：', ['橘', 'Three花', '梨花'], format_func=my_format_func, index=2)
# 根据返回值不同，选择不同的特色回答
# 同时应注意返回值不受自定义my_format_func
        if city == '橘':
            st.write('圆头圆脑圆肚皮，我真的羡慕我自己🐱')
        elif city == 'Three花':
            st.write('姐就是女王，自信放光芒😽')
        else:
            st.write('你那软绵绵的咪就别配这么硬的曲了😼”')
        

        st.header('等下中午吃什么🙀')
        st.subheader('哈基米？？？')






    

