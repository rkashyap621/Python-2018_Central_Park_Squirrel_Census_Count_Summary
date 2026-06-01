import pandas as pd

gray_fur_squirrel_num = 0
cinnamon_fur_squirrel_num = 0
black_fur_squirrel_num = 0
unknown_fur_squirrel_num = 0

squirrel_data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
fur_data = squirrel_data["Primary Fur Color"].to_list()

for fur in fur_data:
    if fur == "Black":
        black_fur_squirrel_num += 1
    elif fur == "Cinnamon":
        cinnamon_fur_squirrel_num += 1
    elif fur == "Gray":
        gray_fur_squirrel_num += 1
    else:
        unknown_fur_squirrel_num += 1
squirrel_count = [gray_fur_squirrel_num, cinnamon_fur_squirrel_num, black_fur_squirrel_num, unknown_fur_squirrel_num]

squirrel_dict= {"Fur Color": ["Gray", "Cinnamon", "Black", "Unknown"],
                "Count": squirrel_count}

pd.DataFrame(squirrel_dict).to_csv('./Output/squirrel_census_summary.csv', index = False)
