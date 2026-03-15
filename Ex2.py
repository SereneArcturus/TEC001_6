def get_season(month):
    seasons = ("Winter", "Spring", "Summer", "Autumn")
    if month in [12, 1, 2]:
        return seasons[0]
    elif 3 <= month <= 5:
        return seasons[1]
    elif 6 <= month <= 8:
        return seasons[2]
    elif 9 <= month <= 11:
        return seasons[3]
    else:
        return "This is not a month number, type again."
month = int(input("Type the number of a month you want here: "))
season = get_season(month)
if "This is not a month number, type again." not in season:
    print("The season in month " + str(month) + " is " + season)
else:
    print(season)