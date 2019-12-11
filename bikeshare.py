import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


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
    while True:
        city = input("Which city would you like to analyze? Chicago, New York City or Washington: ").lower()
        if city in CITY_DATA:
            break
        else:
            print('invalid input please try Chicago, New York City or Washington')


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month name to filter by? january, february, ... , june or type all for no month filter: ").lower()
        if month in months or month == 'all':
            break
        else:
            print('invalid input please try a month name or type all for no month filter')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day of week would you like to filter by? (all, monday, tuesday, ... sunday): ").lower()
        if day in days or day == 'all':
            break
        else:
            print('invalid input please try a day name or type all for no day filter')



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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month == 'all':
        popular_month = df['month'].mode()[0]
        print('The Most Frequent Month of Travel: ', popular_month)


    # TO DO: display the most common day of week
    if day == 'all':
        popular_day = df['day_of_week'].mode()[0]
        print('The Most Frequent Day of Travel: ', popular_day)


    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    print('The Most Frequent Hour of Travel: ', popular_hour)




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most commonly used Start Station: ', popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most commonly used End Station: ', popular_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + ' - ' + df['End Station']
    start_end_station_combination = df['trip'].mode()[0]
    print('The most commonly used Start_End Stations trip: ', start_end_station_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = int(df['Trip Duration'].sum() / 60)
    print('Total travel time is: ' , total_travel_time, 'minutes')


    # TO DO: display mean travel time
    mean_travel_time = int(df['Trip Duration'].mean() / 60)
    print('Average travel time is: ' , mean_travel_time, 'minutes')



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)


    # TO DO: Display counts of gender
    # Gender Data only available for Chicago and New York City
    print()
    if city != 'washington':
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print('\nGender Data unavailable')


    # TO DO: Display earliest, most recent, and most common year of birth
    # Birth Year Data only available for Chicago and New York City
    print()
    if city != 'washington':
        earliest_birth_year = int(df['Birth Year'].min())
        print ('Earliest Birth year: ' , earliest_birth_year)

        recent_birth_year = int(df['Birth Year'].max())
        print ('Most recent Birth year: ' , recent_birth_year)

        common_birth_year = int(df['Birth Year'].mode())
        print('Most common year of birth: ' , common_birth_year)
    else:
        print('\nBirth Year Data unavailable')



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)



        display_raw_data = input('\nWould you like to see first 5 lines of raw data? Enter yes or no.\n')
        if display_raw_data.lower() == 'yes':
            i = 5
            print(df.head(i))
            while True:
                display_more = input('\nWould you like to see more of raw data? Enter yes or no.\n')
                if display_more == 'yes':
                    i += 5
                    print(df.iloc[i:i+5])
                else:
                    break


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
