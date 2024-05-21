import pandas as pd
import os

# MASAUSTU
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# DOSYA KONUMU
railway_file_path = os.path.join(desktop_path, 'railway.csv')
dictionary_file_path = os.path.join(desktop_path, 'railway_data_dictionary.csv')

# VERILERI OKUMAK ICIN
railway_data = pd.read_csv(railway_file_path)
data_dictionary = pd.read_csv(dictionary_file_path)

# İlk birkaç satırı göster
print("\n**railway.csv İLK BİRKAÇ SATIR**\n")
print(railway_data.head())

print("\n**railway_data_dictionary.csv İLK BİRKAÇ SATIR**:\n")
print(data_dictionary.head())

# SUTUN ADLARINI VE VERI TÜRLERİ
print("\n**railway.csv Sütun Adları ve Veri Türleri**:\n")
print(railway_data.dtypes)

# UYGULAMAYI SONLANDIRMA
input("\nÇıkış yapmak için bir tuşa basın...")
