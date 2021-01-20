import pandas as pd

import plotly.express as px

df = pd.read_csv(r"D:\PROGRAMS\PYTHON\C102\Teacher refrence\line_chart.csv")

fig = px.line(df, x="Year", y="Per capita income", color="Country", title='Per Capita Income')

fig.show()
