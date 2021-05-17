########### part 1  one column
# Load file, with Part1StartTime parsed as datetime data
survey_data = pd.read_excel("fcc_survey.xlsx",
                            parse_dates=['Part1StartTime'])

# Print first few values of Part1StartTime
print(survey_data.Part1StartTime.head())




########### part 2  two column to combine a datatime 
# Create dict of columns to combine into new datetime column
datetime_cols = {"Part2Start": ['Part2StartDate','Part2StartTime']}


# Load file, supplying the dict to parse_dates
survey_data = pd.read_excel("fcc_survey_dts.xlsx",
                            parse_dates=datetime_cols)

# View summary statistics about Part2Start
print(survey_data.Part2Start.describe())





########### part 3 parse datetime using customed date format after load
# Parse datetimes and assign result back to Part2EndTime
survey_data["Part2EndTime"] = pd.to_datetime(survey_data['Part2EndTime'],
                                format='%m%d%Y %H:%M:%S')
# Print first few values of Part2EndTime
print(survey_data.Part2EndTime.head())