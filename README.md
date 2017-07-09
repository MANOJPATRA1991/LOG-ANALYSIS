
# LOG ANALYSIS 

This project was done as the third of 6 projects from the [Udacity Full Stack Nanodegree course](https://in.udacity.com/course/full-stack-web-developer-nanodegree--nd004/).

## Table of Contents
1. [Installation](#installation)
2. [Description](#description)
3. [Reference](#reference)
4. [License](#license)

### Installation

**NOTE**: 

This project was built on **Windows 10** OS. All the interaction with the Virtual Machine was done through **Command Prompt on Windows**.

(**Do not use Git Bash for this project. It simply won't work**.)

1. Python

The source code for this project is written in [Python v3.6.1](https://www.python.org/downloads/) programming language.
For direct download of version 3.6.1 [click here](https://www.python.org/ftp/python/3.6.1/python-3.6.1.exe).

2. Code Validators

The source code was checked against bugs and quality using **Pylint** tool, **PEP8** tool and [PEP8 online check](http://pep8online.com).

To install Pylint:

```
pip3 install pylint
```

To check Python file using Pylint:

```
pylint fileName.py
```

To install pep8:

```
pip3 install pep8
```


To check Python file using pep8:

```
pep8 fileName.py
```

3. Virtual Box

To run the Virtual Machine, first we need to download it and then install it.
Virtual Box can be downloaded from [here](https://www.virtualbox.org/wiki/Downloads).

4. Vagrant

Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. 
Vagrant can be downloaded from [here](https://www.vagrantup.com/downloads.html).

### Description

This project is an information reporting tool which provides information regarding the most popular articles, the most popular authors and the most logged errors in a day from a news database.

Following are the views that were created as part of the **news** database:

1. MostViewedPaths

```
create view MostViewedPaths as (
select path, count(*) as views
from log
where path like '/_%'
group by path
order by views desc);
```

2. articleShortInfo

```
create view articleShortInfo as (
select a.title, c.name, b.views
from articles as a join MostViewedPaths as b
on concat('/article/', a.slug) = b.path
join authors as c
on a.author = c.id
order by views desc);
```

3. LogRequests

```
create view LogRequests as (
select time::timestamp::date, count(*) as total
from log
group by time::timestamp::date
order by total desc);
```

4. ErrorRequests

```
create view ErrorRequests as (
select time::timestamp::date, count(*) as errors
from log
where status like '4%' or status like '5%'
group by time::timestamp::date
order by errors desc);
```

The **newsdb.py** file contains the implementations for the three functions:

1. `get_most_popular_articles()`
2. `get_most_popular_authors()`
3. `get_most_logged_errors()`

In each of the these functions, a new connection object and cursor object was created as:

```
DBNAME = "news"
conn = psycopg2.connect(database=DBNAME)
cursor = conn.cursor()
```

Then, the query is run using the `cursor.execute()` function.
The data is fetched using `cursor.fetchall()` and stored in a local variable which is returned by the respective functions.

Finally, the connection was closed using `conn.close()` within each function.

##### Executing the program

1. Copy the python files to the folder which contains the newsdata.sql file.
2. If the folder doesn't already contain a Vagrantfile. Run the following command to create one.
        
```
vagrant init
```
    
3. To start the virtual machine, from your local directory, run the following command:
        
```
vagrant up
```

4. Then to drop a full fledged SSH session, run the following command:
        
```
vagrant ssh
```
        
5. Type `psql` to switch to the interactive terminal for working with PostgreSQL.
6. Now create a new database(if it doesn't exist already):
        
```
create database news;
```
        
7. Then exit with **Ctrl + D**.

8. Run `psql -d news -f newsdata.sql` to create the tables **authors**, **articles** and **log**. This will exit the psql terminal.
 
9. Start the psql terminal with `psql` and move into the **news** database with `\c news`.

10. Now open up another Command Prompt. Move to the project directory. Run `vagrant ssh` to move into the VM.

11. Run the **newsdata.py** file with the following command after moving into the file's location to get the output:

```
python newsdata.py
```


### Reference
1. [Python Documentation](https://docs.python.org/3/)
2. [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
3. [PEP8](https://www.python.org/dev/peps/pep-0008/)

### License
The content of this repository is licensed under [MIT](https://choosealicense.com/licenses/mit/).


