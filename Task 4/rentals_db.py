from sqlite3 import dbapi2 as pysqlite

def __resetdb():
    '''
    __resetdb() --> NONE
    Resets the database to default settings
    '''
    
    conn = pysqlite.connect('rentals.db')
    conn.text_factory = str
    
    cur = conn.cursor()


    # exception handling
    try:
        cur.execute('CREATE TABLE Movies (Title TEXT, Genre TEXT, Director TEXT, Running_Time INTEGER, Movie_Id INTEGER, Review_Rating REAL, Inventory INTEGER, PRIMARY KEY(Movie_Id))')
        cur.execute('CREATE TABLE Customer (Name TEXT, Account_Number INTEGER, Password INTEGER, Account_Balance REAL, PRIMARY KEY(Account_Number))')
        cur.execute('CREATE TABLE Transactions (Trans_Id INTEGER, Movie_Id INTEGER, Account_Number INTEGER, Rent_DropOff TEXT, PRIMARY KEY (Trans_Id))')
    
    except pysqlite.OperationalError:       
        cur.execute('DROP TABLE Movies')
        cur.execute('CREATE TABLE Movies (Title TEXT, Genre TEXT, Director TEXT, Running_Time INTEGER, Movie_ID INTEGER, Review_Rating REAL, Inventory INTEGER, PRIMARY KEY(Movie_Id))')
        
        cur.execute('DROP TABLE Customer')
        cur.execute('CREATE TABLE Customer (Name TEXT, Account_Number INTEGER, Password INTEGER, Account_Balance REAL, PRIMARY KEY(Account_Number))')
        
        cur.execute('DROP TABLE Transactions')
        cur.execute('CREATE TABLE Transactions (Trans_Id INTEGER, Movie_Id INTEGER, Account_Number INTEGER, Rent_DropOff TEXT, PRIMARY KEY (Trans_Id))')
    
    # inserting movies
    cur.execute('INSERT INTO Movies VALUES("Fight Club", "Drama", "David Fincher", 139, 1, 8.8, 5)')
    cur.execute('INSERT INTO Movies VALUES("Pulp Fiction", "Drama", "Quentin Tarantino", 154, 2, 9.0, 7)')
    cur.execute('INSERT INTO Movies VALUES("Robin Hood", "Drama", "Ridley Scott", 140, 3, 6.8, 3)')
    
    cur.execute('INSERT INTO Movies VALUES("The Book of Eli", "Drama", "Albert Hughes and Allen Hughest", 118, 4, 6.8, 4)')
    cur.execute('INSERT INTO Movies VALUES("Wall Street: Money Never Sleeps", "Drama", "Oliver Stone", 133, 5, 6.3, 4)')
    cur.execute('INSERT INTO Movies VALUES("Inception", "Action", "Christopher Nolan", 148, 6, 8.9, 5)')
    
    cur.execute('INSERT INTO Movies VALUES("The Mechanic", "Action", "Simon West", 93, 7, 6.5, 2)')
    cur.execute('INSERT INTO Movies VALUES("The Dark Knight", "Action", "Christopher Nolan", 152, 8, 8.9, 6)')
    cur.execute('INSERT INTO Movies VALUES("Red", "Action", "Robert Schwentke", 111, 9, 7.1, 8)')
    
    cur.execute('INSERT INTO Movies VALUES("Machete", "Action", "Ethan Maniquis and Robert Rodriguez", 105, 10, 7.1, 1)')
    cur.execute('INSERT INTO Movies VALUES("The Hangover", "Comedy", "Todd Phillips", 100, 11, 7.9, 4)')
    cur.execute('INSERT INTO Movies VALUES("Hot Tub Time Machine", "Comedy", "Steve Pink", 101, 12, 6.6, 2)')
    
    cur.execute('INSERT INTO Movies VALUES("Hall Pass", "Comedy", "Bobby Farrelly and Peter Farrelly", 105, 13, 6.1, 6)')
    cur.execute('INSERT INTO Movies VALUES("Life as We Know It", "Comedy", "Greg Berlanti", 114, 14, 6.2, 3)')
    cur.execute('INSERT INTO Movies VALUES("The Other Guys", "Comedy", "Adam McKay", 107, 15, 6.6, 9)')
    
    cur.execute('INSERT INTO Movies VALUES("300", "War", "Zack Snyder", 117, 16, 7.8, 5)')
    cur.execute('INSERT INTO Movies VALUES("Saving Private Ryan", "War", "Steven Spielberg", 169, 17, 8.5, 7)')
    cur.execute('INSERT INTO Movies VALUES("Schindler List", "War", "Steven Spielberg", 195, 18, 8.9, 3)')
    
    cur.execute('INSERT INTO Movies VALUES("The Hurt Locker", "War", "Kathryn Bigelow", 131, 19, 7.8, 4)')
    cur.execute('INSERT INTO Movies VALUES("Full Metal Jacket", "War", "Stanley Kubrick", 116, 20, 8.4, 3)')
    cur.execute('INSERT INTO Movies VALUES("Harry Potter and the Deathly Hallows: Part 1", "Adventure", "David Yates", 146, 21, 7.8, 5)')
    
    cur.execute('INSERT INTO Movies VALUES("The Expendables", "Adventure", "Sylvester Stallone", 103, 22, 6.7, 2)')
    cur.execute('INSERT INTO Movies VALUES("Prince of Persia: The Sands of Time", "Adventure", "Mike Newell", 116, 23, 6.7, 6)')
    cur.execute('INSERT INTO Movies VALUES("Sherlock Holmes", "Adventure", "Guy Ritchie", 128, 24, 7.5, 8)')
    
    cur.execute('INSERT INTO Movies VALUES("The A-Team", "Adventure", "Joe Carnahan", 117, 25, 7.0, 1)')
    cur.execute('INSERT INTO Movies VALUES("The Town", "Crime", "Ben Affleck", 125, 26, 7.7, 4)')
    cur.execute('INSERT INTO Movies VALUES("Faster", "Crime", "George Tillman Jr.", 98, 27, 6.5, 2)')
    
    cur.execute('INSERT INTO Movies VALUES("The Departed", "Crime", "Martin Scorsese", 151, 28, 8.5, 6)')
    cur.execute('INSERT INTO Movies VALUES("Takers", "Crime", "John Luessenhop", 107, 29, 5.8, 3)')
    cur.execute('INSERT INTO Movies VALUES("Salt", "Crime", "Phillip Noyce", 100, 30, 6.5, 5)')

    # inserting customers
    cur.execute('INSERT INTO Customer VALUES("Robin Gerok", 18239, 3009, 12.67)')
    cur.execute('INSERT INTO Customer VALUES("Micheale Hinkhe", 19339, 2135, 15.02)')
    cur.execute('INSERT INTO Customer VALUES("Desir Shawnalke", 17235, 5689, 6.66)')
    
    cur.execute('INSERT INTO Customer VALUES("Regan Foxx", 23598, 6369, 18.50)')
    cur.execute('INSERT INTO Customer VALUES("Pitse Gerkop", 35632, 5429, 1.90)')
    cur.execute('INSERT INTO Customer VALUES("Sandy Feire", 78963, 3531, 71.35)')
    
    cur.execute('INSERT INTO Customer VALUES("Bob Anders", 26562, 0256, 11.38)')
    cur.execute('INSERT INTO Customer VALUES("Robert Wij", 78556, 9325, 19.99)')
    cur.execute('INSERT INTO Customer VALUES("Sert Mickel", 93631, 7412, 14.57)')
    
    cur.execute('INSERT INTO Customer VALUES("Fred Wilco", 45789, 2359, 65.38)')
    cur.execute('INSERT INTO Customer VALUES("Jerry Spice", 86532, 7896, 23.99)')
    cur.execute('INSERT INTO Customer VALUES("Sandy McDonald", 54856, 1235, 2.57)')
    
    #inserting transactions
    cur.execute('INSERT INTO Transactions VALUES(1, 1, 18239, "Rented")')
    cur.execute('INSERT INTO Transactions VALUES(2, 30, 19339, "Rented")')
    cur.execute('INSERT INTO Transactions VALUES(3, 2, 17235, "Rented")')
    
    cur.execute('INSERT INTO Transactions VALUES(4, 6, 23598, "Rented")')
    cur.execute('INSERT INTO Transactions VALUES(19, 1, 18239, "Returned")')
    cur.execute('INSERT INTO Transactions VALUES(5, 4, 35632, "Rented")')
    
    cur.execute('INSERT INTO Transactions VALUES(6, 15, 78963, "Rented")')    
    cur.execute('INSERT INTO Transactions VALUES(7, 3, 26562, "Rented")')
    cur.execute('INSERT INTO Transactions VALUES(8, 8, 78556, "Rented")')
    
    cur.execute('INSERT INTO Transactions VALUES(9, 27, 93631, "Rented")')
    cur.execute('INSERT INTO Transactions VALUES(20, 4, 35632, "Returned")')
    cur.execute('INSERT INTO Transactions VALUES(21, 8, 78556, "Returned")')
    
    cur.execute('INSERT INTO Transactions VALUES(10, 25, 45789, "Rented")')
    cur.execute('INSERT INTO Transactions VALUES(11, 19, 86532, "Rented")')
    cur.execute('INSERT INTO Transactions VALUES(12, 29, 54856, "Rented")')
    
    cur.execute('INSERT INTO Transactions VALUES(13, 6, 26562, "Returned")')
    cur.execute('INSERT INTO Transactions VALUES(14, 9, 78556, "Rented")')
    cur.execute('INSERT INTO Transactions VALUES(15, 30, 93631, "Rented")')
    
    cur.execute('INSERT INTO Transactions VALUES(16, 20, 78963, "Rented")')
    cur.execute('INSERT INTO Transactions VALUES(17, 30, 35632, "Rented")')
    cur.execute('INSERT INTO Transactions VALUES(18, 5, 35632, "Rented")')
    
    cur.execute('INSERT INTO Transactions VALUES(22, 9, 78556, "Returned")')
    cur.execute('INSERT INTO Transactions VALUES(23, 15, 78963, "Returned")')
    cur.execute('INSERT INTO Transactions VALUES(24, 29, 54856, "Returned")')
    
    conn.commit()
    conn.close()
    
    return


