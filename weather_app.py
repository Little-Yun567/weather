import streamlit as st
import requests
import datetime

# ---------- 基本設定 ----------
st.set_page_config(page_title="可愛天氣小助手 ☁️", page_icon="🌸", layout="centered")

st.markdown("""
    <style>
    html, body {
        background-color: #fffaf3;
    }
    .title {
        font-size: 2.2em;
        color: #ff928b;
        text-align: center;
        margin-bottom: 0.5em;
    }
    .subtitle {
        font-size: 1em;
        color: #888888;
        text-align: center;
        margin-bottom: 2em;
    }
    .stTextInput>div>div>input {
        border-radius: 1rem;
        border: 2px solid #ffcab4;
    }
    .stButton button {
        border-radius: 1.5rem;
        background-color: #ffcab4;
        border: none;
        padding: 0.6em 1.5em;
        color: #fff;
        font-weight: bold;
    }
    .stButton button:hover {
        background-color: #ffa58d;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- App 內容 ----------
st.markdown('<div class="title">☀️ 可愛天氣小助手 1.0</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">輸入城市，馬上知道天氣如何～</div>', unsafe_allow_html=True)

API_KEY = "68a25f3ccff109a6bd1221889e65ea44"
city = st.text_input("輸入城市名稱（如 Taipei）")

if city:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=zh_tw&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        icon_code = data["weather"][0]["icon"]

        # 顯示天氣資訊
        st.success(f"{city} 的天氣：{weather}")
        st.metric("🌡️ 溫度", f"{temp}°C")
        st.metric("💧 濕度", f"{humidity}%")
        st.metric("🍃 風速", f"{wind_speed} m/s")

        # 顯示天氣圖示
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        st.image(icon_url, width=100)

        # 顯示當下時間
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        st.caption(f"最後更新時間：{now}")
    else:
        st.error("找不到城市，請檢查名稱是否正確！")

# 小 Yun 陪你報天氣（可以替換成你的角色圖）
st.image("https://i.imgur.com/hJmrZ5D.png", caption="by 小Yun", width=180)