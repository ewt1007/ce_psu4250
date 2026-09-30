# Smart Calendar Syrnchronized Alarm Clock

This project will be an alarm clock which will synchronize to your google calendar app and will wake you up according to your schedule and your preferences.

This project will have several components:

1. Clock
    - Keep track of time
    - display current time
    - handle data/time calculations
2. Calendar Synchronization
    - Connects to a calendar service over Wi-Fi
    - Downloads upcoming events
    - Determines first relevant event
3. Alarm Scheduler
    - Takes the calendar information and user settings
    - calculates appropriate wake-up time
    - programs the alarm
4. User Settings
    - Which events should trigger wake up
    - How much of a buffer should specific events give
5. Physical Interface
    - Buttons for snooze/dismiss
    - diplay time/alarm/next event
    - speaker for alarm sound
6. Additonal/Potential Features
    Gradually increase alarm volume
    Customize alarm sound
    Different alarm for different types of events
    Backup alarm/default alarm settings based on Day of Week

The Milk-V DuoS dev board will act as the main computer for the alarm clock. It will connect to the internet over Wi-Fi or another network connection to retrieve information from Google Calendar. The board will also be connected to several peripherals through its GPIO pins. A display will be used to show the current time, next calendar event, and scheduled wake-up time. Physical buttons will allow the user to interact with the alarm, such as snoozing or dismissing it. A speaker will also be connected to the board and controlled by the Milk-V to produce the alarm sound.
