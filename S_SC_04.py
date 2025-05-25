import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------
# Step 1: Load Sample Data
# ------------------------------------------
data = {
    'Start_Time': ['2021-06-01 08:00:00', '2021-06-01 17:00:00', '2021-06-01 23:30:00',
                   '2021-06-02 07:45:00', '2021-06-02 12:00:00', '2021-06-02 18:15:00'],
    'Weather_Condition': ['Clear', 'Rain', 'Fog', 'Clear', 'Snow', 'Cloudy'],
    'Road_Condition': ['Dry', 'Wet', 'Wet', 'Dry', 'Snow', 'Wet'],
    'City': ['Los Angeles', 'New York', 'Chicago', 'Los Angeles', 'New York', 'Chicago']
}
df = pd.DataFrame(data)
df['Start_Time'] = pd.to_datetime(df['Start_Time'])
df['Hour'] = df['Start_Time'].dt.hour

# ------------------------------------------
# Step 2: Pattern Analysis
# ------------------------------------------
plt.figure(figsize=(10, 6))
sns.countplot(x='Hour', data=df)
plt.title('Accidents by Hour of Day')
plt.xlabel('Hour')
plt.ylabel('Count')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
sns.countplot(x='Weather_Condition', data=df)
plt.title('Accidents by Weather Condition')
plt.xticks(rotation=30)
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
sns.countplot(x='Road_Condition', data=df)
plt.title('Accidents by Road Condition')
plt.grid(True)
plt.show()

# ------------------------------------------
# Step 3: Hotspot Analysis
# ------------------------------------------
plt.figure(figsize=(6, 4))
sns.countplot(x='City', data=df)
plt.title('City-wise Accident Hotspots')
plt.grid(True)
plt.show()
