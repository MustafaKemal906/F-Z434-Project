# SHM Sarkaç Simülatörü (RK2 vs RK4)

Bu proje, basit harmonik hareket (SHM) yapan bir sarkacın ikinci dereceden diferansiyel denklemini sayısal yöntemlerle çözen, modüler yapıda bir Python uygulamasıdır. 

Uygulama, **Geliştirilmiş Euler (RK2)** ve **Ralston'ın 4. Dereceden (RK4)** Runge-Kutta yöntemlerini kullanarak sarkaç hareketini simüle eder ve sonuçları karşılaştırmalı olarak grafik üzerinde sunar. Ayrıca kullanıcıların parametreleri kolayca değiştirebileceği dinamik bir arayüze (GUI) sahiptir.

## Özellikler

- **Görsel Arayüz (GUI):** Tkinter ile geliştirilmiş, kullanıcı dostu kontrol paneli.
- **Dinamik Sarkaç Çizimi:** Girilen sarkaç boyu (L) ve başlangıç açısı (θ) değerlerine göre anında güncellenen görsel sarkaç animasyonu.
- **Karşılaştırmalı Analiz:** RK2 ve RK4 yöntemlerinin aynı grafik üzerinde Matplotlib ile görselleştirilmesi.
- **Modüler Yapı:** Kolay okunabilir, sürdürülebilir ve geliştirilebilir kod mimarisi.

## Proje Yapısı

Proje dosyaları işlevlerine göre `src` klasörü altında modüllere ayrılmıştır:

```text
📁 proje_klasoru/
├── 📄 main.py           # Uygulamayı başlatan ana dosya
└── 📁 src/
    ├── 📄 __init__.py   # Modül dışa aktarımları
    ├── 📄 variables.py  # Değişkenler ve veri sınıfları (Dataclasses)
    ├── 📄 pipline.py    # RK2 ve RK4 matematiksel çözüm algoritmaları
    ├── 📄 graph.py      # Matplotlib ile grafik çizim işlemleri
    └── 📄 gui.py        # Tkinter arayüzü ve Canvas etkileşimleri
```

## Gereksinimler

- Python 3.8+
- `numpy`
- `matplotlib`
- `tkinter` (Python ile gömülü gelir)

## Nasıl Çalıştırılır?

Bu proje, modern Python paket yöneticisi olan **uv** ile tam uyumlu çalışacak şekilde tasarlanmıştır.

Terminalinizi proje dizininde açın ve aşağıdaki komutu çalıştırın:

```bash
uv run main.py
```

*(Eğer `uv` kullanmıyorsanız, doğrudan `python main.py` komutuyla da çalıştırabilirsiniz.)*

## Kullanım

1. Uygulama açıldığında karşınıza parametre giriş ekranı gelecektir.
2. Yerçekimi (g), Sarkaç Boyu (L), Zaman Adımı (h) gibi değerleri dilediğiniz gibi değiştirin.
3. Parametreleri değiştirdikçe ekranın üst kısmındaki sarkaç resminin güncellendiğini görebilirsiniz.
4. **"🚀 Çöz ve Çiz"** butonuna basarak iki farklı sayısal yöntemin (RK2 ve RK4) ürettiği sonuç grafiğini inceleyebilirsiniz.