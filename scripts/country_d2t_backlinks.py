import pandas as pd
import socket
import geoip2.database

# Set the path to the CSV file and the GeoLite2 database file
csv_file_path = '~/Desktop/py4e/dash2trade.com-backlinks_with_domains.csv'
db_file_path = '/Users/marine/Desktop/py4e/GeoLite2-Country.mmdb'

# Load the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Initialize the GeoIP2 reader
reader = geoip2.database.Reader(db_file_path)

# Function to resolve the domain to an IP address
def get_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        return None

# Function to look up the country by IP
def get_country(ip):
    if ip is None:
        return 'No IP Found'  # Return a placeholder or similar text
    try:
        response = reader.country(ip)
        return response.country.name
    except geoip2.errors.AddressNotFoundError:
        return 'Not found'
    except ValueError:
        return 'Invalid IP'


# Resolve the domain to IP addresses first
df['IP Address'] = df['Domain'].apply(get_ip)

# Then apply the function to each IP address in the DataFrame to get the country
df['Country'] = df['IP Address'].apply(get_country)

# Save the updated DataFrame back to a CSV file
df.to_csv(csv_file_path, index=False)

# Close the GeoIP2 reader
reader.close()

# Print the first few rows to verify
print(df.head())
