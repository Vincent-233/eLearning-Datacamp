try:
    # Load the JSON with orient specified
    df = pd.read_json("dhs_report_reformatted.json",
                      orient='split')
    
    # Plot total population in shelters over time
    df["date_of_census"] = pd.to_datetime(df["date_of_census"])
    df.plot(x="date_of_census", 
            y="total_individuals_in_shelter")
    plt.show()
    
except ValueError:
    print("pandas could not parse the JSON.")
    
    
    
    
# orientstr
#   Indication of expected JSON string format. Compatible JSON strings can be produced by to_json() with a corresponding orient value. The set of possible orients is:
#   'split' : dict like {index -> [index], columns -> [columns], data -> [values]}
#   'records' : list like [{column -> value}, ... , {column -> value}]
#   'index' : dict like {index -> {column -> value}}
#   'columns' : dict like {column -> {index -> value}}
#   'values' : just the values array