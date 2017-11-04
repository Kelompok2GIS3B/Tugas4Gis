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

folium.Marker([-6.837912, 107.927848], popup='<i>Biro Jasa, Travel & Tour Perintis</i>').add_to(m)

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

folium.Marker(-6.854103, 107.920521], popup='<i>SMAN 1 Sumedang</i>').add_to(m)

folium.Marker(-6.926752, 107.779859], popup='<i>SMAS PGRI Jatinangor</i>').add_to(m)

folium.Marker(-6.837319, 107.929554], popup='<i>SMAN 3 Sumedang</i>').add_to(m)

folium.Marker(-6.939237, 107.788294], popup='<i>SMP Darul Fatwa</i>').add_to(m)

folium.Marker(-6.835841, 107.928380], popup='<i>SMK Negeri 2 Sumedang</i>').add_to(m)

folium.Marker(-6.825701, 107.849603], popup='<i>SMAN Rancakalong</i>').add_to(m)

folium.Marker(-6.961688, 107.813104], popup='<i>SMAS Plus Guna Cipta</i>').add_to(m)

folium.Marker(-6.837553, 107.927351], popup='<i>SMKN 1 Sumedang</i>').add_to(m)

folium.Marker(-6.848571, 107.946712], popup='<i>SMAN 2 Sumedang</i>').add_to(m)

folium.Marker(-6.761271, 107.879122], popup='<i>SMAN Tanjungkerta</i>').add_to(m)

folium.Marker(-6.838221, 107.927368], popup='<i>Selaz Cafe</i>').add_to(m)

folium.Marker(-6.934464, 107.769324], popup='<i>Checo "The Legendary Place"</i>').add_to(m)

folium.Marker(-6.839422, 107.926784], popup='<i>Cinta Cafe</i>').add_to(m)

folium.Marker(-6.856618, 107.924045], popup='<i>Lazyvery Garden Cafe</i>').add_to(m)

folium.Marker(-6.850604, 107.922965], popup='<i>Orchid Cafe</i>').add_to(m)

folium.Marker(-6.896901, 107.808181], popup='<i>Mahata Cafe</i>').add_to(m)

folium.Marker(-6.853799, 107.922202], popup='<i>Ngopi Bung</i>').add_to(m)

folium.Marker(-6.936808, 107.762047], popup='<i>Bosa Cafe</i>').add_to(m)

folium.Marker(-6.858572, 107.921570], popup='<i>Cloffee Sumedang</i>').add_to(m)

folium.Marker(-6.863721, 107.919123], popup='<i>Bukan Cafe Dan Resto</i>').add_to(m)



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
    
 folium.Marker(-6.735106, 108.123170], popup='<i>Ujung Jaya</i>').add_to(m)

 folium.Marker(-6.890556, 107.974854], popup='<i>Ganeas</i>').add_to(m)
 
 folium.Marker(-6.729651, 108.157502], popup='<i>Kudangwangi</i>').add_to(m)
 
 folium.Marker(-6.935545, 108.009187], popup='<i>Cipeuteuy</i>').add_to(m)
  
 folium.Marker(-6.807383, 107.792207], popup='<i>Rancakalong</i>').add_to(m)
    
 folium.Marker(-6.949177, 107.957002], popup='<i>CItengah</i>').add_to(m)

 folium.Marker(-6.970988, 108.090211], popup='<i>Wado</i>').add_to(m)
    
 folium.Marker(-6.664182, 107.983094], popup='<i>Gendereh</i>').add_to(m)

 folium.Marker(-6.945087, 107.907563], popup='<i>Sindulang</i>').add_to(m)
    
 folium.Marker(-6.991434, 108.058625], popup='<i>Cipasang</i>').add_to(m)

#Faisal Syarifuddin
folium.Marker(-6.898942, 107.352916], popup='<i>Curug Cukang Rahong</i>').add_to(m)

folium.Marker(-6.917003, 107.848504], popup='<i>Pangjugjugan</i>').add_to(m)

folium.Marker(-6.939296, 107.990470], popup='<i>Gn. Margawindu</i>').add_to(m)

folium.Marker(-6.876860, 107.909446], popup='<i>Kampung Toga</i>').add_to(m)

folium.Marker(-6.925465, 107.779360], popup='<i>Jembatan Cincin Cikuda</i>').add_to(m)

folium.Marker(-6.914280, 107.950801], popup='<i>Saung Cibingbin 1 Sumedang</i>').add_to(m)

folium.Marker(-6.861172, 107.921199], popup='<i>Museum Prabu Geusan Ulun</i>').add_to(m)


folium.Marker(-6.876860, 107.909489], popup='<i>Kampung Toga</i>').add_to(m)

folium.Marker(-6.948836, 107.767654], popup='<i>Cipacu</i>').add_to(m)

folium.Marker(-6.950540, 107.805934], popup='<i>Cimanggung</i>').add_to(m)

folium.Marker(-6.874195, 107.763362], popup='<i>Sukasari</i>').add_to(m)

folium.Marker(-6.833290, 107.759243], popup='<i>Genteng</i>').add_to(m)

folium.Marker(-6.900099, 107.818294], popup='<i>Tanjungsari</i>').add_to(m)

folium.Marker(-6.909642, 107.856746], popup='<i>Pamulihan</i>').add_to(m)

folium.Marker(-6.841472, 107.823787], popup='<i>Rancakalong</i>').add_to(m)


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

folium.Marker([-6.8464073, 107.9717699], popup='<i>Masjid Jami Husnul Khotimah</i>').add_to(m)

