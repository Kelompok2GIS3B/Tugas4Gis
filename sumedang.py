#!/bin/python

import folium

def inisiasi (long,lat):
    m = folium.Map(
        location=[long, lat],
        zoom_start=12,
        tiles='Stamen Terrain')
    return m

def test (long,lat):
    a = folium.Map(
        location=[long, lat],
        zoom_start=12,
        tiles='Stamen Toner')
    return a

def peta (long,lat):
    p = folium.Map(
        location=[long, lat],
        zoom_start=12,
        tiles='Stamen Terrain')
    return p

def save (apa, simpan):
    apa.save(simpan)
    
m = inisiasi (-6.838119, 107.927532)
a = test (-6.838119, 107.927532)
p = peta (-6.838119, 107.927532)
tooltip = 'Click me !'

folium.Marker([-6.847306, 107.924153], popup='<i>Taman Endog Sumedang </i>').add_to(m)

folium.Marker([-6.848529, 107.927046], popup='<i>Masjid Besar Tegal Kalong</i>').add_to(m)

folium.Marker([-6.846484, 107.925426], popup='<i>Pasar Sumedang</i>').add_to(m)

folium.Marker([-6.845578, 107.930232], popup='<i>Pemancingan Galatama Patin Apih Jaja</i>').add_to(m)

folium.Marker([-6.835869, 107.929806], popup='<i>Pos Pelayanan Kpp Pratama Sumedang</i>').add_to(m)

folium.Marker([-6.835267, 107.930321], popup='<i>Bunderan Alam Sari Sumedang</i>').add_to(m)

folium.Marker([-6.836854, 107.930627], popup='<i>Gedung Korpri</i>').add_to(m)

folium.Marker([-6.837179, 107.927778], popup='<i>Universitas Pendidikan Indonesia </i>').add_to(m)

folium.Marker([-6.835437, 107.932226], popup='<i>AUDI PRATAMA DANO REGENCY</i>').add_to(m)

folium.Marker([-6.834199, 107.929305], popup='<i>PT. Melon Pijar Gas</i>').add_to(m)

folium.Marker([-6.8451028, 107.9249476], popup='<i>BANK SUMEDANG</i>').add_to(m)

folium.Marker([-6.842935, 107.9246427], popup='<i>Ngopi Heula</i>').add_to(m)

folium.Marker([-6.8448237, 107.9245214], popup='<i>Warung Echo</i>').add_to(m)

folium.Marker([-6.8448036, 107.9242944], popup='<i>Mie Rasa</i>').add_to(m)

folium.Marker([-6.8453361, 107.9247266], popup='<i>Mebel Monalisa</i>').add_to(m)

folium.Marker([-6.8449819, 107.9243184], popup='<i>PGAK</i>').add_to(m)

folium.Marker([-6.8446918, 107.9247126], popup='<i>Rejeki Motor</i>').add_to(m)

folium.Marker([-6.844681, 107.9246972], popup='<i>Ethree Cell</i>').add_to(m)

folium.Marker([-6.845101, 107.9243717], popup='<i>Toko Sahabat</i>').add_to(m)

folium.Marker([-6.8451229, 107.9243798], popup='<i>Toko Panjang Putra</i>').add_to(m)

folium.Marker([-6.875558, 107.969356], popup='<i>Cikadu</i>').add_to(m)

folium.Marker([-6.834591, 107.929401], popup='<i>PT. Srikandi Diamond Motors - Sumedang</i>').add_to(m)

folium.Marker([-6.834621, 107.929130], popup='<i>Apotek Sifa Farma</i>').add_to(m)

folium.Marker([-6.834741, 107.929622], popup='<i>Mitsubishi Motors</i>').add_to(m)

folium.Marker([-6.833535, 107.927851], popup='<i>Masjid Sholahuddin Al-Ayubi</i>').add_to(m)

folium.Marker([-6.835213, 107.928140], popup='<i>Hotel Asri</i>').add_to(m)

folium.Marker([-6.835795, 107.929062], popup='<i>Plaza Asia Sumedang</i>').add_to(m)

folium.Marker([-6.836900, 107.929040], popup='<i>Kantor Kelurahan Kotakaler</i>').add_to(m)

folium.Marker([-6.837912, 107.927848], popup='<i>Biru Jasa, Travel & Tour Perintis</i>').add_to(m)

folium.Marker([-6.838414, 107.929190], popup='<i>Dewan Kebudayaan Sumedang</i>').add_to(m)

folium.Marker([-6.838314, 107.928153], popup='<i>Hotel Sapphire Home</i>').add_to(m)

folium.Marker([-6.901420, 108.020060], popup='<i>Paralayang Batu Dua</i>').add_to(m)

folium.Marker([-6.906843, 108.014631], popup='<i>Gunung Lingga</i>').add_to(m)

folium.Marker([-6.764677, 107.959659], popup='<i>Camp Area Puncak Gunung Tampomas</i>').add_to(m)

