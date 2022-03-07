# pip install pandas
# pip install sklearn

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


data = {'Sleeve': [1, 2, 3],
        'Quality': [4, 4, 2]}

df = pd.DataFrame (data, columns = ['Sleeve','Quality'])

print(df)

similarity = cosine_similarity(df)

print(similarity)