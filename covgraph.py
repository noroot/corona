from matplotlib import pyplot as plt
import math
import csv 
import sys
from cycler import cycler
import datetime

data = []
data_diff = []
data_total = []
data_new = []
data_recovered = []

total_p = 0
total_new = 0
recover_p = 0
recover_diff = 0

deaths_p = 0
deaths_diff = 0
latest_date = ""
with open("./tmp/{0}.csv".format(sys.argv[1])) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        total = int(row[2])
        recovered = int(row[3])
        deaths = int(row[4])
        latest_date = row[0]
        
        total_diff = total - total_p
        total_new = total_new + total_diff
        total_p = total

        recover_diff = recovered - recover_p
        recover_p = recovered
        
        deaths_diff = deaths - deaths_p
        deaths_p = deaths
        
        r = [total_diff, recover_diff, deaths_diff]
        
        data_total.append(total)
        data_diff.append(total_diff)
        data_new.append(total_new)

        
        data.append(r)
        
print(data_total)
plt.title("Country={0} T={1}, R={2}, D={3}, Date={4}"
          .format(sys.argv[1],
                  total_p,
                  recovered,
                  deaths,
                  datetime.datetime.strptime(latest_date, "%Y-%m-%d")))
plt.plot(data)
plt.show()
    






