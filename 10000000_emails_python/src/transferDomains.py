#/usr/bin/python

#====================================================================================
# test Media online test
# Author: Andrew Ho
# Date: Wednesday, June 18, 2014.
#
# file: transferDomains.py
# Description: takes a set of domain names from the mailing table in test_db,
# adds the date to the query result, and then transfers the new data to a new table,
# domain_count which stores the sum of unique domain names of that day
#====================================================================================

# import libraries/packages
import sys
import MySQLdb
import time
import datetime
#from Database import Database


# create connection to database

def db_connection(user_id, password, db):
    try:
        db_conn = MySQLdb.connect(user      = user_id,
                                  passwd    = password,   
                                  db        = db)
        print "successfully connected to", "test_db"

    except MySQLdb.Error, rc:
        print "Error %d: %s" % (rc.args[0], rc.args[1])
        sys.exit(1)

    return db_conn

#==============================
# main
#==============================
def main():
    
    day                 = ""

    # check the arguments
    # if no arguments are present, then assume this script is run for the current day
    # if an argument is present ie) python transferDomains.py 1, it indicates that you're subtracting 1 from the current day
    # this will be implemented for testing purposes, transferring data from the MAILING table to the domain_counter table starting from
    # 30 days ago (transferDomains.py 30) to yesterday (transferDomains.py 1)
    # if more than one argument is inputted, only the first argument is taken, the rest are ignored
    if (len(sys.argv) < 2):
        day = 0
    else:
        try:
            day = int(sys.argv[1])
        except ValueError:
            print "Error: Input is not an integer, please input an integer\n"
            print "ex) python transferDomains.py 1"
            sys.exit(1)

    # declare/initialize variable
    today               = datetime.date.today()
    delta               = datetime.timedelta(days=day)    # established for testing purposes
    today               = today - delta                 # established for testing purposes

    #variables for MySQLdb parts
    user_id             = "andrew"
    password            = "password"
    db_name             = "test_db"
    table_one           = "mailing"
    table_two           = "domain_count"

    connection          = ""
    sel_cursor          = ""
    mailing_results     = ""
    insert_count        = 0
    sel_count           = 0
    insert_cursor       = ""
    row                 = ()

    # SQL query using substr and locate (for the '@'). It is more efficient putting this in SQL (it does fall in a grey area of simple vs complex query).
    # I could select all the data from the table and strip the local parts off the e-mail address but that is not efficient, especailly when dealing
    # with at least 10 000 000 e-mails. SQL can handle the stripping of the values much faster than Python. The load for this will be put on SQL as 
    # there is less overhead  
    sql_query           = "SELECT SUBSTR(addr, LOCATE('@', addr) + 1) AS domain, count(*) AS count FROM %s GROUP BY domain ORDER BY count DESC" % (table_one)


    # create object and new connection to database
    connection = db_connection(user_id, password, db_name)

    # once object has been established, create a cursor
    sel_cursor = connection.cursor()

    #======================================================================
    # Begin by extracting the domains of the e-mail addresses and counting them
    #======================================================================
    try:
        sel_cursor.execute(sql_query)

    except MySQLdb.Error, rc:
        print "Error %d: %s" % (rc.args[0], rc.args[1])
        sel_cursor.close()

    mailing_results = sel_cursor.fetchall()
    sel_cursor.close()

    #count number of rows fetched
    sel_count = len(mailing_results)
    print "retrieved %d rows from %s" % (sel_count, db_name)

    #======================================================================
    # Begin to insert statements into the second table, domain_count
    #======================================================================
    insert_cursor = connection.cursor()

    for row in mailing_results:
        row = list(row)
        row.insert(0, today)    #inserting the date into the tuple/list
        row = tuple(row)

        sql_insert = "INSERT INTO %s values ('%s', '%s', '%d')" % (table_two, row[0], row[1], row[2])

        try:
            insert_cursor.execute(sql_insert)

        except MySQLdb.Error, rc:
            print "Error %d: %s" % (rc.args[0], rc.args[1])
            print "Closing database connection, not committing previously entered rows into %s" % ("domain_count")
            db_conn.close()
            sys.exit(1)

        insert_count = insert_count + 1

    insert_cursor.close()

    print "inserted %d rows into %s" % (insert_count, table_two)

    # Test to see if same number of rows retrieved equals same number of rows inserted
    '''
    if (insert_count == sel_count):
        print "successfully retreived %d rows and successfully inserted %d rows" % (sel_count, insert_count)
        db_conn.commit()
    else:
        print "ERROR: %s" % ("Unsuccessfully inserted the same amount of rows as retrieved")
        db_conn.close()
        sys.exit(1)
    '''

    connection.commit()
    connection.close()

    sys.exit(0)

if __name__ == "__main__":
    main()