# Average UK rainfall (mm) for 1910 by month
# http://www.metoffice.gov.uk/climate/uk/datasets
rainfall = (('JAN',111.4),
            ('FEB',126.1),
            ('MAr', 49.9),
            ('APr', 95.3),
            ('MAY', 71.8),
            ('JUN', 70.2),
            ('JUL', 97.1),
            ('AUG',140.2),
            ('SEP', 27.0),
            ('OCT', 89.4),
            ('NOV',128.4),
            ('DEC',142.2),
           )

# (1) Use a list comprehension to create a list of month,rainfall tuples where
# the amount of rain was greater than 100 mm.

month_large_rainfall = set([entry for entry in rainfall if entry[1] > 100])
print(month_large_rainfall)

# (2) Use a list comprehension to create a list of just month names where the
# amount of rain was less than 50 mm. 
month_low_rainfall = set([entry[0] for entry in rainfall if entry[1] < 50])
print(month_low_rainfall)

# (3) Now do (1) and (2) using conventional loops (you can choose to do 
# this before 1 and 2 !). 

month_large_rainfall_loops = []
for entry in rainfall:
    if entry[1] > 100:
        month_large_rainfall.append(entry)
print(month_large_rainfall_loops)

month_low_rainfall_loops = []
for entry in rainfall:
    if entry[1] < 50:
        month_low_rainfall.append(entry[0])
print(month_low_rainfall_loops)


