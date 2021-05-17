# Create string of lettered columns to load
col_string = 'AD,AW:BA'

# Load data with skiprows and usecols set
survey_responses = pd.read_excel("fcc_survey_headers.xlsx", 
                        usecols=col_string, 
                        skiprows=2)

# View the names of the columns selected
print(survey_responses.columns)