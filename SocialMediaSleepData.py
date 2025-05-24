#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Veri setini yükleme
data = pd.read_csv(r"C:\\Users\\rozer\\OneDrive\\Masaüstü\\SocialMediaUsage_SleepLatencyAnalysis_Singapore.csv")

# İlk birkaç satıra göz atalım
print(data.head())


# In[2]:


# Eksik veri kontrolü
print(data.isnull().sum())


# In[3]:


import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder, MinMaxScaler
# Sayısal olmayan sütunları kontrol et
non_numeric_columns = data.select_dtypes(include=['object']).columns
print("Sayısal olmayan sütunlar:", non_numeric_columns)

# Metin sütunlarını sayıya çevir
label_encoder = LabelEncoder()
for col in non_numeric_columns:
    data[col] = label_encoder.fit_transform(data[col])

print(data.head())

# Korelasyon matrisini oluşturma ve görselleştirme
correlation_matrix = data.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Korelasyon Matrisi")
plt.show()





# In[4]:


from sklearn.model_selection import train_test_split

# Özellikler ve hedef değişken
features = [
    "Average Daily Social Media Use Time (minutes)",
    "Frequency of Social Media Checking (number of times per day)",
    "Pre-Sleep Social Media Use Duration (minutes)",
    "Blue Light Exposure Before Sleep (minutes)",
    "Stress Level Rating",
    "Sleep Efficiency (%)"
]
target = "Sleep Latency (minutes)"

X = data[features]
y = data[target]

# Veriyi %80 eğitim ve %20 test olarak ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[5]:


# Veriyi normalleştirme
scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)


# In[6]:


from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Modeli oluştur ve eğit
model = LinearRegression()
model.fit(X_train, y_train)

# Tahmin yap ve doğruluğu ölç
y_pred = model.predict(X_test)
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
# Veriyi normalleştirme
scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)


# In[7]:


import tkinter as tk
from tkinter import messagebox
import numpy as np

# Model yerine bir tahmin fonksiyonu ekleyelim (örneğin, basit bir formül)
def predict_sleep_time(avg_social_use, social_check_freq, pre_sleep_social, blue_light, stress, sleep_efficiency):
    prediction = (avg_social_use * 0.5 + social_check_freq * 1.2 + pre_sleep_social * 0.8 + 
                  blue_light * 0.3 + stress * 2 + (100 - sleep_efficiency) * 0.4)
    return prediction

# Pencere oluşturma
root = tk.Tk()
root.title("Uykuya Dalma Süresi Tahmini")
root.geometry("400x600")  # Pencere boyutunu artırma

# Arka plan rengini ve yazı tipi stilini belirleme
root.config(bg="#f5f5f5")

# Kullanıcı girdileri için etiketler ve giriş kutuları
def create_label(text):
    label = tk.Label(root, text=text, font=("Arial", 12), bg="#f5f5f5")
    label.pack(pady=5)
    return label

create_label("Günlük Sosyal Medya Kullanımı (dk):")
avg_social_use_entry = tk.Entry(root, font=("Arial", 12), width=20)
avg_social_use_entry.pack(pady=5)

create_label("Sosyal Medya Kontrol Sayısı:")
social_check_freq_entry = tk.Entry(root, font=("Arial", 12), width=20)
social_check_freq_entry.pack(pady=5)

create_label("Uyumadan Önce Sosyal Medya Kullanımı (dk):")
pre_sleep_social_entry = tk.Entry(root, font=("Arial", 12), width=20)
pre_sleep_social_entry.pack(pady=5)

create_label("Mavi Işık Maruziyeti (dk):")
blue_light_entry = tk.Entry(root, font=("Arial", 12), width=20)
blue_light_entry.pack(pady=5)

create_label("Stres Seviyesi (1-10):")
stress_entry = tk.Entry(root, font=("Arial", 12), width=20)
stress_entry.pack(pady=5)

create_label("Uyku Verimliliği (%):")
sleep_efficiency_entry = tk.Entry(root, font=("Arial", 12), width=20)
sleep_efficiency_entry.pack(pady=5)

# Tahmin fonksiyonu
def on_predict_button_click():
    try:
        avg_social_use = float(avg_social_use_entry.get())
        social_check_freq = float(social_check_freq_entry.get())
        pre_sleep_social = float(pre_sleep_social_entry.get())
        blue_light = float(blue_light_entry.get())
        stress = float(stress_entry.get())
        sleep_efficiency = float(sleep_efficiency_entry.get())

        # Tahmini uykuya dalma süresi hesapla
        prediction = predict_sleep_time(avg_social_use, social_check_freq, pre_sleep_social, blue_light, stress, sleep_efficiency)

        # Sonucu göster
        messagebox.showinfo("Tahmin", f"Tahmini Uykuya Dalma Süresi: {prediction:.2f} dakika")
    
    except ValueError:
        messagebox.showerror("Hata", "Lütfen tüm alanları geçerli sayılarla doldurun!")

# Tahmin butonu
predict_button = tk.Button(root, text="Tahmin Et", command=on_predict_button_click, font=("Arial", 14), bg="#4CAF50", fg="white", relief="raised", width=15)
predict_button.pack(pady=20)

# Pencereyi çalıştır
root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




