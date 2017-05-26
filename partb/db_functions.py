# Barry Yang and Lily Xu
# CS 61 Databases
# Lab 3 part b
# May 25, 2017

# helper functions for database execution


import datetime         # get current date
import random


# TODO: add "insert new issue" as a test query


def insert(db, collection, query):
    client = db.get_client()

    result = client[collection].insert_one( query )

    return result.inserted_id


# returns None if query doesn't exist
def find_one(db, collection, query):
    client = db.get_client()

    cursor = client[collection].find_one( query )

    return cursor


def find(db, collection, query):
    client = db.get_client()

    cursor = client[collection].find( query )

    return cursor


# update a single document
def update(db, collection, select, query):
    client = db.get_client()

    cursor = client[collection].update_one( select, query )

    return cursor


def remove(db, collection, query):
    result = db.collection.delete_many( query )

    return result


# TODO: rename to get_client_results
# def get_cursor_results(db, query):
#     client = db.get_client()
#
#
#     return cursor
#
# def get_single_query(db, query):
#     cursor = db.get_cursor()
#     cursor.execute(query)
#
#     to_return = None
#     for row in cursor:
#         for col in row:
#             to_return = col
#
#     return to_return
#
# # process query, but instead of displaying to user,
# # return output to the caller
# # NOTE: each column is delimited by a pipe '|'
# #       each row is delimited by a newline '\n'
# def submit_query_return(db, query):
#     cursor = db.get_cursor()
#     cursor.execute(query)
#
#     output = ''
#
#     # display results
#     for row in cursor:
#         for col in row:
#             output += str(col) + '|'
#         output = output[:-1] + '\n'
#
#     return output
#
#
# def insert_query(db, query, data):
#     con    = db.get_con()
#     cursor = db.get_cursor()
#     cursor.execute(query, data)
#     con.commit()
#
#     return cursor.lastrowid
#
# # single query, useful for update and delete
# def change_query(db, query):
#     con     = db.get_con()
#     cursor  = db.get_cursor()
#     cursor.execute(query)
#     con.commit()


# parse input from user
# process command if 'login' or 'register'
# call appropriate function to process command for author, editor, or reviewer
def parse_input(db, string):
    tokens = string.strip().split('|')

    if len(tokens) == 0:
        print("ERROR: Invalid input. Query cannot be blank.")
        return

    # log in user
    if tokens[0] == 'login' and len(tokens) > 1:
        user_id = tokens[1]
        login(db, user_id)
    # register new user
    elif tokens[0] == 'register' and len(tokens) > 1:
        register(db, tokens)
    # log off user
    elif tokens[0] == 'logoff':
        db.log_off()
    # logged in, so process according to current user
    elif db.is_logged_in():
        if db.get_user_type() == 'author':
            process_author(db, tokens)
        elif db.get_user_type() == 'editor':
            process_editor(db, tokens)
        elif db.get_user_type() == 'reviewer':
            process_reviewer(db, tokens)
    # if not logged in, must either login or register
    else:
        print("ERROR: Invalid input. Please login or register.")


# check if user_id is valid
# if so, determine user type and act accordingly
# if not, print an error message
def login(db, user_id):
    user_id = int(user_id)

    # is the user an author?
    query = { "personID": user_id, "type": "author" }

    result = find_one(db, "person", query)

    if result:     # if not none
        fname = result.get("fname")
        lname = result.get("lname")
        address = result.get("address")

        print("\nWelcome back, author " + str(user_id) + "! Here's what we have stored about you:")
        print("  First name: " + fname)
        print("  Last name:  " + lname)
        print("  Address:    " + address)

        # execute login
        db.change_user_id(int(user_id))
        db.change_user_type('author')
        db.log_on()

        status_author(db, user_id)

        return

    # is the user an editor?
    query = { "personID": user_id, "type": "editor" }

    result = find_one(db, "person", query)

    if result:
        fname = result.get("fname")
        lname = result.get("lname")

        print("\nWelcome back, editor " + str(user_id) + "! Here's what we have stored about you:")
        print("  First name: " + fname)
        print("  Last name:  " + lname)

        # execute login
        db.change_user_id(int(user_id))
        db.change_user_type('editor')
        db.log_on()

        status_editor(db, user_id)

        return

    # is the user a reviewer?
    query = { "personID": user_id, "type": "reviewer" }

    result = find_one(db, "person", query)

    if result:
        fname = result.get("fname")
        lname = result.get("lname")

        print("\nWelcome back, reviewer " + str(user_id) + "! Here's what we have stored about you:")
        print("  First name: " + fname)
        print("  Last name:  " + lname)

        # execute login
        db.change_user_id(int(user_id))
        db.change_user_type('reviewer')
        db.log_on()

        # TODO: everything should be limited to manuscripts assigned to that reviewer
        status_reviewer(db, user_id)

        return

    # no user corresponds to given id
    print('ERROR: No user exists corresponding to ID ' + str(user_id) + '.')



