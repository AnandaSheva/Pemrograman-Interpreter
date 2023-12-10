#data.py
import pandas as pd


def add_additional_data(df):
    new_data = {'Courses': ['TensorFlow', 'PyTorch', 'Scikit-learn', 'JavaScript', 'React'],
                'Categories': ['ML', 'ML', 'ML', 'Web', 'Web'],
                'Fee': [28000, 30000, 26000, 18000, 22000],
                'Duration': ['45days', '40days', '30days', '45days', '35days'],
                'Percentage Discount': ['8%', '12%', '7%', '5%', '8%']}

    return df.append(pd.DataFrame(new_data), ignore_index=True)

def calculate_total(df):
    def calculate_row_total(row):
        discount_percentage = int(row['Percentage Discount'][:-1]) / 100
        total_discount = discount_percentage * row['Fee']
        total_discount_2 = 0.02 * row['Fee']

        if row['Categories'] == 'PI':
            return row['Fee'] * int(row['Duration'][:-4]) - total_discount - total_discount_2
        else:
            return row['Fee'] * int(row['Duration'][:-4]) - total_discount

    df['Total'] = df.apply(calculate_row_total, axis=1)
    return df
