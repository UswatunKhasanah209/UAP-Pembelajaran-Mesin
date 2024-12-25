# 🗑️**Prediksi Kategori Sampah Organik dan Anorganik Berbasis AI dengan Deep Learning**🗑️
---


🐳 **Latar Belakang** 

Sampah merupakan salah satu masalah lingkungan yang semakin mendesak, terutama di era modern ini. Dengan pertumbuhan populasi dan urbanisasi yang pesat, produksi sampah juga meningkat secara signifikan. Menurut data, pemilahan sampah menjadi langkah krusial untuk mengurangi dampak negatif terhadap lingkungan. Pemisahan antara sampah organik dan anorganik tidak hanya penting untuk pengelolaan limbah yang lebih baik tetapi juga untuk mendukung program daur ulang dan pengurangan volume sampah yang dibuang ke tempat pembuangan akhir. Dengan menggunakan algoritma deep learning, sistem dapat dilatih untuk mengenali dan mengklasifikasikan berbagai jenis sampah secara otomatis. Hal ini tidak hanya meningkatkan efisiensi dalam proses pemilahan tetapi juga mengurangi kesalahan manusia yang sering terjadi dalam pemilahan manual24.

---

👾 **Tujuan Pengembangan** 
1. Mengembangkan sistem prediksi berbasis AI yang mampu mengidentifikasi kategori sampah organik dan anorganik secara otomatis dengan menggunakan algoritma deep learning.
2. Memberikan kontribusi nyata pada pengelolaan limbah perkotaan dengan teknologi modern yang mudah diimplementasikan di berbagai skala, mulai dari rumah tangga hingga industri besar.

---

🌱 **Langkah Instalasi**

👽 **dataset** 
1. Dataset [Recyclable and Household Waste Classification](https://www.kaggle.com/datasets/alistairking/recyclable-and-household-waste-classification) diunduh dari kaggle dan diekstraksi.
2. Gambar-gambar diatur ulang dengan memindahkan semua isi subfolder ke folder utama masing-masing kategori.
3. Dataset dibagi menjadi dua kategori besar:
   - organik (coffee_grounds, eggshells, food_waste, tea_bags)
   - anorganik (aerosol_cans, aluminum_food_cans, aluminum_soda_cans, cardboard_boxes, cardboard_packaging, clothing, disposable_plastic_cutlery, glass_beverage_bottles, glass_cosmetic_containers, glass_food_jars, magazines, newspaper, office_paper, paper_cups, plastic_cup_lids, plastic_detergent_bottles, plastic_food_containers, plastic_shopping_bags, plastic_soda_bottles, plastic_straws, plastic_trash_bags, plastic_water_bottles, shoes, steel_food_cans, styrofoam_cups, styrofoam_food_containers).
4. Kemudian dataset dibagi menjadi tiga subset: train (70%), validation (15%), dan test (15%) untuk setiap kategori.

👽 **Preprocessing**
1. Gambar di-rescale (normalisasi) ke rentang 0 dan 1 menggunakan ImageDataGenerator.
2. Subset train, validation, dan test di-load menggunakan generator dengan ukuran target gambar 224x224 piksel.

👽 **Model**
1. Model CNN (_Convolutional Neural Network_)
   - Dua lapisan Conv2D diikuti dengan MaxPooling2D.
   - Lapisan Flatten untuk mengubah data ke dimensi 1D.
   - Lapisan Dense dengan 128 neuron dan aktivasi relu.
   - Lapisan Dropout untuk mengurangi overfitting.
   - Lapisan keluaran dengan aktivasi softmax sesuai jumlah kelas.
2. Transfer Learning dengan VGG16(_Visual Geometry Group_)
   - Menggunakan model VGG16 yang sudah dilatih sebelumnya (pretrained) pada dataset ImageNet.
   - Lapisan-lapisan VGG16 dibekukan (tidak dilatih ulang), dan ditambahkan lapisan:
   - GlobalAveragePooling2D untuk mengurangi dimensi fitur.
   - Dense dengan 256 neuron dan aktivasi relu.
   - Dropout untuk mengurangi overfitting.
   - Lapisan keluaran dengan aktivasi softmax.
  
👽 **Evaluasi Model**
1. Model CNN (_Convolutional Neural Network_)
<!DOCTYPE html>
<html>
<body>
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
            <td>accuracy</td>
            <td> </td>
            <td> </td>
            <td>0.97</td>
            <td>10219</td>
        </tr>
       <tr>
            <td>macro avg</td>
            <td>0.97</td>
            <td>0.97</td>
            <td>0.97</td>
            <td>10219</td>
        </tr>
       <tr>
            <td>weighted avg</td>
            <td>0.97</td>
            <td>0.97</td>
            <td>0.97</td>
            <td>10219</td>
        </tr>
    </table>
 </body>
</html>  

2. Transfer Learning dengan VGG16(_Visual Geometry Group_)
   <!DOCTYPE html>
<html>
<body>
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
            <td>accuracy</td>
            <td> </td>
            <td> </td>
            <td>0.80</td>
            <td>10219</td>
        </tr>
       <tr>
            <td>macro avg</td>
            <td>0.81</td>
            <td>0.80</td>
            <td>0.80</td>
            <td>10219</td>
        </tr>
       <tr>
            <td>weighted avg</td>
            <td>0.81</td>
            <td>0.80</td>
            <td>0.80</td>
            <td>10219</td>
        </tr>
    </table>
</body>
</html>

---

👽 **Aplikasi Web**
1. Install PDM pada powershell
2. Masukkan perintah "pdm init"
3. Install bberapa Pustaka seperti : Streamlit, Tensorflow, Joblib dan Scikit-learn
4. Membuat file :
   - app.py : Berfungsi sebagai pengatur navigasi aplikasi 
   - home.py : Halaman utama dengan informasi umum
   - classification.py: Halaman untuk prediksi kategori sampah berdasarkan model yang dipilih (CNN/VGG).
5. lalu menjalankan perintah ["pdm run start"](http://localhost:8501/)

---

Berikut link Google colab : [UAP Machine Learning](https://colab.research.google.com/drive/1zPSyVg8ZvGocSFpxiTs5p3mxewrIpNiR?usp=sharing)

---


🔥 **Hasil dan analisis**

   ✨ Hasil
   
1. Model CNN (_Convolutional Neural Network_)
   ![image](https://github.com/user-attachments/assets/3faeaf7c-867e-43c0-8edc-e21db6738f2c)
   ![image](https://github.com/user-attachments/assets/d1d0201b-c954-4e61-a60e-fe96df782470)
2. Transfer Learning dengan VGG16(_Visual Geometry Group_)
   ![image](https://github.com/user-attachments/assets/a117275c-ed55-49eb-945b-13b843b62fba)
   ![image](https://github.com/user-attachments/assets/4ce9520e-612e-41b0-be88-cff758f5009a)

   ✨ Analisis
   
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



   









