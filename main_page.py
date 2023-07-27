import streamlit as st
import requests
# import sqlConnection
from streamlit_folium import st_folium
import folium

# if __name__ == '__main__':
#     print(__name__)
#     main()

# def main():
    
#     sqlConnection.connect()

# option = st.selectbox("정류장 위치" , ['행정동', '1단지'])

m = folium.Map(location=[36.99139, 126.35882], zoom_start = 16) #zoom_start 확대 범위 최대 18
folium.Marker(
    [36.99139, 126.35882],
    popup="행정동", # 마우스 클릭 시 
    tooltip="행정동" # 마우스 오버 시 
).add_to(m)

folium.Marker(
    [36.77507, 126.44410],
    popup="보건소", # 마우스 클릭 시 
    tooltip="보건소" # 마우스 오버 시 
).add_to(m)

st_data = st_folium(m, width=725)

lat1 = '36.99139'
long1 = '126.35882'
lat2 = '36.77507'
long2 = '126.44410'

def get_directions_response(lat1, long1, lat2, long2, mode='drive'):
   url = "https://route-and-directions.p.rapidapi.com/v1/routing"
   key = "fba337f228msh43095716c977e25p1fd1d4jsn54bf08f8e1a4"
   host = "route-and-directions.p.rapidapi.com"
   headers = {"X-RapidAPI-Key": key, "X-RapidAPI-Host": host}
   querystring = {"waypoints":"{str(lat1)},{str(long1)}|{str(lat2)},{str(long2)}","mode":mode}
   response = requests.request("GET", url, headers=headers, params=querystring)
   return response
response = get_directions_response(52.4013, 4.5425, 52.402, 4.5426)