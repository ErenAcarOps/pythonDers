#-----------------FORM TOOLS(tkinter)---------------------------------------
# import tkinter as tk #Dışardan kütüphaneleri çağırmak için kullanılır
# pencere=tk.Tk() #pencere oluşturma
# pencere.title("Eren ACAR") #pencere başlık ekleme
# pencere.geometry("700x500") #pencere boyutunu ayarlama
#pencere.resizable(False,False) #pencereyi kullanıcının boyutlandırmasını kapatma
#pencere.minsize("100x100") #pencerenin olabilecek en küçük boyut değeri 
#pencere.maxsize("800x800") #pencerenin olabilecek en büyük boyut değeri
#---------------------------------------------------------------------------
# pencere.update() #pencere güncelleme
# en=pencere.winfo_width() #winfo>>pencere bilgilerini çekeriz
# boy=pencere.winfo_height()
# sol=pencere.winfo_x()
# ust=pencere.winfo_y()
# print("En   :",en)
# print("Boy  :",boy)
# print("Sol  :",sol)
# print("Ust  :",ust)
#------------------------------------------------------------------------
# pencere.state("zoomed") #state kullanımı ve komutları
# zoomed>> pencereyi ekrana doldurur
# iconic>>simge oluşturmak
# withdrawn>>Gözükmeyen pencere
# normal>>bizim belirlediğimiz boyutlarda açar
#-------------------------------------------------------------
#pencere.vm_attributes("-alpha",0.6) # pencereyi saydamlık ekler
#pencere.vm_attributes("-fullscreen",1) # başlık kısmı ve penceriyi kapatma butonları yok eder
#pencere.vm_attributes("-topmost",1) # açtığınız pencereyi en önde tutar
#-------------------------------------------------------------------

# tk.mainloop() #Ana Döngü>>komutların sürekli çalışması için

#--------------------------------------------------------------
#--------------------------------------------------------------
#-------------LABEL----------------------------
# from tkinter import * # bu kütühaneyi isim verilmeden kullanılır birden fazla kütüphane olursa kullanma
# pencere= Tk()
# pencere.title("Label Deneme")
# pencere.geometry("200x200")

# etiket=Label(text="Merhaba Eren ACAR",fg="blue",bg="yellow",padx=50,pady=30,font=("Open Sans","30","bold","italic"))
#padx>>sağına soluna boşluk
#pady>>üst alt boşluk

# etiket.pack() #paketleyip pencerenin içine yüklüyor
# mainloop()

#---------------------------------------------------------------
#---------------------------------------------------------------
#--------------------Resim Ekleme--------------------------------
# from tkinter import *
# pencere=Tk()
# pencere.title("Resim Ekleme")
# pencere.geometry("800x800")
# 
# resim=PhotoImage(file="sinopLogo.png")
# yazi=Label(image=resim)
# yazi.pack()
# mainloop()
#-------------------------------------------------------------------