# register a new user in the system
def register(db, tokens):
    user_type = tokens[1]

    if user_type == 'author':
        personID = register_author(db, tokens[2], tokens[3], tokens[4], tokens[5], tokens[6])

    elif user_type == 'editor':
        personID = register_editor(db, tokens[2], tokens[3])

    elif user_type == 'reviewer':
        if len(tokens) == 7:
            personID = register_reviewer(db, tokens[2], tokens[3], tokens[4], tokens[5], tokens[6])
        elif len(tokens) == 8:
            personID = register_reviewer(db, tokens[2], tokens[3], tokens[4], tokens[5], tokens[6], tokens[7])
        elif len(tokens) == 9:
            personID = register_reviewer(db, tokens[2], tokens[3], tokens[4], tokens[5], tokens[6], tokens[7], tokens[8])
        else:
            print("ERROR: Invalid input. Too many arguments.")
            return

    else:
        print("ERROR: User type " + user_type + " is invalid.")
        return


# get ID of next person
def get_next_id(db, collection):
    client = db.get_client()
    coll = client[collection]

    for item in coll.find().sort(collection + "ID", -1).limit(1):
        return item.get("personID") + 1


def register_author(db, fname, lname, email, address, affiliation):
    personID = get_next_id(db, "person")

    query = { "personID": personID, "fname": fname, "lname": lname, "type": "author", "email": email, "address": address, "affiliation": affiliation }

    result = insert(db, "person", query)

    return personID


def register_editor(db, fname, lname):
    personID = get_next_id(db, "person")

    query = { "personID": personID, "fname": fname, "lname": lname, "type": "editor" }

    result = insert(db, "person", query)

    return personID


def register_reviewer(db, fname, lname, email, affiliation, *ricodes):
    personID = get_next_id(db, "person")

    query = { "personID": personID, "fname": fname, "lname": lname, "type": "reviewer", "affiliation": affiliation, "email": email, "reviewer_status": "active", "riCodeID": ricodes }

    result = insert(db, "person", query)

    return personID


def process_author(db, tokens):
    command = tokens[0]
    authorID = db.get_user_id()

    if command == 'status':
        print("Manuscript statuses for user ID {}: \n".format(authorID))
        status_author(db, authorID)

    # submit manuscript to system
    elif command == 'submit':

        now = datetime.datetime.now()

        manuscriptID = get_next_id(db, "manuscript")
        title        = tokens[1]
        affiliation  = tokens[2]
        RICode       = tokens[3]

        # assign an editor to manuscript
        query = { "type": "editor" }
        cursor = find(db, "person", query)

        # compile list of possible editors
        editors_array = []
        for item in cursor:
            editors_array.append(item.get("personID"))

        # randomly pick an editor
        editor_id = random.choice(editors_array)

        # secondary authors (if any)
        secondary_authors = tokens[4:]


        query = { "manuscriptID": manuscriptID,
                  "authorID": authorID,
                  "editorID": editor_id,
                  "title": title,
                  "status": "underReview",
                  "ricodeID": RICode,
                  "numPages": None,
                  "startingPage": None,
                  "issueOrder": None,
                  "dateReceived": "2014-03-21",
                  "dateSentForReview": None,
                  "dateAccepted": None,
                  "issue_publicationYear": None,
                  "issue_periodNumber": None,
                  "secondaryAuthor": secondary_authors
              }

        insert(db, "manuscript", query)

        query_select = { "personID": authorID }
        query = { "affiliation": affiliation }
        update(db, "person", query_select, query)

        print("Submitted and updated:\n"
              "  Manuscript ID is " + str(manuscript_id) + "\n"
              "  Manuscript SUBMITTED on " + now.strftime("%Y-%m-%d") + " \n")


    # immediately remove manuscript, regardless of status
    elif command == 'retract':
        manuscriptID = int(tokens[1])

        # ensure that author can only retract his/her own manuscripts
        query = { "manuscriptID": manuscriptID, "authorID": authorID }
        result = find_one(db, "manuscript", person)

        if not result:
            print("Sorry, you are not the author of this manuscript.")
            return

        s = raw_input('Are you sure? (y/n): ')
        if s.lower() == 'y':
            query = "DELETE FROM manuscript WHERE manuscriptID = " + str(manuscript_num) + ';'
            change_query(db, query)

            query = "DELETE FROM feedback WHERE manuscriptID = " + str(manuscript_num) + ';'
            change_query(db, query)

            print("Manuscript {} has been deleted".format(manuscript_num))

        else:
            print("No action taken.")

    else:
        print("ERROR: Invalid input. Command '" + command + "' not recognized.")



