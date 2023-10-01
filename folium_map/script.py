import folium
from folium import IFrame
import os
import base64

maps = folium.Map(location=[13.7294363, 100.7785291], zoom_start=16)
route = os.path.join("routes.json")

tooltip = "ทางเข้าสจล."
html = """<center>
<h2>ทางเข้าสจล.</h2> 
<br/> 
<img src="data:image/jpg;base64,{}" style="width:75%;height=75%">
</center>""".format
pic1 = base64.b64encode(open('./folium_map/images/kmitl.jpg', 'rb').read()).decode()
iframe1 = IFrame(html(pic1), width=600, height=400)
popup1 = folium.Popup(iframe1, max_width=650)
icon1 = folium.CustomIcon('./folium_map/images/kmitl.jpg', icon_size=(60, 60))

marker1 = folium.Marker(location=[13.724705075669817, 100.7800474824299], popup=popup1, tooltip=tooltip).add_to(maps)

maps.save("./flasksnaja/templates/routemap.html")
