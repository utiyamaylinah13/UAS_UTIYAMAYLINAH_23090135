import pandas as pd

data_mahasiswa = [
    [90,80],
    [50,60],
    [65,70]

]

mahasiswa=['mahasiswa1','mahasiswa2','mahasiswa3']

data_mahasiswa = {
    'mahasiswa1' : [90,80],
    'mahasiswa2' : [50,60],
    'mahasiswa3' : [65,70]
}

df = pd.DataFrame(data_mahasiswa)
print(df)

rata_rata_nilai_setiap_mata_kuliah = df.mean()
rata_rata_nilai_setiap_mahasisa = df.mean(axis=1)
print(f'{rata_rata_nilai_setiap_mata_kuliah}')
print(f'{rata_rata_nilai_setiap_mahasisa}')
