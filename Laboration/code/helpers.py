import pandas as pd



def rename_columns(df):
    """
    Function to rename columns for more informative plots.
    To get rid of unecessary code from report.

    Parameters: df = pd.Dataframe

    """
    #Rename columns for plot
    df["cholesterol"] = df["cholesterol"].replace({1:"Normal", 2:"Above normal", 3:"Well above normal"}) # 1 = normal cholesterol, 2 = above normal, 3 = well above normal
    df["gender"] = df["gender"].replace({1:"Women", 2:"Men"}) # 1 = women, 2 = men
    df["cardio"] = df["cardio"].replace({0:"No Cardio", 1:"Cardio"}) # 0 = no cardio disease, 1 = cardio disease
    df["smoke"] = df["smoke"].replace({0:"Non smoker", 1:"Smoker"}) # 0 = Non smoker, 1 = smoker

    return df

