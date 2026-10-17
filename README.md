# Google Calendar Syrnchronized Alarm Clock

This project will be an alarm clock which when synchronized to your google calendar app and will wake you up according to your schedule and preferences.

This project will have several components:

1. Clock
    - Keep track of time
    - display current time
    - handle data/time calculations
2. Calendar Synchronization
    - Connects to a calendar service over Wi-Fi
    - Downloads upcoming events
    - Determines relevant events
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
    - Gradually increase alarm volume
    - Customize alarm sound
    - Different alarm sound for different types of events
    - Backup alarm/default alarm settings based on Day of Week

## Project Timeline

The development board is already running an image, connected to Wi-Fi, and
accessible over SSH. The eight-week schedule starts from that milestone. The
software feature set should be complete by the end of Week 6, leaving Weeks 7
and 8 for building and testing the enclosure.

| Week of | Focus | Milestones |
| --- | --- | --- |
| Oct 19 | Define and scaffold the software | Confirm the minimum viable features and component interfaces; set up the project, development workflow, and configuration; verify the board can run a small test program. |
| Oct 26 | Clock and physical interface | Display the current time; connect and test the display and buttons; establish the basic screen and snooze/dismiss behavior. |
| Nov 2 | Calendar synchronization | Choose and configure the Google Calendar access method; retrieve upcoming events over Wi-Fi; handle missing connectivity and calendar errors. |
| Nov 9 | Event selection and alarm scheduling | Add event filters and wake-up buffers; calculate and schedule alarm times; add the user settings needed for the minimum viable version. |
| Nov 16 | Alarm and device integration | Connect and test the speaker or buzzer; integrate the clock, calendar, scheduler, settings, display, and controls on the board. |
| Nov 23 | End-to-end testing and software completion | Test normal operation, restart behavior, time/calendar failures, and alarm controls; fix critical issues and document setup. Freeze the software feature set by the end of the week. |
| Nov 30 | Enclosure design and first build | Measure the assembled components; plan access to the display, buttons, speaker, power, and ventilation; build the first enclosure version. |
| Dec 7 | Enclosure completion and final testing | Finish and assemble the body; fit and secure the components; test the complete clock in its enclosure and make final physical adjustments. |

Keep optional features such as custom sounds, gradual volume, and event-specific
alarms out of the Week 1–6 commitment. Add them only if the minimum viable
software is complete and stable before the end of Week 6.