def process_editor(db, tokens):
    command = tokens[0]

    now    = datetime.datetime.now()
    cursor = db.get_cursor()

    if command == 'status':
        status_editor(db, db.get_user_id())

    elif command == 'assign' and len(tokens) == 3:
        manuscriptID = tokens[1]
        reviewer_id = tokens[2]

        # check to make sure that RICode matches
        getManuscriptRICode = "SELECT ricodeID FROM manuscript WHERE manuscriptID = " + str(manuscriptID) + ';'
        manuscriptRICode    = get_single_query(db, getManuscriptRICode)

        getReviewerRICodes  = "SELECT RICode_RICodeID  from reviewer_has_RICode WHERE reviewer_personID = " + str(reviewer_id) + ';'
        cursor.execute(getReviewerRICodes)

        reviewerRICodes = []

        for row in cursor:
            for col in row:
                if col > 0:
                    reviewerRICodes.append(col)

        if manuscriptRICode in reviewerRICodes:

            getDate = "SELECT dateReceived FROM manuscript WHERE manuscriptID = " + str(manuscript_num) + ';'

            date = get_single_query(db, getDate)

            add_feedback = ("INSERT INTO feedback "
                            "(manuscriptID,reviewer_personID,appropriateness,clarity,methodology,"
                            "contribution,recommendation,dateReceived) VALUES "
                            "(%(manuscriptID)s, %(reviewer_personID)s, NULL, NULL, NULL, NULL, NULL, %(dateReceived)s)")

            data_feedback = {
                'manuscriptID': manuscriptID,
                'reviewer_personID': reviewer_id,
                'dateReceived': date,
            }

            insert_query(db, add_feedback, data_feedback)

            query = "UPDATE manuscript SET `status` = 'underReview', dateSentForReview = NOW() WHERE manuscriptID = " + str(manuscript_num) + ';'
            change_query(db, query)
            # date received?
            # insert_feedback = ""
            print("Manuscript ID {} assigned to reviewer {}. Manuscript status set to 'underReview'.".format(manuscript_num, reviewer_id))
        else:
            print("ERROR: Invalid entry. This reviewer does not have the appropriate RICode.")

    elif command == 'reject' and len(tokens) == 2:
        manuscript_num  = tokens[1]
        query = "UPDATE manuscript SET `status` = 'rejected' WHERE manuscriptID = " + str(manuscript_num) + ';'
        change_query(db, query)
        print("Manuscript {} rejected on {}").format(manuscript_num, now.strftime("%Y-%m-%d"))

    elif command == 'accept' and len(tokens) == 2:
        manuscript_num  = tokens[1]
        query = "UPDATE manuscript SET `status` = 'accepted', dateAccepted = NOW() WHERE manuscriptID = " + str(manuscript_num) + ';'
        change_query(db, query)
        print("Manuscript {} accepted on {}").format(manuscript_num, now.strftime("%Y-%m-%d"))

    elif command == 'typeset' and len(tokens) == 3:
        manuscript_num = tokens[1]
        pp             = tokens[2]

        query = "UPDATE manuscript SET `status` = 'typeset', numPages = {} WHERE manuscriptID = {};".format(pp, manuscript_num)
        change_query(db, query)
        print("Manuscript {} status set to 'typeset' on {}. {} pages logged").format(manuscript_num, now.strftime("%Y-%m-%d"), pp)

    elif command == 'schedule' and len(tokens) == 4:
        manuscript_num = tokens[1]
        issueYear      = tokens[2]
        issuePeriod    = tokens[3]

        getNumPages = "SELECT numPages FROM manuscript WHERE issue_publicationYear = {} AND issue_periodNumber = {};".format(issueYear, issuePeriod)
        cursor.execute(getNumPages)

        page_sum = 0

        for row in cursor:
            for col in row:
                if col > 0:
                    page_sum += int(col)

        getNumManuscriptPage = "SELECT numPages FROM manuscript WHERE manuscriptID = {}".format(manuscript_num)
        page = get_single_query(db, getNumManuscriptPage)

        # ensure that we do not exceed 100 pages per issue
        if page and (page + page_sum <= 100):
            query = "UPDATE manuscript SET status = 'scheduled', issue_publicationYear = {}, issue_periodNumber = {} WHERE manuscriptID = {};".format(issueYear, issuePeriod, manuscript_num)
            change_query(db, query)

            print("Manuscript {} scheduled for issue year {}, period {}").format(manuscript_num, issueYear, issuePeriod)
        else:
            print("ERROR: Invalid entry. Check if manuscript {} has a valid number of pages or number of pages in issue does not have any errors.".format(manuscript_num))


    elif command == 'publish' and len(tokens) == 3:
        issueYear   = tokens[1]
        issuePeriod = tokens[2]

        query = "UPDATE manuscript SET status = 'published' WHERE issue_publicationYear = {} AND issue_periodNumber = {};".format(issueYear, issuePeriod)
        change_query(db, query)

        query = "UPDATE issue SET datePrinted = NOW() WHERE publicationYear = {} AND periodNumber = {};".format(issueYear, issuePeriod)
        change_query(db, query)

        print("Issue year {}, period {} printed on {}. Status of all corresponding manuscripts changed to 'published'").format(issueYear, issuePeriod, now.strftime("%Y-%m-%d"))

    else:
        print("ERROR: Invalid input. Command '" + command + "' not recognized, or corresponding arguments are not correct")



