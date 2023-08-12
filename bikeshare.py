import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#t display raw data - 5 rows at a time


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
    #a = message to ask user to input one of the cities.
    while True:
        a = "Enter the name of one of the three cities [Chicago, New York city, Washington] you would like to know about its bikeshare data "
        city = str(input(a)).lower()                                    #handling various user inputs in different cases
        if city in CITY_DATA:
# TO DO: get user input for month (all, january, february, ... , june)
#b = message to input month
            while True:
                b = "Enter the month [from January to June] you would like to know about {}'s bikeshare data "
                month = str(input(b.format(city.title()))).lower()       #handling various user inputs in different cases
                months = ['january', 'february', 'march', 'april', 'may', 'june']
#for a specific month found in the database
                if month == 'all' or month in months:
                    while True:
# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
#c = message to input day of the week
                        c = "Enter the day of the week would you like to know "
                        day = str(input(c)).lower()                       #handling various user inputs in different cases
                        days =['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
                        if day in days:
                            return (city, month, day)
                            print("You have requested for bikeshare data for {} in the month of {} on {}s".format(city.title(), month.title,day.title))
                        else:
                            print("Invalid day! Try again")               #all other exceptions:
                else:
                    print("Invalid input for month, try again.")
        else:
            print("Invalid input! Kindly try again.")
        print('-'*40)

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
#loading dataframe of selected city
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['chosen_day'] = df['Start Time'].dt.weekday_name
    if month!= 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df[df['month'] == month]
    if day != 'all':
        df[df['chosen_day'] == day.title()]
    return df

def view_raw_data(df):
    i = 0
    raw = str(input("Would you like to view 5 rows of raw data? Yes/No ")).lower()
    pd.set_option('display.max_columns',200)
    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df[i:i+5])
            raw = str(input("Would you like to the next 5 rows of data? Yes/No ")).lower() 
            i += 5
        else:
            raw = (str(input("Invalid input! Would you like to view 5 rows of raw data? Yes/No ")))
            print(raw)

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df["Start Time"]=pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    most_common_month_index = df["month"].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    a = most_common_month_index
    most_common_month = months[a-1].title()
    
    
    # TO DO: display the most common day of week
    df["day"] = df["Start Time"].dt.weekday_name
    most_common_day_of_the_week = df["day"].mode()[0]

    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    most_common_start_hour = df["hour"].mode()[0]
    print("The most common month is {}, the most common day of week is {} and the most common start hour is {} hours".format(most_common_month, most_common_day_of_the_week, most_common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and tr.cip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df["Start Station"].mode()[0]

# TO DO: display most commonly used end station
    most_common_end_station = df["End Station"].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    #e = combination of start station and end station trip
    #f = most frequent combination of start station and end station trip
    e = (df["Start Station"] + " and " + df["End Station"])
    f = e.mode()[0]

    print("The most commonly used start station is {}, the most commonly used end station is {} and the most frequent combination of these two are {}, as the start and end stations respectively".format(most_common_start_station, most_common_end_station, f))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_duration = df['Trip Duration']
    total_travel_time = trip_duration.sum()

    # TO DO: display mean travel time
    mean_travel_time = trip_duration.mean()
    print(" The total and average trip durations are {} and {}, repsectively".format(total_travel_time,mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()
    print("The distribution of user types are : {}".format(user_types))

    # TO DO: Display counts of gender
    if "Gender" in df:
        gender = df["Gender"].value_counts()
    else:
        print("Sorry,data on gender is currently unavailable")

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        earliest_year_of_birth = int(df["Birth Year"].min())
        most_recent_year_of_birth = int(df["Birth Year"].max())
        most_common_year_of_birth = int(df["Birth Year"].mode())
        print("The gender distribution are : {}. The earliest, most recent, and most common year of birth are {}, {} and {} respectively".format( gender, earliest_year_of_birth, most_recent_year_of_birth, most_common_year_of_birth))
    else:
        print("Sorry,data on year of birth is currently unavailable")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        view_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

