import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True: 
        city = input('Enter name of city you want to analyze: ').lower() 
        try: 
            CITY_DATA[city]
            break
        except: 
            print('{} is not a city in database, want to try again?'.format(city.title()))
    print('You entered {} as city.'.format(city.title())) 
    
    
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter month for which data should be processed (example: April) or enter all: ').lower() 
        months = ['all','january','february','march','april','may','june'] 
        if month in months:
            break
        else:
            print('data for {} is not available!'.format(month.title()))
    print('Data will be processed for {} month/s.'.format(month.title()))


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True: 
        day = input('Enter day for which data should be processed (example: Sunday) or enter all: ').lower()
        days = ['all','sunday','monday','tuesday','wednesday','thursday','friday','saturday'] 
        if day in days:
            break 
        else: 
            print('Please provide correct input!') 
    print('Data on {} will be processed.'.format(day.title()))
    

    print('-'*40)
    return (city, month, day)


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])  
    
    print('\nLoading data from file: {}\n'.format(CITY_DATA[city]))
    
    df['Start Time'] = pd.to_datetime(df['Start Time']) 
    df['month'] = df['Start Time'].dt.month 
    df['day_of_week'] = df['Start Time'].dt.day_name() 
    df['hour'] = df['Start Time'].dt.hour


    if month != 'all': 
        # use the index of the months list to get the corresponding int
        months = ['all','january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) 
    
        # filter by month to create the new dataframe
        df = df[df['month']== month]


    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]

    print('-'*40)   

    return df 
    

def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month 
    if month == 'all':
        
        popular_month_index = df['month'].mode()[0] 
        months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    
        popular_month = months.pop(popular_month_index).title()
           
        print('\nMost common month is: {}'.format(popular_month)) 
        
    else: 
        print('\nData is being processed for month of: {}'.format(month.title()))
    
    # display the most common day of week
    if day == 'all':
        
        popular_dayofweek = df['day_of_week'].mode()[0].title() 
           
        print('\nMost common day of week is: {}'.format(popular_dayofweek.title()))

    else: 
        print('\nData is being processed for: {}'.format(day.title()))

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]

    print('\nMost common start hour is: {}'.format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0] 
    
    print('\nMost commonly used start station is: {}'.format(popular_start_station))

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0] 
    
    print('\nMost commonly used end station is: {}'.format(popular_end_station))

    # display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station']+' to '+df['End Station'] 
    
    freq_trip = df['trip'].mode()[0] 
    
    print('\nMost frequent combination of stations for trip are: {}'.format(freq_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum() 
    
    print('\nTotal travel time for selected data is: {} seconds.'.format(total_travel_time))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean() 
    
    print('\nMean travel time for selected data is: {} seconds.'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts() 
    
    print('Count of user types are: \n{}'.format(user_types))

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        
        print('\nTravellers of each gender are as: \n{}\n'.format(gender_count))
    
    else: 
        print('\nData on Gender is not available for selected city\n')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('\nEarliest birth year of traveller is: {}\n'.format(df['Birth Year'].min()))
        print('\nMost recent birth year of traveller is: {}\n'.format(df['Birth Year'].max()))
        print('\nMost common birth year of traveller is: {}\n'.format(df['Birth Year'].mode()[0])) 
        
    else: 
        print('\nData on birth  year not available for selected city\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40) 
    
    
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

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df) 
        disp_data(df)
        
        print('-'*40)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
