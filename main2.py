from __future__ import division
# from math import ceil
import doublemetaphone
import jarowinkler
import stringao
import io
import sys


# try:
#     file = open(raw_input("Masukkan Nama File Transliterasi : "),'rb')
#     data = file.read().splitlines()
# except IOError:
#     print "Nama File Salah"

print '\n','Mohon Tunggu ... ', '\n'
# buka file
file = open("Alquran(nf).txt", "rb")
data = file.read().splitlines()
# baca isi file
# print 'data', data

# TOKENISASI
# ======================================================================================================================
tampung = []
#Memisahkan data berdasarkan ','
for i in data:
    # print i
    for j in i:
        # print j
        # if t < len(i):
            s = i.split(',')
            # print s
            kalimat = s[3].lower()
    tampung.append(kalimat)

# print tampung


kata = []
for i in tampung:
    # print i
    for j in i:
        # print j
        # if t < len(i):
            r = i.split(' ')
    kata.append(r)
# print 'kata', kata

# ======================================================================================================================

# PENGKODEAN FONETIS
# ======================================================================================================================
kode = []
for t in range(len(kata)):
    # print kata[t]
    for i in kata[t]:
        # print i
        a = doublemetaphone.dmetaphone(i)
        # print a
        kode.append(a)

# print kode

# untuk menampung rentang pembagian kata dan kode per ayat
rentang = []
for i in kata:
    a = len(i)
    rentang.append(a)
# print rentang

#buat menemukan pola, need extra time to think about this huhu, sabar, semangat mining
# w = kode[sum(rentang[0:0]):sum(rentang[0:1])]
# print w
# w2 = kode[sum(rentang[0:1]):sum(rentang[0:2])]
# print w2
# w3 = kode[sum(rentang[0:2]):sum(rentang[0:3])]
# print w3
# w4 = kode[sum(rentang[0:3]):sum(rentang[0:4])]
# print w4

# print sum(rentang[0:3]) #percobaan mining
# print len(rentang)
# print len(kode)

# membuat matriks dengan dimensi sesuai rentang atau informasi jumlah kata per ayat
kodefix = []
for t in range(len(rentang)):
    w = kode[sum(rentang[0:t+0]):sum(rentang[0:t+1])]
    # print w
    kodefix.append(w)
# print 'kodefix', kodefix

show = []
for i in data:
    # print i
    for j in i:
        # print j
        # if t < len(i):
            s = i.split(',')
    show.append(s)

# print show

pls = 0
a = ""
datas = []
#Menampilkan data
for i in show:
    a = i[1] + ' [Q.S. ' + i[0] + ':' + i[2] + '] ' + i[3] , pls#i[3].lower
    # print a
    pls += 1
    datas.append(a)
# print datas

# ARAB
file2 = io.open("quran-simple(nf).txt", mode="r", encoding="utf-8")
data2 = file2.read().splitlines()
t = []
idx = 0
for i in data2:
    a = i.split('|'), idx
    idx += 1
    if idx <= 6236:
        t.append(a)

# print t[6234][0][2]

arab = []
ida = 0
for i in t:
    a = t[ida][0][2], ida
    ida += 1
    arab.append(a)

# =================================================
#Menampilkan data surat dan kode fonetis dibawahnya
# for i in range(len(datas)):
#     print datas[i]
#     print kodefix[i]
#     i += 1
# ======================================================================================================================

# PENCOCOKKAN KODE DAN HITUNG NILAI KESAMAAN STRING
# ======================================================================================================================
# Menghitung nilai similarity dengan jaro
tm = []
masuk = raw_input('Masukkan ayat/kata yang dicari : ')
# input = ("yas'urun").split(' ')
input = masuk.split(' ')
print '\n'
for i in input:
    # print i
    ip = doublemetaphone.dmetaphone(i)
    tm.append(ip)
print 'pencarian ',input, ' ',tm

p = kodefix
# print 'ini p', p

jd = []
js = []
# tr = []
for i in tm:
    # print 'ini i', i
    for k in p:
        # print k
        for j in k:
            # print j[1]
            w = jarowinkler.get_jaro_distance(j[0],i[0])
            v = jarowinkler.get_jaro_distance(j[1],i[0])
            x = jarowinkler.get_jaro_distance(j[0],i[1])
            y = jarowinkler.get_jaro_distance(j[1],i[1])
            # x = jarowinkler._score(j[0],i[0])
            # js.append(max(w,v))
            jd.append(max(w,v,x,y))
    # tr.append(jd)
# print tr
# print js
# print jd


kata3 = []
for i in kata:
    kata2 = []
    for j in i:
        a = stringao.metaphone(j)
        kata2.append(a)
    kata3.append(kata2)

inputstr = []
for i in input:
    ip = stringao.metaphone(i)
    inputstr.append(ip)
# print inputstr

perstring = []
for i in inputstr:
    for j in kata3:
        for k in j:
            y = jarowinkler.get_jaro_distance(k,i)
            perstring.append(y)

idx = len(kode)
sama3 = []
for i in range(len(input)): #ini untuk string
    b = perstring[i*idx:idx*(i+1)]
    sama3.append(b)


tn = []
for i in input: # ini untuk mencocokkan kesamaan string query dengan string di dataset
    for j in kata:
        for k in j:
            y = jarowinkler.get_jaro_distance(k,i)
            tn.append(y)
# print 'tn' ,tn


idx = len(kode)
# print 'kode', kode
# print 'lenkode', idx
# print jd[0:idx]
# print jd[idx:idx*2]
# print jd[idx*2:idx*3]

