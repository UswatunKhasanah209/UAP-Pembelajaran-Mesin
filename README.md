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
1. Model _Convolutional Neural Network_ (CNN)
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
3. Google drive : [🐳 UAP MACHINE LEARNING](https://drive.google.com/drive/folders/1p8jcJ2TTlqO-xUVYRwEVwsDc607Liu_f?usp=sharing)

---

✨Hasil dan Analisis
1. Model _Convolutional Neural Network_ (CNN)
![image](https://github.com/user-attachments/assets/50587e0e-1ca3-4089-87ee-6d34ded81667)

   <!DOCTYPE html>
<html>
<body>
    <h2>Classification Report</h2>
    <table>
        <tr>
            <th>Class</th>
            <th>Precision</th>
            <th>Recall</th>
            <th>F1-Score</th>
            <th>Support</th>
        </tr>
        <tr>
            <td>aerosol_cans</td>
            <td>1.00</td>
            <td>1.00</td>
            <td>1.00</td>
            <td>348</td>
        </tr>
        <tr>
            <td>aluminum_food_cans</td>
            <td>0.82</td>
            <td>0.85</td>
            <td>0.83</td>
            <td>336</td>
        </tr>
        <tr>
            <td>aluminum_soda_cans</td>
            <td>0.97</td>
            <td>0.99</td>
            <td>0.98</td>
            <td>341</td>
        </tr>
        <tr>
            <td>cardboard_boxes</td>
            <td>0.81</td>
            <td>0.91</td>
            <td>0.85</td>
            <td>352</td>
        </tr>
        <tr>
            <td>cardboard_packaging</td>
            <td>0.90</td>
            <td>0.77</td>
            <td>0.83</td>
            <td>333</td>
        </tr>
        <tr>
            <td>clothing</td>
            <td>0.99</td>
            <td>1.00</td>
            <td>1.00</td>
            <td>330</td>
        </tr>
        <tr>
            <td>coffee_grounds</td>
            <td>1.00</td>
            <td>1.00</td>
            <td>1.00</td>
            <td>351</td>
        </tr>
        <tr>
            <td>disposable_plastic_cutlery</td>
            <td>1.00</td>
            <td>0.99</td>
            <td>0.99</td>
            <td>340</td>
        </tr>
        <tr>
            <td>eggshells</td>
            <td>1.00</td>
            <td>1.00</td>
            <td>1.00</td>
            <td>355</td>
        </tr>
        <tr>
            <td>food_waste</td>
            <td>1.00</td>
            <td>1.00</td>
            <td>1.00</td>
            <td>340</td>
        </tr>
        <tr>
            <td>glass_beverage_bottles</td>
            <td>0.99</td>
            <td>1.00</td>
            <td>0.99</td>
            <td>328</td>
        </tr>
        <tr>
            <td>glass_cosmetic_containers</td>
            <td>0.99</td>
            <td>0.99</td>
            <td>0.99</td>
            <td>323</td>
        </tr>
        <tr>
            <td>glass_food_jars</td>
            <td>1.00</td>
            <td>0.99</td>
            <td>1.00</td>
            <td>340</td>
        </tr>
        <tr>
            <td>magazines</td>
            <td>1.00</td>
            <td>1.00</td>
            <td>1.00</td>
            <td>346</td>
        </tr>
        <tr>
            <td>newspaper</td>
            <td>1.00</td>
            <td>0.99</td>
            <td>1.00</td>
            <td>343</td>
        </tr>
        <tr>
            <td>office_paper</td>
            <td>1.00</td>
            <td>1.00</td>
            <td>1.00</td>
            <td>342</td>
        </tr>
        <tr>
            <td>paper_cups</td>
            <td>0.99</td>
            <td>0.95</td>
            <td>0.97</td>
            <td>338</td>
        </tr>
        <tr>
            <td>plastic_cup_lids</td>
            <td>0.95</td>
            <td>0.98</td>
            <td>0.97</td>
            <td>334</td>
        </tr>
        <tr>
            <td>plastic_detergent_bottles</td>
            <td>1.00</td>
            <td>0.99</td>
            <td>0.99</td>
            <td>331</td>
        </tr>
        <tr>
            <td>plastic_food_containers</td>
            <td>0.98</td>
            <td>0.98</td>
            <td>0.98</td>
            <td>337</td>
        </tr>
        <tr>
            <td>plastic_shopping_bags</td>
            <td>0.99</td>
            <td>0.99</td>
            <td>0.99</td>
            <td>359</td>
        </tr>
        <tr>
            <td>plastic_soda_bottles</td>
            <td>0.98</td>
            <td>0.96</td>
            <td>0.97</td>
            <td>341</td>
        </tr>
        <tr>
            <td>plastic_straws</td>
            <td>1.00</td>
            <td>1.00</td>
            <td>1.00</td>
            <td>338</td>
        </tr>
        <tr>
            <td>plastic_trash_bags</td>
            <td>1.00</td>
            <td>0.99</td>
            <td>0.99</td>
            <td>356</td>
        </tr>
        <tr>
            <td>plastic_water_bottles</td>
            <td>0.95</td>
            <td>0.98</td>
            <td>0.96</td>
            <td>343</td>
        </tr>
        <tr>
            <td>shoes</td>
            <td>1.00</td>
            <td>1.00</td>
            <td>1.00</td>
            <td>338</td>
        </tr>
        <tr>
            <td>steel_food_cans</td>
            <td>0.86</td>
            <td>0.83</td>
            <td>0.85</td>
            <td>333</td>
        </tr>
        <tr>
            <td>styrofoam_cups</td>
            <td>0.99</td>
            <td>0.99</td>
            <td>0.99</td>
            <td>341</td>
        </tr>
        <tr>
            <td>styrofoam_food_containers</td>
            <td>0.97</td>
            <td>1.00</td>
            <td>0.98</td>
            <td>343</td>
        </tr>
        <tr>
            <td>tea_bags</td>
            <td>1.00</td>
            <td>1.00</td>
            <td>1.00</td>
            <td>339</td>
        </tr>
        <tr>
            <td colspan="3"><b>Accuracy</b></td>
            <td>0.97</td>
            <td>10219</td>
        </tr>
        <tr>
            <td></td>Macro Avg</td>
            <td>0.97</td>
            <td>0.97</td>
            <td>0.97</td>
            <td>10219</td>
        </tr>
        <tr>
            <td>Weighted Avg</td>
            <td>0.97</td>
            <td>0.97</td>
            <td>0.97</td>
            <td>10219</td>
        </tr>
    </table>
</body>
</html>

![image](https://github.com/user-attachments/assets/ab98f84c-94f9-4601-8e04-a47ab9b4fe53)

2. Transfer Learning dengan _Visual Geometry Group_ (VGG16)
![image](https://github.com/user-attachments/assets/765775fc-5d05-4e9f-8e7a-23311e7f9d27)


   <!DOCTYPE html>
<html>
<body>
   <h2>Classification Report</h2>
    <table>
        <tr>
            <th>Class</th>
            <th>Precision</th>
            <th>Recall</th>
            <th>F1-Score</th>
            <th>Support</th>
        </tr>
        <tr>
            <td>aerosol_cans</td>
            <td>0.90</td>
            <td>0.84</td>
            <td>0.87</td>
            <td>348</td>
        </tr>
        <tr>
            <td>aluminum_food_cans</td>
            <td>0.48</td>
            <td>0.80</td>
            <td>0.60</td>
            <td>336</td>
        </tr>
        <tr>
            <td>aluminum_soda_cans</td>
            <td>0.69</td>
            <td>0.87</td>
            <td>0.77</td>
            <td>341</td>
        </tr>
        <tr>
            <td>cardboard_boxes</td>
            <td>0.66</td>
            <td>0.70</td>
            <td>0.67</td>
            <td>352</td>
        </tr>
        <tr>
            <td>cardboard_packaging</td>
            <td>0.66</td>
            <td>0.56</td>
            <td>0.61</td>
            <td>333</td>
        </tr>
        <tr>
            <td>clothing</td>
            <td>0.84</td>
            <td>0.83</td>
            <td>0.83</td>
            <td>330</td>
        </tr>
        <tr>
            <td>coffee_grounds</td>
            <td>0.89</td>
            <td>0.91</td>
            <td>0.90</td>
            <td>351</td>
        </tr>
        <tr>
            <td>disposable_plastic_cutlery</td>
            <td>0.93</td>
            <td>0.91</td>
            <td>0.92</td>
            <td>340</td>
        </tr>
        <tr>
            <td>eggshells</td>
            <td>0.87</td>
            <td>0.90</td>
            <td>0.88</td>
            <td>355</td>
        </tr>
        <tr>
            <td>food_waste</td>
            <td>0.73</td>
            <td>0.94</td>
            <td>0.82</td>
            <td>340</td>
        </tr>
        <tr>
            <td>glass_beverage_bottles</td>
            <td>0.89</td>
            <td>0.79</td>
            <td>0.84</td>
            <td>328</td>
        </tr>
        <tr>
            <td>glass_cosmetic_containers</td>
            <td>0.88</td>
            <td>0.74</td>
            <td>0.81</td>
            <td>323</td>
        </tr>
        <tr>
            <td>glass_food_jars</td>
            <td>0.87</td>
            <td>0.87</td>
            <td>0.87</td>
            <td>340</td>
        </tr>
        <tr>
            <td>magazines</td>
            <td>0.93</td>
            <td>0.90</td>
            <td>0.92</td>
            <td>346</td>
        </tr>
        <tr>
            <td>newspaper</td>
            <td>0.82</td>
            <td>0.80</td>
            <td>0.81</td>
            <td>343</td>
        </tr>
        <tr>
            <td>office_paper</td>
            <td>0.67</td>
            <td>0.77</td>
            <td>0.71</td>
            <td>342</td>
        </tr>
        <tr>
            <td>paper_cups</td>
            <td>0.82</td>
            <td>0.69</td>
            <td>0.75</td>
            <td>338</td>
        </tr>
        <tr>
            <td>plastic_cup_lids</td>
            <td>0.84</td>
            <td>0.74</td>
            <td>0.79</td>
            <td>334</td>
        </tr>
        <tr>
            <td>plastic_detergent_bottles</td>
            <td>0.96</td>
            <td>0.88</td>
            <td>0.92</td>
            <td>331</td>
        </tr>
        <tr>
            <td>plastic_food_containers</td>
            <td>0.83</td>
            <td>0.78</td>
            <td>0.81</td>
            <td>337</td>
        </tr>
        <tr>
            <td>plastic_shopping_bags</td>
            <td>0.85</td>
            <td>0.80</td>
            <td>0.83</td>
            <td>359</td>
        </tr>
        <tr>
            <td>plastic_soda_bottles</td>
            <td>0.75</td>
            <td>0.77</td>
            <td>0.76</td>
            <td>341</td>
        </tr>
        <tr>
            <td>plastic_straws</td>
            <td>0.94</td>
            <td>0.88</td>
            <td>0.91</td>
            <td>338</td>
        </tr>
        <tr>
            <td>plastic_trash_bags</td>
            <td>0.94</td>
            <td>0.82</td>
            <td>0.88</td>
            <td>356</td>
        </tr>
        <tr>
            <td>plastic_water_bottles</td>
            <td>0.78</td>
            <td>0.79</td>
            <td>0.79</td>
            <td>343</td>
        </tr>
        <tr>
            <td>shoes</td>
            <td>0.97</td>
            <td>0.88</td>
            <td>0.92</td>
            <td>338</td>
        </tr>
        <tr>
            <td>steel_food_cans</td>
            <td>0.72</td>
            <td>0.25</td>
            <td>0.37</td>
            <td>333</td>
        </tr>
        <tr>
            <td>styrofoam_cups</td>
            <td>0.75</td>
            <td>0.86</td>
            <td>0.80</td>
            <td>341</td>
        </tr>
        <tr>
            <td>styrofoam_food_containers</td>
            <td>0.75</td>
            <td>0.90</td>
            <td>0.82</td>
            <td>343</td>
        </tr>
        <tr>
            <td>tea_bags</td>
            <td>0.72</td>
            <td>0.78</td>
            <td>0.75</td>
            <td>339</td>
        </tr>
        <tr>
            <td colspan="2"><b>Accuracy</b></td>
            <td>0.80</td>
            <td>10219</td>
        </tr>
        <tr>
            <td>Macro Avg</td>
            <td>0.81</td>
            <td>0.80</td>
            <td>0.80</td>
            <td>10219</td>
        </tr>
        <tr>
            <td>b>Weighted Avg</td>
            <td>0.81</td>
            <td>0.80</td>
            <td>0.80</td>
            <td>10219</td>
        </tr>
    </table>
</body>
</html>

![image](https://github.com/user-attachments/assets/104b9ed1-b0bb-4596-b18a-c7462b26b43c)

Akurasi Keseluruhan :
   - CNN: 97%
   - VGG: 80%

CNN menunjukkan akurasi keseluruhan yang jauh lebih tinggi dibandingkan VGG, menunjukkan bahwa CNN lebih efektif dalam mengklasifikasikan data pada dataset ini.

**CNN**
- Kelas dengan Performa Tinggi: Banyak kelas memiliki skor sempurna (1.00) untuk precision, recall, dan F1-score, seperti clothing, coffee_grounds, eggshells, food_waste, dll.
- Kelas dengan Performa Rendah: Performa sedikit lebih rendah pada kelas seperti aluminum_food_cans (precision: 0.82, recall: 0.85).

**VGG**
- Kelas dengan Performa Tinggi: Kelas seperti plastic_detergent_bottles (precision: 0.96, recall: 0.88, F1-score: 0.92) memiliki performa yang baik.
- Kelas dengan Performa Rendah: Kelas seperti steel_food_cans memiliki F1-score sangat rendah (0.37), menunjukkan kesulitan besar dalam mengklasifikasikan kelas ini.

---

🐣 **Kesimpulan**
   - CNN secara signifikan lebih baik daripada VGG di hampir semua metrik, baik secara keseluruhan maupun per kelas.
   - CNN memiliki performa lebih stabil dan presisi tinggi, yang membuatnya lebih cocok untuk dataset ini.
   - VGG memiliki kelemahan signifikan pada beberapa kelas, seperti steel_food_cans, yang mempengaruhi akurasi keseluruhan.

---

Author : [Uswatun Khasanah](https://github.com/UswatunKhasanah209) - 202110370311209



