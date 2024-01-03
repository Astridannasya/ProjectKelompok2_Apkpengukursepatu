from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk

root = ttk.Window(themename="flatly")
root.title("Step In Style Shoe")
root.geometry('600x700')

ttk.Label(root, text="Aplikasi Menentukan Ukuran Sepatu", font=('Calibri', 15, 'bold')).pack(pady=15)
ttk.Label(root, text="Masukkan panjang kaki anda (cm): ").pack(pady=15)

panjang_kaki = Entry()
panjang_kaki.insert(END, 0)
panjang_kaki.pack()

ttk.Label(root, text="Pilih Jenis Sepatu: ").pack(pady=15)
# Pilihan jenis sepatu menggunakan Combobox
opsi_sepatu = ttk.Combobox(root, values=["Sneakers", "Heels", "Pantofel", "Sandal Sepatu"])
opsi_sepatu.pack()

# Label untuk menampilkan gambar
gambar_label = ttk.Label(root)
gambar_label.pack(pady=15)

# Load untuk Gambar
sneakers = Image.open("D:/project/ddpsi01/projectuas/images/sneakers.jpg")  
heels = Image.open("D:/project/ddpsi01/projectuas/images/Heels.jpg") 
Pantofel = Image.open("D:/project/ddpsi01/projectuas/images/Pantofel.jpg") 
Sandalsepatu = Image.open("D:/project/ddpsi01/projectuas/images/Sandalsepatu.jpg") 
sneakers = sneakers.resize((200, 200), Image.BICUBIC)
heels = heels.resize((200, 200), Image.BICUBIC)
Pantofel = Pantofel.resize((200, 200), Image.BICUBIC)
Sandalsepatu = Sandalsepatu.resize((200, 200), Image.BICUBIC)
sneakers = ImageTk.PhotoImage(sneakers)
heels = ImageTk.PhotoImage(heels)
Pantofel = ImageTk.PhotoImage(Pantofel)
Sandalsepatu = ImageTk.PhotoImage(Sandalsepatu)

# Fungsi menampilkan gambar sepatu sesuai pilihan
def tampil_gambar(selection):
    gambar_label.configure(image=None)  # Hapus gambar sebelumnya jika ada
    if selection == "Sneakers":
        gambar_label.configure(image=sneakers)
    elif selection == "Heels":
        gambar_label.configure(image=heels)
    elif selection == "Pantofel":
        gambar_label.configure(image=Pantofel)
    elif selection == "Sandal sepatu":
        gambar_label.configure(image=Sandalsepatu)

# Variabel global untuk label hasil
result_label = ttk.Label(root)
result_label.pack()

def hitung(): 
    hitung_panjang_kaki = int(panjang_kaki.get())

    if hitung_panjang_kaki < 22.5:
        result = "Ukuran sepatu Eropa Anda: 36 (Eropa) \nUkuran sepatu Amerika anda: 6 (Amerika)"
    elif hitung_panjang_kaki == 23:
        result = "Ukuran sepatu Eropa Anda: 37-38 (Eropa) \nUkuran sepatu Amerika anda: 7 (Amerika)"
    elif hitung_panjang_kaki == 24:
        result = "Ukuran sepatu Eropa Anda: 38-39 (Eropa) \nUkuran sepatu Amerika anda: 8-8.5 (Amerika)"
    elif hitung_panjang_kaki >= 25:
        result = "Ukuran sepatu Eropa Anda: 39-40 (Eropa) \nUkuran sepatu Amerika anda: 9 (Amerika)"
    else:
        result = "Ukuran sepatu anda tidak ada"

    # Memanggil fungsi untuk menampilkan gambar sesuai pilihan
    tampil_gambar(opsi_sepatu.get())

    
    # Memperbarui teks pada label hasil
    result_label.configure(text=result)


ttk.Button(root, text="Hitung", command=hitung, bootstyle=SUCCESS).pack(pady=10)

root.mainloop()
