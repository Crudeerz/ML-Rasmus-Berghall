
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


def categorical_bmi(BMI):
    """
    Returns BMI category represented with numbers: 

    Underweight = 0,
    Normal weight = 1,
    Overweight = 2,
    Obese class 1 = 3,
    Obese class 2 = 4,
    Obese class 3 = 5
    
    """
    if BMI <= 18.4:
        return "Underweight"
    elif 18.5 <= BMI <= 24.9:
        return "Normal"
    elif 25.0 <= BMI <= 29.9:
        return "Overweight"
    elif 30.0 <= BMI <= 34.9:
        return "Obese 1"
    elif 35.0 <= BMI <= 39.9:
        return "Obese 2"
    elif BMI >= 40.0:
        return "Obese 3"
    else: 
        return "Fault"
    

def categorical_bloodpressure(df):
    """
    Returns categorical bloddpressure based on ap_hi and ap_lo in dataframe

    Parameters: df = pd.DataFrame

    Normal: ap_hi <= 120 & ap_lo <= 80,
    Elevated: 121 < ap_hi <= 129 & ap_lo <= 80,
    Hypertension 1: 130 < ap_hi <= 139 | 80 < ap_lo <= 89,
    Hypertension 2: 140 < ap_hi <= 180 | 90 < ap_lo <= 120,
    Hypertension crisis: 180 < ap_hi | 120 < ap_lo,
    
    """
    if (df["ap_hi"] < 120) and (df["ap_lo"] < 80):
        return "Normal"
    elif (120 <= df["ap_hi"] <= 129) and (df["ap_lo"] < 80):
        return "Elevated"
    elif (130 <= df["ap_hi"] <= 139) or (80 <= df["ap_lo"] <= 89):
        return "Hypertension 1"
    elif (140 <= df["ap_hi"] <= 180) or (90 <= df["ap_lo"] <= 120):
        return "Hypertension 2"
    elif (180 < df["ap_hi"]) or (120 < df["ap_lo"]):
        return "Hypertension crisis"
    else: 
        return "Calculation-fault"
