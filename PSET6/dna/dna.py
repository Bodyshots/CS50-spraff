import csv
from sys import argv


def main():
    # Checking for 2 inputs in command line
    if not len(argv) == 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    # Reading csv file
    with open(argv[1], 'r') as f:
        reader = csv.reader(f)
        # Creating empty list
        people = []

        # Adding people to list
        for row in reader:
            try:
                people.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]])
            except:
                people.append([row[0], row[1], row[2], row[3]])

    # Setting counter, most and creating dictionary
    counter = 0
    STR = {
        "AGATC": 0,
        "TTTTTTCT": 0,
        "AATG": 0,
        "TCTAG": 0,
        "GATA": 0,
        "TATC": 0,
        "GAAA": 0,
        "TCTG": 0
    }

    # Opening text file
    with open(argv[2], 'r') as text:  # Automatically closes file after loop finishes
        temp_holder = text.read()
        temp_holder2 = temp_holder
        for i in range(0, len(temp_holder)):  # LOOP WORKS - SCANS EVERY LETTER
            # Read first four letters
            temp_holder = temp_holder2
            contents = temp_holder[i:i + 4]
            if (contents.partition('AATG')[1] or contents.partition('GATA')[1]
                or contents.partition('TATC')[1] or contents.partition('GAAA')[1]
                    or contents.partition('TCTG')[1]):
                FourLetterPatterns = ['GATA', 'TATC', 'GAAA', 'TCTG', 'AATG']
                for k in range(0, 5):
                    FourLetterPatternLoop(FourLetterPatterns[k], i, temp_holder, STR)
            else:
                contents = temp_holder[i:i + 5]
                if (contents.partition('TCTAG')[1] or contents.partition('AGATC')[1]):
                    FiveLetterPatterns = ['TCTAG', 'AGATC']
                    for k in range(0, 2):
                        FiveLetterPatternLoop(FiveLetterPatterns[k], i, temp_holder, STR)
                else:
                    contents = temp_holder[i:i + 8]
                    if contents.partition('TTTTTTCT')[1]:
                        counter = 0
                        counter += 1
                        temp_holder = temp_holder[i:]
                        holder = temp_holder.partition('TTTTTTCT')[2]
                        for j in range(0, len(holder), 8):
                            holder2 = holder[j:j + 8]
                            if holder2.partition('TTTTTTCT')[1]:
                                counter += 1
                            elif counter > STR["TTTTTTCT"]:
                                STR["TTTTTTCT"] = counter
                                break
                            else:
                                break

                    else:
                        continue

    # Loop to convert list into ints
    for i in range(0, len(people) - 1):
        people[i + 1][1] = int(people[i + 1][1])
        for j in range(1, len(people[0]) - 1):
            people[i + 1][1 + j] = int(people[i + 1][1 + j])
    matches = 0
    for keys in STR:
        # Checking if each pattern in the csv file matches to the dict (specifically large.csv)
        if keys == people[0][matches + 1]:
            matches += 1
            if matches > 1:
                Finder(STR, 9, people)
        # If they do not match, then the csv file must be small.csv and the extra keys must be deleted
        else:
            # Key deletion loop from here: https://stackoverflow.com/questions/8995611/removing-multiple-keys-from-a-dictionary-safely
            delete_keys = ("TTTTTTCT", "TCTAG", "GATA", "GAAA", "TCTG")
            for keys in delete_keys:
                if keys in STR:
                    del STR[keys]
            Finder(STR, 4, people)

# Determines number of consecutive patterns for four letter words


def FourLetterPatternLoop(n, i, temp_holder, dictionary):
    counter = 0
    counter += 1
    temp_holder = temp_holder[i:]
    holder = temp_holder.partition(n)[2]
    for j in range(0, len(holder), 4):
        hold = holder[j:j + 4]
        if hold.partition(n)[1]:
            counter += 1
        elif counter > dictionary[n]:
            dictionary[n] = counter
            break
        else:
            break

# Determines number of consecutive patterns for five letter words


def FiveLetterPatternLoop(n, i, temp_holder, dictionary):
    counter = 0
    counter += 1
    temp_holder = temp_holder[i:]
    holder = temp_holder.partition(n)[2]
    for j in range(0, len(holder), 5):
        hold = holder[j:j + 5]
        if hold.partition(n)[1]:
            counter += 1
        elif counter > dictionary[n]:
            dictionary[n] = counter
            break
        else:
            break

# Finds person that matches the number of found consecutive patterns. If unavailable, output "No Match"


def Finder(dictionary, number, people):
    matches = 0
    no_matches = 0
    for keys, values in dictionary.items():
        for i in range(1, len(people)):
            if values == people[i][1]:
                matches += 1
                for keys, values in dictionary.items():
                    if values == people[i][matches]:
                        matches += 1
                        if matches == number:
                            # If all of the person's patterns match with the dictionary, print out their name as a string and exit the program
                            print(f"{str(people[i][0])}")
                            exit(0)
                    else:
                        values = dictionary["AGATC"]    # Both csv files have "AGATC" first
                        matches = 0
                        break
            else:
                no_matches += 1
                if no_matches == len(people):   # If the whole list of people is searched, output "No Match" and exit the program
                    print("No match")
                    exit(0)


main()
