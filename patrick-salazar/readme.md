Newsy is a command line program designed to answer the following questions provided in the newsdata.sql database. 

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

Example:
"Princess Shellfish Marries Prince Handsome" — 1201 views
"Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
"Political Scandal Ends In Political Scandal" — 553 views

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

Example:
Ursula La Multa — 2304 views
Rudolf von Treppenwitz — 1985 views
Markoff Chaney — 1723 views
Anonymous Contributor — 1023 views

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. 

Example:
July 29, 2016 — 2.5% errors

When run, the answers to these questions is in plain-text format and easily readable on the command line interface or as seen in output.txt in this repository. 














Setup – Instructions provided by Udacity.com

Dependencies: 
psycopg2 

Tools/Programs/Files:
PostgreSQL database server
VirtualBox
Vagrant
Install VirtualBox
VirtualBox is the software that actually runs the virtual machine. You can download it from virtualbox.org, here. Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.
Ubuntu users: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.

Install Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from vagrantup.com. Install the version for your operating system.
Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.


If Vagrant is successfully installed, you will be able to run vagrant --version
in your terminal to see the version number.
The shell prompt in your terminal may differ. Here, the $ sign is the shell prompt.

Download the VM configuration
There are a couple of different ways you can download the VM configuration.
You can download and unzip this file: FSND-Virtual-Machine.zip This will give you a directory called FSND-Virtual-Machine. It may be located inside your Downloads folder.
Note: If you are using Windows OS you will find a Time Out error, to fix it use the new Vagrant file configuration to replace you current Vagrant file.
Alternately, you can use Github to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm.
Either way, you will end up with a new directory containing the VM files. Change to this directory in your terminal with cd. Inside, you will find another directory called vagrant. Change directory to the vagrant directory:


Navigating to the FSND-Virtual-Machine directory and listing the files in it.
This picture was taken on a Mac, but the commands will look the same on Git Bash on Windows.

Start the virtual machine
From your terminal, inside the vagrant subdirectory, run the command vagrant up. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.


Starting the Ubuntu Linux installation with vagrant up.
This screenshot shows just the beginning of many, many pages of output in a lot of colors.

When vagrant up is finished running, you will get your shell prompt back. At this point, you can run vagrant ssh to log in to your newly installed Linux VM!


Logging into the Linux VM with vagrant ssh.

Logged in!
If you are now looking at a shell prompt that starts with the word vagrant (as in the above screenshot), congratulations — you've gotten logged into your Linux VM.
If not, take a look at the Troubleshooting section below.
The files for this course
Inside the VM, change directory to /vagrant and look around with ls.
The files you see here are the same as the ones in the vagrant subdirectory on your computer (where you started Vagrant from). Any file you create in one will be automatically shared to the other. This means that you can edit code in your favorite text editor, and run it inside the VM.
Files in the VM's /vagrant directory are shared with the vagrant folder on your computer. But other data inside the VM is not. For instance, the PostgreSQL database itself lives only inside the VM.
Running the database
The PostgreSQL database server will automatically be started inside the VM. You can use the psqlcommand-line tool to access it and run SQL statements:


Running psql, the PostgreSQL command interface, inside the VM.

Logging out and in
If you type exit (or Ctrl-D) at the shell prompt inside the VM, you will be logged out, and put back into your host computer's shell. To log back in, make sure you're in the same directory and type vagrant ssh again.
If you reboot your computer, you will need to run vagrant up to restart the VM.

Download the data
Next, download the data here. You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.
To build the reporting tool, you'll need to load the site's data into your local database. Review how to use the psql command in this lesson: (FSND version)
To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql.
Here's what this command does:
• psql — the PostgreSQL command line program
• -d news — connect to the database named news which has been set up for you
• -f newsdata.sql — run the SQL statements in the file newsdata.sql
Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

Getting an error?
If this command gives an error message, such as —
psql: FATAL: database "news" does not exist
psql: could not connect to server: Connection refused
— this means the database server is not running or is not set up correctly. This can happen if you have an older version of the VM configuration from before this project was added. To continue, download the virtual machine configuration into a fresh new directory and start it from there.
Explore the data
Once you have the data loaded into your database, connect to your database using psql -d newsand explore the tables using the \dt and \d table commands and select statements.
• \dt — display tables — lists the tables that are available in the database.
• \d table — (replace table with the name of a table) — shows the database schema for that particular table.
Get a sense for what sort of information is in each column of these tables.
The database includes three tables:
• The authors table includes information about the authors of articles.
• The articles table includes the articles themselves.
• The log table includes one entry for each time a user has accessed the site.
As you explore the data, you may find it useful to take notes! Don't try to memorize all the columns. Instead, write down a description of the column names and what kind of values are found in those columns.

