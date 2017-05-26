# Barry Yang and Lily Xu
# CS 61 Databases
# Lab 3 part b
# May 25, 2017


# import traceback                            # for error handling
# import sys                                  # for misc errors

from pymongo import MongoClient
from database import Database
from db_functions import *


TEAM_NAME = 'Team28DB'

if __name__ == "__main__":
    db = Database(TEAM_NAME)

    print("Connection established.\n")


    # prompt user for request
    print("Please input your request. Use '|' to split commands.")
    print("  e.g. register|author|Lily|Xu|lily.18@dartmouth.edu|4774 Hinman Box, Hanover, NH 03755")
    print("  Type 'q' or 'quit' to exit.")
    s = raw_input('--> ')

    while (s != 'quit' and s != 'q'):
        try:
            parse_input(db, s)

        except:                                   # anything else
            print("Unexpected error: {0}".format(sys.exc_info()[0]))
            traceback.print_exc()

        s = raw_input('--> ')


    print("\nConnection terminated.\n", end='')
