#==========
 # author:               Andrew Ho
 # date:                 June 18, 2014
 #==========


how_to.txt

DIRECTORY STRUCTURE
==============================
|-- test
    |-- src
        topDomains.py
        transferDomains.py
        
    |-- test
        |-- sample_data
                day1.txt
                day2.txt
                day3.txt
                day4.txt
                day5.txt

        performance.sh
        generate_emails.py
        
    |-- brainstorm    
        notes.txt
        notes2.txt
        notes3.txt

    design.txt
    test_requirements.txt
    README.txt
    sample_input.txt
    testing.txt
    
    

        
HOW TO RUN
=================================
1. Ensure that the database test_db has been created with username andrew and password 'password'
    
    CREATE DATABASE test_db
    CREATE USER 'andrew'@'localhost' IDENTIFIED BY 'password';
    
2. set the inline-data=1 in the /etc/mysql/my.cnf file

3. setup_db can be run in the shell
    ie) mysql < setup_db

4. run the test/generate_emails.py script (if don't already have sample_data)
    ie) python generate_emails.py <day_x>.txt <number_of_rows>
            This generates sample e-mails (for testing purposes) and loads the file into the table

5. execute src/transferDomains.py <days used to subtract from current date>     #for example if argument was 29, then date = today() - 29 days 
    ie) python transferDomains.py 1
            - transfers the data from MAILING table to the second table with the subtracted date
            - For testing purposes (to simulate the past few days), an argument is put in the script 
              so when run, the sample data will be data from the previous day as it is being inserted into the second table

6.  Due to a design design decision, assume a separate process will be used to delete the e-mails in MAILING
    every day (refer to design.txt)
    
7. continue executing steps 4, 5 (decrement the argument from 29 to 0 to simulate 30 days), and 6 in order until 30 of days 
   worth of data has been reached
   
example run to get the data in the past 5 days:

python test/generate_emails.py day5.txt 100000
python src/transferDomains.py 5
python src/topDomains.py
* separate process to delete

python test/generate_emails.py day4.txt 10000
python src/transferDomains.py 4
python src/topDomains.py
* separate process to delete

python test/generate_emails.py day3.txt 5000
python src/transferDomains.py 3
python src/topDomains.py
* separate process to delete

python test/generate_emails.py day2.txt 3000
python src/transferDomains.py 2
python src/topDomains.py
* separate process to delete

python test/generate_emails.py day2.txt 1000
python src/transferDomains.py 2
python src/topDomains.py
* separate process to delete
