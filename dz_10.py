"""
Задача 44: В ячейке ниже представлен код генерирующий DataFrame, 
которая состоит всего из 1 столбца. Ваша задача перевести 
его в one hot вид. Сможете ли вы это сделать без get_dummies?
"""
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Ваш исходный DataFrame
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})


encoder = OneHotEncoder(sparse=False)
one_hot_encoded = encoder.fit_transform(data[['whoAmI']]).astype(int)
columns = [category for category in encoder.get_feature_names_out(['whoAmI'])]
data = pd.concat(
    [data, pd.DataFrame(one_hot_encoded, columns=columns)], axis=1)
print(data)
