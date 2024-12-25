import streamlit as st
import tensorflow as tf
from pathlib import Path
import numpy as np


# Judul aplikasi
st.title("✨ Klasifikasi Citra: Organik & Anorganik ✨")

# Pilihan model
model_choice = st.radio(
    "Pilih Model:",
    ("CNN", "VGG"),
    index=0,
    horizontal=True,
)

# Fungsi untuk memuat model berdasarkan pilihan
@st.cache_resource
def load_model(model_name):
    model_path = Path(__file__).parent.parent / "model" / f"{model_name.lower()}_model.h5"
    return tf.keras.models.load_model(model_path)

# Memuat model yang dipilih
model = load_model("cnn" if model_choice == "CNN" else "vgg")

# Fungsi untuk prediksi
def predict(image, model):
    class_names = [
        "aerosol_cans",
        "aluminum_food_cans",
        "aluminum_soda_cans",
        "cardboard_boxes",
        "cardboard_packaging",
        "clothing",
        "disposable_plastic_cutlery",
        "glass_beverage_bottles",
        "glass_cosmetic_containers",
        "glass_food_jars",
        "magazines",
        "newspaper",
        "office_paper",
        "paper_cups",
        "plastic_cup_lids",
        "plastic_detergent_bottles",
        "plastic_food_containers",
        "plastic_shopping_bags",
        "plastic_soda_bottles",
        "plastic_straws",
        "plastic_trash_bags",
        "plastic_water_bottles",
        "shoes",
        "steel_food_cans",
        "styrofoam_cups",
        "styrofoam_food_containers"]
    
    organik_classes = [
        "coffee_grounds", 
        "eggshells", 
        "food_waste", 
        "tea_bags"]

    img = tf.keras.utils.load_img(image, target_size=(224, 224))
    img_array = tf.keras.utils.img_to_array(img) / 255.0
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)
    scores = tf.nn.softmax(predictions[0])
    predicted_class = np.argmax(scores)
    
    category = "organik" if class_names[predicted_class] in organik_classes else "anorganik"
    scores_dict = {class_names[i]: scores[i].numpy() * 100 for i in range(len(class_names))}
    
    return scores_dict, category

# Input gambar
st.write("Unggah gambar atau gunakan kamera:")
camera_input = st.camera_input("Ambil gambar menggunakan kamera 📸")
file_upload = st.file_uploader("Atau unggah file gambar 📂", type=['png', 'jpg', 'jpeg'])

# Tombol prediksi
if st.button("🔍 Predict", type="primary"):
    if camera_input is not None:
        st.image(camera_input, caption="Gambar dari kamera", use_container_width=True)
        image_path = "temp_image.png"
        with open(image_path, "wb") as f:
            f.write(camera_input.getvalue())
    elif file_upload is not None:
        st.image(file_upload, caption="Gambar dari file", use_container_width=True)
        image_path = "temp_image.png"
        with open(image_path, "wb") as f:
            f.write(file_upload.getvalue())
    else:
        st.write("Silakan unggah gambar terlebih dahulu!")
        st.stop()

    # Prediksi
    st.subheader("🧠 Hasil Prediksi:")
    with st.spinner('⏳ Memproses citra untuk prediksi...'):
        scores_dict, category = predict(image_path, model)

    # Menampilkan hasil
    st.write(f"**Kategori:** {category.capitalize()}")

    st.write("**Perbandingan Kelas:**")
    for class_name, score in sorted(scores_dict.items(), key=lambda x: x[1], reverse=True):
        st.write(f"- {class_name}: {score:.2f}%")
