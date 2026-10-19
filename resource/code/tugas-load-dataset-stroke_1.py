import pandas as pd

# Memuat Stroke Prediction Dataset
url = 'https://raw.githubusercontent.com/FauzanTrisuladana/content/refs/heads/master/healthcare-dataset-stroke-data.csv'
df_stroke = pd.read_csv(url)
print("Informasi Dataset Stroke:")
print(df_stroke.info())
print("\nDimensi Dataset:", df_stroke.shape)
