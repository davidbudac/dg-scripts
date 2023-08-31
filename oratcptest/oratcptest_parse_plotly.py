import plotly.express as px
import pandas as pd

# Parsing the data
lines = data.split("\n")
timestamps, throughputs, latencies = [], [], []
for line in lines:
    if 'Mbytes/s' in line and 'Throughput' not in line and 'Avg.' not in line:
        parts = line.split()
        timestamps.append(parts[0][1:-1])
        throughputs.append(float(parts[1]))
        latencies.append(float(parts[3].replace("ms", "")))

# Creating a DataFrame from the parsed data
df = pd.DataFrame({
    'Time': timestamps,
    'Throughput (Mbytes/s)': throughputs,
    'Latency (ms)': latencies
})

# Plotting the data with plotly express
fig = px.line(df, x='Time', y=df.columns[1:], title="Network Performance over Time")
fig.show()
