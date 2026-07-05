# ARROW
#### Video Demo:  <https://youtu.be/W9u1md9XwoQ>
#### Description:
Arrow is a productivity-focused web application designed for students, freelancers, and anyone looking to boost their productivity. It combines task management, daily time tracking, and visual analytics to help users stay organized and track their personal growth over time.
## The Problem: 
Many people in our community struggle to maintain productivity in their work, studies or even while learn new skills!
## solving the problem: 
To solve this problem, I came up with “Arrow“ , a web-application with a simple and modern UI . This website is based on three tools: to-do list, daily progress tracker and a progress dashboard . these  tools  help users stay organized, track their progress and boost their productivity. Also,“Arrow” comes with a login system that allows every user to keep their own data private and access their account from different devices.

## Explaining The Tools:
### TO-DO LIST : 
It is the first feature that allows users to manage their daily tasks. It supports three main operations: Adding new tasks, marking tasks as completed (checked) and deleting tasks, whether completed or not.
### DAILY PROGRESS TRACKER : 
It provides you an interactive calendar that allows users to select any date  and  record their daily progress.Users can enter the number of hours spent on any activity they want to track, such as studying, working, or any personal goal.They can also rate their mood for that day providing additional insights into their productivity and well-being. 
This feature is to help users maintain a consistent record of their daily activities. Users are not limited to the current day because they can return at any time to add information for previous dates if they forgot to submit it or update existing entries if corrections are needed. 
### PROGRESS DASHBOARD : 
This page converts the Daily Progress Tracker’s entries into visual charts (line charts and bar charts), ...making the data easier to understand and analyze at a glance, and stay motivated throughout their  journey... 
              
 - And of course, all these tools are completely private thanks to the login system, which ensures that each user can access and manage only their own data. and no user can access or see another user’s data.

## Technologies sed :
- Python
- Flask
- SQL
- HTML
- CSS
- JavaScript

## Function of Files :

### app.py:
It is the brain of “Arrow”… It uses Flask framework, Python and SQL. It handles the main functions of the website, such as logging in, creating accounts, managing user sessions, and interacting with the database. It also processes the data from the To-Do List and Daily Progress Tracker so that it can be displayed correctly on the Progress Dashboard.

### Templates folder:
I wrote 8 HTML files, all of them are located in a folder called “templates” …I used html to create the structure of the website … each file have had a purpose : 
1. “layout.html”: I created on it the navigation bar of the website (a small nav-bar contains the logo, login button , sign up button ) and then , I then use Jinja template to  connect this main file with the other HTML files in the same folder.
2. “index.html”: I used it to built the structure of the whole homepage that contains texts, pictures, cards, buttons …
3. “login.html” : I create with it the page that will appear to the user when he clicks the log-in button…in this page the user will be able to log in to the website by writing his username and password.
4. “signup.html” : I create with it the page that will appear to the user when he click the sign-up button …in this page the user will be able to sign up ( create a new account ) by writing a valid (not taken) username and then a password and the confirmation of it .
5. “apology.html” : I create with it the apology page that will appear to the user in case of an error (e.g: write a wrong password in the log-in processing ) with a text that will tell the user what they did wrong (e.g: Incorrect password! )
6. “todo.html”: I create with it the page of the first feature(the to-do list)
7. “time.html”: I create with it the page of the second feauture(the daily progress tracker)
8. “graph.html”:I create with it the third feauture (the progress dashboard)
                  In "todo.html", "time.html", and "graph.html", I extended the navigation bar by adding three buttons that allow users to navigate easily between the different features of the website.
### Static folder :
In the static folder I wrote the “styles.css” file and two JavaScript files, and also the images that I use(the logo, the to-do circle…etc) 
1. ”styles.css” : I used CSS to design and style the entire website. The stylesheet controls the layout, colors, typography, spacing, and responsiveness of the pages. I aimed for a simple and modern design...which provides a relaxing environment for the user.
2. ”script.js” :  This file is responsible for the interactive behavior of the Daily Progress Tracker. It uses the FullCalendar library to create an interactive calendar where users can click on any date, highlight the selected day, and automatically display the form used to submit their progress data.
3. “graph.js”: I created with it the charts shown on the Progress Dashboard. It uses Chart.js library to turn users' progress data into a line chart for study or work hours and a bar chart for mood ratings. I also added a custom neon effect and gradient backgrounds to make the charts more modern and visually appealing.
### Design choices:
For the user interface (UI ) I chose a dark color palette (black , gray and silver) with shades of  white  to create a modern look with a sense of depth and contrast…and offer a comfortable and relaxing experience for the users.
### Problems that I faced:
I faced many challenges while working on my final project,I can mention some:
  1.  in TO-DO list tool. At first, I built it with HTML,CSS and JavaScript …I stored the tasks in the browser’s local storage .however, I realized then that if another user logged in from the same device ,he would reach the previous user’s tasks , which contradicts with the privacy feature of the project. So, I changed the storage method to store the tasks in an SQL database , ensuring that each user could access only their own data and also log in from any device without losing their data.
  2.  Another challenge that I faced was linking the user’s data entries in  the Daily Progress Tracker with the 
  Progress Dashboard to draw the charts . I solved this problem by storing each user’s progress data in the SQL database in a new table linking it to their account too… retrieving it using Flask. Then, I used Chart.js to convert the data into visual charts and display them to the user.
