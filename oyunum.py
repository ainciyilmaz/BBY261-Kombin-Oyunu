import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

gardirob = {
    "ceket": [
        {"ad": "Blazer Ceket", "tarz": "Ofis", "resim": "resimler/ceket_ofis.jpg"},
        {"ad": "Kürk", "tarz": "Parti", "resim": "resimler/ceket_parti.jpg"},
        {"ad": "Fermuarlı Hırka", "tarz": "Spor", "resim": "resimler/ceket_spor.jpg"},
        {"ad": "Deri Ceket", "tarz": "Günlük", "resim": "resimler/ceket_gunluk.jpg"}
    ],
    "ust": [
        {"ad": "Beyaz Gömlek", "tarz": "Ofis", "resim": "resimler/ust_ofis.jpg"},
        {"ad": "Payetli Üst", "tarz": "Parti", "resim": "resimler/ust_parti.jpg"},
        {"ad": "Spor Atlet", "tarz": "Spor", "resim": "resimler/ust_spor.jpg"},
        {"ad": "Salaş Kazak", "tarz": "Günlük", "resim": "resimler/ust_gunluk.jpg"}
    ],
    "alt": [
        {"ad": "Kumaş Pantolon", "tarz": "Ofis", "resim": "resimler/alt_ofis.jpg"},
        {"ad": "Mini Etek", "tarz": "Parti", "resim": "resimler/alt_parti.jpg"},
        {"ad": "Spor Tayt", "tarz": "Spor", "resim": "resimler/alt_spor.jpg"},
        {"ad": "Jean Pantolon", "tarz": "Günlük", "resim": "resimler/alt_gunluk.jpg"}
    ],
    "ayakkabi": [
        {"ad": "Platform Topuklu Bot", "tarz": "Ofis", "resim": "resimler/ayakkabi_ofis.jpg"},
        {"ad": "Topuklu Ayakkabı", "tarz": "Parti", "resim": "resimler/ayakkabi_parti.jpg"},
        {"ad": "Koşu Ayakkabısı", "tarz": "Spor", "resim": "resimler/ayakkabi_spor.jpg"},
        {"ad": "Sneaker", "tarz": "Günlük", "resim": "resimler/ayakkabi_gunluk.jpg"}
    ],
    "canta": [
        {"ad": "Büyük Omuz Çantası", "tarz": "Ofis", "resim": "resimler/canta_ofis.jpg"},
        {"ad": "Simli El Çantası", "tarz": "Parti", "resim": "resimler/canta_parti.jpg"},
        {"ad": "Spor Çantası", "tarz": "Spor", "resim": "resimler/canta_spor.jpg"},
        {"ad": "Kot Çanta", "tarz": "Günlük", "resim": "resimler/canta_gunluk.jpg"}
    ],
    "aksesuar": [
        {"ad": "Bilgisayar", "tarz": "Ofis", "resim": "resimler/aksesuar_ofis.jpg"},
        {"ad": "Kurdele Küpe", "tarz": "Parti", "resim": "resimler/aksesuar_parti.jpg"},
        {"ad": "Termos", "tarz": "Spor", "resim": "resimler/aksesuar_spor.jpg"},
        {"ad": "Minimal Küpe", "tarz": "Günlük", "resim": "resimler/aksesuar_gunluk.jpg"}
    ]
}

gorevler = [
    {"metin": "Telefonun çalıyor... Arayan patronun!\nAcil şirkete gitmen lazım, yönetim kurulu toplantısı var.\n\nGÖREV: Ciddi ve şık bir OFİS kombini yap.", "hedef_tarz": "Ofis"},
    {"metin": "Haftasonu arkadaşlarınla en sevdiğiniz kafeye gidiyorsunuz.\nGÖREV: Rahat ama havalı bir GÜNLÜK kombin yap.", "hedef_tarz": "Günlük"},
    {"metin": "Aylardır beklediğin o partiye gidiyorsun!\nHerkes orada olacak.\n\nGÖREV: Göz kamaştırıcı bir PARTİ kombini yap.", "hedef_tarz": "Parti"},
    {"metin": "Uzun zamandır sporu aksattın.\nBugün o gün! Spor salonuna gitme zamanı.\n\nGÖREV: Seni motive edecek bir SPOR kombini yap.", "hedef_tarz": "Spor"}
]