def table_output_format(table):
    '''
    table_output_format(list) --> str
    Returns a nice string format for the list
    '''
    num_of_fields = len(table[0])
    fld_max_len = [1]
    
    for e in range(num_of_fields -1 ):
        fld_max_len += [1]             # creates a dummy placeholder for the max lengths of the strings
    
    for record in table:
        fl_no = -1
        
        for field in record:
            fl_no += 1
            
            if len(str(field)) > abs(fld_max_len[fl_no]):
                fld_max_len[fl_no] = fld_max_len[fl_no] / abs(fld_max_len[fl_no]) * len(str(field)) 
            
            if not str(field).isdigit() and fld_max_len[fl_no] > 0:
                fld_max_len[fl_no] = - fld_max_len[fl_no]     

    returned_format="%" + str(fld_max_len[0]) + "s"
    
    for fl_no in range(1, num_of_fields):
        returned_format += " %" + str(fld_max_len[fl_no]) + "s"        # formats the str
        
    return returned_format


start_menu = int(raw_input("\n\
1. Reset database\n\
2. Insert a movie\n\
3. Insert a customer\n\
4. Movie names with ratings above average\n\
5. Top 10 value customer\n\
6. Top risky customers\n\
7. Rented Movies\n\
8. Search by Title, Director or Genre\n\
9. Custom query\n\
10. Quit\n\
\n\
Please select your choice, number only?: "))

