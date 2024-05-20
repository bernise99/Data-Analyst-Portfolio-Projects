# In case I need to run queries on the data; converted to db using '1_Convert to db.py' for convenience

import sqlite3
import csv # for output

output = 1

db_file = sqlite3.connect("CMS_Data.db")
cursor = db_file.cursor()

# For testing: Gets a list of tables
# tables = [a for a in cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")]
# print(tables)

query = "SELECT providertype, COUNT(DISTINCT npi) FROM cms_data WHERE gender = 'M' AND zip IN (32725, 32174, 32738, 32724, 32114, 32127, 32720, 32117, 32168, 32119, 32763, 32129, 32713, 32128, 32141, 32118, 32176, 32754, 32130, 32169, 32136, 32132, 32764, 32744, 32180, 32124, 32759, 32102, 32190, 32723, 32105, 32116, 32115, 32120, 32122, 32121, 32123, 32126, 32125, 32170, 32173, 32175, 32198, 32706, 32721, 32722, 32728, 32739, 32753, 32774, 32174, 32164, 32137, 32110, 32136, 32112, 32145, 32187, 32135, 32142, 32151, 32765, 32771, 32792, 32746, 32708, 32714, 32707, 32779, 32773, 32750, 32751, 32701, 32766, 32730, 32732, 32716, 32715, 32719, 32718, 32733, 32747, 32752, 32762, 32772, 32791, 32795, 32799, 32907, 32955, 32935, 32940, 32780, 32904, 32909, 32926, 32905, 32937, 32927, 32953, 32901, 32952, 32796, 32934, 32922, 32931, 32903, 32951, 32908, 32754, 32920, 32976, 32950, 32948, 32949, 32925, 32815, 32919, 32782, 32954, 32956, 32959, 32775, 32781, 32783, 32902, 32906, 32911, 32910, 32912, 32924, 32923, 32932, 32936, 32941, 32259, 32092, 32084, 32086, 32082, 32003, 32080, 32081, 32095, 32145, 32033, 32004, 32085, 32260, 32162, 34472, 34491, 34476, 34471, 34481, 34482, 34470, 34480, 34473, 34420, 34475, 34474, 34432, 32784, 34479, 32696, 32179, 32134, 34488, 34431, 32113, 32668, 32195, 32686, 32617, 32667, 32102, 32702, 32111, 32133, 32182, 32183, 32192, 32663, 32664, 32681, 32634, 34421, 34430, 34477, 34478, 34483, 34489, 34492, 32177, 32640, 32148, 32134, 32666, 32112, 32131, 32189, 32181, 32187, 32140, 32139, 32193, 32007, 32138, 32147, 32149, 32157, 32178, 32185) GROUP BY providertype ORDER BY COUNT(DISTINCT npi) DESC"
data = cursor.execute(query).fetchall()

# Output query results to a csv:
if output == 1:
    with open('results.csv','w') as out_csv_file:
        csv_out = csv.writer(out_csv_file)
        # Header row:                    
        csv_out.writerow([d[0] for d in cursor.description])
        # Rest of the data:
        for i in range(len(data)):
          csv_out.writerow(data[i])
else:
    print("No output")

db_file.close()