class ModaOyunu:
    def __init__(self, pencere):
        self.pencere = pencere
        self.pencere.title("Stil İkonu")
        self.pencere.geometry("1100x800") 
        self.pencere.configure(bg="white")
        
        self.secimler = {"ceket": 0, "ust": 0, "alt": 0, "ayakkabi": 0, "canta": 0, "aksesuar": 0}
        self.mevcut_gorev = None
        
        self.giris_ekranini_goster()

    def giris_ekranini_goster(self):
        self.temizle()
        self.pencere.configure(bg="white")

        frame_giris = tk.Frame(self.pencere, bg="white")
        frame_giris.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame_giris, text="MODA KOMBİN\nYARIŞMASI", font=("Helvetica", 32, "bold"), 
                 bg="white", fg="black").pack(pady=40)

        tk.Button(frame_giris, text="OYNA", font=("Arial", 16, "bold"), 
                  bg="black", fg="white", width=20, height=2, cursor="hand2",
                  command=self.oyun_baslat).pack(pady=10)

        tk.Button(frame_giris, text="ÇIKIŞ", font=("Arial", 16, "bold"), 
                  bg="white", fg="black", width=20, height=2, cursor="hand2", bd=2, relief="solid",
                  command=self.pencere.destroy).pack(pady=10)

    def oyun_baslat(self):
        self.temizle()
        self.pencere.configure(bg="white")
        
        self.mevcut_gorev = random.choice(gorevler)
        
        self.lbl_senaryo = tk.Label(self.pencere, text="", font=("Courier New", 14, "bold"), 
                                    bg="white", fg="black", justify="left", anchor="nw", padx=20, pady=20,
                                    bd=2, relief="solid", width=90, height=5, wraplength=900)
        self.lbl_senaryo.pack(pady=20)

        self.yazi_efekti(self.mevcut_gorev["metin"], 0)

    def yazi_efekti(self, metin, index):
        if index < len(metin):
            self.lbl_senaryo.config(text=metin[:index+1])
            self.pencere.after(35, self.yazi_efekti, metin, index+1)
        else:
            self.kiyafet_secim_ekranini_getir()

    def kiyafet_secim_ekranini_getir(self):
        self.content_frame = tk.Frame(self.pencere, bg="white")
        self.content_frame.pack(pady=10, expand=True)

        
        self.create_selector(self.content_frame, "Üst Giyim", "ust", row=0, col=0)
        self.create_selector(self.content_frame, "Alt Giyim", "alt", row=0, col=1)
        self.create_selector(self.content_frame, "Dış Giyim / Ceket", "ceket", row=0, col=2)
        
        
        self.create_selector(self.content_frame, "Ayakkabı", "ayakkabi", row=1, col=0)
        self.create_selector(self.content_frame, "Çanta", "canta", row=1, col=1)
        self.create_selector(self.content_frame, "Aksesuar", "aksesuar", row=1, col=2)

        btn_frame = tk.Frame(self.pencere, bg="white")
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="KOMBİNİ TAMAMLA", font=("Arial", 12, "bold"), 
                  bg="black", fg="white", width=25, height=2, cursor="hand2",
                  command=self.sonuc_goster).pack()

    def create_selector(self, parent, title, key, row, col):
        frame = tk.Frame(parent, bg="white", bd=1, relief="solid")
        frame.grid(row=row, column=col, padx=15, pady=10)

        tk.Label(frame, text=title, font=("Arial", 11, "bold"), bg="white", fg="black").pack(pady=5)

        lbl = tk.Label(frame, bg="#f0f0f0", width=20, height=10) 
        lbl.pack(padx=5, pady=2)
        setattr(self, f"lbl_{key}", lbl)

        ctrl_frame = tk.Frame(frame, bg="white")
        ctrl_frame.pack(pady=5)
        
        tk.Button(ctrl_frame, text="<", font=("Arial", 10, "bold"), bg="white", fg="black", bd=1, relief="solid", width=3,
                  command=lambda: self.degistir(key, -1)).pack(side="left", padx=10)
        
        tk.Button(ctrl_frame, text=">", font=("Arial", 10, "bold"), bg="white", fg="black", bd=1, relief="solid", width=3,
                  command=lambda: self.degistir(key, 1)).pack(side="left", padx=10)
        
        self.gorsel_guncelle(key)

    def degistir(self, key, yon):
        limit = len(gardirob[key])
        self.secimler[key] += yon
        if self.secimler[key] >= limit: self.secimler[key] = 0
        elif self.secimler[key] < 0: self.secimler[key] = limit - 1
        self.gorsel_guncelle(key)

    def gorsel_guncelle(self, key):
        idx = self.secimler[key]
        veri = gardirob[key][idx]
        lbl = getattr(self, f"lbl_{key}")
        try:
            img = Image.open(veri["resim"])
            img = img.resize((140, 140), Image.LANCZOS) 
            photo = ImageTk.PhotoImage(img)
            lbl.config(image=photo, text=veri["ad"], compound="top", font=("Arial", 9), width=150, height=160) 
            lbl.image = photo
        except:
            lbl.config(text=f"{veri['ad']}\n(Resim Yok)", image="", width=20, height=10)

    def sonuc_goster(self):
        hedef = self.mevcut_gorev["hedef_tarz"]
        puan = 0
        dogru_sayisi = 0

        for key, idx in self.secimler.items():
            secilen = gardirob[key][idx]
            secilen_tarz = secilen["tarz"]
            
            if secilen_tarz == hedef:
                puan += 15
                dogru_sayisi += 1
            elif hedef == "Günlük" and secilen_tarz == "Ofis":
                puan -= 5
            elif hedef == "Spor" and (secilen_tarz == "Ofis" or secilen_tarz == "Parti"):
                puan -= 10
            else:
                puan -= 2 

        if dogru_sayisi == 6:
            puan = 100

        if puan < 0: puan = 0

        
        mesaj = f"Puanın: {puan} / 100"
            
        cevap = messagebox.askyesno("Sonuç", mesaj + "\n\nTekrar oynamak ister misin?")
        if cevap:
            self.oyun_baslat() 
        else:
            self.giris_ekranini_goster()

    def temizle(self):
        for widget in self.pencere.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    uygulama = ModaOyunu(root)
    root.mainloop()