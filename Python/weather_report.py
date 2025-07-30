import pandas as pd
#import ssl
#ssl._create_default_https_context = ssl._create_unverified_context

#link to website for the latest forecast
weather_site = "https://forecast.weather.gov/MapClick.php?lat=42.5101&lon=-83.7866&lg=english&&FcstType=digital&menu=1"

#scrap using pandas
weather_data = pd.read_html(weather_site)

#pull the datetime of the latest forecast
fcst_as_of_date = weather_data[0][1].values[0]

#place webscarp of weaher forecast into dataframe
weather_fcst_df = pd.DataFrame(weather_data[2])

#slice the latest forecast into df1 which is the most recent forecast and transpose
df1 = weather_fcst_df.iloc[1:14:,:].transpose()
#set column names from first row
df1 = df1.set_axis(df1.iloc[0,:],axis=1)
#drop the header row with column names
df1.drop(0, inplace=True)
#fill in the null dates
df1['Date'] = df1['Date'].ffill()

#slice the remaining dataframe into df2 which is the rest of the extended forecast
df2 = weather_fcst_df.iloc[15:28,:].transpose()
#set column names from first row
df2 = df2.set_axis(df2.iloc[0,:],axis=1)
#drop the header row with column names
df2.drop(0, inplace=True)
#fill the date of the first row if null using the date in the last row of df1
if pd.isna(df2.iloc[0,0]):
    df2.iloc[0,0] = df1.iloc[-1,0]
else: pass
#fill in the null dates
df2['Date'] = df2['Date'].ffill()

#concat both dataframes and assign datatypes
final_df = pd.concat([df1,df2], ignore_index=True)
print(f"Combined the two forecast dataframes (df1 and df2)")

print(f"Convert the dataypes in the forecast dataframe")
for col in final_df.columns:
    if col in ['Date','Wind Dir','Rain','Thunder']:
        print(f"{col} is being converted to string")
        final_df[col] = final_df[col].astype(str)
    else:
        print(f"{col} is being converted to float")
        final_df[col] = final_df[col].astype('float32')