# Foto Motivasi

Foto Motivasi adalah aplikasi web interaktif yang menggunakan kecerdasan buatan untuk memberikan pujian dan motivasi berdasarkan foto yang diunggah pengguna. Aplikasi ini menggunakan Gemini API untuk analisis gambar dan generasi teks.

## Fitur

- Upload foto dengan antarmuka yang user-friendly
- Analisis gambar menggunakan Gemini API
- Generasi pujian dan motivasi yang personal
- UI modern dan responsif dengan Vue.js dan Tailwind CSS
- Loading teks yang interaktif dengan tema memasak

## Teknologi yang Digunakan

- Backend: Python dengan Flask
- Frontend: Vue.js dan Tailwind CSS
- AI: Gemini API

## Cara Menjalankan Aplikasi

1. Clone repositori ini
2. Install dependencies:
   ```
   pip install flask google-generativeai
   ```
3. Set environment variable untuk Gemini API key:
   ```
   export GEMINI_API_KEY=your_api_key_here
   ```
4. Jalankan aplikasi:
   ```
   python app.py
   ```
5. Buka browser dan akses `http://localhost:5002`

## Kontribusi

Kontribusi selalu diterima dengan senang hati. Silakan buat issue atau pull request jika Anda memiliki saran atau perbaikan.

## Lisensi

[MIT License](https://opensource.org/licenses/MIT)
