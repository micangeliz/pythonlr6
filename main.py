import functions
import pandas as pd

df = pd.read_csv("students.csv")

# 1

functions.matplotlibAny()

functions.matplotlibAlcohol(df)

# 2

functions.boxplot(df)

functions.plotFreetime(df)

functions.plotTopMarks(df)

# 3

functions.pairplot(df)

functions.jointplot(df)

functions.violinplot(df)

functions.heatmam(df)

# 4

functions.plotly(df)
