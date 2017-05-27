Barry Yang and Lily Xu
CS 61 Databases
Lab 3 part b
May 25, 2017


# Overview

This database is a manuscript management system for the Journal of E-commerce Research Knowledge. There are three types of users: author, editor, reviewer.

Our management system consists of:
- `setup.sql` creates the tables, views, triggers, and initial inserts
- `database.py` defines a class to establish the specific database
- `db_driver.py` runs the database management system
- `db_functions.py` specifies all the functionality for commands


# Running the code

Execute `setup.sql` to create the tables, views, triggers, and insert initial data.

Note that Python 3 and a Python Driver for MongoDB are required to run our code. To run the front-end application, execute `db_driver.py` by entering the following in the command line:
```
python3 db_driver.py
```

The user may then type in any valid command, which are explained below. The program will continue to run indefinitely until the user inputs 'q' or 'quit' to exit the management system.


# Commands
For all commands, we use the pipe character `|` as the delimiter. The general commands can be executed at any point. The author-, editor-, and reviewer-specific commands can only be executed when a user of that category is logged in.

### General commands
Log in
```
login|<id>
```
Register a new author
```
register|author|<fname>|<lname>|<email>|<address>|<affiliation>
```
Register a new editor
```
register|editor|<fname>|<lname>
status
```
Register a new reviewer
```
register|reviewer|<fname>|<lname>|<RICode1>|<RICode2>|<RICode3>
```


### Author-specific
View status of all submitted manuscripts
```
status
```
Submit a new manuscript
```
submit|<title>|<affiliation>|<RICode>|<author2>|<author3>|<author4>
```
Retract a specific manuscript
```
retract|<manuscript_id>
```


### Editor
Assign a reviewer to a manuscript
```
assign|<manuscript_id>|<reviewer_id>
```
Reject a manuscript
```
reject|<manuscript_id>
```
Accept a manuscript
```
accept|<manuscript_id>
```
Typeset a manuscript
```
typeset|<manuscript_id>|<pp>
```
Schedule a manuscript to an issue
```
schedule|<manuscript_id>|<issue_year>|<issue_period>
```
Publish a manuscript
```
publish|<issue_year>|<issue_period>
```


### Reviewer
View status of all reviewed manuscripts
```
status
```
Resign and leave the system
```
resign
```
Reject a manuscript
```
reject|<manuscriptID>|<appropriateness>|<clarity>|<methodology>|<contribution>
```
Accept a manuscript
```
accept|<manuscriptID>|<appropriateness>|<clarity>|<methodology>|<contribution>
```


# Limitations
- The title of a manuscript cannot contain apostrophes or quotations marks ` "
- No inputs can include the pipe character `|`
- The secondary author name cannot include spaces in the first name or last name
- There is no "log out" functionality; an active user is logged out only when a different user is logged in.
- The master key must be entered anew each time the database starts up. For encryption to work properly, the master key ought to be constant each time.
- When a new manuscript is submitted, it is randomly assigned to an avilable editor.
- We have not implemented certain checks of defensive programming, such as ensuring integers are valid.
- Does not accept RICodes outside what was provided by the professor
- To switch users, we must log out
- For extra, inserted data cannot be used
