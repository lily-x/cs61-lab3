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


def delete(db, collection, query):
    client = db.get_client()

    result = client[collection].delete_many( query )

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

        s = input('Are you sure? (y/n): ')
        if s.lower() == 'y':
            query = { "manuscriptID": manuscriptID }

            # remove from manuscript and feedback tables
            result = delete(db, "manuscript", query)
            result = delete(db, "feedback", query)

            print("Manuscript {} has been deleted".format(manuscriptID))

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
        reviewerID = tokens[2]

        # check to make sure that reviewer has a corresponding RICode
        query    = { "manuscriptID": manuscriptID }
        result   = find_one(db, "manuscript", query)
        m_RICode = result.get("ricodeID")

        query     = { "personID": reviewerID }
        result    = find_one(db, "person", query)
        r_RICodes = result.get("ricodeID")

        # reviewer does have a corresponding RICode
        if m_RIcode in r_RICodes:
            query = { 
                        "manuscriptID": manuscriptID,
                        "reviewerID": reviewerID,
                        "appropriateness": None,
                        "clarity": None,
                        "methodology": None,
                        "contribution": None,
                        "recommendation": None,
                        "dateReceived": None 
                    }

            insert(db, "feedback", query)

            select = { "manuscriptID": manuscriptID }
            query  = { "status": "underReview" }

            update(db, "manuscript", select, query)

            print("Manuscript ID {} assigned to reviewer {}. Manuscript status set to 'underReview'.".format(manuscriptID, reviewerID))
        
        # reviewer does not have a corresponding RICode
        else:
            print("ERROR: Invalid entry. This reviewer does not have the appropriate RICode.")

    elif command == 'reject' and len(tokens) == 2:
        manuscriptID = tokens[1]
        
        select = { "manuscriptID": manuscriptID }
        query  = { "status": "rejected" }
        
        update(db, "manuscript", select, query)

        print("Manuscript {} rejected on {}").format(manuscriptID, now.strftime("%Y-%m-%d"))

    elif command == 'accept' and len(tokens) == 2:
        manuscriptID = tokens[1]

        select = { "manuscriptID": manuscriptID }
        query  = { "status": "accepted", "dateAccepted": datetime.datetime.now().date() }

        update(db, "manuscript", select, query)

        print("Manuscript {} accepted on {}").format(manuscriptID, now.strftime("%Y-%m-%d"))

    elif command == 'typeset' and len(tokens) == 3:
        manuscriptID = tokens[1]
        pp           = int(tokens[2])

        select = { "manuscriptID": manuscriptID }
        query  = { "status": "typeset", "numPages": pp }

        update(db, "manuscript", select, query)

        print("Manuscript {} status set to 'typeset' on {}. {} pages logged").format(manuscriptID, now.strftime("%Y-%m-%d"), pp)

    elif command == 'schedule' and len(tokens) == 4:
        manuscriptID = tokens[1]
        issueYear    = int(tokens[2])
        issuePeriod  = int(tokens[3])

        query = { "issue_publicationYear": issueYear, "issue_periodNumber": issuePeriod }

        cursor = find(db, "manuscript", query)

        page_sum = 0
        for row in cursor:
            page_sum += int(row)


        query = { "manuscriptID": manuscriptID }
        result = find_one(db, "manuscript", query)

        page = int(result.get("numPages"))

        # manuscript has no listed page count
        if not page:
            print("ERROR: Manuscript {} has not yet been typeset.").format(manuscriptID)
        # ensure that we do not exceed 100 pages per issue
        elif page + page_sum > 100:
            print("ERROR: Invalid entry. Publication would exceed 100 page limit with manuscript {}.".format(manuscriptID))
        # successfully schedule manuscript
        else:
            select = { "manuscriptID": manuscriptID }
            query = { "status": "scheduled", "issue_publicationYear": issueYear, "issue_periodNumber": issuePeriod }

            update(db, "manuscript", select, query)

            print("Manuscript {} scheduled for issue year {}, period {}").format(manuscriptID, issueYear, issuePeriod)


    elif command == 'publish' and len(tokens) == 3:
        issueYear   = int(tokens[1])
        issuePeriod = int(tokens[2])

        # update manuscripts in issue to 'published'
        select = { "issue_publicationYear": issueYear, "issue_periodNumber": issuePeriod }
        query  = { "status": "published" }

        update(db, "manuscript", select, query)

        # update issue
        select = { "publicationYear": issueYear, "periodNumber": issuePeriod }
        query  = { "datePrinted": datetime.datetime.now().date() }
        
        update(db, "issue", select, query)

        print("Issue year {}, period {} printed on {}. Status of all corresponding manuscripts changed to 'published'.").format(issueYear, issuePeriod, now.strftime("%Y-%m-%d"))

    else:
        print("ERROR: Invalid input. Command '" + command + "' not recognized, or corresponding arguments are not correct.")



