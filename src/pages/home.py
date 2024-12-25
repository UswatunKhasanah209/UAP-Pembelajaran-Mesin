import streamlit as st

# Set halaman
st.set_page_config(
    page_title="UAP Machine Learning",
    page_icon="🐳",
    layout="wide",
)

import streamlit as st

# Tambahkan CSS untuk estetika
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Poppins', sans-serif;
        background-color: #1e1e2f; /* Background hitam */
        color: #f0f0f0; /* Warna teks terang */
    }
    
    .title {
        color: #FFB86C; /* Warna orange terang */
        text-align: center;
        font-size: 42px;
        font-weight: 600;
        margin-top: 20px;
    }

    .subtitle {
        color: #8BE9FD; /* Warna biru cerah */
        text-align: center;
        font-size: 22px;
        font-weight: 300;
        margin-bottom: 20px;
    }

    .info-card {
        background: linear-gradient(135deg, #6272A4, #44475A); /* Gradasi abu gelap */
        border-radius: 12px;
        padding: 10px;
        margin: 10px auto;
        text-align: center;
        color: #F8F8F2; /* Warna teks putih */
        font-size: 20px;
        font-weight: 400;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        width: 50%;
        animation: slide-in 1s ease-out;
    }

    @keyframes slide-in {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .emoji {
        font-size: 30px;
        margin-right: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header Utama
st.markdown("<div class='title'>✨ UAP MACHINE LEARNING ✨</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Prediksi Kategori Sampah Organik dan Anorganik Berbasis AI dengan Deep Learning</div>", unsafe_allow_html=True)

# Informasi User
st.markdown("<div class='info-card'><span class='emoji'>👤</span>Nama: Uswatun Khasanah</div>", unsafe_allow_html=True)
st.markdown("<div class='info-card'><span class='emoji'>🆔</span>NIM: 202110370311209</div>", unsafe_allow_html=True)
