# Internet Status Notification Using Tkinter and Task Scheduler

This is a simple GUI that displays a message box anytime you lose connection to the internet.

The motivation for this project came from my internet connection dropping while I was still on a webpage and not realizing until I tried navigating to a new page
to get 'No Internet' message. Tired of this, I thought 'wouldn't it be nice if my computer would send me a notification whenever my internet would randomly drop connection.'
And so I got to work.

I will say that the actual code for this project was quite simple and intuitive. What took the majority of my time on this project was trying to get Windows to play nice.

# Basic Setup

To get this up and running properly, these are the steps that I used to work for me:

- First, you're going to want to get Python on Windows if you don't already (navigate to https://www.python.org/downloads/)

- Next, use the message_box.py file above.

- You are going to want to open Notepad and write a batch file connecting your python executable to the message_box.py file:
  ```
  @echo off
  "C:\PATH_TO_PYTHON\python.exe" "C:\PATH_TO_FILE\message_box.py"
  ```
  (Your python executable probably follows this path: C:\Users\YOUR_USERNAME\AppData\Local\Programs\Python\Python39\python.exe)
  
 - When you are done writing this, save it with .bat extension in the same folder you have message_box in.
 
 # Creating the Task
 
 - Now, open up Task Scheduler by hitting the windows key and typing it into the search box.

 - Click 'Create Basic Task'
 
 - Give it a name, such as 'Run Internet Message'
 
 - For this to work for me, I checked the 'Run with highest privileges' box.
 
 - Navigate to 'Triggers' tab and select 'New' at the bottom.
 
 - Select the 'On an event' option in the dropdown at the top next to 'Begin the task'
 
 - Now, next to 'Log' scroll down until you find 'Microsoft-NetworkProfile/Operational', select it.
 
 - Select 'NetworkProfile' next to 'Source'
 
 - Next to 'Event ID' type 10001. This says that your internet status is disconnected. (10000 means you are connected)
 
 - Click 'Enabled' and 'OK'
 
 - Navigate to  the 'Actions' tab and select 'New'
 
 - Select 'Start a Program' next to 'Action'
 
 - Next to 'Program/Script' navigate to you .bat file
 
 - Click 'OK'
 
 - Go to the 'Conditions' tab and uncheck the box next to 'Start the task only if the computer is on AC power' if it is checked.
 
 - Select 'OK' and then 'Run' to test it out.

If everything is input properly, you should get a tkinter message box with the message displayed in it!
Thanks for reading and feel free to make any improvements that you see fit.
 
 
