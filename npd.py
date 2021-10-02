import statistics
import plotly.figure_factory as ff 
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")
math_list = df["math score"].to_list()

math_mean = statistics.mean(math_list)
math_median = statistics.median(math_list)
math_mode = statistics.mode(math_list)
math_std = statistics.stdev(math_list)

std1_start,std1_end = math_mean-math_std,math_mean+math_std
std2_start,std2_end = math_mean-(2*math_std),math_mean+(2*math_std)
std3_start,std3_end = math_mean-(3*math_std),math_mean+(3*math_std)

fig = ff.create_distplot([math_list],["math score"],show_hist=False)
fig.add_trace(go.Scatter(x=[math_mean,math_mean],y=[0,0.17],mode="lines",name="MEAN"))

fig.add_trace(go.Scatter(x=[std1_start,std1_start],y=[0,0.17],mode="lines",name="STD1"))
fig.add_trace(go.Scatter(x=[std1_end,std1_end],y=[0,0.17],mode="lines",name="STD1"))

fig.add_trace(go.Scatter(x=[std2_start,std2_start],y=[0,0.17],mode="lines",name="STD2"))
fig.add_trace(go.Scatter(x=[std2_end,std2_end],y=[0,0.17],mode="lines",name="STD2"))

fig.add_trace(go.Scatter(x=[std3_start,std3_start],y=[0,0.17],mode="lines",name="STD3"))
fig.add_trace(go.Scatter(x=[std3_end,std3_end],y=[0,0.17],mode="lines",name="STD3"))

fig.show()

print("Mean, Median and Mode of the math scores are {}, {} and {} respectively".format(math_mean, math_median, math_mode))
print("The standard deviation of the math score is:",math_std)



