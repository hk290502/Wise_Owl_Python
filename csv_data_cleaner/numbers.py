
def process_numbers():
    file = open(r'C:\WiseOwl\csv_data_cleaner\numbers.csv','r')


    total = 0
    valid = 0
    invalid = 0

    for line in file:
        line = line.strip()

        if line == "" or line == "value":
            continue

        try:
            number = int(line)
            total += number
            valid += 1
        except ValueError:
            invalid += 1

    file.close()

    
    print("Total of valid numbers:", total)
    print("Valid rows:", valid)
    print("Invalid rows:", invalid)


process_numbers()

