import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("data.csv")
data = df["average"].tolist()

# code to show the plot of raw data
fig = ff.create_distplot([data], ["average"], show_hist=False)
# fig.show()

dataset = []
for i in range(0,100):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)

mean = statistics.mean(dataset)
std_deviation = statistics.stdev(dataset)
print("The mean of sample data is ", mean)
print("The standard diveation of sample data is :",std_deviation)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,100):
      random_index = random.randint(0,len(data)-1)
      value = data[random_index]
      dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df],["average"],show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)

setup()

population_mean = statistics.mean(data)
# mean_sample = statistics.mean(mean_list)
print("The population is:" ,population_mean)
# print("the mean is :", mean_sample)

def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)

    std_deviation = statistics.stdev(mean_list)
    print("The standard deviation",std_deviation)

standard_deviation()


