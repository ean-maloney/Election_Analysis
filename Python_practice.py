counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for k,v in counties_dict.items():
    print(f"{k} county has {v:6,.1f} voters")