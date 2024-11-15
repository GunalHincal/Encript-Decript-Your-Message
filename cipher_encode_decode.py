# -*- coding: utf-8 -*-

import streamlit as st

# Türkçe karakterlerle uyumlu Sezar Şifreleme fonksiyonu
def caesar_cipher_encode(plaintext, key):
    # Türkçe alfabesi (küçük harflerle)
    alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
    alphabet_hash = {char: index for index, char in enumerate(alphabet)}
    reverse_alphabet_hash = {index: char for char, index in alphabet_hash.items()}
    ciphertext = []
    
    for char in plaintext:
        if char.lower() in alphabet_hash:  # Eğer karakter Türkçe alfabesinde varsa
            # Şifrelenmiş konumu hesapla
            new_position = (alphabet_hash[char.lower()] + key) % len(alphabet)
            encoded_char = reverse_alphabet_hash[new_position]
            # Büyük harf kontrolü ve Türkçe karakterlerin uyumlu dönüşümü
            if char.isupper():
                # Türkçe karakterlerin büyük harf uyumu sağlanıyor
                if encoded_char == 'i':
                    encoded_char = 'İ'
                elif encoded_char == 'ı':
                    encoded_char = 'I'
                else:
                    encoded_char = encoded_char.upper()
            ciphertext.append(encoded_char)
        else:
            # Alfabe dışında bir karakter ise olduğu gibi ekle
            ciphertext.append(char)
    return ''.join(ciphertext)

# Türkçe karakterlerle uyumlu Sezar Çözme fonksiyonu
def caesar_cipher_decode(ciphertext, key):
    # Türkçe alfabesi (küçük harflerle)
    alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
    alphabet_hash = {char: index for index, char in enumerate(alphabet)}
    reverse_alphabet_hash = {index: char for char, index in alphabet_hash.items()}
    plaintext = []
    
    for char in ciphertext:
        if char.lower() in alphabet_hash:  # Eğer karakter Türkçe alfabesinde varsa
            # Orijinal konumu hesapla
            original_position = (alphabet_hash[char.lower()] - key) % len(alphabet)
            decoded_char = reverse_alphabet_hash[original_position]
            # Büyük harf kontrolü ve Türkçe karakterlerin uyumlu dönüşümü
            if char.isupper():
                # Türkçe karakterlerin büyük harf uyumu sağlanıyor
                if decoded_char == 'i':
                    decoded_char = 'İ'
                elif decoded_char == 'ı':
                    decoded_char = 'I'
                else:
                    decoded_char = decoded_char.upper()
            plaintext.append(decoded_char)
        else:
            # Alfabe dışında bir karakter ise olduğu gibi ekle
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
st.caption("Sezar Şifreleme ve Çözme Aracı - Güvenli ve Eğlenceli!")
