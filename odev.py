# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 19:49:23 2026

@author: gmzes
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. VERİ TANITIMI VE VERİLERİN BİRLEŞTİRİLMESİ
# ==========================================
print("=== DÜNYA MUTLULUK ENDEKSİ ANALİZ RAPORU ===")
print("Bu çalışmada, 2017, 2018 ve 2019 yıllarına ait Dünya Mutluluk Raporu incelenmiştir.\n")

# Bilgisayarımızdaki 3 yılı okuyoruz
df_2017 = pd.read_csv("2017.csv")
df_2018 = pd.read_csv("2018.csv")
df_2019 = pd.read_csv("2019.csv")

# Sütun isimlerini birbiriyle eşitlemek ve Türkçeleştirmek için gerekli düzenleme
df_17 = df_2017[['Country', 'Happiness.Score', 'Economy..GDP.per.Capita.', 'Health..Life.Expectancy.']].copy()
df_17.columns = ['Ülke', 'Mutluluk_Skoru', 'Ekonomi_GDP', 'Sağlık_Yaşam']

df_18 = df_2018[['Country or region', 'Score', 'GDP per capita', 'Healthy life expectancy']].copy()
df_18.columns = ['Ülke', 'Mutluluk_Skoru', 'Ekonomi_GDP', 'Sağlık_Yaşam']

df_19 = df_2019[['Country or region', 'Score', 'GDP per capita', 'Healthy life expectancy']].copy()
df_19.columns = ['Ülke', 'Mutluluk_Skoru', 'Ekonomi_GDP', 'Sağlık_Yaşam']

# Üç yılı alt alta birleştirerek 300 satır sınırını fazlasıyla aşıyoruz (Yaklaşık 460 satır)
df = pd.concat([df_17, df_18, df_19], ignore_index=True)

# İlk 5 satırı konsola yazdıralım
print("--- Veri Setinin İlk 5 Satırı ---")
print(df.head())


# ==========================================
# 2. HOCANIN İSTEDİĞİ 4 TANE İSTATİSTİK
# ==========================================
print("\n=== İSTATİSTİKSEL ÖZETLER ===")

# İstatistik 1: Genel özet (Ortalamalar, min, max değerleri)
print("\n1. Veri Seti Matematiksel Özeti:")
print(df.describe())

# İstatistik 2: En yüksek mutluluk skoru
print("\n2. En Yüksek Mutluluk Skoru:", df['Mutluluk_Skoru'].max())

# İstatistik 3: En düşük mutluluk skoru
print("3. En Düşük Mutluluk Skoru:", df['Mutluluk_Skoru'].min())

# İstatistik 4: Değişkenlerin birbiriyle ilişkisi (Korelasyon)
print("\n4. Değişkenlerin Birbiriyle İlişkisi (Korelasyon):")
print(df[['Mutluluk_Skoru', 'Ekonomi_GDP', 'Sağlık_Yaşam']].corr())


# ==========================================
# 3. HOCANIN İSTEDİĞİ 5 GRAFİK VE YORUMLARI
# ==========================================
print("\n=== GRAFİKLER ÇİZİLİYOR ===")

# GRAFİK 1: Dağılım Grafiği (Histogram)
plt.figure(figsize=(6,4))
df['Mutluluk_Skoru'].hist(bins=20, color='skyblue', edgecolor='black')
plt.title('Dünya Mutluluk Skorlarının Dağılımı')
plt.xlabel('Mutluluk Skoru')
plt.ylabel('Ülke Sayısı')
plt.show()
print("\nYorum 1: Mutluluk skorlarının çoğunlukla 4.5 ile 6 puan arasında yoğunlaştığı görülmektedir.")

# GRAFİK 2: Kutu Grafiği (Boxplot)
plt.figure(figsize=(6,4))
sns.boxplot(x=df['Mutluluk_Skoru'], color='lightgreen')
plt.title('Mutluluk Skorlarının Kutu Grafiği (Çeyreklikler)')
plt.show()
print("Yorum 2: Kutu grafiği incelendiğinde medyan değerinin 5.5 civarında olduğu anlaşılır.")

# GRAFİK 3: Saçılım Grafiği (Scatter Plot)
plt.figure(figsize=(6,4))
sns.scatterplot(data=df, x='Ekonomi_GDP', y='Mutluluk_Skoru', color='purple')
plt.title('Ekonomi ile Mutluluk Arasındaki İlişki')
plt.xlabel('Ekonomik Durum (GDP)')
plt.ylabel('Mutluluk Skoru')
plt.show()
print("Yorum 3: Ekonomik güç (GDP) arttıkça mutluluk skorunun da arttığı doğrusal olarak gözlemlenmektedir.")

# GRAFİK 4: Sağlık ile Mutluluk Arasındaki İlişki (Scatter Plot)
plt.figure(figsize=(6,4))
sns.scatterplot(data=df, x='Sağlık_Yaşam', y='Mutluluk_Skoru', color='coral')
plt.title('Sağlık-Yaşam Süresi ile Mutluluk Arasındaki İlişki')
plt.xlabel('Sağlık ve Yaşam Beklentisi')
plt.ylabel('Mutluluk Skoru')
plt.show()
print("Yorum 4: Sağlıklı yaşam süresi beklentisi yüksek olan ülkelerin mutluluk seviyeleri de daha yüksektir.")

# GRAFİK 5: Isı Haritası (Heatmap)
plt.figure(figsize=(6,4))
sns.heatmap(df[['Mutluluk_Skoru', 'Ekonomi_GDP', 'Sağlık_Yaşam']].corr(), annot=True, cmap='coolwarm')
plt.title('Faktörlerin Birbiriyle Olan İlişki Haritası')
plt.show()
print("Yorum 5: Isı haritasına göre, mutluluk skoru ile ekonomi ve sağlık değişkenleri arasında güçlü pozitif bir ilişki vardır.")


# ==========================================
# 4. BULGULAR VE SONUÇ
# ==========================================
print("\n=== BULGULAR VE SONUÇ ===")
print("* Bulgu 1: Dünyadaki mutluluk dağılımı dengeli bir yayılım göstermektedir; aşırı uç değerler azınlıktadır.")
print("* Bulgu 2: Maddi refah (GDP) arttıkça insanların mutluluk puanı doğrudan yükselmektedir.")
print("* Bulgu 3: Kaliteli sağlık hizmetlerine erişim ve uzun yaşam süresi, toplumsal mutluluğu en çok tetikleyen ikinci büyük etkendir.")