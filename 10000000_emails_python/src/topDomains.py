#/usr/bin/python

#====================================================================================
# test Media online test
# Author: Andrew Ho
# Date: Wednesday, June 18, 2014.
#
# file: topDomains.py
# Description: finds the total number of e-mail domains in the domain_count table
# and calculates the top 50 domain names in terms of growth in the past 30 days
#====================================================================================


#import libraries/packags
import sys
import MySQLdb
import datetime


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

#
# main
#
def main():

    #declare/initialize variables
    user_id             = "andrew"
    password            = "password"
    db_name             = "test_db"
    table_two           = "domain_count"

    connection          = ""
    rc                  = ""
    today               = datetime.date.today()
    delta               = datetime.timedelta(days=30)
    previous_day        = today - delta

    tol_cursor          = ""
    


    connection = db_connection(user_id, password, db_name)

    tol_cursor = connection.cursor()
    try:
        tol_cursor.execute("SELECT SUM(domaincount) AS total FROM %s WHERE day BETWEEN '%s' AND '%s' " % (table_two, previous_day, today))

    except MySQLdb.Error, rc:
        print "Error %d: %s" % (rc.args[0], rc.args[1])
        sys.exit(1)


    sum_total = tol_cursor.fetchall()   #outputted as a tuple instead of an integeer, must convert to int
    sum_total = sum_total[0][0]    #what if sum_total is 0? divide by 0 == boo!
    tol_cursor.close()

    print sum_total
    # error check to make sure that you don't divide by 0 when calculating the percentage
    if ((sum_total == 0) or (sum_total == None)):
        print "Error: Unable to find the total number of domains, please check the table"
        sys.exit(1)

    print "the total sum of the domains between %s and %s is: %d " % (previous_day, today, sum_total)

    fifty_cursor = connection.cursor()
    fifty_cursor.execute("select domain, max(domaincount) as total_number, sum(domaincount) * 100.0 / %d as percent_increase from domain_count where day between '%s' and '%s' group by domain order by percent_increase desc limit 50" % (sum_total, previous_day, today))
    fifty_result = fifty_cursor.fetchall()
    column_names = [i[0] for i in fifty_cursor.description]
    fifty_cursor.close()


    print "The top 50 domains in terms of growth between %s and %s" % (previous_day, today)
    print column_names
    for element in fifty_result:
        #print "%-*s | %-*s | %-*d |" % (element[0], element[1], element[2])
        #print "%s\t | %d\t | %.2f\t |" % (element[0], element[1], element[2])
        print element[0], element[1], element[2]



    #print fifty_result

    connection.commit()
    connection.close()

if __name__ == "__main__":
    main()
