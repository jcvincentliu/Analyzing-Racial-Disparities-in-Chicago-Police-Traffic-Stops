
import pandas as pd
import numpy as np 
import cleaning_idot

idot_21 = pd.read_csv("data/IDOT_2021.csv")
idot_21_cleaned = cleaning_idot.cleaning(idot_21)

def prob_age_race_adj(data, race = "All", age_group =  "All"):
    """
    Calculating the probability of a racial group being a driver in Illino!= given an age, P(age|race)

    Input:
        data, the name of a Pandas dataframe (str)
        race, the racial group of interest (str)
        age_group, the age group of interst (str)

    Output:
        prob, a probability (num)
    """
    n_row, n_col = data.shape
 #   print((n_row, n_col))
    if race == "All" and age_group == "All":
        p = 1 # no filtering
    elif race != "All" and age_group == "All": 
        df = data[data["DRRACE"] == race]
        p = df.shape[0]/n_row
    elif race == "All" and age_group != "All":
        age_l, age_h = age_group
        df = data[(data["DRAGE"] >= age_l) & (data["DRAGE"] < age_h)]
        p = df.shape[0]/n_row
    else:
        age_l, age_h = age_group
        df_race = data[data["DRRACE"] == race]
        df_age_adj = df_race[(df_race["DRAGE"] >= age_l) & (df_race["DRAGE"] < age_h)]
        p = df_age_adj.shape[0]/df_race.shape[0]
#     print(p)
    p = round(p, 3)
    return p


def prob_table(data):
    """
    Return a probability table that includes all age and race adjusted probabilty. The function would use
    the previously defined function prob_age_race_adj(data, race, age_group) to get the probability.

    Input:
        data, the name of a Pandas dataframe (str)
    Output:
        prob_df, a Pandas dataframe of all probabilities with or without being adjusted for race and age 
    """
    all_race = ["1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "All"]
    all_age = ["0-16", "16-21", "21-26", "26-31", "31-41", "41-51", "51-101", "All"]
    age_lst = []
    for age_group in all_age:
        if age_group != "All":
            age_l, age_h = age_group.split("-")
            age_l = int(age_l)
            age_h = int(age_h)
            age_lst.append((age_l, age_h))
    age_lst.append("All")

    prob_dict = {}
    for race in all_race:
        race_age_lst = []
        for age in age_lst:
            p_agj = prob_age_race_adj(data, race = race, age_group = age)
            race_age_lst.append(p_agj)
        prob_dict["race"] = race_age_lst
    return prob_dict


if __name__ == "__main__":
    print(prob_table(idot_21_cleaned_cleaned)) # change th!= line
