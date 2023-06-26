import csv
import datetime as dt

#Open the CSV file with UTF-8 encoding, do not read in new line characters
with open('sample.csv', encoding='utf-8', newline='') as f:
    # Create a CSV row counter and row reader
    reader = enumerate(csv.reader(f))
    # Loop through one row at a time, i is counter, row is entire row 
    for i, row in reader:
        # Row 0 is just column heading, ignore it.
        if i > 0:
            # Whole name split into two at comma
            try:
                full_name = row[0].split(',')
                # Last name, strip extra spaces
                last_name = full_name[0].strip()
                # First name has same problem
                first_name = full_name[1].strip()
            except IndexError:
                full_name = last_name = first_name = ""
            # Birth year integer, zero for empty string
            birth_year = int(row[1] or 0)
            # Date Joined is a date 
            try:
                date_joined = dt.datetime.strptime(row[2], "%m/%d/%Y").date()
            except ValueError:
                date_joined = None

            # Is active is boolean, automatically False for empty string
            is_active = bool(row[3])
            # Remove $, commas, leading and trailing spaces
            str_balance = (row[4].replace('$','').replace(',','')).strip()
            # Balance is a float or zero for empty string
            balance = float(str_balance or 0)

            print(first_name, last_name, birth_year, date_joined, is_active, balance)
print('Done!')