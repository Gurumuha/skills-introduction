
y = np.array([211000, 500000, 81000, 1400000, 450000, 210000, 7000])
x = ["Salary & Benefits", "Startup Costs", "Monthly Bills", "Medical Supplies", "Technology", "Transportation", "Other"]

font1 ={'family':'serif', 'color':'black', 'size':25}
plt.title("Estimated Budget", fontdict= font1)
plt.pie(y, labels= x, startangle=175)
plt.show()

