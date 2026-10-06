### inputs and project layout ####

# loader to be able to read csv files
import csv


def load_observations(path):
    with open(path, newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))

# function 
def parse_count(count_text):
    if count_text == "":
        return None
    count = int(count_text)

    if count < 0:
        raise ValueError("count can't be negative")
    return count 

# summarise site
