import csv
import matplotlib.pyplot as pl
import numpy as np

csv_file = open("input/train.csv", mode="r")

csv_file_content = csv.reader(csv_file, delimiter=',')

pclass = []     # Passenger Class
fare = []
survived = []
sex = []        # 0 - female 1- male ;) ;)
age = []
sibsp = []      # No. of siblings on board
parch = []      # No. of parents
ticket = []     # Ticket number
cabin = []      # Cabin number
embarked = []   # Which station (out of three) the passenger chadaoed

for i, row in enumerate(csv_file_content):
    if i > 0:  # because the first line was field names
        pclass.append(int(row[2]))
        fare.append(float(row[9]))
        survived.append(int(row[1]))
        sex.append(0 if "fem" in row[4] else 1)
        age.append(-1 if len(row[5]) == 0 else float(row[5])) # Some age fields are empty, so checking length.
        sibsp.append(int(row[6]))
        parch.append(int(row[7]))
        ticket.append(row[8])
        cabin.append(row[10])
        embarked.append(row[11])

corr_pclass_fare = np.corrcoef(pclass, fare)[0, 1]
# TODO look at correlation coefficients

# Now fare and pclass are lists.
# Lists have the advantage that they can be easily appended.
# We cant do that with arrays. Lists
# TODO Learn lists vs arrays

# mean_fare

ind_class1 = np.where(np.array(pclass) == 1)
ind_class2 = np.where(np.array(pclass) == 2)
ind_class3 = np.where(np.array(pclass) == 3)

fare_class1 = np.array(fare)[ind_class1]
fare_class2 = np.array(fare)[ind_class2]
fare_class3 = np.array(fare)[ind_class3]

mean_fare1 = np.mean(fare_class1)
mean_fare2 = np.mean(fare_class2)
mean_fare3 = np.mean(fare_class3)


def plot_data(x, y):
    pl.figure()
    pl.plot(pclass, fare, ".", color="b")
    pl.plot([1, 2, 3], [mean_fare1, mean_fare2, mean_fare3], "x", color="r", markersize=10)
    pl.xlabel("Passenger Class")
    pl.ylabel("Fare")
    pl.show()
