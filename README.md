Log-Analysis Project

This project is a requirement for the Udacity Full-stack Nanodegre. The task is to create a Python based
reporting tool that prints out reports (in plain text) based on the data in a mock database created and maintained by Udacity. 
The report should answer the following 3 questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which day(s) did more than 1% of requests lead to errors?

Setup Project:

Install Vagrant and VirtualBox
Download or Clone fullstack-nanodegree-vm repository.
Download the newsdata.zip from here. Unzip the file and place newsdata.sql in the vagrant file


Launching the Virtual Machine:

Launch the Vagrant VM inside Vagrant sub-directory in the downloaded repository using command:
  $ vagrant up

Then ssh connect to it:
  $ vagrant ssh

Change directory to /vagrant.

Setting up the database:

Load the data in PostgreSQL database:
 $ psql -d news -f newsdata.sql

Then run the program:
  $ python log_analysis_project.py