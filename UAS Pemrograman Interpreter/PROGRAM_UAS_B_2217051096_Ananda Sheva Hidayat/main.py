#main.py
from stats import CustomStatistics
import pandas as pd

#Menyiapkan DataFrame
data = {'Fee': [20000, 25000, 30000, 22000, 26000],
        'Total': [18000, 22000, 27000, 19800, 25000]}
df = pd.DataFrame(data)

#Membuat instance method dari CustomStatistics
custom_stats = CustomStatistics(df)

#Menghitung mean, median, dan modus untuk 'Fee'
mean_fee = custom_stats.calculate_mean('Fee')
median_fee = custom_stats.calculate_median('Fee')
mode_fee = custom_stats.calculate_mode('Fee')

#Menghitung mean, median, dan modus untuk 'Total'
mean_total = custom_stats.calculate_mean('Total')
median_total = custom_stats.calculate_median('Total')
mode_total = custom_stats.calculate_mode('Total')

#Menampilkan hasil
print("Statistik untuk Fee")
print("Median : ", median_fee)
print("Modus : ", mode_fee)
print("Mean : ", mean_fee)

print("\nStatistik untuk Total")
print("Median : ", median_total)
print("Modus : ", mode_total)
print("Mean : ", mean_total)