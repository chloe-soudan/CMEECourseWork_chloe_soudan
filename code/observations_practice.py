#!/usr/bin/env python3
#chloe.soudan26@imperial.ac.uk
# OBSERVATIONS PRACTICE

####### PSEUDOCODE #####
# INPUT: observations with site, date, and count
# For one (and then each) site; calculate the results
# OUTPUT: sum for one (and then each site)


# importing the data
import csv

def load_observations(path):
    with open(path, newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))

#loading in the bootcamp data
observations = load_observations("data/bootcamp_observations.csv")

# inspecting the data
if __name__ == "__main__":
    rows = load_observations("data/bootcamp_observations.csv")
    print(rows[0])
    print(rows[2])
# writing the function for site a

def calc_function1(site):
     """writing a reusable function that calculates the results for one 
requested site"""
     site_sum = 0
     site_missing_count = 0
     for count in site:
          if count == "": # when string is empty
               site_missing_count += 1 # adding one to the missing counts sum 
          else:
               site_sum += int(count)
     return site_sum, site_missing_count


# note: site a sum is 4 and there is 1 missing count

def calc_function2(observations):
     """"A reusable function that calculates the results for each
     site"""
     
     results = []

     for site in set(row["site"] for row in observations):
          site_sum = 0
          site_missing_count = 0
          
          for observation in observations:
               if observation["site"] == site:
                    count = observation["count"]
                    if count == "": # when string is empty
                         site_missing_count += 1 # adding one to the missing counts sum 
                    else:
                         site_sum += int(count)
                
          results.append((site, site_sum, site_missing_count))

     return(results)

print(calc_function2(observations))
# ran in bash terminal by running python3 code/observations_practice.py



def parse_count(count_text):
    """guided conversion of count text """
    if count_text== "":
        return None

    count=int(count_text)

    if count <0:
        raise ValueError("Count must be non-negative")

    return count
    
