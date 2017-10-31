import folium

maps = folium.Map(
        location=[-6.838119, 107.927532],
        zoom_start=12,
        tiles='Stamen Terrain')

tooltip = 'Click me !'

folium.Marker([-6.847306, 107.924153], popup='<i>Taman Endog Sumedang </i>').add_to(maps)

folium.Marker([-6.848529, 107.927046], popup='<i>Masjid Besar Tegal Kalong</i>').add_to(maps)

folium.Marker([-6.846484, 107.925426], popup='<i>Pasar Sumedang</i>').add_to(maps)

folium.Marker([-6.845578, 107.930232], popup='<i>Pemancingan Galatama Patin Apih Jaja</i>').add_to(maps)

folium.Marker([-6.835869, 107.929806], popup='<i>Pos Pelayanan Kpp Pratama Sumedang</i>').add_to(maps)

folium.Marker([-6.835267, 107.930321], popup='<i>Bunderan Alam Sari Sumedang</i>').add_to(maps)

folium.Marker([-6.836854, 107.930627], popup='<i>Gedung Korpri</i>').add_to(maps)

folium.Marker([-6.837179, 107.927778], popup='<i>Universitas Pendidikan Indonesia </i>').add_to(maps)

folium.Marker([-6.835437, 107.932226], popup='<i>AUDI PRATAMA DANO REGENCY</i>').add_to(maps)

folium.Marker([-6.834199, 107.929305], popup='<i>PT. Melon Pijar Gas</i>').add_to(maps)

maps