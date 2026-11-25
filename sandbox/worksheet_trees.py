


# checking for missing record_id
if row["record_id"] is None or row["record_id"] == "":
    print("missing record_id)"  
 
# removing record_id whitespaces
record_id = row["record_id"].strip()

# checking for invalid record_id
if not re.fullmatch(r"ST[0-9]{3}"):
    print("invalid record_id")

# checking for missing location 
if row["location"] is None or row["location"] == "":
    print("missing location)" 

# removing location whitespaces
location = row["location"].strip()

# checking for invalid location
locations = ["Silwood Bottom", "Nash's Field", "Manor House","Reactor Wood"]

if row["location"].casefold() not in [locations.casefold()]: 
    print("invalid location")

# checking for missing genus 
if row["genus"] is None or row["genus"] == "":
    print("missing genus")

# removing genus whitespaces (and getting rid of casefold)
genus = row["genus"].strip().casefold()

# checking for invalid genus 
genera = ["Querscus", "Acer", "Betula", "Fagus", "Fraxinus"]

if (genus) not in genera:
    print(invalid genus)

# checking for missing species
if row["species"] is None or row["species"] == "":
    print("missing soecies)" 

# removing species whitespaces and getting rid of casefold

species = row["species"].strip().casefold()

# checking for invalid species
species1 = ["robur", "petraea","pseudoplatanus","pendula","sylvatica","excelsior"]

if (species) not in genera:
    print(invalid species)

# checking for invalid genus/species combination
genus_species = [("Quercus", "robur"), ("Quercus", "petraea"), ("Acer", "pseudoplatanus"), ("Betula", "pendula"),
                 ("Fagus", "sylvatica"), ("Fraxinus", "excelsior")]


if (genus, species) not in genus_species:
    print("Error: wrong genus - species pair")

# checking for missing distance_m
if row["distance_m"] is None or row["distance_m"] == "":
    print("missing distance_m)" 
        
# checking for invalid distance_m

distance_m_value = float(row["distance_m"])

if not math.isfinite(angle_degrees_value):
    print("distance_m")

except ValueError:
    print("distance_m")
# checking for range of distance_m

XXXXXX

# checking for missing angle_degrees
if row["angle_degrees"] is None or row["angle_degrees"] == "":
    print("missing angle_degrees") 
        
# checking for invalid angle_degrees

angle_degrees_value = float(row["angle_degrees"])

if not math.isfinite(angle_degrees_value):
    print("invalid angle_degrees")

except ValueError:
    print("invalid angle_degrees")

# checking for range of angle_degrees

# removing duplicated identifiers

if record_id in accepted_ids:
    print("Error: duplicated identifier")


###########################

def validate_record(
    row: dict[str, str],
    source_row: int,
    accepted_ids: set[str],
) -> tuple[dict[str, str] | None, list[str]]:
    """Clean one record, or return the reasons it cannot be used."""

    reasons = []
    #checking for missing fields 
    for field in INPUT_FIELDS:
        if row[field] is None or row[field].strip == "":
            reasons.append(f"missing {field}") 
        else: #removing whitspaces and casefld sensitivity
            row[field] = row[field].strip()

    # checking for invalid record_id
    if not re.fullmatch(r"ST[0-9]{3}", row["record_id"]):
        reasons.append("invalid record_id")

    # checking for invalid location
    locations = ["silwood Bottom", "nash's Field", "manor House","reactor Wood"]

    if row["location"].casefold() not in locations: 
        reasons.append("invalid location")

    # checking for invalid genus 
    valid_genus = ["quercus", "acer", "betula", "fagus", "fraxinus"]

    if row["genus"].casefold() not in valid_genus:
        reasons.append("invalid genus") 

    # checking for invalid species
    valid_species = ["robur", "petraea","pseudoplatanus","pendula","sylvatica","excelsior"]

    if row["species"].casefold() not in valid_species:
     reasons.append("invalid species")

    # checking for invalid genus-species combinations
    # checking for invalid genus/species combination
    valid_combinations = [("quercus", "robur"), ("quercus", "petraea"), ("Acer", "pseudoplatanus"), ("Betula", "pendula"),
                   ("fagus", "sylvatica"), ("fraxinus", "excelsior")]

    if row["genus"].casefold|() in valid_genus and row["species"].casefold() in valid_species:
        if (row["genus"], row["species"]) not in valid_combinations:
            reasons.append("invalid genus/species combination")

    # checking for invalid numerical fields

    NUMERIC_FIELDS = ["distance_m", "angle_degrees"]

    for field in NUMERIC_FIELDS:
        try:
            value = float(row[field])

            if not math.isfinite(value):
                reasons.append(f"invalid {field}")
        except ValueError:
            reasons.append(f"invalid {field}")

    # checking the range of numerical fields

    # checking for duplicata record_id
    if record_id in accepted_ids:
        reasons.append("duplicate record_id")


    REASONS_ORDER = ["missing record_id", "invalid record_id", "duplicate record_id", "missing location", "invalid location", "missing genus",
                 "invalid genus", "missing species", "invalid species", "invalid genus/species combination", "missing distance_m",
                 "invalid distance_m", "distance_m out of range", "missing angle_degrees", "invalid angle_degrees", "angle_degrees out of range"]

    reasons_sorted = sorted(reasons, key=REASONS_ORDER.index)

    if reasons_sorted:
        return None, reasons_sorted
    return row, []
# source: https://www.geeksforgeeks.org/python/python-sort-list-of-list-by-specified-index/
# wasn't working, asked ai why and itsuggested i add .index to the key 


###############################


def process_records(
    rows: Iterable[dict[str, str]],
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    """Sort records into accepted rows and issue reports."""

    valid_records = []
    invalid_records = {}
    raise NotImplementedError("Write the loop that processes all records")


for xxx in xxx:
    fffvalidate_record:
    if no issues: youpi, if issue print reasons

cleaned_record = INPUT_PATH[1]

#
####### testing validate_record using the following: 


if __name__ == "__main__":

    test_record = {
        "record_id": "ST001",
        "location": "Silwood Bottom",
        "genus": "Quercus",
        "species": "robur",
        "distance_m": "12.5",
        "angle_degrees": "45",
    }

    accepted_ids = set()

    cleaned_record, reasons = validate_record(
        test_record,
        2,
        accepted_ids,
    )

    print("Cleaned record:", cleaned_record)
    print("Reasons:", reasons)

####################


test_rows = [
    {
        "record_id": "ST001",
        "location": "Silwood Bottom",
        "genus": "Quercus",
        "species": "robur",
        "distance_m": "12.5",
        "angle_degrees": "45",
    },
    {
        "record_id": "ST002",
        "location": "Unknown Place",
        "genus": "Quercus",
        "species": "robur",
        "distance_m": "10",
        "angle_degrees": "90",
    },
    {
        "record_id": "ST003",
        "location": "Manor House",
        "genus": "Acer",
        "species": "pseudoplatanus",
        "distance_m": "8.2",
        "angle_degrees": "30",
    },
]

accepted, rejected = process_records(test_rows)

print("Accepted records:", accepted)
print("Rejected records:", rejected)

from collections import Counter

def summarise_oaks(clean_records: Iterable[dict[str, str]]) -> list[dict[str, str]]:
    """Count accepted oak records by species."""

    oak_counts = Counter.items()

    for row in clean_records:
        if row["genus"].casefold().strip() == "quercus":
            species = row["species"]
            if species not in oak_counts:
                oak_counts[species] = 0

            oak_counts[species] += 1


    return oak_counts
