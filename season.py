def get_season(month):
    seasons = ('Winter', 'Spring', 'Summer', 'Autumn')

    if month in (12, 1, 2):
        return seasons[0]  # Winter
    elif month in (3, 4, 5):
        return seasons[1]  # Spring
    elif month in (6, 7, 8):
        return seasons[2]  # Summer
    elif month in (9, 10, 11):
        return seasons[3]  # Autumn
    else:
        return "Invalid month"

month_number = int(input("Enter the number of a month (1-12): "))
season = get_season(month_number)
print("The corresponding season is", season)