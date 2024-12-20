# -*- coding: utf-8 -*-
"""Tugas_3_STDA4101_M_Faqih.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1c-F277TRElIbwqYzcgaL8JqcW7m3u2Fr

# Import Library
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

"""# Data Load"""

df_penyakit = pd.read_excel('/content/Tugas 3 STDA4101-2024.1 (1).xlsx')
print(df_penyakit)

"""**Keterangan:**
* Y : Ukuran kuantitatif perkembangan penyakit setelah satu tahun amatan
* AGE : Age in Years
* BMI : Body Mass Index (indeks massa tubuh)
* BP : Average Blood Pressure (Rata rata tekanan darah)
* S1 : Total serum cholesterol (Kolesterol serum total)
"""

# mengambil kolom tertentu untuk analisis
df = df_penyakit[['AGE', 'BMI', 'BP', 'S1', 'Y']].dropna()
print(df)

"""# Data Wrangling"""

#mengecek tipe datanya terlebih dahulu
df.info()

# Mengecek duplikasi
df.duplicated().sum()

# Mengecek missing values
df.isna().sum()

"""# EDA"""

#statistik deskriptif
df.describe()

"""

*  Kolom AGE:berkisar antara 19 hingga 72 tahun, dengan rata-rata 45.82 tahun
*  Kolom BMI: Indeks massa tubuh antara 18.6 hingga 38, rata-rata 25.40.
*  Kolom BP: Tekanan darah rata-rata 91.37, dengan rentang dari 63 hingga 131.
*  Kolom S1: Serum kolesterol total antara 97 hingga 264, dengan rata-rata 180.91.
*  Dan kolom Y: Ukuran perkembangan penyakit berkisaran 37 hingga 341, rata-rata 133.56.
"""

# Korelasi antara variabel numerik
df.corr()

"""# Jawaban Tugas 3"""

# Soal 1.Membuat visualisasi data multivariat dengan menggunakan scatter plot untuk mengetahui hubungan antar variabel
sns.pairplot(df, diag_kind='kde', markers ='+', corner = True)
plt.suptitle("Scatter Plot Multivariat", y=1.02, fontsize=14)
plt.show()

"""* Kita memodelkan hubungan variabel dependen Y (ukuran perkembangan penyakit) dengan variabel independen AGE, BMI, BP, dan S1"""

#Soal 2.Tentukan model persamaan regresi linear
X = df[['AGE', 'BMI', 'BP', 'S1']]
y = df['Y']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())

#Soal 3.Berikan ulasan Anda tentang model tersebut.

"""1.   Kualitas model R-squared = 0.270  ini hanya menjelaskan 27% variabilitas variabel dependen Y. Ini menunjukkan bahwa sebagian besar variabilitas perkembangan penyakit tidak dapat dijelaskan oleh variabel independen dalam model ini,F-statistic = 8.768 dimana model secara keseluruhan signifikan, yang berarti setidaknya satu variabel independen memiliki hubungan yang signifikan dengan Y.


---



2.   Durbin-Watson = 1.986: Nilai ini mendekati 2, menunjukkan bahwa tidak ada autokorelasi dalam residual, yang baik untuk model regresi.
Omnibus dan Jarque-Bera = P-value > 0.05 menunjukkan bahwa residual berdistribusi normal, sehingga asumsi regresi terpenuhi.

---



3.   Signifikansi koefisien individual

* const	=-119.89 ;nilai perkembangan penyakit tanpa pengaruh variabel lain
* AGE	=-0.0748 Tidak signifikan (p > 0.05). Usia tidak memiliki hubungan yang berarti dengan perkembangan penyakit dalam model ini.
* BMI	=8.3701	Sangat signifikan (p < 0.01). BMI memiliki hubungan positif, artinya peningkatan 1 unit BMI meningkatkan Y sebesar 8.37 unit.
* BP	=0.8582 Tidak signifikan (p > 0.05). Tekanan darah memiliki kontribusi kecil yang tidak signifikan.
* S1  =-0.1886 Tidak signifikan (p > 0.05). Serum kolesterol tidak menunjukkan hubungan yang berarti.

---

4. Masalah Multikolinearitas (Condition Number) = 1.87e+03 (1,870): Angka ini cukup besar, menunjukkan kemungkinan adanya multikolinearitas antara variabel independen. Hal ini dapat memengaruhi stabilitas estimasi koefisien.

# Insight

**Kesimpulan**

Dari keempat variabel independen, hanya BMI yang signifikan secara statistik dalam menjelaskan perkembangan penyakit (Y). Variabel lainnya mungkin tidak terlalu relevan,dengan kemampuan model regresi ini dalam menjelaskan varibel dependen Y (ukuran perkembangan penyakit) masih terbatas....Sekian
"""