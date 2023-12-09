#stats.py
import pandas as pd
import numpy as np

class CustomStatistics:
    def __init__(self, data):
        #Memastikan input data merupakan pandas DataFrame
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Data input harus berupa pandas Data Frame.")
        self.data = data

    def calculate_mean(self, nama_kolom):
        try:
            #Menghitung rata-rata menggunakan fungsi mean dari NumPy
            data_kolom = self.data[nama_kolom]
            mean = np.mean(data_kolom)
            return mean
        except Exception as e:
            #Menangani exception jika terjadi kesalahan
            raise Exception(f"Error menghitung rata-rata untuk kolom '{nama_kolom}': {e}")

    def calculate_median(self, nama_kolom):
        try:
            #Menghitung median menggunakan fungsi median dari NumPy
            data_kolom = self.data[nama_kolom]
            median = np.median(data_kolom)
            return median
        except Exception as e:
            #Menangani exception jika terjadi kesalahan
            raise Exception(f"Error menghitung median untuk kolom '{nama_kolom}': {e}")

    def calculate_mode(self, nama_kolom):
        try:
            #Menghitung modus menggunakan fungsi argmax dan bincount dari NumPy
            data_kolom = self.data[nama_kolom]
            mode = float(np.argmax(np.bincount(data_kolom)))
            return mode
        except Exception as e:
            #Menangani exception jika terjadi kesalahan
            raise Exception(f"Error menghitung modus untuk kolom '{nama_kolom}': {e}")