# untuk membuat matrix yang berisi nilai kesamaan kode pada query dengan tiap kode pada dataset, dimensinya jumlah kode dataset x jumlah inputan (baris x kolom)
sama = []
for i in range(len(tm)): #ini untuk kode fonetis
    a = jd[i*idx:idx*(i+1)]
    # print a
    sama.append(a)
# print 'sama', sama

sama2 = []
for i in range(len(input)): #ini untuk string
    b = tn[i*idx:idx*(i+1)]
    sama2.append(b)
# print 'sama2', sama2

# menggabungkan sejumlah list dalam matriks yg berisi nilai kesamaan paling besar dan akan menjadi satu list.
nilai = map(lambda pair: max(pair), zip(*sama)) #untuk kode fonetis
# print 'ini nilai', nilai

nilai2 = map(lambda pair: max(pair), zip(*sama2)) #untuk string
# print 'ini nilai2', nilai2

nilai3 = map(lambda pair: max(pair), zip(*sama3))

# menghasilkan matriks yang berisi nilai kesamaan per ayat, satu list menandakan satu ayat
x = []
for t in range(len(rentang)): #untuk kode fonetis
    w = nilai[sum(rentang[0:t+0]):sum(rentang[0:t+1])]
    # print w
    x.append(w)
# print 'nilai kesamaan kode fonetis per ayat', x

x2 = []
for i in range(len(rentang)): #untuk string
    y = nilai2[sum(rentang[0:i+0]):sum(rentang[0:i+1])]
    x2.append(y)
# print 'nilai kesamaan string per ayat', x2

# syrt = int(ceil(len(x[0])/len(input)))+1
# print syrt


# untuk meberikan peringkat kesamaan jika jumlah query lebih dari satu,
# rata2 = []
#
# for j in x: #untuk kode fonetis
#     rata = []
#     if len(j) >= len(input):
#         # syrt = int((len(j)//2))+1 #dibulatkan ke bawah
#         syrt = (len(j) - len(input)) + 1
#         for i in range(syrt):
#             # pp = j[i:len(input)+i]
#             g = sum(j[i:len(input)+i])/(len(input))
#             # print g
#             rata.append(g)
#             # print rata
#             # print pp
#     # if len(j) == len(input):
#     #     for i in range(len(j)):
#     #         g = sum(j[i:len(input)])/len(input)
#     #         rata.append(g)
#     else:
#         rata.append(0)
#     rata2.append(rata)
# print 'nilai rata2 kesamaan fonetis query panjang', rata2

x3 = []
for i in range(len(rentang)): #untuk string
    y = nilai3[sum(rentang[0:i+0]):sum(rentang[0:i+1])]
    x3.append(y)

rata2x = []
for i in x2: #untuk string
    ratax = []
    if len(i) >= len(input):
        syrt = (len(i) - len(input)) + 1
        for j in range(syrt):
            h = sum(i[j:len(input)+j])/(len(input))
            ratax.append(h)
    else:
        ratax.append(0)
    rata2x.append(ratax)
# print 'nilai rata2 kesamaan string query panjang', rata2x

# untuk mengambil nilai maksimal pada list didalam matriks rata2, satu list mewakili satu ayat
# fonetis = []
# for i in rata2: #kode fonetis
#     fonetis.append(max(i))
# print rt

# hasil2 = zip(rt,datas)
# print hasil2 #ini untuk kode fonetis

rata3x = []
for i in x3: #untuk string yg sudah di stringao
    ratax = []
    if len(i) >= len(inputstr):
        syrt = (len(i) - len(inputstr)) + 1
        for j in range(syrt):
            h = sum(i[j:len(inputstr)+j])/(len(inputstr))
            ratax.append(h)
    else:
        ratax.append(0)
    rata3x.append(ratax)

query = []
for i in rata2x: #string query
    query.append(max(i))

queryao = []
for i in rata3x:
    queryao.append(max(i))
# jum = penjumlahan.jumlah(rata2,rata2x)
# print '(jumlah kesamaan fonetis + query)/2 per lafaz', jum, '\n'
# fonqu = []
# for i in jum:
#     fonqu.append(max(i))

# hasil2 = zip(query,datas)
# coba = zip(fonetis,datas)

# gab = zip(hasil2, coba) #rata2 kesamaan (string, kode)

# ======================================================================================================================

# PEMERINGKATAN HASIL
# ======================================================================================================================

fon = []
for i in x:
    a = sorted(i, reverse=True)
    hit = sum(a[0:len(input)])/len(input)
    fon.append(hit)


# matriks isi kode fonetis dan nilai kesamaannya
koni = []
for i in range(len(x)):
    a = zip(kodefix[i], x[i])
    koni.append(a)
# print koni

gab2 = zip(datas, query, fon, koni, queryao)
# print gab2

gab2.sort(key=lambda x:x[4], reverse=True)
# for i in gab2:
#     print i
print '\n'

gab2.sort(key=lambda x:x[2], reverse=True)

print '========================================================================================================================================================================================='
print 'Hasil Pencarian : '
print '=========================================================================================================================================================================================', '\n'

index = []
idk = 1
for i in gab2:
    if i[2] >= 0.95 and i[1] > 0.4:
        print 'Alhamdulillah hasil', idk, i[0][0],
        for j in arab:
            if i[0][1] == j[1]:
                print '|',j[0].encode(sys.stdout.encoding), '\n','_____________________', i[3], '\n_____________________ Kesamaan String ', i[1], '\n'
        idk += 1
        index.append(idk)

if len(index) == 0:
    print "Hasil Tidak Ditemukan"
