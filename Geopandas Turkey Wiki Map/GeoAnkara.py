import geopandas as gpd
import folium
from folium import Html, Element

# GeoJSON oku
gdf = gpd.read_file("tr.json")

# Harita oluştur
m = folium.Map(location=[39, 35], zoom_start=6)

# İlleri çiz + Wikipedia bağlantısı
for _, row in gdf.iterrows():
    il_adi = row['name']
    wiki_url = f"https://tr.wikipedia.org/wiki/{il_adi.replace(' ', '_')}"
    
    popup_html = f'<b>{il_adi}</b><br><a href="{wiki_url}" target="_blank">Wikipedia sayfası</a>'
    
    folium.GeoJson(
        data=row['geometry'],
        tooltip=folium.Tooltip(il_adi),
        popup=folium.Popup(popup_html, max_width=300)
    ).add_to(m)

# Haritayı kaydet
m.save("turkiye_streetview_modu.html")
print("✅ Harita oluşturuldu: turkiye_streetview_modu.html") 
