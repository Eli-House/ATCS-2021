# All code created by Eli Housenbold - Monday December 6th 2021
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#This line of code Reads my data and stores it as the variable df
df = pd.read_csv("/Users/elihousenbold/Desktop/Eli H - Data Science - Sheet1.csv")


# -- Covid Cases Slide --

#Variables that hold the total poulation of each color and the total number of Cases
BlueNumCovidCase = 0
RedNumCovidCase = 0
BluePop = 0
RedPop = 0

#   -- This Code if for the Two Bar Charts on the Number of Covid Cases --
#This variable is used to get the length of a colum later in the code
col = df["Red or Blue"]

#This for loop and gets us the total number of cases in Red and Blue States
for i in range(len(col)):
    #If a state is red this if statement will add it to the total of Covid cases in Red States
    if col[i] == "Red":
        RedNumCovidCase = RedNumCovidCase + df["Number of Covid Cases"][i]
    # If a state is blue this if statement will add it to the total of Covid cases in blue States
    if col[i] == "Blue":
        BlueNumCovidCase = BlueNumCovidCase + df["Number of Covid Cases"][i]

#This For loop gets the total population of all the Blue States and all the Red States. These Variables are used in the Covid Vaccine Slide
for i in range(len(col)):
    if col[i] == "Red":
        RedPop = RedPop + df["Population"][i]
    if col[i] == "Blue":
        BluePop = BluePop + df["Population"][i]

#This code creates the bar chat for the total number of covid cases for each color
RedCaseNum = [RedNumCovidCase]
BlueCaseNum = [BlueNumCovidCase]
indexNum = ["Number of Cases Comparing Red and Blue State Populations"]
num = pd.DataFrame({'RedCaseNum': RedCaseNum, 'BlueCaseNum': BlueCaseNum}, index=indexNum)
numPlot = num.plot.bar(rot=0, color={"RedCaseNum": "red", "BlueCaseNum": "Blue"})
plt.show()

#These two lines of code calculates the percentage of covid cases compared to the total population of each color
BlueCasePopPercent = (BlueNumCovidCase / BluePop) * 100
RedCasePopPercent = (RedNumCovidCase / RedPop) * 100

#This code creates the bar chat for the percentage of covid cases for each color
RedPercent = [RedCasePopPercent]
BluePercent = [BlueCasePopPercent]
indexPercent = ["Percentage of Cases Compared to Red and Blue State Populations"]
percent = pd.DataFrame({'RedPercent': RedPercent, 'BluePercent': BluePercent}, index=indexPercent)
percentPlot = percent.plot.bar(rot=0, color={"RedPercent": "red", "BluePercent": "Blue"})
plt.show()

# -- Covid Death Slide --

#This creates the slices that is on the pie chart
df1 = df.groupby("What Region is the State in?").sum()

# This line is the reason for why the South East section is offset on the graph
explode = (0, 0, 0.075, 0, 0)
# This code is creading the pie graph. The y is the percentages that is being plotted, the explode is the offset of one slice,
#the autopct labels the % on each slice, and the shadow gives the chart a 3d effect
df1.plot.pie(y="Number of Covid Deaths", explode = explode, autopct='%1.1f%%', shadow=True)
plt.show()

#These are variables that store the number of red in blue states in each region
BlueNumSouthEast = 0
BlueNumSouthWest = 0
BlueNumNorthEast = 0
BlueNumMidWest = 0
BlueNumWest = 0
RedNumSouthEast = 0
RedNumSouthWest = 0
RedNumNorthEast = 0
RedNumMidWest = 0
RedNumWest = 0

#This for lop and if statments fills the variables above with the number of each state in each region based on color
for i in range(len(col)):
    if col[i] == "Red":
        if df["What Region is the State in?"][i] == "South East":
            RedNumSouthEast = RedNumSouthEast + 1
        if df["What Region is the State in?"][i] == "South West":
            RedNumSouthWest = RedNumSouthWest + 1
        if df["What Region is the State in?"][i] == "North East":
            RedNumNorthEast = RedNumNorthEast + 1
        if df["What Region is the State in?"][i] == "Mid West":
            RedNumMidWest = RedNumMidWest + 1
        if df["What Region is the State in?"][i] == "West":
            RedNumWest = RedNumWest + 1
    if col[i] == "Blue":
        if df["What Region is the State in?"][i] == "South East":
            BlueNumSouthEast = BlueNumSouthEast + 1
        if df["What Region is the State in?"][i] == "South West":
            BlueNumSouthWest = BlueNumSouthWest + 1
        if df["What Region is the State in?"][i] == "North East":
            BlueNumNorthEast = BlueNumNorthEast + 1
        if df["What Region is the State in?"][i] == "Mid West":
            BlueNumMidWest = BlueNumMidWest + 1
        if df["What Region is the State in?"][i] == "West":
            BlueNumWest = BlueNumWest + 1

#This code creates the bar chart. We have two arrays RedRegion an BlueRegion we have two because there are two bars at each x index
RedRegion = [RedNumSouthEast, RedNumSouthWest, RedNumNorthEast, RedNumMidWest, RedNumWest]
BlueRegion = [BlueNumSouthEast, BlueNumSouthWest, BlueNumNorthEast, BlueNumMidWest, BlueNumWest]
indexRegion = ["SouthEast", "SouthWest", "NorthEast", "MidWest", "West"]
region = pd.DataFrame({'RedRegion': RedRegion, 'BlueRegion': BlueRegion}, index=indexRegion)
regionPlot = region.plot.bar(rot=0, color={"RedRegion": "red", "BlueRegion": "Blue"})
plt.show()

# -- Vaccine Slide --

# Variable that hold the total number of Vaccinated people in Red and Blue States
RedNumVaccine = 0
BlueNumVaccine = 0

#For loop that sees if a state is red or blue then adds the number of vaccinated people to the correct variable above
for i in range(len(col)):
    if col[i] == "Red":
        RedNumVaccine = RedNumVaccine + df["Number of Vaccinated People "][i]
    if col[i] == "Blue":
        BlueNumVaccine = BlueNumVaccine + df["Number of Vaccinated People "][i]

#Gets the total percent of vacine in Blue and Red States
BlueVaccinePercent = (BlueNumVaccine / BluePop) * 100
RedVaccinePercent = (RedNumVaccine / RedPop) * 100

#Creats and plots a Bar Graph using the numbers created from the data above. Also sets the colors to red and blue
RedVaccine = [RedVaccinePercent]
BlueVaccine = [BlueVaccinePercent]
indexVaccine = ["Percentage of Vaccinated People in Red vs Blue State"]
vaccine = pd.DataFrame({'RedVaccine': RedVaccine, 'BlueVaccine': BlueVaccine}, index=indexVaccine)
vaccine = vaccine.plot.bar(rot=0, color={"RedVaccine": "red", "BlueVaccine": "Blue"})
plt.show()