# Klasifikasi Gambar Rock-Paper-Scissors dengan Model Sequential menggunakan TensorFlow pada Google Colabs

Keterangan:
- Dataset diambil dari https://dicodingacademy.blob.core.windows.net/picodiploma/ml_pemula_academy/rockpaperscissors.zip
- menggunakan teknik split folder
- Dataset berisi 2.188 gambar (rock-paper-scissor), yang terdiri dari 726 gambar rock, 712 gambar paper, dan 750 gambar scissors
- Dataset dibagi kedalam 2 bagian, yaitu data tarining (60%), data validation (40%)
- Penulisan kode dilakukan dengan Python pada Google Colabs
- Menggunakan TensorFlow, beserta library lainnya untuk mendukung proses komputasi yang dilakukan
- Menerapkan proses Augmentasi Gambar untuk menciptakan data-data gambar baru yang sesuai untuk format algoritma yang digunakan
- Menerapkan Image Data Generator
- Pelatihan data latih menggunakan Model Sequential
- melakukan visualisasi terhadap akurasi model dan loss-nya
- Klasifikasi gambar dilakukan melalui media upload di Google Colabs
- Tingkat akurasi diatas 85%
- Model yang dibuat bisa memprediksi gambar yang di upload
- train-stop menggunakan callback saat akurasi di atas 85%
