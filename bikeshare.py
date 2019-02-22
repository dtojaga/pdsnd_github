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

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input('Please select one of the following cities: chicago, new york city, or washington:\n')
    city = city.lower().strip()
    while city not in CITY_DATA:
        city = input('Input not recognized as chicago, new york city, or washington. Please try again:\n')
        city = city.lower().strip()

    # TO DO: get user input for month (all, january, february, ... , june)

    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = input("Please select a month, or 'all' to see data for all months:\n")
    month = month.lower().strip()
    while month not in months:
        month = input('Input not recognized as valid month, please try again:\n')
        month = month.lower().strip()
                
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    days = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    day = input("Please select a day, or 'all' to see data for all days:\n")
    day = day.lower().strip()
    while day not in days:
        day = input('Input not recognized as valid day, please try again:\n')
        day = day.lower().strip()


    print('-'*40)
    return city, month, day


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
    if month != 'all':        
        df['month'] = pd.to_datetime(df['Start Time']).dt.month
        month_dict = {'january': 1, 'february': 2, 'march': 3, 'april':4 , 'may': 5, 'june': 6}
        df = df[df['month']==month_dict[month]]
    if day != 'all':
        df['day'] = pd.to_datetime(df['Start Time']).dt.dayofweek
        day_dict = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}
        df = df[df['day']==day_dict[day]]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    int_to_month = {1: 'january', 2: 'february', 3: 'march', 4: 'april', 5:'may', 6:'june'}
    most_common_month = pd.to_datetime(df['Start Time']).dt.month.mode()[0]
    print('The most common month is: {}'.format(int_to_month[most_common_month]))
    # TO DO: display the most common day of week
    int_to_day = {0: 'monday', 1: 'tuesday', 2: 'wednesday', 3: 'thursday', 4: 'friday', 5:'saturday', 6:'sunday'}
    most_common_day = pd.to_datetime(df['Start Time']).dt.dayofweek.mode()[0]
    print('The most common day of the week is: {}'.format(int_to_day[most_common_day]))
    # TO DO: display the most common start hour
    most_common_hour = pd.to_datetime(df['Start Time']).dt.hour.mode()[0]
    print('The most common start hour is: {}'.format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used Start Station is: {}'.format(most_common_start_station))

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most commonly used End Station is: {}'.format(most_common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combo'] = df['Start Station'] + ' and ' + df['End Station']
    most_common_combo = df['Station Combo'].mode()[0]
    print('The most commonly used combination of stations is: {}'.format(most_common_combo))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Total Time'] = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time']))
    sum_all_time = df['Total Time'].sum()
    print('Total travel time: {}'.format(sum_all_time))
    # TO DO: display mean travel time
    avg_travel_time = df['Total Time'].mean()
    print('Mean travel time: {}'.format(avg_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_sub = df[df['User Type'] == 'Subscriber'].count()[0]
    user_type_cust = df[df['User Type'] == 'Customer'].count()[0]
    print('Number of subscribers: {}'.format(user_type_sub))
    print('Number of customers: {}'.format(user_type_cust))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:    
        user_type_male = df[df['Gender'] == 'Male'].count()[0]
        user_type_female = df[df['Gender'] == 'Female'].count()[0]
        print('Number of male users: {}'.format(user_type_male))
        print('Number of female users: {}'.format(user_type_female))
    else:
        print("No 'Gender' data available")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earlist_byear = df['Birth Year'].min()
        most_recent_byear = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print('The earliest birth year is: {}'.format(earlist_byear))
        print('The most recent birth year is: {}'.format(most_recent_byear))
        print('The most common birth year is: {}'.format(most_common_year))
    else:
        print("No 'Birth Year' data available")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        see_raw_data = input("\nWould you like to see the first five lines of raw data? Enter 'yes' or 'no'\n")
        see_raw_data = see_raw_data.lower().strip()
        repeat_counter = 1
        while see_raw_data != 'no':
            print(df.iloc[(5*(repeat_counter-1)):(5*repeat_counter)])
            see_raw_data = input("\nWould you like to see five more lines of raw data? Enter 'yes' or 'no'\n")
            repeat_counter = repeat_counter + 1
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
