
# path where files are stored (you'll need to change this)
file_path = r"C:\WiseOwl\working_with_sets\\"

# read first file into a list
with open(file_path + "grand_prix_2022.csv", 'r') as gp_2022:

    # read all lines into list, split this and return the second column entry (a list comprehension!)
    grand_prix_2022 = [line.split(",")[1] for line in gp_2022.read().splitlines()]

# read second file into a list
with open(file_path + "grand_prix_2023.csv", 'r') as gp_2023:

    # read all lines into list, split this and return the second column entry (a second list comprehension!)
    grand_prix_2023 = [line.split(",")[1] for line in gp_2023.read().splitlines()]

gp_2022_set = set(grand_prix_2022)
gp_2023_set = set(grand_prix_2023)

# GPs only in 2023
only_2023 = gp_2023_set - gp_2022_set
print("Only in 2023:")
print(only_2023)

# GPs only in 2022
only_2022 = gp_2022_set - gp_2023_set
print("\nOnly in 2022:")
print(only_2022)

# GPs in both years
both_years = gp_2022_set & gp_2023_set
print("\nIn both years:")
print(both_years)

