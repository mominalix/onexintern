import pandas as pd
#for visualization
import plotly.offline as plt
#import graph_object library for scatter visualization
import plotly.graph_objects as go
#for visualization of scatter plot
import plotly.express as px
#to read csv file
inp=input("enter csv path with file name\n")
csv_1=pd.read_csv(inp)   
print("original file\n",csv_1)
# to remove null values from dataset
csv_1.dropna(inplace=True)
#to remove duplicates values from dataset
csv_1.drop_duplicates(inplace=True)
updated_csv=csv_1
print("updated csv file \n",updated_csv)
 #calculating summary statistics such as mean, median,standard deviation, min and max values for both temperature and humidity
x=updated_csv.describe()
print(x)
med=updated_csv.median(numeric_only=True)
print("med\n",med)
# visualization on chart 
#cut function used to convert continous data into categorical data
updated_csv["Timecategory"]=pd.cut(pd.to_datetime(updated_csv.Timestamp).dt.hour,
    bins=[0,12,17,20,22],
    labels=["Morning","Afternoon","Evening","Night"])
# remove none value 
updated_csv.dropna(inplace=True)
#to show huimidity ,temperature over a time period in line chart
Data1=go.Scatter(
    x=updated_csv.Timecategory,
    y=updated_csv.Humidity,
    text="Humidity",
    mode="lines+markers",
    line=dict(color="green"),
)
Data2=go.Scatter(
    x=updated_csv.Timecategory,
    y=updated_csv.Temperature,
    text="Temperature",
    mode="lines+markers",
    line=dict(color="purple"),
)
td=[Data1,Data2]
plt.plot(td)
#to scatter plot the humidity and temperature with colored coded point of time of day
Data=px.scatter(
    data_frame=updated_csv,
    x="Temperature",
    y="Humidity",
    color_discrete_sequence=["aqua","red","yellow","pink"],
    color = "Timecategory", 
)
Data.show()
#heatmap which describe the relation between temperature and humidity
visualize=px.density_heatmap(updated_csv,title="Realtionship between Humidity and Temperature over time of day",
                        x="Temperature",
                        y="Humidity",
)

visualize.show()










































    