import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york city', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
day_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

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
    is_city_valid = False
    while not is_city_valid:
        city = input("Enter a city name: ").lower()
        if city in cities:
            is_city_valid = True
        else:
            is_city_valid = False

    # get user input for month (all, january, february, ... , june)
    is_month_valid = False
    while not is_month_valid:
        month = input("Enter a valid month to filter by, or 'all' to apply no month filter: ").lower()
        if month in months or month == 'all':
            is_month_valid = True
        else:
            is_month_valid = False

    # get user input for day of week (all, monday, tuesday, ... sunday)
    is_day_valid = False
    while not is_day_valid:
        day = input("Enter a day of the week to filter by, or 'all' to apply no day filter: ").lower()
        if day in day_of_week or day == 'all':
            is_day_valid = True
        else:
            is_day_valid = False

    print('-'*40)
    return city, month, day


def load_filtered_data(city, month, day):
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
   
# Convert Start Time column to datetime format     
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
# Filters by month
    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month'] == month]
# Filters by day of the week
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print("\nThe most common month is: %s" % most_common_month)

    # display the most common day of week
    most_common_dow = df['day_of_week'].mode()[0]
    print("\nThe most common day of the week is: %s" % most_common_dow)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print("\nThe most common start hour is: %s" % most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station is: %s" % most_common_start_station)

    # display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station is: %s" % most_common_end_station)

    # display most frequent combination of start station and end station trip
    df['Trip Station'] = df['Start Station'] + ' || ' + df['End Station']
    most_frequent_station_combination = df['Trip Station'].value_counts().idxmax()
    print("The most frequent combination of start station and end station is: %s" % most_frequent_station_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel is: %s seconds' % total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is: %s seconds' % mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print("The count of user types: %s" % user_type_counts )

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print("Gender counts are: %s" % gender_count)
    else:
        print("No gender data available for Washington")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        print('The earliest birth year is: %s' % earliest_birth_year)
        
        latest_birth_year = df['Birth Year'].max()
        print('The most recent birth year is: %s' % latest_birth_year)
        
        most_common_birth_year = df['Birth Year'].value_counts().idxmax()
        print('The most common birth year is: %s' % most_common_birth_year)
    else:
        print('No birth year data available for Washington')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    print("Printing raw data..")
    display_data = False
    display_data = input("Do you want to view the raw data?( enter yes/no:) ").lower()
    index = 0
    while True:
        for i in range(5):
            if display_data == 'yes':
                display_data == True
                print(df.iloc[index])
                index += 1
                if index >= len(df):
                    print("No more data to display")
                    break
            else:
                display_data = False
                break
    
        else:
            display_more_data = input("Do you want to view more raw data? ")
            if display_more_data == 'no':
                display_data = False
                break
            continue
        break

def main():
    while True:
        city, month, day = get_filters()
        df = load_filtered_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
