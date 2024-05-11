import streamlit as st 
import requests
st.set_page_config(layout='wide')
# MAIN
main=st.container()
with main:
    st.title("Tra cứu thông tin thời tiết")

api_key='33f1ebf370a26a00554189497227db6f'

with st.sidebar.container():
    st.image('https://brands.home-assistant.io/_/openweathermap/logo.png', width=200) 
    st.divider()

    city_name = st.text_input('Nhập tên thành phố: ')
    btn_search=st.button('Xem thông tin')
# Click button
if btn_search:
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&lang=vi&units=metric'
    response=requests.get(url)
    data=response.json()
    if data['cod'] == '404':
        st.error('Không tìm thấy thành phố')
    else:
    # Bóc tách dữ liệu
        temp= data['main'] ['temp']
        humidity= data['main'] ['humidity']
        description = data['weather'] [0] ['description']
        name=data['name']
        # Hiển thị dữ liệu
        st.header(f':blue-background[Thời tiết tại: {name}]')
        st.header(f':gray-background[Mô tả: {description}]')
        st.metric(label="Nhiệt độ", value=f"{temp} °C")
        st.metric(label="Độ ẩm", value=f"{humidity} %")