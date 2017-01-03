## Latar Belakang Masalah :
1. Snort
2. Cara Instalasi Snort Pada CentOS

## Snort
Snort adalah sebuah sistem open source untuk pencegahan penyusupan jaringan yang mampu melakukan analisis lalu lintas jaringan secara real-time dan packet logger pada jaringan IP. Snort juga dapat melakukan analisis protokol, konten pencarian atau pencocokan dan dapat digunakan untuk mendeteksi berbagai serangan.

## Cara Instalasi Snort Pada CentOS
Sebelum menginstall snort, install dulu beberapa paket yang dibutuhkan snort untuk berjalan.
~~~
# yum install libdnet libdnet-devel pcre pcre-devel gcc make flex byacc bison kernel-devel libxml2-devel wget -y
~~~

Selanjutnya membuat direktori atau folder untuk digunakan sebagai tempat instalasi.
~~~
# mkdir /usr/local/src/snort
# cd /usr/local/src/snort
~~~

Instalasi Libpcap.
~~~
# wget http://www.tcpdump.org/release/libpcap-1.3.0.tar.gz -O libpcap.tar.gz
# tar zxvf libpcap.tar.gz
# cd libpcap-*
# ./configure && make && make install
# echo “/usr/local/lib” >> /etc/ld.so.conf
# ldconfig -v
~~~

Instalasi DAQ.
~~~
# wget https://www.snort.org/downloads/snort/daq-2.0.6.tar.gz -O daq.tar.gz
# tar zxvf daq.tar.gz
# cd daq-*
# ./configure && make && make install
# ldconfig -v
~~~

Buat user dan group untuk snort.
~~~
# groupadd snort
# useradd -g snort snort
~~~

Masuk ke folder snort dan instalasi snort.
~~~
# cd /usr/local/src/snort
# wget https://www.snort.org/downloads/snort/snort-2.9.9.0.tar.gz -O snort.tar.gz
# tar zxvf snort.tar.gz
# cd snort-2*
# ./configure –prefix /usr/local/snort –enable-sourcefire && make && make install
~~~

## Kesimpulan
Jadi, snort adalah sebuah sistem open source untuk pencegahan penyusupan jaringan yang mampu melakukan analisis lalu lintas jaringan secara real-time dan packet logger pada jaringan IP.

## Saran
Diharapkan memahami materi dan praktikumnya secara mendetail dan perhatikan setiap langkah proses instalasi Snort dengan baik dan benar.
<br>
* Nama : Bayu Rahmad Azhari
* NPM : 1144125
* Kelas : 3C
* Prodi : D4 Teknik Informatika
* Kampus : Politeknik Pos Indonesia

Link Matakuliah : http://kampus.awangga.net/assignments/keamananjaringan2016

Referensi :
* https://www.snort.org/ 
* https://rozzada.wordpress.com/2013/04/11/install-snort-centos-6-2-64bit/

Scan Plagiarisme :
* https://drive.google.com/open?id=0B5FSMUsdCMU4MWMyNDRtZ25CTU0
* https://drive.google.com/open?id=0B5FSMUsdCMU4LVZReG9NSjhYaVE