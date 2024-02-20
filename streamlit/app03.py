import streamlit as st

h = st.header("my wed site on Diffusion")
s = st.subheader("เว็บไซต์ส่วนตัว")
p = st.write("เว็บไซต์นี้แลกมาด้วยหยาดเหงื่อของข้าพเจ้า")
banner = st.image("https://picsum.phtos/800250")
b = st.button("click me")
text = st. text_input("primpt: ")
if text:
    st.write(f"กำลังสร้างภาพ...."{text}"")
    b = st.button("จะไปต่อหรือพอแค่นี้...")
    