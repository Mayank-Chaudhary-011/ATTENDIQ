import streamlit as st

def header_home():

    logo_url = "https://i.ibb.co/LDpKN5xc/Copilot-20260508-102938.png"
    st.markdown(f"""
    <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:10px">
        <img src ='{logo_url}' style='height:100px'/>
        <h1 style="text-align:center; color:#E0E3FF">AttendIQ</h1>
    </div>
    """ , unsafe_allow_html=True)

def header_dashboard():

    logo_url = "https://i.ibb.co/LDpKN5xc/Copilot-20260508-102938.png"
    st.markdown(f"""
    <div style="display:flex; align-items:center; justify-content:center; gab:10px;">
        <img src ='{logo_url}' style='height:85px'/>&nbsp;&nbsp;&nbsp;
        <h2 style="text-align:left; color:#5865F2";>AttendIQ</h2>
    </div>
    """ , unsafe_allow_html=True)