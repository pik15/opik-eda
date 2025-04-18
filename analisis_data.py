import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('Most Streamed Spotify Songs 2024.csv', encoding='ISO-8859-1')

# Menampilkan 5 baris pertama
print("🔹 5 Baris Pertama:")
print(df.head())

# Info tipe data dan jumlah non-null
print("\n🔹 Info Dataset:")
print(df.info())

# Deskripsi statistik
print("\n🔹 Deskripsi Statistik:")
print(df.describe())

# Membersihkan nama kolom (hapus spasi)
df.columns = df.columns.str.strip()

# Cek nama kolom
print("\n🔹 Nama Kolom dalam DataFrame:")
print(df.columns)

# Cek missing values
print("\n🔹 Jumlah Missing Values:")
print(df.isnull().sum())

# Tangani missing values - contoh (isi NaN dengan median jika numerik)
# Gantilah kolom sesuai kasus
# df['KolomNumerik'] = df['KolomNumerik'].fillna(df['KolomNumerik'].median())

# Cek dan hapus duplikasi
print("\n🔹 Jumlah Duplikat:")
print(df.duplicated().sum())
df = df.drop_duplicates()

# Visualisasi Distribusi Popularitas
plt.figure(figsize=(8, 5))
sns.histplot(df['Spotify Popularity'], bins=30, kde=True)
plt.title('Distribusi Popularitas Spotify')
plt.xlabel('Popularitas')
plt.ylabel('Frekuensi')
plt.tight_layout()
plt.show()

# Boxplot untuk deteksi outlier
plt.figure(figsize=(8, 4))
sns.boxplot(x=df['Spotify Popularity'])
plt.title('Boxplot Popularitas Spotify')
plt.tight_layout()
plt.show()

# Heatmap Korelasi (untuk kolom numerik saja)
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Heatmap Korelasi antar Variabel Numerik')
plt.tight_layout()
plt.show()

# Simpan data yang sudah dibersihkan (opsional)
# df.to_csv('data_bersih.csv', index=False)
