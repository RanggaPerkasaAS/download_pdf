import os
import requests
import pandas as pd

# URL file Google Sheets CSV atau Excel (unduh sebagai CSV atau Excel terlebih dahulu)
sheet_url = 'Data SNI - data_sni_all.csv'
df = pd.read_csv(sheet_url)  # Untuk Excel, gunakan pd.read_excel(sheet_url)

# Kolom dengan URL file PDF
url_columns = ['Kolom 3', 'Kolom 4', 'Kolom 5', 'Kolom 6']

# Folder tempat menyimpan semua file
base_folder = 'Downloaded_PDFs'
os.makedirs(base_folder, exist_ok=True)

for index, row in df.iterrows():
    # Buat folder untuk baris ini
    row_folder = os.path.join(base_folder, f'Row_{index + 1}')
    os.makedirs(row_folder, exist_ok=True)
    
    for column in url_columns:
        url = row.get(column)
        if pd.notna(url):  # Pastikan URL tidak kosong
            try:
                response = requests.get(url)
                filename = url.split('/')[-1]
                file_path = os.path.join(row_folder, filename)
                
                with open(file_path, 'wb') as file:
                    file.write(response.content)
                
                print(f"Downloaded: {filename} into {row_folder}")
            except Exception as e:
                print(f"Failed to download {url}: {e}")



