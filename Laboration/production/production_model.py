import pandas as pd
import joblib


df = pd.read_csv("../data/test_samples.csv")
X_test, y_test = df.drop(columns="cardio", axis="columns"), df["cardio"]


model = joblib.load(filename="../production//model.pkl")

prediction = model.predict(X_test)
probability = model.predict_proba(X_test)

df_results = pd.DataFrame(probability, columns=["probability class_0", "probability class_1"], index=None)
df_results.insert(len(df_results.columns), "prediction", prediction)

df_results.to_csv("../production/result.csv")
