import tkinter
import pyqrcode
import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk
#dosya kontrolu icin

#window

# Ana pencereyi olustur
root = tk.Tk()
root.title("QR Code Creator")
root.geometry("400x250")

background_image = Image.open("QRCODEMAKER.jpg")
background_photo = ImageTk.PhotoImage(background_image)

background_label = tkinter.Label(root, image = background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
def create_qr():
    url = url_entry.get() #kullanicinin girdigi url yi al
    if not url:
        messagebox.showerror("Hata", "Lutfen gecerli/aktif bir URL giriniz: ")
        return


    #QRcode olusturma
    try:

        qr_code = pyqrcode.create(url)

        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        file_path = os.path.join(desktop_path,"NEWqrcode.svg")
        
        qr_code.svg(file_path,scale=5) #svg formatinda kaydet

        if os.path.exists('NEWqrcode.svg'):
            messagebox.showinfo("Basarili, QR Code basariyla olusturuldu, kaydedildi! ")
        else:
            messagebox.showerror("Hata, Qr Kodu olusturulamadi! ")
    except Exception as e:
        messagebox.showerror("Hata",f"bir hataolustu:{e}")




#URL giris icin etiket ve giris kutusu
url_label = tk.Label(root, text ="Olusturmak Istedigin Site linkini gir: ")
url_label.pack(pady=10)

url_entry = tk.Entry(root,width =40)
url_entry.pack(pady= 5)

#QR kodu olusturma butonu

generate_button = tk.Button(root, text="Simdi Olustur", command=create_qr)
generate_button.pack(pady=20)
#Ana donguyu otomatik baslat
root.mainloop()