def submit_feedback(db, manuscript_num, appropriateness, clarity, methodology, contribution, recommendation, new_status):

    cursor = db.get_cursor()

    getManuscripts = "SELECT manuscriptID from manuscriptWReviewers WHERE reviewer_personID = " + str(db.get_user_id()) + ';'
    cursor.execute(getManuscripts)

    manuscripts = []

    for row in cursor:
        for col in row:
            if col > 0:
                manuscripts.append(int(col))

    getManuscriptStatus  = "SELECT `status` from manuscript WHERE manuscriptID = " + str(manuscript_num) + ';'
    check_status = get_single_query(db, getManuscriptStatus)

    if (int(manuscript_num) in manuscripts) and (check_status == "underReview"):
        getDate = "SELECT dateReceived FROM manuscript WHERE manuscriptID = " + str(manuscript_num) + ';'
        date = get_single_query(db, getDate)

        update_feedback = ("UPDATE feedback "
                           "SET appropriateness = %(appropriateness)s, "
                           "clarity = %(clarity)s, "
                           "methodology = %(methodology)s, "
                           "contribution = %(contribution)s, "
                           "recommendation = %(recommendation)s, "
                           "dateReceived = %(dateReceived)s"
                           "WHERE manuscriptID = %(manuscriptID)s AND reviewer_personID = %(reviewer_personID)s")

        data_feedback = {
            'appropriateness': appropriateness,
            'clarity': clarity,
            'methodology': methodology,
            'contribution': contribution,
            'recommendation': recommendation,
            'dateReceived': date,
            'manuscriptID': manuscript_num,
            'reviewer_personID': db.get_user_id()
        }

        insert_query(db, update_feedback, data_feedback)

        if new_status == "rejected":
            print("rejected")
            query = "UPDATE manuscript SET `status` = 'rejected' WHERE manuscriptID = {};".format(manuscript_num)
        elif new_status == "accepted":
            print("accepted")
            query = "UPDATE manuscript SET `status` = 'accepted', dateAccepted = NOW() WHERE manuscriptID = {};".format(manuscript_num)

        change_query(db, query)

        print("Feedback for manuscript {} recorded. Status set to {}").format(manuscript_num, new_status)

    else:
        print("User cannot review this manuscript at this time.")



