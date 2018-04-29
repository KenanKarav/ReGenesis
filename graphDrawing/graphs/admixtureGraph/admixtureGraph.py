#Temporary Hard Code Admix Graph of K = 4
'''
import matplotlib.pyplot as plt
import csv

#Declaring Variables
ancestry1 = []
ancestry2 = []
ancestry3 = []
ancestry4 = []
temp = []
totalRatio = 0


#Reading in data from file and inputting the ratios into respective ancestry lists
with open('data.Q.4', 'r') as csvfile:
    file = csv.reader(csvfile, delimiter=' ')
    for line in file:
        totalRatio = float(line[0]) + float(line[1]) + float(line[2]) + float(line[3])
        ancestry1.append((100 *float(line[0])/totalRatio))
        ancestry2.append((100 * float(line[1])/totalRatio))
        ancestry3.append((100 * float(line[2])/totalRatio))
        ancestry4.append((100 * float(line[3])/totalRatio))
        temp.append((100 *float(line[0])) + (100 *float(line[1])) + (100 *float(line[2])) + (100 *float(line[3])))

#Prints the sum of all the ancestry ratios per subject (To see if they add up 100% - Spoiler* they dont)
print (temp)

#Temporarily create IDs for each subject
subjects = [x for x in range(len(ancestry1))]

#Plotting the chart
plt.stackplot(subjects, ancestry1,ancestry2, ancestry3, ancestry4,  colors=['green', 'blue', 'red', 'orange'])

#Label stuff
plt.xlabel('Subjects')
plt.ylabel('Ancestry Ratios')
plt.title('Admixture Chart')
plt.legend()

#Plotting the graph
plt.show()

'''



