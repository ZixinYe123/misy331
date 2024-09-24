import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
@st.cache_data
def load_data():
  data = pd.read_csv('housing.csv')
  return data
df = load_data()
st.title('California Housing Data(1990) by Zixin Ye')
min_house_value = st.slider("Minimal Median House Value", 0, 500001, 200000)

location_types = df['ocean_proximity'].unique().tolist()  # 获取所有位置类型
selected_location_types = st.multiselect("Choose the location type", location_types, default=location_types)

# 单选按钮：选择收入等级
income_level = st.radio(
    "Choose income level",
    ("Low ", "Medium ", "High ")
)

# 根据收入等级过滤数据
if income_level == "Low ":
    filtered_df = df[df['median_income'] <= 2.5]
elif income_level == "Medium ":
    filtered_df = df[(df['median_income'] > 2.5) & (df['median_income'] < 4.5)]
else:
    filtered_df = df[df['median_income'] > 4.5]

# 进一步根据用户选择的房价和位置类型过滤数据
filtered_df = filtered_df[
    (filtered_df['median_house_value'] >= min_house_value) &
    (filtered_df['ocean_proximity'].isin(selected_location_types))
]

# 绘制房屋中位价格的直方图
st.subheader("Histogram of Median House Values")
fig, ax = plt.subplots(figsize=(10, 6))

# 设置Seaborn样式
sns.set(style="whitegrid")

# 绘制直方图
ax.hist(filtered_df['median_house_value'], bins=30, edgecolor='black')
ax.set_xlabel("Median House Value")
ax.set_ylabel("Number of Houses")

# 显示图表
st.pyplot(fig)