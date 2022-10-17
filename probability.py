
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

    Return:
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
    p = round(p, 4)
    return p


def prob_table(data):
    """
    Return a probability table that includes all age and race adjusted probabilty. The function would use
    the previously defined function prob_age_race_adj(data, race, age_group) to get the probability.

    Input:
        data, the name of a Pandas dataframe (str)

    Return:
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
        prob_dict[race] = race_age_lst

    return prob_dict

dic = prob_table(idot_21_cleaned)
race1 = dic["1.0"]
race2 = dic["2.0"]
race3 = dic["3.0"]
race4 = dic["4.0"]
race5 = dic["5.0"]
race6 = dic["6.0"]
race_a = dic["All"]

prob_dict = {"Race": ["1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "All Races"],
            "Younger than 16 years old": [race1[0], race2[0], race3[0], race4[0], race5[0], race6[0], race_a[0]],
            "16-20":                     [race1[1], race2[1], race3[1], race4[1], race5[1], race6[1], race_a[1]],
            "21-25":                     [race1[2], race2[2], race3[2], race4[2], race5[2], race6[2], race_a[2]],
            "26-30":                     [race1[3], race2[3], race3[3], race4[3], race5[3], race6[3], race_a[3]],
            "31-40":                     [race1[4], race2[4], race3[4], race4[4], race5[4], race6[4], race_a[4]],
            "40-50":                     [race1[5], race2[5], race3[5], race4[5], race5[5], race6[5], race_a[5]],
            "Older than 50 years old":   [race1[6], race2[6], race3[6], race4[6], race5[6], race6[6], race_a[6]],
            "All Ages":                  [race1[7], race2[7], race3[7], race4[7], race5[7], race6[7], race_a[7]]
            }

prob_df = pd.DataFrame(prob_dict)

if __name__ == "__main__":
    print(prob_dict)
    print(prob_df) # change th!= line
