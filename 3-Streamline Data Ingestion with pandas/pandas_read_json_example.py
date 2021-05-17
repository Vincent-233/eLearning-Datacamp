# Load pandas as pd
import pandas as pd

# Load the daily report to a data frame
pop_in_shelters = pd.read_json('dhs_daily_report.json')

# View summary stats about pop_in_shelters
print(pop_in_shelters.describe())


# JSON isn't a tabular format, so pandas makes assumptions about its orientation when loading data.
# Most JSON data you encounter will be in orientations that pandas can automatically transform 
# into a data frame.