import pandas as pd

# Load the uploaded CSV file
file_path = '/Data/historical_stock_data.csv'
stock_data = pd.read_csv(file_path)

### AAPL data
# Extract relevant columns for AAPL and rename them
aapl_data = stock_data[['Unnamed: 0', 'AAPL.4', 'AAPL.2', 'AAPL.3', 'AAPL.1', 'AAPL.5']]
aapl_data.columns = ['time', 'open', 'high', 'low', 'close', 'volume']

# Remove non-date entries in the 'time' column
aapl_data = aapl_data[aapl_data['time'].str.match(r'\d{4}-\d{2}-\d{2}.*')]

# Convert 'time' to datetime and set as index
aapl_data['time'] = pd.to_datetime(aapl_data['time'])
aapl_data.set_index('time', inplace=True)

# Display the cleaned and formatted AAPL stock data
aapl_data.to_csv('aapl_data.csv')


###########################################################################

### MMM data
# Extract relevant columns for AAPL and rename them
mmm_data = stock_data[['Unnamed: 0', 'MMM.4', 'MMM.2', 'MMM.3', 'MMM.1', 'MMM.5']]
mmm_data.columns = ['time', 'open', 'high', 'low', 'close', 'volume']

# Remove non-date entries in the 'time' column
mmm_data = mmm_data[mmm_data['time'].str.match(r'\d{4}-\d{2}-\d{2}.*')]

# Convert 'time' to datetime and set as index
mmm_data['time'] = pd.to_datetime(mmm_data['time'])
mmm_data.set_index('time', inplace=True)

# Display the cleaned and formatted AAPL stock data
mmm_data.to_csv('mmm_data.csv')

###########################################################################

### AMZN data
# Extract relevant columns for AAPL and rename them
amzn_data = stock_data[['Unnamed: 0', 'AMZN.4', 'AMZN.2', 'AMZN.3', 'AMZN.1', 'AMZN.5']]
amzn_data.columns = ['time', 'open', 'high', 'low', 'close', 'volume']

# Remove non-date entries in the 'time' column
amzn_data = amzn_data[amzn_data['time'].str.match(r'\d{4}-\d{2}-\d{2}.*')]

# Convert 'time' to datetime and set as index
amzn_data['time'] = pd.to_datetime(amzn_data['time'])
amzn_data.set_index('time', inplace=True)

# Display the cleaned and formatted AAPL stock data
amzn_data.to_csv('amzn_data.csv')

###########################################################################

### ABT data
# Extract relevant columns for AAPL and rename them
abt_data = stock_data[['Unnamed: 0', 'ABT.4', 'ABT.2', 'ABT.3', 'ABT.1', 'ABT.5']]
abt_data.columns = ['time', 'open', 'high', 'low', 'close', 'volume']

# Remove non-date entries in the 'time' column
abt_data = abt_data[abt_data['time'].str.match(r'\d{4}-\d{2}-\d{2}.*')]

# Convert 'time' to datetime and set as index
abt_data['time'] = pd.to_datetime(abt_data['time'])
abt_data.set_index('time', inplace=True)

# Display the cleaned and formatted AAPL stock data
abt_data.to_csv('abt_data.csv')

###########################################################################

### AXP data
# Extract relevant columns for AAPL and rename them
axp_data = stock_data[['Unnamed: 0', 'AXP.4', 'AXP.2', 'AXP.3', 'AXP.1', 'AXP.5']]
axp_data.columns = ['time', 'open', 'high', 'low', 'close', 'volume']

# Remove non-date entries in the 'time' column
axp_data = axp_data[axp_data['time'].str.match(r'\d{4}-\d{2}-\d{2}.*')]

# Convert 'time' to datetime and set as index
axp_data['time'] = pd.to_datetime(axp_data['time'])
axp_data.set_index('time', inplace=True)

# Display the cleaned and formatted AAPL stock data
axp_data.to_csv('axp_data.csv')