def submit_feedback(db, manuscriptID, appropriateness, clarity, methodology, contribution, recommendation, new_status = None):

    manuscriptID = int(manuscriptID)
    reviewerID = int(db.get_user_id)

    # find all manuscripts associated with current reviewer
    query  = { "reviewerID": reviewerID }
    cursor = find(db, "feedback", query)

    manuscripts = []

    for row in cursor:
        manuscriptID = row.get("manuscriptID")
        manuscripts.append(int(manuscriptID))


    # find status of requested manuscript
    query  = { "manuscriptID": manuscriptID }
    result = find_one(db, "manuscript", query)

    check_status = result.get("status")


    # manuscript does not exist, feedback does not exist, or reviewer not listed on feedback
    if int(manuscriptID) not in manuscripts:
        print("You are not listed as a reviewer for manuscript {}.").format(manuscriptID)

    # manuscript not under review
    elif check_status != "underReview":
        print("You cannot review manuscript {} at this time.").format(manuscriptID)

    # feedback successfully submitted
    else: 
        query = {
            "manuscriptID": manuscriptID,
            "reviewerID": reviewerID,
            "appropriateness": int(appropriateness),
            "clarity": int(clarity),
            "methodology": int(methodology),
            "contribution": int(contribution),
            "recommendation": recommendation,
            "dateReceived": datetime.datetime.now().date()
        }

        update(db, "feedback", query)

        print("Feedback for manuscript {} recorded.").format(manuscriptID)

        if new_status == "rejected":
            select = { "manuscriptID": manuscriptID }
            query  = { "status": "rejected" }
            update(db, "manuscript", select, query)

            print("Manuscript {} rejected.").format(manuscriptID)

        elif new_status == "accepted":
            select = { "manuscriptID": manuscriptID }
            query  = { "status": "accepted" }
            update(db, "manuscript", select, query)

            print("Manuscript {} accepted.").format(manuscriptID)




def process_reviewer(db, tokens):
    command = tokens[0]

    reviewerID = int(db.get_user_id())

    if command == 'status' and len(tokens) == 1:
        status_reviewer(db, db.get_user_id())

    elif command == 'resign' and len(tokens) == 1:
        # prompt to enter unique ID
        s = input('Please enter your user ID to confirm: ')
        if s == str(reviewerID):
            select = { "personID": reviewerID }
            query = { "status": "resigned" }

            update(db, "person", select query)

            print("Thank you for your service!")

            db.log_off()

        else:
            print("No action taken. User ID does not match.")

    elif command == 'reject':
        manuscriptID  = tokens[1]
        appropriateness = tokens[2]
        clarity         = tokens[3]
        methodology     = tokens[4]
        contribution    = tokens[5]
        recommendation  = tokens[6]

        submit_feedback(db, manuscriptID, appropriateness, clarity, methodology, contribution, recommendation, 'rejected')

    elif command == 'accept':
        manuscriptID  = tokens[1]
        appropriateness = tokens[2]
        clarity         = tokens[3]
        methodology     = tokens[4]
        contribution    = tokens[5]
        recommendation  = tokens[6]

        submit_feedback(db, manuscriptID, appropriateness, clarity, methodology, contribution, recommendation, 'accepted')

    else:
        print("ERROR: Invalid input. Command '" + command + "' not recognized or arguments are not appropriate.")


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


def status_reviewer(db, reviewerID):
    query = { "reviewerID": reviewerID }

    # TODO: fix this because right now no good way to link reviewer and manuscript
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
