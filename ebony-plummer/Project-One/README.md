# README

## Project Description

This project is a reporting tool that runs queries a a database called `news`. This reporting tool will use the data from the `news` database to return data on the articles that readers like the best. This project will use the PostgreSQL dialect of SQL to query the `news` database. This reporting will report data for the following questions:

1. What are the most popular articles at all times?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?


## Dependencies/Pre-Requisites

 * Linux Based Virtual Machine-In order to start this project you will need database software which will be provided by a Linux based virtual machine. The virtual machine and the software to run it can be downloaded at the following links:
     * Virtual Box: https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
     * Vagrant: https://www.vagrantup.com/
 * Unix-Style Terminal
 * This project uses the PostgreSQL dialect of SQL the  PostgreSQL documentation to be able to create the queries for this project can be found here:
     * PostgreSQL Documentation: https://www.postgresql.org/docs/9.5/index.html
 * The `psycogp2` Python module which will be used to connect the code from the report tool to the `news` database.

 
## Setup/Installation

### Installing and Configuring the Virtual Machine.

* This project makes uses of a Linux based virtual Machine. The tools Vagrant and Virtual box are used to install and manage the virtual machine.
    * Install Virtual Box
    * Instal Vagrant
* The configuration for the Linux base virtual machine can be downloaded
  here: https://github.com/udacity/fullstack-nanodegree-vm
* Use the command `vagrant up` to start the Linux based virtual machine. Please note that it may take several minutes to download.
* Once `vagrant up` is finish running use `vagrant ssh` to log into and run the virtual machine.

### Download the Data

* The data for this project can be downloaded from the Databases with SQL and Python section of the Udacity Full Stack Nanodegree Course at Udacity.com.
    * https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
    * Unzip the above file, and inside there will be a file called `newsdata.sql`, plave this file in the `vagrant` directory that is shared with your virtual machine.
    * to load the file `cd` in to the `vagrant` directory and use the
    the command `psql -d news -f newsdata.sql`.

### The Psycopg2 Module
* The `psycopg2` module will be used to connect the code for the report tool to the 
`news` database.
    * Import the `psycopg2` module into your code by running `pip install psycopg2`.


## Using the `news` Database     

* Once you loaded the data into your databse, you can explore your database using
`psql -d news`.
* You can explore the tables in the database uy using the following commands:
    * `\dt`
    * `\dt table`
    * `SELECT`

* The `news` database has the following tables:
    * articles
    * authors
    * log

* Use views to print out your answers.

1. create view top_articles as select slug, count slug as pageviews from articles
   left join log on replace(log.path, '/article/', ') = articles.slug group by slug

2. create view top_authors as select slug, count slug as pageviews from articles
   left join log on replace(log.path, '/article/', ') = articles.slug group by slug

3. create view as num_errors select time, status, count(status) as num_errors group
   by time order by num_errors      

