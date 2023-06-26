import datetime as dt
import csv

# Use these functions to convert any string to appropriate Python data type
# Get just the first name from full name

def fname(any):
    try:
        nm = any.split(',')
        return nm[1]
    except IndexError:
        return ''

# Get just the last name from full name
def lname(any):
    try:
        nm = any.split(',')
        return nm[0]
    except IndexError:
        return ''

# Convert string to integer, None if empty value 
def birth_year(any):
    try:
        return int(any)
    except ValueError:
        return None

# Convert mm/dd/yyyy date to date or None if empty value
def date(any):
    try:
        return dt.datetime.strptime(any, "%m/%d/%Y").date()
    except ValueError:
        return None

# Convert any string to Boolean, False if no value
def boolean(any):
    return bool(any)

# Convert string to float, or to zero if no value 
def floatnum(any):
    s_balance = (any.replace('$','').replace(',','')).strip()
    return float(s_balance or 0)

# Create an empty list of people
people = []

# Define a class where each person is an object
class Person:
    def __init__(self, id, first_name, last_name, birth_year, date_joined, is_active, balance):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.date_joined = date_joined
        self.is_active = is_active
        self.balance = balance
        
# Open CSV file with Utf-8 encoind, do not read in new line characters
with open('sample.csv', encoding='utf-8', newline='') as f:
    # Set up a csv reader with a counter
    reader = enumerate(csv.reader(f))
    # Skip the first row 
    f.readline()
    # Loop through remaining rows one at a time, i is counter, row is entire row
    for i, row in reader:
        # From each data row in the csv file, create a Person object with unique id and appropriate data types, add to people list
        people.append(Person(i, fname(row[0]), lname(row[0]), birth_year(row[1]), date(row[2]), boolean(row[3]), floatnum(row[4])))

# When above loop is done, show all object in the people list

for p in people:
    print(p.id, p.first_name, p.last_name, p.birth_year, p.date_joined, p.is_active, p.balance)