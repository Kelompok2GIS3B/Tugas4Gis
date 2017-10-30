import folium

maps = folium.Map(
        location=[-6.1783, 106.6319],
        zoom_start=12,
        tiles='Stamen Terrain')

tooltip = 'Click me !'

folium.Marker([-6.197492, 106.644078], popup='<i>Modern Golf & Country Club</i>').add_to(maps)

folium.Marker([-6.193354, 106.640048], popup='<i>ACS MOBILINDO</i>').add_to(maps)

folium.Marker([-6.197479, 106.639393], popup='<i>PT. Buana Citra Abadi Tangerang</i>').add_to(maps)

folium.Marker([-6.197020, 106.640075], popup='<i>Apartment KBGB KOTA MADYA TANGERANG</i>').add_to(maps)

folium.Marker([-6.193068, 106.641410], popup='<i>SMP Gemilang Modernlano</i>').add_to(maps)

folium.Marker([-6.204849, 106.638780], popup='<i>Perumahan Cluster Pulau Dewa Modernland</i>').add_to(maps)

folium.Marker([-6.127294, 106.655024], popup='<i>Kantor Kesehatan Pelabuhan Soekarno-Hatta</i>').add_to(maps)

folium.Marker([-6.132883, 106.642533], popup='<i>PT. Garuda Indonesia</i>').add_to(maps)

folium.Marker([-6.169444, 106.626751], popup='<i>RS. Hermina Tangerang</i>').add_to(maps)

folium.Marker([-6.171035, 106.627664], popup='<i>Taman Dayung</i>').add_to(maps)

maps