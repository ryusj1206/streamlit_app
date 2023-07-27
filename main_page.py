import streamlit as st
import requests
import pandas as pd
# import sqlConnection
from streamlit_folium import st_folium
import folium

# Using object notation
st.sidebar.title ("한화토탈 출/퇴근 노선표")
add_selectbox = st.sidebar.selectbox(
    "노선을 선택해주세요",
    ("주간 출근", "주간 퇴근")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "노선",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

option = st.selectbox("정류장 위치" , ['행정동', '1단지'])

m = folium.Map(location=[36.99139, 126.35882], zoom_start = 13) #zoom_start 확대 범위 최대 18

# featG = folium.FeatureGroup(name = 'featGrp1')
# m.add_child(featG)

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

# def get_directions_response(lat1, long1, lat2, long2, mode='drive'):
#    url = "https://map.kakao.com/link/map/{},{}"
#    key = "fba337f228msh43095716c977e25p1fd1d4jsn54bf08f8e1a4"
#    host = "route-and-directions.p.rapidapi.com"
#    headers = {"X-RapidAPI-Key": key, "X-RapidAPI-Host": host}
#    querystring = {"waypoints":f"{str(lat1)},{str(long1)}|{str(lat2)},{str(long2)}","mode":mode}
#    response = requests.request("GET", url, headers=headers, params=querystring, verify=False)
#    return response

# response = get_directions_response(36.99139, 126.35882, 36.77507, 126.44410)

# def create_map(response):
#    # use the response
#    mls = response.json()['features'][0]['geometry']['coordinates']
#    points = [(i[1], i[0]) for i in mls[0]]
#    m = folium.Map()
#    # add marker for the start and ending points
#    for point in [points[0], points[-1]]:
#       folium.Marker(point).add_to(m)
#    # add the lines
#    folium.PolyLine(points, weight=5, opacity=1).add_to(m)
#    # create optimal zoom
#    df = pd.DataFrame(mls[0]).rename(columns={0:'Lon', 1:'Lat'})[['Lat', 'Lon']]
#    sw = df[['Lat', 'Lon']].min().values.tolist()
#    ne = df[['Lat', 'Lon']].max().values.tolist()
#    m.fit_bounds([sw, ne])
#    return m
# m = create_map(response)