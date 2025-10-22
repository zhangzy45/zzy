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


