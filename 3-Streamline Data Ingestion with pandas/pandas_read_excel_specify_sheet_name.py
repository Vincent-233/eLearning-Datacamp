# Create df from second worksheet by referencing its name
responses_2017 = pd.read_excel("fcc_survey.xlsx",sheet_name=1)

# sheet_name can be both position (start from 0) or sheet name string 
# sheet_name = None will load all sheets

# responses_2017 = pd.read_excel("fcc_survey.xlsx",sheet_name='2017')
                               
# Graph where people would like to get a developer job
job_prefs = responses_2017.groupby("JobPref").JobPref.count()
job_prefs.plot.barh()
plt.show()