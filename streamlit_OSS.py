import streamlit as st

OSS_Score = [80, 70, 55, 30, 3, 3, 1, 0]

st.write("# OSS 중간시험 결과")
st.write("## 얘들아 공부좀 하자")
st.write("### OSS 중간시험 결과")


OSS_Score

st.bar_chart(OSS_Score)
