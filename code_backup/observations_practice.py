
#!/usr/bin/env python3
# Chloe Soudan - chloe.soudan26@imperial.ac.uk
# Script: observations_practice.py
# Desc: Practice with observations data
# Date: Oct 2026


# Importing the data
import csv

def load_observations(path):
    with open(path, newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))

# Loading in the bootcamp data
observations = load_observations("data/bootcamp_observations.csv")

# Inspecting the data (only if script is being run directly)
if __name__ == "__main__":
    rows = load_observations("data/bootcamp_observations.csv")
    print(rows[0])
    print(rows[2])

# Checking and converting the count data 
def parse_count(count_text):
    """Conversion of count text """
    if count_text== "": # returning None if stirng is empty
        return None
    
    if not isinstance(count_text, str):
         raise ValueError("The input must be text")
    
    count  = int(count_text) # converting the text strings to integers

    if count < 0: # if count is negative, raise ValueError
         raise ValueError
    
    return count    


def summarise_site_stage1(rows, site):

     """ Calculate count total in valid, unique rows"""
     known_total = 0 # creating an object to store the total count in, and initially setting it at 0

     for row in rows: # for each row
          if row["site"] == site: #if the row's site is the site of interest 
               count = parse_count(row["count"]) # pass the parse_count function on the count field

               if count is not None: # if count is not None
                    known_total += count # add the count to the known_total 

     return known_total, 0

def summarise_site_stage2(rows, site):
     """ Calculate count total, missing counts, and observed zeros"""
     missing_count = 0 # creating an object to store the number of missing counts in, and initially setting it at 0
     has_known_count = False #setting has_known_count as False by default
     known_total = 0


     for row in rows:
          if row["site"] == site:
               count = parse_count(row["count"])

               if count is None:  # if count is None
                    missing_count += 1 # add 1 to missing_count

               if count is not None: 
                    known_total += count
                    has_known_count = True 
     if not has_known_count: # if we haven't encountered any known counts, return None as the known_total
          known_total = None

     return known_total, missing_count

def summarise_site_stage3(rows, site):
     """ Calculate count total, missing counts, and observed zeros, while handling duplicates"""

     missing_count = 0
     has_known_count = False
     known_total = 0

     records = set() # creating an empty set named records, it will stored the records that were already processes


     for row in rows:
          if row["site"] == site:

               record = (row["site"], row["date"], row["count"])

               if record in records: # if the record is already in records (duplicate), skip that record
                    continue  
               records.add(record)

               count = parse_count(row["count"])

               if count is None: 
                    missing_count += 1

               if count is not None: 
                    known_total += count
                    has_known_count = True 
     if not has_known_count: # if we haven't encounter any known counts, return None
          known_total = None

     return known_total, missing_count


def summarise_site(rows,site): 
     # Validating the data

     # checking that rows is a list
     if not isinstance(rows,list):
          raise ValueError("Rows should be a list")
     # Checking that site is non-empty text string
     if not isinstance (site, str) or site =="":
          raise ValueError("site is empty")
      
     required_fields = {"site", "date", "count"}
     validated_rows = []

     for row in rows:
          # checking that every row is a dictionary
          if not isinstance (row, dict):
               raise ValueError("Each row should be a dictionary")
          # checking that every row contains exactly the required fields
          if set(row) != required_fields:
               raise ValueError ("Each row should excatly contain the fiels site, date, and count")
          # checking that every value is text
          for value in row.values():
               if not isinstance (value, str):
                    raise ValueError ("Each value should be text")
          # checking that sites and dates are not empty
          if row["site"] == "" or row["date"] == "":
               raise ValueError ("Site and date fields should be non-empty ")
          #checking that the count is accepted by parse_count
          count = parse_count(row["count"])

          # Appending rows that were validated to validates_rows,
          # so that they can be use for count calculations

          validated_rows.append((row,count))

     # Initializing the count objects
     missing_count = 0
     has_known_count = False
     known_total = 0
     records = set()

     #Calculate count total, missing counts, and observed zeros, while handling duplicates

     for row, count in validated_rows:
          if row["site"] == site:
               record = (row["site"], row["date"], row["count"])
               if record in records:
                    continue 
               
               records.add(record)
               
               if count is None:
                    missing_count += 1
               
               if count is not None:
                    known_total += count
                    has_known_count = True 
     if not has_known_count: # if we haven't encounter any known counts, return None
          known_total = None
               
     return known_total, missing_count


