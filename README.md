# D2T-Backlink-Analysis


### Python-Powered Backlink Analysis

Our backlink analysis leverages the power of Python to resolve domain names to IP addresses and map these IPs to their respective countries. The script utilizes the `socket` and `geoip2.database` libraries to efficiently process our dataset. Here's a quick rundown of the process:

- **Domain Resolution**: The script converts each domain from our `dash2trade.com-backlinks_with_domains.csv` file into an IP address using Python's built-in `socket` module.
  
- **Country Lookup**: With the GeoLite2 Country database, we identify the country of each IP address, enriching our dataset with geographic insights.

- **Data Augmentation**: The DataFrame is updated with new columns for IP Addresses and corresponding Countries, adding a valuable dimension to our analysis.

- **Export**: The enriched DataFrame is then saved back into a CSV file for further analysis or interactive visualization in platforms like Tableau.

- **Clean Workflow**: After processing, the script ensures that resources are closed properly, maintaining an efficient and clean Python environment.

This Python approach provides us with a scalable method to analyze backlink profiles, helping inform our SEO and competitive strategy. Check out the script [here](https://github.com/MarineBauerle/D2T-Backlink-Analysis/blob/main/scripts/D2T_Backlink_Analysis.py).



### Dash 2 Trade Backlink and Competitive Strategy Analysis

Our latest Tableau Dashboard offers a comprehensive analysis of backlink strategies and competitive positioning for Dash 2 Trade, covering the period from October 2022 to February 2023. Here's what you can expect from the dashboard:

- **Total Backlinks**: An in-depth look at the 3,154 backlinks acquired, providing insights into the volume and diversity of the backlink profile.

- **Total Domains**: Analysis of the 584 unique domains, offering a glimpse into the broad reach and domain authority within the backlink portfolio.

- **Average Page Authority Score**: A snapshot of the average page authority score of 4.560, highlighting the influence and credibility of the pages linking back.

- **Geographical Distribution**: A geographical breakdown of backlinks by country, showcasing the global footprint and regional strengths of the backlink strategy.

- **Backlinks by Domain**: An overview of backlinks categorized by referring domains, with tr.cryptonews.com leading the pack, indicating strategic partnerships or favored content distribution networks.

- **Backlinks by Title**: Insight into the most referenced content, with titles like "How To Link PayPal..." drawing significant attention, reflecting the content's relevance and engagement.

- **Top 10 Anchors**: Identification of the most effective anchor texts, with 'Dash 2 Trade' being predominant, signifying brand-centric linking practices.

- **Backlinks by Target URL**: Details of the specific Dash 2 Trade URLs targeted by backlinks, which can be crucial for understanding the focused pages for SEO and content strategy efforts.

Access the interactive Dashboard [here](https://public.tableau.com/views/BusinessBacklinksAnalysis-Oct22toFeb23/D2TBacklinksDashboard?:language=fr-FR&:display_count=n&:origin=viz_share_link) to explore the data and gain actionable insights into enhancing your backlink strategy in the competitive crypto analytics space.
