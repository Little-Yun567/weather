# -*- coding: utf-8 -*-
import streamlit as st
import requests
import datetime
from googletrans import Translator

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
        padding: 0.5em;
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

# ---------- App 標題 ----------
st.markdown('<div class="title">☀️ 可愛天氣小助手 1.0</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">輸入你所在的城市（支援中文），一起看今天的天氣吧～</div>', unsafe_allow_html=True)

# ---------- API 金鑰 ----------
API_KEY = st.secrets["API_KEY"]

# ---------- 使用者輸入 & 翻譯 ----------
translator = Translator()
user_city = st.text_input("🏙️ 請輸入城市名稱（可用中文，如：台北、首爾）")

if user_city:
    try:
        translated_city = translator.translate(user_city, dest="en").text
        st.write(f"🔎 查詢城市：{translated_city}")

        # ---------- 天氣查詢 ----------
        url = f"https://api.openweathermap.org/data/2.5/weather?q={translated_city}&appid={API_KEY}&lang=zh_tw&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            icon_code = data["weather"][0]["icon"]

            # 顯示天氣資訊
            st.success(f"📍 {user_city}（{translated_city}）的天氣是：{weather}")
            st.metric("🌡️ 溫度", f"{temp}°C")
            st.metric("💧 濕度", f"{humidity}%")
            st.metric("🍃 風速", f"{wind_speed} m/s")

            # 顯示天氣圖示
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
            st.image(icon_url, width=100)

            # 顯示當下時間
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            st.caption(f"🕒 最後更新時間：{now}")
        else:
            st.error("⚠️ 找不到這個城市喔，請確認拼字或再換個方式輸入看看～")

    except Exception as e:
        st.error("❌ 無法翻譯城市名稱，請稍後再試一次。")
        st.caption(f"錯誤訊息：{e}")

# ---------- 可愛角色結尾 ----------
st.markdown("---")
st.image("https://i.imgur.com/hJmrZ5D.png", caption="by 小Yun 陪你看天氣 ☁️", width=180)
