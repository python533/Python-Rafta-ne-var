import _sqlite3


con=_sqlite3.connect("kitaplar.db")
cursor=con.cursor()

def tabloolsutur():
    cursor.execute("CREATE TABLE IF NOT EXIST tablo1(kitap_no INT,kitap_adi TEXT,kitap_yazar TEXT)")

def veriekle():
    print("İstenilen Bilgileri Girniz:")
    kitap_no=kitap_no = input("Kitap Numarasını Giriniz:")
    kitap_adı=kitap_adı = input("Kitap Adını Giriniz:")
    kitap_yazar=kitap_yazar = input("Kitap Yazarı:")
    ekle=cursor.execute("INSERT INTO tablo1(kitap_no,kitap_adı,kitap_yazar) VALUES(?,?,?)",(kitap_no,kitap_adı,kitap_yazar))
    if ekle:
        print("Veriler Başarıyla Eklendi")
    else:
        print("Bir Hata Meydana Geldi! Tekrar Deneyin")

def verial():
    cursor.excute("SELECT * FROM tablo1")
    data=cursor.fetchall()
    kitapno=input("Kitap Numarasını Girin:")
    if kitapno not in['ç','Ç']:
        for k in data:
            if k == kitapno:
                print("kitap_no"+[0],"Kitap_adı"+[1],"Kitap Yazar"+[2])



