import csv
flu_deaths = 0
lower_respiratory_deaths = 0
other_deaths = 0

with open('./MORespiratoryDeaths.csv') as file:
    reader = csv.DictReader(file, delimiter=',')
    with open('MORespiratoryDeathsAggregated.csv', 'w', newline='') as newfile:
        writer = csv.writer(newfile, delimiter=',')
        writer.writerow(["YEAR", "WEEK", "Influenza and pneumonia", "Chronic lower respiratory disease", "Other diseases of the respiratory system"])
        for row in reader:
            if row['DISEASE'] == "Influenza and pneumonia":
                flu_deaths = row['DEATHS']
                writer.writerow([row["YEAR"], row["WEEK"], flu_deaths, 0, 0])
