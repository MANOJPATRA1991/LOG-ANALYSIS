# LOG ANALYSIS 

This project was done as the third of 6 projects from the [Udacity Full Stack Nanodegree course](https://in.udacity.com/course/full-stack-web-developer-nanodegree--nd004/).

## Table of Contents
1. [Installation](#installation)
3. [Description](#description)
5. [Reference](#reference)
6. [License](#license)

### Installation

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

##### Executing the program

1. Copy the python files to the folder which contains the newsdata.sql file.
2. If the folder doesn't already contain a Vagrantfile. Run the following command to create one.
        
    `vagrant init hashicorp/precise64`
  



### Reference
1. [Python Documentation](https://docs.python.org/3/)
2. [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
3. [PEP8](https://www.python.org/dev/peps/pep-0008/)

### License
The content of this repository is licensed under [MIT](https://choosealicense.com/licenses/mit/).


