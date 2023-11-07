import pandas as pd
from urllib.parse import urlparse

# Load the CSV file into a DataFrame
file_path = '~/Desktop/py4e/dash2trade.com-backlinks.csv'
df = pd.read_csv(file_path)

# Define a function to extract the domain from a URL
def extract_domain(url):
    try:
        # Parse the URL and extract the domain
        domain = urlparse(url).netloc
        # Sometimes URLs start with 'www.', we strip this for consistency
        return domain.replace('www.', '')
    except:
        return None

# Apply the function to the 'Source URL' column to create a new 'Domain' column
df['Domain'] = df['Source url'].apply(extract_domain)

# Count the number of backlinks for each domain
backlink_counts = df['Domain'].value_counts().reset_index()
backlink_counts.columns = ['Domain', 'Backlinks']

# Save the modified DataFrame back to a CSV file
output_path = '~/Desktop/py4e/dash2trade.com-backlinks_with_domains.csv'
df.to_csv(output_path, index=False)

# Display the first few rows of the new backlink counts DataFrame
print(backlink_counts.head())
