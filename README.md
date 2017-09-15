# Project: Logs Analysis

In this project, students will practice interacting with a live database both from the command line and from code. Students will explore a large database with over a million rows. And students will build and refine complex queries and use them to draw business conclusions from data.

## Getting Started

These instructions will show you how to run the application locally.

### Prerequisites

* [Vagrant](https://www.vagrantup.com/)
* [Virtual Box](https://www.virtualbox.org/)
* [Python 2.7](https://www.python.org/downloads/)

### How To Run
1. Install [Virtual Box](https://www.virtualbox.org/)
  1. VirtualBox is the software that actually runs the virtual machine.
2. Install  [Vagrant](https://www.vagrantup.com/)
  1. Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem.
3. Download the VM configuration:
  1. Clone the repo by running the following command from the command prompt
    1. `$ git clone https://github.com/jefferygraham992/FSND-Project-Log-Analysis.git`
  2. Change to the  application directory
    1. `$ cd /FSND-Project-Log-Analysis`
  3. Download the date from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.
  4. Change directory to the vagrant directory inside (this directory contains the VM configuration)
    1. `$ cd /vagrant`
4. Start the virtual machine:
  1. From your terminal, inside the vagrant subdirectory, run the command **vagrant up**. This will cause Vagrant to download the Linux operating system and install it.
    1. `$ vagrant up`
  2. When vagrant up is finished running, you can run **vagrant ssh** to log in to your newly installed Linux VM.
    1. `$ vagrant ssh`
  3. Change directory to /vagrant
    1. `$ cd /vagrant`
5. Load the database
    1. `$  psql -d news -f newsdata.sql`
6. Create Views
  1. `CREATE VIEW errors AS SELECT status, to_char(time, 'mm/dd/yyyy') AS DAY, COUNT(STATUS) FROM log GROUP BY DAY, status HAVING status = '404 NOT FOUND';`

 2. `CREATE VIEW all_events AS SELECT status, to_char(time, 'mm/dd/yyyy') AS DAY, COUNT(STATUS) FROM log GROUP BY DAY, status;`

 3. `CREATE VIEW total_events AS SELECT day, SUM (count) as total FROM all_events GROUP BY day;`
 4. Disconnect from database
	 1.  `$ \q`
7. Run the logs analysis program
	1. `$ python logs.py`
