import streamlit as st
import pandas as pd

# 准备南宁西乡塘5家门店数据
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