Connecting from your code
The database that you're working with in this project is running PostgreSQL, like the forum database that you worked with in the course. So in your code, you'll want to use the psycopg2 Python module to connect to it, for instance:
db = psycopg2.connect("dbname=news")








Running the Program:

Creating Custom Views
You may see the database structure, including original tables and custom views on the newsdb_tables_views.xlsx document included in this repository.
In order to answer each of the proposed questions in one query, at least one custom view was created for each question. The original tables remain unaltered and the SQL commands to create the views are included as comments in the newsy.py file.

The first question

 – “What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.” –

requires the VIEWS data from the LOG table as well as the SLUG and TITLE data from the ARTICLES table. The VIEWS are counted and grouped. As the PATH column from the LOG table is the only reference to an article, the string must be formatted to match the SLUG in the ARTICLES table. The result is a view called TOPS, which shows article titles and number of views. 

create view tops as select replace(path, '/article/', '') as slugpath, count(*) as views from log group by slugpath order by views;




the TOPS view can then be queried to find the top 3 viewed articles:

              title               | views
----------------------------------+--------
 Bears love berries, alleges bear | 253801
 Bad things gone, say good people | 170098
 Goats eat Google's lawn          |  84906

The second question
-“Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.” –

requires the NAME data from the AUTHORS table and the SLUG data from the ARTICLES table. I created a custom view AUTHNAMESLUG to capture that join:

create view authnameslug as select authors.name, articles.slug from authors join articles on authors.id = articles.author group by authors.name, articles.slug order by authors.name;


          name          |           slug
------------------------+---------------------------
 Anonymous Contributor  | bad-things-gone
 Markoff Chaney         | balloon-goons-doomed
 Rudolf von Treppenwitz | candidate-is-jerk
 Rudolf von Treppenwitz | trouble-for-troubled
 Ursula La Multa        | bears-love-berries
 Ursula La Multa        | goats-eat-googles
 Ursula La Multa        | media-obsessed-with-bears
 Ursula La Multa        | so-many-bears


The query can also use the VIEWS data which we have already obtained from the LOG table in the TOPS view. Joining AUTHNAMESLUG and TOPS results in
         author         | views
------------------------+--------
 Ursula La Multa        | 507594
 Rudolf von Treppenwitz | 423457
 Anonymous Contributor  | 170098
 Markoff Chaney         |  84557


The third question

 – “On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.” –

requires the TIME and STATUS data from the LOG table. 4 views were created in order to isolate the data needed. 

This first view ALLSTATUS counts all responses by status type and date
create view allstatus as select date(time) as date, count(status) as total from log group by date order by date;

    date    | responses
------------+-----------
 2016-07-01 |     38705
 2016-07-02 |     55200
 2016-07-03 |     54866
 2016-07-04 |     54903
 2016-07-05 |     54585
 2016-07-06 |     54774
 2016-07-07 |     54740
 2016-07-08 |     55084
 2016-07-09 |     55236
 2016-07-10 |     54489
 2016-07-11 |     54497



The second view ERRORS isolates only those responses that were errors:
create view errors as select date(time) as date, count(status) as err_responses from log where status != '200 OK' group by date order by date;

    date    | err_responses
------------+---------------
 2016-07-01 |           274
 2016-07-02 |           389
 2016-07-03 |           401
 2016-07-04 |           380
 2016-07-05 |           423
 2016-07-06 |           420


The third view PERCENT combines DATE, ERR_RESPONSES, and RESPONES to view all in rows by date.
 create view percent as select errors.date, errors.err_responses, allstatus.responses from errors join allstatus on allstatus.date = errors.date order by errors.date;

     date    | err_responses | responses
------------+---------------+-----------
 2016-07-01 |           274 |     38705
 2016-07-02 |           389 |     55200
 2016-07-03 |           401 |     54866
 2016-07-04 |           380 |     54903
 2016-07-05 |           423 |     54585
 2016-07-06 |           420 |     54774
 2016-07-07 |           360 |     54740


The fourth view FINALP provides error responses, all responses and the percentage that the error responses represent.
create view finalp as select date, err_responses, responses, round(err_responses * 100.0 / responses, 1) as percent from percent;

    date    | err_responses | responses | percent
------------+---------------+-----------+---------
 2016-07-01 |           274 |     38705 |     0.7
 2016-07-02 |           389 |     55200 |     0.7
 2016-07-03 |           401 |     54866 |     0.7
 2016-07-04 |           380 |     54903 |     0.7
 2016-07-05 |           423 |     54585 |     0.8

The final query may now be made to determine what days the errors reached more than one percent of all responses.
select date, percent from finalp where percent > 1.0;
    date    | percent
------------+---------
 2016-07-17 |     2.3


I was then able to format the returned data into string text in order to format it legibly for the user.

Thank you!

