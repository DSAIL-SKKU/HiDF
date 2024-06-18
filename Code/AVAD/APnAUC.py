import pandas as pd
from sklearn.metrics import roc_auc_score, average_precision_score

df_real = pd.read_csv('./save/FakeAVCeleb_Real_score.csv')
df_fake = pd.read_csv('./save/FakeAVCeleb_Fake_score.csv')

df_real['label'] = 0
df_fake['label'] = 1

df_combined = pd.concat([df_real, df_fake])
df_combined = df_combined[df_combined['score'] != 'Error']

y_scores = df_combined['score'].astype(float)
y_true = df_combined['label']

ap = average_precision_score(y_true, y_scores)
auc = roc_auc_score(y_true, y_scores)

num_real = sum(y_true == 0)
num_fake = sum(y_true == 1)

print(f"Average Precision (AP): {ap:.4f}")
print(f"Area Under the Curve (AUC): {auc:.4f}")