def process_reviewer(db, tokens):
    command = tokens[0]

    if command == 'status' and len(tokens) == 1:
        status_reviewer(db, db.get_user_id())

    elif command == 'resign' and len(tokens) == 1:
        # prompt to enter unique ID
        s = raw_input('Please enter your user ID to confirm: ')
        if s == str(db.get_user_id()):
            # UPDATE reviewer SET reviewer_status = "resigned" WHERE personID = 416;
            query = "UPDATE reviewer SET reviewer_status = 'resigned' WHERE personID = " + str(db.get_user_id()) + ';'
            change_query(db, query)

            print("Thank you for your service!")

            db.log_off()

        else:
            print("No action taken. User ID does not match.")

    elif command == 'reject':
        manuscript_num  = tokens[1]
        appropriateness = tokens[2]
        clarity         = tokens[3]
        methodology     = tokens[4]
        contribution    = tokens[5]
        recommendation  = tokens[6]

        submit_feedback(db, manuscript_num, appropriateness, clarity, methodology, contribution, recommendation, 'rejected')

    elif command == 'accept':
        manuscript_num  = tokens[1]
        appropriateness = tokens[2]
        clarity         = tokens[3]
        methodology     = tokens[4]
        contribution    = tokens[5]
        recommendation  = tokens[6]

        submit_feedback(db, manuscript_num, appropriateness, clarity, methodology, contribution, recommendation, 'accepted')

    else:
        print("ERROR: Invalid input. Command '" + command + "' not recognized or arguments are not appropriate.")


def status_query_return(db, query):
    cursor = db.get_cursor()
    cursor.execute(query)

    # display results
    for row in cursor:
        for col in row:
            if col > 0:
                return col

    return 0


def status_author(db, author_id):
    # query = "SELECT count FROM authorNumSubmitted WHERE personID = " +  str(author_id) + ';'
    # print("{} manuscripts submitted".format(status_query_return(db, query)))
    #
    # query = "SELECT count FROM authorNumUnderReview WHERE personID = " +  str(author_id) + ';'
    # print("{} manuscripts under review".format(status_query_return(db, query)))
    #
    # query = "SELECT count FROM authorNumRejected WHERE personID = " +  str(author_id) + ';'
    # print("{} manuscripts rejected".format(status_query_return(db, query)))
    #
    # query = "SELECT count FROM authorNumAccepted WHERE personID = " +  str(author_id) + ';'
    # print("{} manuscripts accepted".format(status_query_return(db, query)))
    #
    # query = "SELECT count FROM authorNumTypeset WHERE personID = " +  str(author_id) + ';'
    # print("{} manuscripts typeset".format(status_query_return(db, query)))
    #
    # query = "SELECT count FROM authorNumScheduled WHERE personID = " +  str(author_id) + ';'
    # print("{} manuscripts scheduled".format(status_query_return(db, query)))
    #
    # query = "SELECT count FROM authorNumPublished WHERE personID = " +  str(author_id) + ';'
    # print("{} manuscripts published\n".format(status_query_return(db, query)))

    query = { "authorID": author_id }

    display_manuscripts(db, query)


def status_editor(db, editor_id):
    query = { "editorID": editor_id }

    display_manuscripts(db, query)


def status_reviewer(db, reviewer_id):
    query = { "reviewerID": reviewerID }

    display_manuscripts(db, query)


def display_manuscripts(db, query):
    result = find(db, "manuscript", query)

    if result:
        print("Manuscript detail: ")
        for row in result:
            status       = row.get("status")
            manuscriptID = row.get("manuscriptID")
            title        = row.get("title")
            print("   ID {} -- status: {}: '{}' ".format(manuscriptID, status, title))
    else:
        print("You have no manuscripts at this time.")
