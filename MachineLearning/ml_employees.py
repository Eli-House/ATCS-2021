import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# read the data
data = pd.read_csv("data/employees.csv")

x = data[["DailyRate", "Education", "HourlyRate", "JobInvolvement", "JobLevel", "MonthlyIncome", "PercentSalaryHike", "StandardHours", "StockOptionLevel", "TotalWorkingYears", "YearsAtCompany", "YearsInCurrentRole","YearsSinceLastPromotion","YearsWithCurrManager"]].values
y = data["MonthlyRate"].values

# Split into train and test data
x_train, x_test, y_train, y_test, = train_test_split(x, y, test_size=0.2)
model = LinearRegression().fit(x_train, y_train)
r_squared = model.score(x_train, y_train)

# print out the model information
print("Model Information:")
print("Daily Rate coef:", model.coef_[0])
print("Education coef:", model.coef_[1])
print("Hourly Rate coef:", model.coef_[2])
print("Job Involvement coef:", model.coef_[3])
print("Job Level coef:", model.coef_[4])
print("Monthly Income coef:", model.coef_[5])
print("Percent Salary Hike:", model.coef_[6])
print("Standard Hours coef:", model.coef_[7])
print("Stock Option Level coef:", model.coef_[8])
print("Total Working Years coef:", model.coef_[9])
print("Years At Company coef:", model.coef_[10])
print("Years In Current Role coef:", model.coef_[11])
print("Years Since Last Promotion coef:", model.coef_[12])
print("Years With Curr Manager coef:", model.coef_[13])

print("R squared", r_squared)
print()

predict = model.predict(x_test)
print("Testing Linear Model with testing Data: ")
for index in range(len(x_test)):
    # actual y value
    actual = y_test[index]
    # predicted y value
    y_pred = round(predict[index], 2)
    # Test x value
    x_dr = x_test[index][0]
    x_ed = x_test[index][1]
    x_hr = x_test[index][2]
    x_ji = x_test[index][3]
    x_jl = x_test[index][4]
    x_mi = x_test[index][5]
    x_ps = x_test[index][6]
    x_sh = x_test[index][7]
    x_so = x_test[index][8]
    x_tw = x_test[index][9]
    x_yc = x_test[index][10]
    x_cr = x_test[index][11]
    x_sp = x_test[index][12]
    x_cm = x_test[index][13]
    print(" x_dr:",  x_dr, "x_ed:", x_ed, "x_hr:", x_hr, "x_ji:", x_ji, "x_jl:", x_jl, "x_mi:", x_mi, "x_ps:", x_ps, "x_sh:", x_sh, "x_so:", x_so, "x_tw:", x_tw, "x_yc:", x_yc, "x_cr:", x_cr, "x_sp:", x_sp, "x_cm:", x_cm, " Predicted y value:", y_pred, " Actual y value:", actual)