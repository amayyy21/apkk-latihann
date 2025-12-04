import streamlit as st
import pandas as pd

st.title("Aplikasi Manajemen Keuangan Pribadi")

st.write("Catat pemasukan dan pengeluaranmu di sini.")

# Form input
with st.form("form_keuangan"):
    tanggal = st.date_input("Tanggal")
    kategori = st.selectbox("Kategori", ["Pemasukan", "Pengeluaran"])
    jumlah = st.number_input("Jumlah (Rp)", min_value=0)
    deskripsi = st.text_input("Deskripsi")
    submit = st.form_submit_button("Simpan")

if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Tanggal", "Kategori", "Jumlah", "Deskripsi"])

if submit:
    st.session_state.data.loc[len(st.session_state.data)] = [tanggal, kategori, jumlah, deskripsi]
    st.success("Data berhasil disimpan!")

# Tampilkan tabel
st.subheader("Riwayat Keuangan")
st.dataframe(st.session_state.data)
