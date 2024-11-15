# -*- coding: utf-8 -*-

import streamlit as st

# Türkçe alfabeye göre küçük ve büyük harf eşlemeleri
alphabet_lower = "abcçdefgğhıijklmnoöprsştuüvyz"
alphabet_upper = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"

# Şifreleme fonksiyonu
def caesar_cipher_encode(plaintext, key):
    ciphertext = []
    
    for char in plaintext:
        if char in alphabet_lower:
            # Küçük harflerde şifreleme
            new_position = (alphabet_lower.index(char) + key) % len(alphabet_lower)
            ciphertext.append(alphabet_lower[new_position])
        elif char in alphabet_upper:
            # Büyük harflerde şifreleme
            new_position = (alphabet_upper.index(char) + key) % len(alphabet_upper)
            ciphertext.append(alphabet_upper[new_position])
        else:
            # Harf dışında karakter ise olduğu gibi ekle
            ciphertext.append(char)
    
    return ''.join(ciphertext)

# Çözme fonksiyonu
def caesar_cipher_decode(ciphertext, key):
    plaintext = []
    
    for char in ciphertext:
        if char in alphabet_lower:
            # Küçük harflerde çözme
            original_position = (alphabet_lower.index(char) - key) % len(alphabet_lower)
            plaintext.append(alphabet_lower[original_position])
        elif char in alphabet_upper:
            # Büyük harflerde çözme
            original_position = (alphabet_upper.index(char) - key) % len(alphabet_upper)
            plaintext.append(alphabet_upper[original_position])
        else:
            # Harf dışında karakter ise olduğu gibi ekle
            plaintext.append(char)
    
    return ''.join(plaintext)

# Streamlit uygulaması
st.title("🔐 Sezar Şifreleme ve Çözme Aracı")
st.write("Metinlerinizi güvenli bir şekilde şifreleyin veya şifrelerini çözün!")

# Yan sekmeler oluştur
tab1, tab2 = st.tabs(["Şifreleme", "Çözme"])

# Şifreleme Paneli
with tab1:
    st.header("🔒 Şifreleme Paneli")
    plaintext = st.text_area("Şifrelemek istediğiniz metni buraya yazın:", placeholder="Metninizi buraya yazın...")
    key = st.number_input("Anahtar (key) değeri girin:", min_value=1, max_value=29, value=3, step=1)
    if st.button("Şifrele"):
        if plaintext.strip():
            encrypted_text = caesar_cipher_encode(plaintext, key)
            st.success(f"Şifrelenmiş Metin: {encrypted_text}")
        else:
            st.warning("Lütfen şifrelemek için bir metin girin.")

# Çözme Paneli
with tab2:
    st.header("🔓 Çözme Paneli")
    ciphertext = st.text_area("Çözmek istediğiniz şifreli metni buraya yazın:", placeholder="Şifreli metni buraya yazın...")
    key = st.number_input("Anahtar (key) değeri girin:", min_value=1, max_value=29, value=3, step=1, key="decode_key")
    if st.button("Çöz"):
        if ciphertext.strip():
            decrypted_text = caesar_cipher_decode(ciphertext, key)
            st.success(f"Çözümlenmiş Metin: {decrypted_text}")
        else:
            st.warning("Lütfen çözmek için bir şifreli metin girin.")

# Alt bilgi
st.write("---")
st.caption("Sezar Şifreleme ve Çözme Aracı - Güvenli ve Eğlenceli! ")

st.caption("📝 Unutmayın ki, Sezar'ın hakkı Sezar'a! 😆")
