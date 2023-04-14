import pandas as pd 
import plotly.graph_objs as go 
import plotly.express as px

# this code will read the pandas data frame.
csv_read = pd.read_csv("E:\\Onex\\task\\sensor.csv")
print(csv_read)
print("=================================")

# from task    (the part--2)
# this part of code will remove all the duplicates form the selected csv_file.
dropt_dup =csv_read.drop_duplicates(subset='Timestamp', keep='first')
print(dropt_dup)
print("=================================")

# from task    (the part--2)
# this part of code will remove all the null values form the selected csv_file.
dropt_null= dropt_dup.dropna()
print(dropt_null)
print("=================================")

# from task    (the part--2)
# this part of code will create a new updated csv_file having no duplicates or any null values at given path directory.
# if the path of directoryis not given the file will be stored in the given working directory.
updated_data_frame= dropt_null.to_csv('E:\\Onex\\task\\sensor_updated.csv', index=False)
print(updated_data_frame)
print("=================================")

# from task    (the part--2)
# this code will read the updated csv file.
updated_file_path = "E:\\Onex\\task\\sensor_updated.csv"
updated_csvfile_read = pd.read_csv(updated_file_path)
print(updated_csvfile_read)
print("=================================")


# from task    (the part--3)
# this part of code will discribe mean, median, standard deviation, min and max values
# for both temperature and humidity
Discribe = updated_csvfile_read.describe()
print(Discribe)


# from task    (the part--4)
# this part of the code will describe the visualization of the data using plotly. this will Plot temperature 
# and humidity over time in a line chart with different colors for each.
fig = go.Figure()
fig.add_trace(go.Scatter(x=updated_csvfile_read['Timestamp'], y=updated_csvfile_read['Temperature'], name='temperature'))
fig.add_trace(go.Scatter(x=updated_csvfile_read['Timestamp'], y=updated_csvfile_read['Humidity'], name='humidity',))
fig.update_layout(title='temperature and humidity Over timestamp', xaxis_title='Datetime', yaxis_title='Value')
print(fig.show())


# from task    (the part--5)
updated_csvfile_read['Timestamp'] = pd.cut(pd.to_datetime(updated_csvfile_read['Timestamp']).dt.hour, 
                             bins=[0,3,6,9,12,15,18,21,24], 
                             labels=['early_morning','morning','early_afternon','afternoon','mid_afternoon', 'evening','night', 'mid_night'])
fig = px.scatter(updated_csvfile_read, x='Temperature', y='Humidity', color='Timestamp', 
                 color_discrete_sequence=px.colors.qualitative.Dark24)
fig.update_layout(title='Temperature and Humidity Scatter Plot by Timestamp', 
                  xaxis_title='Temperature', yaxis_title='Humidity')
print(fig.show())


# from task part__6
df = pd.read_csv('E:\\Onex\\task\\sensor.csv')
df['Timestamp'] = pd.cut(pd.to_datetime(df['Timestamp']).dt.hour, bins=['0', '6', '12', '18', '24'],
                         labels=(['night', 'morning', 'afternoon', 'evening']))
fig = px.density_heatmap(df, x='Temperature', y='Humidity')
fig.update_layout(title='Temperature and Humidity by Time of Day', xaxis_title='Temperature', yaxis_title='Humidity')
print(fig.show())