folium.Marker([-6.8463576, 107.9722877], popup='<i>POM MINI</i>').add_to(m)

folium.Marker([-6.8463812, 107.9723746], popup='<i>Pertamina</i>').add_to(m)

folium.Marker([-6.8462047, 107.9724896], popup='<i>Bengkel Mobil Pak Acin</i>').add_to(m)

folium.Marker([-6.8462151, 107.9725305], popup='<i>Salon Elpa Sae</i>').add_to(m)

folium.Marker([-6.8462586, 107.973224], popup='<i>Indomaret Ganeas</i>').add_to(m)

folium.Marker([-6.8462478, 107.9732411], popup='<i>apotek ganeas</i>').add_to(m)

folium.Marker([-6.8463335, 107.9736083], popup='<i>BAKSO MORO SENENG</i>').add_to(m)

folium.Marker([-6.8463442, 107.9736418], popup='<i>Mie Baso & Mie Ayam Moro Seneng</i>').add_to(m)

folium.Marker([-6.8463431, 107.9736559], popup='<i>Baso Sunami Moroseneng</i>').add_to(m)

folium.Marker([-6.8140297, 107.9488648], popup='<i>Dewhirst Menswear</i>').add_to(m)

folium.Marker([-6.8140647, 107.9488752], popup='<i>Adrian Juice</i>').add_to(m)

folium.Marker([-6.8141243, 107.9483978], popup='<i>D17 Merchandise</i>').add_to(m)

folium.Marker([-6.8141504, 107.9484093], popup='<i>Hotel Hegarmanah</i>').add_to(m)

folium.Marker([-6.8141251, 107.9486225], popup='<i>Depot Isi Ulang Aqua Galon</i>').add_to(m)

folium.Marker([-6.8141411, 107.9487227], popup='<i>Terminal Cimalaka</i>').add_to(m)

folium.Marker([-6.8142032, 107.9491908], popup='<i>Big Cellular Cimalaka</i>').add_to(m)

folium.Marker([-6.8142094, 107.9494168], popup='<i>Base SSFL Chapter Sumedang</i>').add_to(m)

folium.Marker([-6.8142058, 107.949503], popup='<i>BJB Cimalaka</i>').add_to(m)

folium.Marker([-6.8142147, 107.9495215], popup='<i>Ar Cell Cimalaka</i>').add_to(m)



#punya ara
folium.Marker([-6.770038, 107.970807], popup='<i>Gunung Karang. Anak Gunung Tampomas </i>').add_to(m)

folium.Marker([-6.797147, 107.929517], popup='<i>Adiluhung Futsal</i>').add_to(m)

folium.Marker([-6.800098, 107.930365], popup='<i>Majelis Taklim (MT) Darussalam</i>').add_to(m)

folium.Marker([-6.794774, 107.935292], popup='<i>Getx</i>').add_to(m)

folium.Marker([-6.796450, 107.930447], popup='<i>Kantor Desa Nyalindung</i>').add_to(m)

folium.Marker([-6.796397, 107.933164], popup='<i>Warung Bu Neno</i>').add_to(m)

folium.Marker([-6.795726, 107.930586], popup='<i>LAPANGAN BOLA NYALINDUNG</i>').add_to(m)

folium.Marker([-6.794670, 107.924566], popup='<i>PT. Pertani Sumedang</i>').add_to(m)

folium.Marker([-6.793120, 107.921288], popup='<i>Majelis Taklim (MT) Al Musri</i>').add_to(m)

folium.Marker([-6.858972, 107.920560], popup='<i>Gedung DPRD Sumedang</i>').add_to(m)

folium.Marker(
    location=[-6.859733, 107.920774],
    popup='Alun-Alun Sumedang',
    icon=folium.Icon(icon='cloud')
)add_to(m)

folium.Marker(
    location=[-6.858983, 107.921123],
    popup='Kantor Kejaksaan Negri Sumedang',
    icon=folium.Icon(icon='cloud')
)add_to(m)

folium.Marker(
    location=[-6.859180, 107.922126],
    popup='BPJS Kesehatan',
    icon=folium.Icon(icon='cloud')
)add_to(m)

folium.Marker(
    location=[-6.858146, 107.921976],
    popup='Koperasi Pegawai Kesehatan Sumedang',
    icon=folium.Icon(icon='cloud')
)add_to(m)

folium.Marker(
    location=[-6.859785, 107.921607],
    popup='Lapas Sumedang',
    icon=folium.Icon(icon='cloud')
)add_to(m)

folium.Marker(
    location=[-6.859626, 107.921942],
    popup='Warung Telkom',
    icon=folium.Icon(icon='cloud')
)add_to(m)

folium.Marker(
    location=[-6.858893, 107.921586],
    popup='Honda Pasteur Sumedang',
    icon=folium.Icon(icon='cloud')
)add_to(m)

folium.Marker(
    location=[-6.858688, 107.921564],
    popup='Warung Nasi Kabengbat',
    icon=folium.Icon(icon='cloud')
)add_to(m)

folium.Marker(
    location=[-6.860829, 107.920481],
    popup='BPBD SUMEDANG',
    icon=folium.Icon(icon='cloud')
)add_to(m)

folium.Marker(
    location=[-6.861482, 107.920612],
    popup='Kantor Bupati Sumedang',
    icon=folium.Icon(icon='cloud')
)add_to(m)


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

#syntax [ diperhatiin ya pada gak ada edit sendiri
