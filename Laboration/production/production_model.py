import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, ConfusionMatrixDisplay, confusion_matrix

df = pd.read_csv("../data/test_samples.csv")
X_test, y_test = df.drop(columns="cardio", axis="columns"), df["cardio"]


model = joblib.load(filename="../production//model.pkl")


y_pred = model.predict(X_test)
cr = classification_report(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

# Create and save ConfusionMatrix to folder
ConfusionMatrixDisplay(cm).plot()
plt.savefig(f"../production/result_cm.png")

# Write results to result.txt
with open("../production/result.txt", "a") as f:
    f.write(f"{cr}\n\n")