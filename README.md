### Date created
11<sup>th</sup> Nov 2022

### Project Title
Bikeshare data analysis using Python

### Description
Python script is used to analyze bikeshare data from three cities Washington, New York City and Chicago. The script asks user for input regarding whole/part of data to be processed. 

### Files used
bikeshare.py

### Credits
Basic repo is forked from: https://github.com/udacity/pdsnd_github 

### Modification to function: time_stats

```
def time_stats(df, month, day):
``` 
**month** and **day** are also taken as input along with predefined **df** 

### Addition of Disp_data function 

New function is defined to ask user if output of 5 lines should be printed using code
```
def disp_data(df):
    """Ask user if they want to see raw data and display if yes """
    start_data = 0
    while True: 
        check = input('Enter yes/no, if you want to see 5 lines of raw data:').lower()
        if check == 'no':            
            break 
        else: 
            print(df.iloc[start_data:start_data+5]) 
            start_data += 5 
```