folium.Marker([-6.752123, 107.985788], popup='<i>Curug Ciputrawangi</i>').add_to(m)

folium.Marker([-6.962981, 107.882695], popup='<i>Curug Cinulang (Sindulang)</i>').add_to(m)

folium.Marker([-6.913678, 107.977646], popup='<i>Curug Gorobog</i>').add_to(m)

folium.Marker([-6.791094, 107.924570], popup='<i>Mata Air Cikandung</i>').add_to(m)

folium.Marker([-6.706107, 107.909527], popup='<i>Danau Biru Situ Cilembang</i>').add_to(m)

folium.Marker([-6.769249, 108.003982], popup='<i>Sirah Cipelang</i>').add_to(m)

folium.Marker([-6.855555, 107.909586], popup='<i>Gn. Palasari</i>').add_to(m)

folium.Marker([-6.856026,+108.096522], popup='<i>Waduk Jatigede</i>').add_to(m)

folium.Marker(-6.929583, 107.763515], popup='<i>La Fasa Hotel</i>').add_to(m)

folium.Marker(-6.935194, 107.759305], popup='<i>Hotel Jatinangor</i>').add_to(m)

folium.Marker(-6.854387, 107.919227], popup='<i>Amory Boutique Hotel</i>').add_to(m)

folium.Marker(-6.854389, 107.919222], popup='<i>Puri Mutiara Hotel</i>').add_to(m)

folium.Marker(-6.819240, 107.941527], popup='<i>Hotel Pesona Sumedang</i>').add_to(m)

folium.Marker(-6.934690, 107.769848], popup='<i>Hotel Citra Papan 1</i>').add_to(m)

folium.Marker(-6.916890, 107.765785], popup='<i>Bandung Giri Gahana Golf and Resort</i>').add_to(ma)

folium.Marker(-6.725559, 107.944638], popup='<i>Bojongloa</i>').add_to(m)

folium.Marker(-6.740561, 108.006436], popup='<i>Conggeang</i>').add_to(m)

folium.Marker(-7.030962, 108.135526], popup='<i>Wado</i>').add_to(m)

folium.Marker(-6.946450, 107.885587], popup='<i>Cimanggung</i>').add_to(m)

folium.Marker(-6.606890, 107.869107], popup='<i>Tanjung</i>').add_to(m)

folium.Marker(-6.811901, 107.945918], popup='<i>R.M Joglo Sumedang</i>').add_to(m)

folium.Marker(-6.822698, 107.939604], popup='<i>Saung Teko</i>').add_to(m)

folium.Marker(-6.803828, 107.969396], popup='<i>Rumah Makan Fish 88</i>').add_to(m)

folium.Marker(-6.824482, 107.938373], popup='<i>Rumah Makan Alam Sari</i>').add_to(m)

folium.Marker(-6.797927, 107.990906], popup='<i>Rumah Makan Mah Nini</i>').add_to(m)

folium.Marker(-6.808967, 107.955017], popup='<i>Kartika Rumah Makan</i>').add_to(m)

folium.Marker(-6.922459, 107.782507], popup='<i>Rumah Makan Tahu Sumedang Sari Kedele,</i>').add_to(m)

folium.Marker(-6.914389, 107.789620], popup='<i>Rumah Makan Organik Saung Nini</i>').add_to(m)

folium.Marker(-6.864310, 107.872910], popup='<i>Ponyo Sumedang</i>').add_to(m)

folium.Marker(-6.835067, 107.925451], popup='<i>Rumah Makan Minang Bahari</i>').add_to(m)

folium.Marker(-6.840218, 107.925675], popup='<i>Tahu Palasari Sumedang</i>').add_to(m)

folium.Marker(-6.928392, 107.779781], popup='<i>Rumah Makan Sawargi</i>').add_to(m)

folium.Marker(-6.844475, 107.915667], popup='<i>Rumah Makan Saung Cibingbin 2</i>').add_to(m)


 #M.Fajri Mualim
 folium.Marker(-6.713284, 108.053132], popup='<i>Ungkal</i>').add_to(m)
 folium.Marker(-6.707829, 107.963868], popup='<i>Buahdua</i>').add_to(m)
 folium.Marker(-6.650542, 108.043519], popup='<i>Cibuluh</i>').add_to(m)
 folium.Marker(-6.960082, 107.807313], popup='<i>Cimanggung</i>').add_to(m)
 folium.Marker(-6.823746, 107.751008], popup='<i>Genteng</i>').add_to(m)
 folium.Marker(-6.582335, 107.860871], popup='<i>Tanjung</i>').add_to(m)
 folium.Marker(-6.642358, 108.043519], popup='<i>Cibuluh</i>').add_to(m)
 folium.Marker(-6.988708, 108.039399], popup='<i>Jayamandiri</i>').add_to(m)
 folium.Marker(-7.036414, 108.131410], popup='<i>Cilengkrang</i>').add_to(m)
 folium.Marker(-6.981893, 108.038026], popup='<i>Cibugel</i>').add_to(m)

