# 🗑 **Prediksi Kategori Sampah Organik dan Anorganik Berbasis AI dengan Deep Learning** 🗑

---

💸 **Latar Belakang**

Sampah adalah salah satu masalah terbesar yang dihadapi wilayah metropolitan di era modern ini. Produksi sampah meningkat setiap tahunnya sebagai akibat dari pertambahan populasi dan peningkatan konsumsi. Sayangnya, pengelolaan sampah yang buruk sering kali menyebabkan kerusakan ekosistem, degradasi lingkungan, dan bahkan risiko kesehatan bagi manusia. Namun, dengan menggunakan algoritma deep learning, sistem dapat dilatih untuk mengenali dan mengklasifikasikan berbagai jenis sampah secara otomatis. Hal ini tidak hanya meningkatkan efisiensi dalam proses pemilahan tetapi juga mengurangi kesalahan manusia yang sering terjadi dalam pemilahan manual.

---

👾 **Tujuan Pengembangan**
1. Mengembangkan sistem prediksi berbasis AI yang mampu mengidentifikasi kategori sampah organik dan anorganik secara otomatis dengan menggunakan algoritma deep learning.
2. Memberikan kontribusi nyata pada pengelolaan limbah perkotaan dengan teknologi modern yang mudah diimplementasikan di berbagai skala, mulai dari rumah tangga hingga industri besar.

---

🌱 **Langkah Instalasi**


👽 Dataset
1. Dataset [Recyclable and Household Waste Classification](https://www.kaggle.com/datasets/alistairking/recyclable-and-household-waste-classification) diunduh dari Kaggle dan diekstraksi.
2. Gambar-gambar diatur ulang dengan memindahkan semua isi subfolder ke folder utama masing-masing kategori.
3. Dataset dibagi menjadi dua kategori besar:
   - organik : coffee grounds, eggshells, food waste dan tea bags.
   - anorganik : aerosol cans, aluminum food cans, aluminum soda cans, cardboard boxes, cardboard packaging, clothing, disposable plastic cutlery, glass beverage bottles, glass cosmetic containers, glass food jars, magazines, newspaper, office paper, paper cups, plastic cup lids, plastic detergent bottles, plastic food containers, plastic shopping bags, plastic soda bottles, plastic straws, plastic trash bags, plastic water bottles, shoes, steel food cans, styrofoam cups, styrofoam food containers.
4. Kemudian dataset dibagi menjadi tiga subset: train (70%), validation (15%), dan test (15%) untuk setiap kategori.

👽 Preprocessing
1. Gambar di-rescale (normalisasi) ke rentang 0 dan 1 menggunakan ImageDataGenerator.
2. Subset train, validation, dan test di-load menggunakan generator dengan ukuran target gambar 224x224 piksel.

👽 Model
1. _Convolutional Neural Network_ (CNN)
   - Dua lapisan Conv2D diikuti dengan MaxPooling2D.
   - Lapisan Flatten untuk mengubah data ke dimensi 1D.
   - Lapisan Dense dengan 128 neuron dan aktivasi relu.
   - Lapisan Dropout untuk mengurangi overfitting.
   - Lapisan keluaran dengan aktivasi softmax sesuai jumlah kelas.
2. Transfer Learning dengan _Visual Geometry Group_ (VGG16)
   - Lapisan-lapisan VGG16 dibekukan (tidak dilatih ulang), dan ditambahkan lapisan:
   - GlobalAveragePooling2D untuk mengurangi dimensi fitur.
   - Dense dengan 256 neuron dan aktivasi relu.
   - Dropout untuk mengurangi overfitting.
   - Lapisan keluaran dengan aktivasi softmax.
  
👽 Aplikasi Web
1. Install PDM pada powershell
2. Masukkan perintah "pdm init"
3. membuat file :
   - app.py: Berfungsi sebagai pengatur navigasi aplikasi 
   - home.py: Halaman utama dengan informasi umum
   - classification.py: Halaman untuk prediksi kategori sampah berdasarkan model yang dipilih (CNN/VGG).
4. masukkan perintah "pdm run start"

---

Berikut link :
1. Google Colab : [🐳 UAP MACHINE LEARNING](https://colab.research.google.com/drive/1zPSyVg8ZvGocSFpxiTs5p3mxewrIpNiR?usp=sharing)
2. Web : [🐳 UAP MACHINE LEARNING](http://192.168.1.8:8501)

---


