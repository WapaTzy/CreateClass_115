import tkinter as tk

# --- Fungsi untuk Tombol Hasil Prediksi ---
def tampilkan_prediksi():
    """
    Fungsi ini dipanggil saat tombol 'Hasil Prediksi' diklik.
    Sesuai tugas, hasilnya selalu 'Teknologi Informasi'.
    """
    hasil_label.config(text="Hasil Prediksi: Teknologi Informasi")

# --- Pengaturan Jendela Utama GUI ---
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("450x450") # Mengatur ukuran jendela yang lebih ramping

# --- Widget GUI ---

# 1. Label Judul Aplikasi
judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16, "bold"), fg="darkblue", pady=15)
judul.pack()

# Frame untuk Input Nilai (Wadah utama)
input_frame = tk.Frame(root, padx=20, pady=10)
input_frame.pack(pady=10)

input_nilai_entries = [] # List untuk menyimpan 10 kotak input

# 2. 10 Input Nilai Mata Pelajaran (disusun dalam 1 kolom Entry)
for i in range(10):
    row_num = i
    
    # Label untuk setiap mata pelajaran (di kolom 0)
    tk.Label(input_frame, text=f"Nilai Mata Pelajaran {i+1}:").grid(row=row_num, column=0, sticky="w", padx=5, pady=2)

    # Kotak Input (Entry) tunggal (di kolom 1)
    entry = tk.Entry(input_frame, width=15)
    entry.grid(row=row_num, column=1, padx=5, pady=2, sticky="ew")
    input_nilai_entries.append(entry)

# 3. Tombol Hasil Prediksi
tombol_prediksi = tk.Button(root, text="Hasil Prediksi", command=tampilkan_prediksi, font=("Arial", 12), bg="#A3D9A3", padx=10, pady=5)
tombol_prediksi.pack(pady=20)

# 4. Label Luaran Hasil Prediksi
hasil_label = tk.Label(root, text="Hasil Prediksi: (akan muncul di sini)", font=("Arial", 12, "italic"), fg="blue", pady=10)
hasil_label.pack()

# --- Menjalankan Aplikasi ---
root.mainloop()

# Contoh mengisi nilai awal pada kolom tunggal
input_nilai_entries[0].insert(0, "85.0")
input_nilai_entries[1].insert(0, "92.5")
input_nilai_entries[2].insert(0, "78.0")
input_nilai_entries[3].insert(0, "88.0")
input_nilai_entries[4].insert(0, "90.0")
input_nilai_entries[5].insert(0, "95.0")
input_nilai_entries[6].insert(0, "80.0")
input_nilai_entries[7].insert(0, "86.0")
input_nilai_entries[8].insert(0, "84.0")
input_nilai_entries[9].insert(0, "91.0")