#jangan dihapus gan ini punya faisal
folium.Marker(-6.898942, 107.352916], popup='<i>Curug Cukang Rahong</i>').add_to(m)
folium.Marker(-6.917003, 107.848504], popup='<i>Pangjugjugan</i>').add_to(m)
folium.Marker(-6.939296, 107.990470], popup='<i>Gn. Margawindu</i>').add_to(m)
folium.Marker(-6.876860, 107.909446], popup='<i>Kampung Toga</i>').add_to(m)
folium.Marker(-6.925465, 107.779360], popup='<i>Jembatan Cincin Cikuda</i>').add_to(m)
folium.Marker(-6.914280, 107.950801], popup='<i>Saung Cibingbin 1 Sumedang</i>').add_to(m)
folium.Marker(-6.861172, 107.921199], popup='<i>Museum Prabu Geusan Ulun</i>').add_to(m)

folium.RegularPolygonMarker(
    [-6.898942, 107.352916],
    popup='Curug Cukang Rahong',
    fill_color='#769d96',
    number_of_sides=6,
    radius=10
).add_to(m)

folium.RegularPolygonMarker(
    [-6.917003, 107.848504],
    popup='Pangjugjugan',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
).add_to(m)


#jangan dihapus gan ini punya agung
folium.Marker([-6.8357715, 107.9294052], popup='<i>KPPN Sumedang</i>').add_to(m)
folium.Marker([-6.8358094, 107.9294468], popup='<i>ATM BRI KPPN Sumedang</i>').add_to(m)
folium.Marker([-6.8358272, 107.9293961], popup='<i>ATM CIMB Niaga (Plaza Asia Sumedang)</i>').add_to(m)
folium.Marker([-6.8358326, 107.9293944], popup='<i>The Cups</i>').add_to(m)
folium.Marker([-6.8358541, 107.9294088], popup='<i>DKOFFIE LAB</i>').add_to(m)
folium.Marker([-6.8358127, 107.9294333], popup='<i>Raja Sosis</i>').add_to(m)
folium.Marker([-6.8357366, 107.9294853], popup='<i>Juragan Seafood</i>').add_to(m)
folium.Marker([-6.8357065, 107.9295226], popup='<i>Rumah Ice Cream</i>').add_to(m)
folium.Marker([-6.8356806, 107.9295304], popup='<i>Dorado Fresh Drinks</i>').add_to(m)
folium.Marker([-6.8356198, 107.9295337], popup='<i>Davina Baby Shop</i>').add_to(m)


folium.RegularPolygonMarker(
    [-6.865854, 108.064279],
    popup='Puncak Damar Waduk Jatigede',
    fill_color='#769d96',
    number_of_sides=6,
    radius=10
).add_to(m)

folium.RegularPolygonMarker(
    [-6.875888, 108.067394],
    popup='Camping Ground Jatigede',
    fill_color='#45647d',
    number_of_sides=8,
    radius=10
).add_to(m)

folium.RegularPolygonMarker(
    [-6.971641, 108.008176],
    popup='Bumi Perkemahan Kec. Cibugel',
    fill_color='#132b5e',
    number_of_sides=3,
    radius=10
).add_to(m)

folium.RegularPolygonMarker(
    [-6.903814, 108.078489],
    popup='Wisata Air Historis Kampung Cibogo',
    fill_color='#45647d',
    number_of_sides=6,
    radius=10
).add_to(m)

folium.RegularPolygonMarker(
    [-6.918496, 108.075361],
    popup='Kantor Pos Darmaraja',
    fill_color='#132b5e',
    number_of_sides=6,
    radius=10
).add_to(m)

m

folium.Circle(
    radius=100,
    location=[-6.918170, 108.074720],
    popup='Alun-alun Darmaraja',
    color='Crimson',
    fill=False
).add_to(a)

a

folium.Marker(
    location=[-6.918101, 108.074260],
    popup='Masjid Agung Darmaraja',
    icon=folium.Icon(icon='cloud')
).add_to(p)

folium.Marker(
    location=[-6.918557, 108.073914],
    popup='Pasar Tradisional Darmaraja',
    icon=folium.Icon(icon='cloud')
).add_to(p)

folium.Marker(
    location=[-6.922410, 108.074122],
    popup='Air Minum Fajar',
    icon=folium.Icon(icon='cloud')
).add_to(p)

folium.Marker(
    location=[-6.928525, 108.070223],
    popup='Majelis Taklim (MT) Al Hikmah',
    icon=folium.Icon(icon='cloud')
).add_to(p)

p

save(m, '4.html')
save(a, '5.html')
save(p, '6.html')

#ada perubahan dalam pendeklarasian jadi mohon menyesuaikan yg lainnya.
