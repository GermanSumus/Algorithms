"""
Calander or Event tracker that executes on command and cli start up. (.bachrc)

Each event is a class with multiple attributes. Time, date, name, etc.

A month will be a dictionary with keys numbered from 1 to 31, 30, and, 28 or 29.


A months values will be Event Objects in a list.
"""
import os
import datetime

class Event():
    def __init__(self, date, title, description, time, end_time, calendar):
        self.date = date
        self.title = title
        self.description = description
        self.time = time
        self.end_time = end_time
        self.calendar = calendar
        self.day = int(self.date[3:5])
        
    def __repr__(self):
        return f'{self.date}|{self.title} @ {self.time}'

    def change_date(self, date):
        self.date = date


    def change_title(self, title):
        self.title = title


    def change_calendar(self, calendar):
        self.calendar = calendar

    def change_time(self, time):
        self.time = time

    def change_description(self, description):
        self.description = description

    def change_end_time(self, end_time):
        self.end_time = end_time
        
    def show_event(self):
        print(self.date, self. time)
        print(self.title)
        print(self.description)

class Month():

    def __init__(self, days, month, start_day='Monday'):
        self.title = month
        self.month = dict(zip([x for x in range(1,days + 1)],
                              [[] for x in range(days)]))
        self.star_day = start_day
        self.week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                     'Saturday', 'Sunday']
    def __repr__(self):
        return f'{self.title}'

    def add_event(self, event):
        self.month[event.day].append(event)

    def make_event(self):
        date = input('Enter in date xx-xx-xxxx: ')
        title = input('Enter in title: ')
        description = input('Enter in description: ')
        start = input('Enter in start time: ')
        end = input('Enter in end time: ')
        calendar = input('Enter in calendar type: ')
        event = Event(date, title, description, start, end, calendar)
        self.add_event(event)

    def week_events(self):
        today = datetime.datetime.now().day
        next_week = today + 8
        for x in range(today, next_week):
            print(self.month[x])
            
    def week_day(self):
        off_set = find(self.start_day, self.week)
        

def main():
    """Main execution that may run several times in a day"""
    today = datetime.datetime.now()
    
    print('This weeks events')
    
