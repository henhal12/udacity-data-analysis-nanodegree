## Import Important Library

import unicodecsv
from datetime import datetime
from collections import Counter
import time

## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'

## Date and Month Lists
month_list = [('january', 1), ('february', 2), ('march', 3), ('april', 4), ('may', 5), ('june', 6)]
day_list = [('monday', 1), ('tuesday', 2), ('wednesday', 3), ('thursday', 4), ('friday', 5), ('saturday', 6), ('sunday', 7)]

def read_csv(filename):
    '''Import CSV files and convert them to dictionaries

    Args:
        Bikshare csv Filename
    Returns:
        List of Dictionaries containing the bikeshare data
    '''
    with open(filename,'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

def change_timeclass(date_time):
    '''Function to change str to datetime class

    Args:
        (str) each row in bikeshare data that will be converted to datetime
    Returns:
        (datetime) each row in bikeshare data
    '''
    return datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')

def change_intclass(integer):
    '''Function to change str to int class and empty str to None

    Args:
        (str) each row in bikeshare data that will be converted to integer
    Returns:
        (int) each row in bikeshare data
    '''
    if integer == '':
        return None
    else:
        return int(float(integer))

def fix_data_type(city_file):
    '''Function to fix data type for each column in bikeshare file

    Args:
        Bikeshare city file ; str data
    Returns:
        Bikeshare city file with correct type for each data (str, int, datetime)
    '''
    for row in city_file:
        '''Fixing data type'''
        row['Start Time'] = change_timeclass(row['Start Time'])
        row['End Time'] = change_timeclass(row['End Time'])
        row['Trip Duration'] = change_intclass(row['Trip Duration'])

def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for city's bikeshare data.
    '''
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')

    city_list = ['chicago', 'new york', 'washington']
    ## Handle Invalid Raw Input
    if city.lower() not in city_list:
        print('\nInvalid Input! Please choose Chicago, New York, or Washington.\n')
        return get_city()

    return city

def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        (str) Time Period for filtering city's bikeshare data.
    '''
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')

    period_list = ['month', 'day', 'none']
    ## Handle Invalid Raw Input
    if time_period.lower() not in period_list:
        print('\nInvalid Input! Please choose month, day, or none.\n')
        return get_time_period()

    return time_period

def get_what_month():
    '''Asks the user for month name and returns the specified filter.

    Args:
        none.
    Returns:
        (str) Month name for filtering city's bikeshare data.
    '''
    month_filter = input('\nWhich month? January, February, March, April, May, June.\n')

    month_list = ['january', 'february', 'march', 'april', 'may', 'june']
    ## Handle Invalid Raw Input
    if month_filter.lower() not in month_list:
        print('\nInvalid Input! Please choose a month.\n')
        return get_what_month()

    return month_filter

def get_what_day():
    '''Asks the user for day name and returns the specified filter.

    Args:
        none.
    Returns:
        (str) Day name for filtering city's bikeshare data.
    '''
    day_filter = input('\nWhich day?\n')

    day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    ## Handle Invalid Raw Input
    if day_filter.lower() not in day_list:
        print('\nInvalid Input! Please choose a day.\n')
        return get_what_day()

    return day_filter

def popular_month(city_file):
    '''Get Only Month from Start Time

        Args:
            (str) Rows of bikeshare data in list
        Returns:
            (str) Popular Month for given filter'''

    month_count = []
    for data in city_file:
        month_count.append(data['Start Time'].month)

    result = Counter(month_count).most_common()
    for month in month_list:
        if month[1] == result[0][0]:
            month_result = month[0]
    return month_result

def popular_day(city_file):
    '''Get Popular Day from Start Time

        Args:
            (str) Rows of bikeshare data in list
        Returns:
            (str) Popular Day for given filter '''

    day_count = []
    for data in city_file:
        day_count.append(data['Start Time'].isoweekday())

    result = Counter(day_count).most_common()
    for day in day_list:
        if day[1] == result[0][0]:
            day_result = day[0]
    return day_result

def popular_hour(city_file):
    '''Get Popular Hour from Start Time

        Args:
            (str) Rows of bikeshare data in list
        Returns:
            (int) Popular Hour for given filter '''

    hour_count = []
    for data in city_file:
        hour_count.append(data['Start Time'].hour)

    result = Counter(hour_count).most_common()
    return result[0][0]

def trip_duration(city_file):
    '''Get Statistic from Trip_Duration

        Args:
            (str) Rows of bikeshare data in list
        Returns:
            (int) Total Trip Duration and Average Trip Duration for given filter '''

    total_duration, trip_count = 0, 0
    for data in city_file:
        total_duration += data['Trip Duration']
        trip_count += 1

    average_duration = total_duration / trip_count
    return (total_duration, average_duration)

def popular_stations(city_file):
    '''Get Popular Start and End Station

        Args:
            (str) Rows of bikeshare data in list
        Returns:
            (str) Popular Start and End Station for given filter '''

    start_station, end_station = [], []
    for data in city_file:
        start_station.append(data['Start Station'])
        end_station.append(data['End Station'])

    start_result = Counter(start_station).most_common()
    end_result = Counter(end_station).most_common()

    return (start_result[0][0], end_result[0][0])

def popular_trip(city_file):
    '''Get Popular Trip

        Args:
            (str) Rows of bikeshare data in list
        Returns:
            (str) Popular Trip for given filter '''

    trip = []
    for data in city_file:
        trip.append((data['Start Station'], data['End Station']))

    trip_result = Counter(trip).most_common()
    return trip_result[0][0]

def users(city_file):
    '''Get Total Count of Each User Type

        Args:
            (str) Rows of bikeshare data in list
        Returns:
            (int) Total Count of Each User Type for given filter '''

    sub_count, cust_count = 0, 0
    for data in city_file:
        if data['User Type'] == 'Subscriber':
            sub_count += 1
        else:
            cust_count += 1

    return (sub_count, cust_count)

def gender(city_file):
    '''Get Total Count of Each Gender

        Args:
            (str) Rows of bikeshare data in list
        Returns:
            (int) Total Count of Each Gender for given filter '''

    male_count, female_count = 0, 0
    for data in city_file:
        if data['Gender'] == 'Male':
            male_count += 1
        elif data['Gender'] == 'Female':
            female_count += 1

    return (male_count, female_count)

def birth_years(city_file):
    '''Get Birth Years Statistic

        Args:
            (str) Rows of bikeshare data in list
        Returns:
            (int) Oldest User, Youngest User, Popular Birth Year for given filter '''

    birth_year = []
    for data in city_file:
        if type(data['Birth Year']) == int:
            birth_year.append(data['Birth Year'])

    year_result = Counter(birth_year).most_common()
    oldest_result = min(birth_year)
    youngest_result = max(birth_year)

    return (oldest_result, youngest_result, year_result[0][0])

def display_data(city_file,start_row,end_row):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        (str) Rows of bikeshare data in list
    Returns:
        (str) Five rows from bikeshare data
    '''
    display = input('\nWould you like to view individual trip data? '
                     'Type \'yes\' or \'no\'.\n')

    ## Handle Invalid Raw Input
    if display.lower() == 'yes':
        print(city_file[start_row:end_row])
        start_row += 5
        end_row += 5
        display_data(city_file,start_row,end_row)
    elif display.lower() != 'yes' and display.lower() != 'no':
        print('\nInvalid Input!')
        display_data(city_file,start_row,end_row)

def restart():
    '''Ask if the user want to restar the program or not

    Args:
        None
    Returns:
        None
    '''

    answer = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')

    ## Handle Invalid Raw Input
    if answer.lower() == 'yes':
        statistics()
    elif answer.lower() != 'yes' and answer.lower() != 'no':
        print('\nInvalid Input\n')
        restart()

def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city().lower()

    # Open the correct CSV file base on city filter and fix the data type
    if city == 'chicago':
        city_data = read_csv(chicago)
        fix_data_type(city_data)
        for row in city_data:
            row['Birth Year'] = change_intclass(row['Birth Year'])

    elif city == 'new york':
        city_data = read_csv(new_york_city)
        fix_data_type(city_data)
        for row in city_data:
            row['Birth Year'] = change_intclass(row['Birth Year'])

    else:
        city_data = read_csv(washington)
        fix_data_type(city_data)

    # Filter by time period (month, day, none)
    time_period = get_time_period().lower()

    ## Statistic for "none" filter
    if time_period == 'none':

        print('Calculating the Statistic...\n')

        start_time = time.time()

        # What is the most popular month for start time?
        pop_month = popular_month(city_data)
        print('\nPopular Month is {}'.format(pop_month.title()))

        # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
        pop_day = popular_day(city_data)
        print('\nPopular Day is {}'.format(pop_day.title()))

        # What is the most popular hour of day for start time?
        pop_hour = popular_hour(city_data)
        print('\nPopular Hour is {}'.format(pop_hour))

        # What is the total trip duration and average trip duration?
        trip_result = trip_duration(city_data)
        print('\nTotal Trip Duration: {}'
              '\nAverage Trip Duration: {}'.format(trip_result[0],trip_result[1]))

        # What is the most popular start station and most popular end station?
        station_result = popular_stations(city_data)
        print('\nPopular Start Station: {}'
              '\nPopular End Station: {}'.format(station_result[0],station_result[1]))

        # What is the most popular trip?
        most_trip = popular_trip(city_data)
        print('\nPopular Trip is {}'.format(most_trip))

        # What are the counts of each user type?
        user_result = users(city_data)
        print('\nSubscriber: {}'
              '\nCustomer: {}'.format(user_result[0], user_result[1]))

        if city == 'chicago' or city == 'new york':

        # What are the counts of gender?
            gender_result = gender(city_data)
            print('\nMale: {}'
                  '\nFemale: {}'.format(gender_result[0], gender_result[1]))

        # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
        # most popular birth years?
            birthyear_result = birth_years(city_data)
            print('\nOldest User: {}'
                  '\nYoungest User: {}'
                  '\nPopular Birth Year: {}'.format(birthyear_result[0], birthyear_result[1], birthyear_result[2]))

        print("\nThat took %s seconds." % (time.time() - start_time))

        # Display five lines of data at a time if user specifies that they would like to
        start_row, end_row = 0, 4
        display_data(city_data,start_row,end_row)

    ## Statistic for "month" filter
    if time_period == 'month':

        # Filter by what month?
        month_filter = get_what_month().lower()

        # List of row based on selected month filter
        selected_data = []
        for month in month_list:
            if month[0] == month_filter:
                month_index = month[1]
        for data in city_data:
            if data['Start Time'].month == month_index:
                selected_data.append(data)

        print('\nCalculating the Statistic...')

        start_time = time.time()

        # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
        pop_day = popular_day(selected_data)
        print('\nPopular Day is {}'.format(pop_day.title()))

        # What is the most popular hour of day for start time?
        pop_hour = popular_hour(selected_data)
        print('\nPopular Hour is {}'.format(pop_hour))

        # What is the total trip duration and average trip duration?
        trip_result = trip_duration(selected_data)
        print('\nTotal Trip Duration: {}'
              '\nAverage Trip Duration: {}'.format(trip_result[0],trip_result[1]))

        # What is the most popular start station and most popular end station?
        station_result = popular_stations(selected_data)
        print('\nPopular Start Station: {}'
              '\nPopular End Station: {}'.format(station_result[0],station_result[1]))

        # What is the most popular trip?
        most_trip = popular_trip(selected_data)
        print('\nPopular Trip is {}'.format(most_trip))

        # What are the counts of each user type?
        user_result = users(selected_data)
        print('\nSubscriber: {}'
              '\nCustomer: {}'.format(user_result[0], user_result[1]))

        if city == 'chicago' or city == 'new york':

        # What are the counts of gender?
            gender_result = gender(selected_data)
            print('\nMale: {}'
                  '\nFemale: {}'.format(gender_result[0], gender_result[1]))

        # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
        # most popular birth years?
            birthyear_result = birth_years(selected_data)
            print('\nOldest User: {}'
                  '\nYoungest User: {}'
                  '\nPopular Birth Year: {}'.format(birthyear_result[0], birthyear_result[1], birthyear_result[2]))

        print("\nThat took %s seconds." % (time.time() - start_time))

        # Display five lines of data at a time if user specifies that they would like to
        start_row, end_row = 0, 4
        display_data(selected_data,start_row,end_row)

    ## Statistic for "day" filter
    if time_period == 'day':

        # Filter by what day?
        day_filter = get_what_day().lower()

        # List of row based on selected day filter
        selected_data = []
        for day in day_list:
            if day[0] == day_filter:
                day_index = day[1]
        for data in city_data:
            if data['Start Time'].isoweekday() == day_index:
                selected_data.append(data)

        print('\nCalculating the Statistic...')

        start_time = time.time()

        # What is the most popular hour of day for start time?
        pop_hour = popular_hour(selected_data)
        print('\nPopular Hour is {}'.format(pop_hour))

        # What is the total trip duration and average trip duration?
        trip_result = trip_duration(selected_data)
        print('\nTotal Trip Duration: {}'
              '\nAverage Trip Duration: {}'.format(trip_result[0],trip_result[1]))

        # What is the most popular start station and most popular end station?
        station_result = popular_stations(selected_data)
        print('\nPopular Start Station: {}'
              '\nPopular End Station: {}'.format(station_result[0],station_result[1]))

        # What is the most popular trip?
        most_trip = popular_trip(selected_data)
        print('\nPopular Trip is {}'.format(most_trip))

        # What are the counts of each user type?
        user_result = users(selected_data)
        print('\nSubscriber: {}'
              '\nCustomer: {}'.format(user_result[0], user_result[1]))

        if city == 'chicago' or city == 'new york':

        # What are the counts of gender?
            gender_result = gender(selected_data)
            print('\nMale: {}'
                  '\nFemale: {}'.format(gender_result[0], gender_result[1]))

        # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
        # most popular birth years?
            birthyear_result = birth_years(selected_data)
            print('\nOldest User: {}'
                  '\nYoungest User: {}'
                  '\nPopular Birth Year: {}'.format(birthyear_result[0], birthyear_result[1], birthyear_result[2]))

        print("\nThat took %s seconds." % (time.time() - start_time))

        # Display five lines of data at a time if user specifies that they would like to
        start_row, end_row = 0, 4
        display_data(selected_data,start_row,end_row)

    # Restart?
    restart()

if __name__ == "__main__":
	statistics()