__resetdb()

while start_menu < 10:
    if start_menu == 1:
        #reset database
        __resetdb()

    elif start_menu == 2:
        #insert a movie
        
        conn = pysqlite.connect('rentals.db')
        conn.text_factory = str
    
        cur = conn.cursor()
        
        title = str(raw_input("Name of movie?: "))
        genre = str(raw_input("Type of genre?: "))
        director = str(raw_input("Name of director(s)?: "))
        
        mins = int(raw_input("How long is the movie (in mins)?: "))
        movie_id = int(raw_input("Enter movie id (> 30)?: "))
        
        rating = float(raw_input("What is the rating out of 10?: "))
        copies = int(raw_input("How many copies are there?: "))
                
        cur.execute('INSERT INTO Movies VALUES("%s", "%s", "%s", %i, %i, %f, %i)' %(title, genre, director, mins, movie_id, rating, copies))
        
        conn.commit()       
        conn.close()
        
    elif start_menu == 3:
        #insert a customer
        
        conn = pysqlite.connect('rentals.db')
        conn.text_factory = str
    
        cur = conn.cursor()
        
        name = str(raw_input("Name of customer?: "))
        account_num = int(raw_input("Account number (5-digit)?: "))
        
        password = int(raw_input("Password (4-digit)?: "))
        balance = float(raw_input("How much money in the account?: "))
        
        cur.execute('INSERT INTO Customer VALUES("%s", %i, %i, %f)' %(name, account_num, password, balance))
        
        conn.commit()
        conn.close()
    
    elif start_menu == 4:
        #Q1 how many movies have a rating higher than the avg rating
        conn = pysqlite.connect('rentals.db')
        conn.text_factory = str
    
        cur = conn.cursor()

        cur.execute('SELECT Title, Review_Rating       \
                     FROM MOVIES                       \
                     WHERE (                           \
                            SELECT AVG (Review_Rating) \
                            FROM MOVIES                \
                             ) < Review_Rating         \
                    ')


        records = cur.fetchall()
        
        print "\n"
            
        print table_output_format(records) %("Title", "R_R")

        for record in records:
            print table_output_format(records) %(record)
        
    
    elif start_menu == 5:
        #Q2 Top 10 value customer
        conn = pysqlite.connect('rentals.db')
        conn.text_factory = str
    
        cur = conn.cursor()
        
        cur.execute('SELECT COUNT(*), T.Account_Number, C.Name       \
                     FROM Transactions T                             \
                     JOIN Customer C                                 \
                     WHERE Rent_DropOff = "Rented"                   \
                       AND C.Account_Number = T.Account_Number       \
                     GROUP BY T.Account_Number                       \
                     ORDER BY 1 DESC                                 \
                     LIMIT 10                                        \
                     ')
        
        
        records = cur.fetchall()
        
        print "\n"
            
        print table_output_format(records) %("C", "Ac_No", "Name")

        for record in records:
            print table_output_format(records) %(record)
    
    elif start_menu == 6:
        #Q3 Top risky customers
        conn = pysqlite.connect('rentals.db')
        conn.text_factory = str
    
        cur = conn.cursor()
        
        cur.execute('                                                     \
                     SELECT COUNT (*) CO, C.Account_Number, C.Name        \
                     FROM Transactions L                                  \
                     JOIN Customer C                                      \
                     WHERE L.Rent_DropOff = "Rented"                      \
                     And NOT EXISTS (                                     \
                           SELECT * FROM Transactions R                   \
                           WHERE R.Rent_DropOff = "Returned"              \
                             AND R.Movie_Id = L.Movie_ID                  \
                             AND L.Account_Number = R.Account_Number      \
                                     )                                    \
                       AND C.Account_Number = L.Account_Number            \
                       GROUP BY C.Account_Number                          \
                       ORDER BY 1 DESC                                    \
                       LIMIT 10                                           \
                    ')
        
        records = cur.fetchall()
        
        print "\n"
            
        print table_output_format(records) %("C", "Ac_No", "Name")

        for record in records:
            print table_output_format(records) %(record)
            
    elif start_menu == 7:
        #Q4 find all the Movies that have been rented but not returned
        conn = pysqlite.connect('rentals.db')
        conn.text_factory = str
    
        cur = conn.cursor()
       
        cur.execute('                                                     \
                     SELECT C.Name, C.Account_Number, M.Movie_Id, M.Title \
                     FROM Transactions L                                  \
                     JOIN Customer C                                      \
                     JOIN Movies M                                        \
                     WHERE L.Rent_DropOff = "Rented"                      \
                     And NOT EXISTS (                                     \
                           SELECT * FROM Transactions R                   \
                           WHERE R.Rent_DropOff = "Returned"              \
                             AND R.Movie_Id = L.Movie_ID                  \
                             AND L.Account_Number = R.Account_Number      \
                                       )                                  \
                       AND C.Account_Number = L.Account_Number            \
                       AND M.Movie_Id = L.Movie_Id                        \
                    ')
          
        records = cur.fetchall()
        
        print "\n"
            
        print table_output_format(records) %("Name", "Ac_No", "M", "Title")
            
        for record in records:
            print table_output_format(records) %(record)
        
    
    elif start_menu == 8:
        #Q5 browsing queries
        conn = pysqlite.connect('rentals.db')
        conn.text_factory = str
    
        cur = conn.cursor()
        
        search = int(raw_input("Search by:\n1. Director\n2. Genre\n3. Title\nNumber only: "))
        
        
        if search == 1:
            name = raw_input("Enter name: ")
            
            cur.execute('SELECT Title, Genre,Director, Movie_ID, Review_Rating, Inventory \
                         FROM MOVIES                                                      \
                         WHERE Director                                                   \
                           LIKE "%%%s%%"' %(name))
            
            records = cur.fetchall()
            
            print "\n"
            
            print table_output_format(records) %("Title", "Genre", "Director", "M", "R_R", "I")

            for record in records:
                print table_output_format(records) %(record)
          
                
        elif search == 2:
            genre = raw_input("Enter type of genre: ")
            
            cur.execute('SELECT Title, Genre,  Director, Movie_ID, Review_Rating, Inventory \
                         FROM MOVIES                                                        \
                         WHERE Genre                                                        \
                           LIKE "%%%s%%"' %(genre))
            
            records = cur.fetchall()
            
            print "\n"
            
            print table_output_format(records) %("Title", "Genre", "Director", "M", "R_R", "I")

            for record in records:
                print table_output_format(records) %(record)
        
                
        elif search == 3:
            title = raw_input("Enter title: ")
            
            cur.execute('SELECT Title, Genre,  Director, Movie_ID, Review_Rating, Inventory \
                         FROM MOVIES                                                        \
                         WHERE Title                                                        \
                           LIKE "%%%s%%"' %(title))
            
            records = cur.fetchall()
            
            print "\n"
            
            print table_output_format(records) %("Title", "Genre", "Director", "M", "R_R", "I")
            
            for record in records:
                print table_output_format(records) %(record)
        
    
    elif start_menu == 9:
        #Custom Q
        conn = pysqlite.connect('rentals.db')
        conn.text_factory = str
    
        cur = conn.cursor()
        
        cur.execute(str(raw_input("Enter SQL command line: ")))
        
        conn.commit()
        conn.close()
            
    
    start_menu = int(raw_input("\n\
1. Reset database\n\
2. Insert a movie\n\
3. Insert a customer\n\
4. Movie names with ratings above average\n\
5. Top 10 value customer\n\
6. Top risky customers\n\
7. Rented Movies\n\
8. Search by Title, Director or Genre\n\
9. Custom query\n\
10. Quit\n\
\n\
Please select your choice, number only?: "))
