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
1. [Recyclable and Household Waste Classification](https://www.kaggle.com/datasets/alistairking/recyclable-and-household-waste-classification) dari kaggle
2. Dataset dibagi menjadi dua kategori besar:
   - organik (coffee_grounds, eggshells, food_waste, tea_bags)
   - anorganik (aerosol_cans, aluminum_food_cans, aluminum_soda_cans, cardboard_boxes, cardboard_packaging, clothing, disposable_plastic_cutlery, glass_beverage_bottles, glass_cosmetic_containers, glass_food_jars, magazines, newspaper, office_paper, paper_cups, plastic_cup_lids, plastic_detergent_bottles, plastic_food_containers, plastic_shopping_bags, plastic_soda_bottles, plastic_straws, plastic_trash_bags, plastic_water_bottles, shoes, steel_food_cans, styrofoam_cups, styrofoam_food_containers).
3. Kemudian dataset dibagi menjadi tiga subset: train (70%), validation (15%), dan test (15%) untuk setiap kategori.

👽 **Preprocessing**
1. Gambar di-rescale (normalisasi) ke rentang 0 dan 1 menggunakan ImageDataGenerator.


