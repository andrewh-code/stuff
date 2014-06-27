#!/usr/bin/python

#====================================================================================
# Author: Andrew Ho
# Date: Wednesday, June 18, 2014.
#
# file: transferDomains.py
# Description: 
#   use:    python generate_emails.py <filename>.txt <number>
#   This python application generates <number> amount of e-mails which are created from random
#   by the e-mail_generator function. The local part of the e-mails and hte domain part of the
#   e-mails (aside from the @ symbol and the .com) are randomly generated from a set list of 
#   predefined characters.
#   once the e-mails have been generated and saved to a file, they are loaded into the table
#   using the infile loading function.
#====================================================================================

# import packages/libraries
import string
import random
import MySQLdb
import sys
import os


def connect_db(user_id, password, db_name):
    try:
        db_conn = MySQLdb.connect(user      = user_id,
                                  passwd    = password,
                                  db        = db_name)

    except MySQLdb.Error, rc:
        print "Error %d: %s" % (rc.args[0], rc.args[1])
        sys.exit(1)

    print "successfully connected to", "test_db"

    return db_conn


#def disconnect_db(db_name):


# set list of existing domain names
# random string generator
def email_generator(file_name, upper_limit):


    # define/initialize variables
    size        = 8
    size2       = 5
    temp_char   = "";
    char_set    = string.ascii_uppercase
    domain_list = ['a', 'b', 'c', 'd', 'e', 'f']

    '''
    domain_list = [ '@outlook.com',
                    '@hotmail.com',
                    '@gmail.com',
                    '@msn.ca',
                    '@msn.com',
                    '@yahoo.ca',
                    '@aol.com',
                    '@tuc.org',
                    '@test.ca',
                    '@testing.com',
                    '@computer.in',
                    '@facebook.com',
                    '@asdfb.com',
                    '@fdas.com']
    '''

    file = open(file_name, "w")

    for x in range(0, upper_limit):
        # generate the local part of the e-mail    
        local_email = ''.join(random.choice(char_set) for temp_char in range(size))
        # choose a domain name from the list
        domain_email = "@" + ''.join(random.choice(domain_list) for temp_char in range(size2)) + ".com"

        #domain_email = random.choice(domain_list)

    # combine the local with domain
        email = local_email + domain_email + "\n"

        file.write(email)

    file.close()



# main
def main():

    if (len(sys.argv) < 3):
        print "error, please input the name of a file\n"
        sys.exit(1)

    file_name   = sys.argv[1]
    upper_limit = int(sys.argv[2])   #max number of e-mails generated

    current_dir = os.getcwd()
    print current_dir

    # generate emails and save them to a file
    email_generator(file_name, upper_limit)



    # open up a database connection
    connection = connect_db("andrew", "password", "test_db")
    cur = connection.cursor()

    # load the file into a table
    #cur.execute("INSERT INTO mailing values('%s') ", % (output))
    try:
        cur.execute("LOAD DATA LOCAL INFILE 'day1.txt' INTO TABLE mailing LINES TERMINATED BY '\n'")
    except MySQLdb.Error, rc:
        print "Error %d: %s" % (rc.args[0], rc.args[1])
        print "Unable to load %s into table" % file_name
        sys.exit(1)

    connection.commit()
    connection.close()



if __name__ == "__main__":
    main()