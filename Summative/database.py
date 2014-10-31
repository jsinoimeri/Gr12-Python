from sqlite3 import dbapi2 as pysqlite

class Database():
    '''
    Creates a database
    '''
    
    def __init__(self):
        '''
        D.__init__() or Database() --> NONE
        Creates the database needed to store the high scores
        '''
        
        conn = pysqlite.connect('high_scores.db')
        conn.text_factory = str
        
        cur = conn.cursor()
    
    
        # exception handling
        try:
            cur.execute('CREATE TABLE Original (User_Name TEXT, High_Score INTEGER, PRIMARY KEY (User_Name))')
            cur.execute('CREATE TABLE TimeTrial (User_Name TEXT, High_Score INTEGER, PRIMARY KEY (User_Name))')

        
        except pysqlite.OperationalError:       
            cur.execute('DROP TABLE Original')
            cur.execute('CREATE TABLE Original (User_Name TEXT, High_Score INTEGER, PRIMARY KEY (User_Name))')
            
            cur.execute('DROP TABLE TimeTrial')
            cur.execute('CREATE TABLE TimeTrial (User_Name TEXT, High_Score INTEGER, PRIMARY KEY (User_Name))')
            

            
        conn.commit()
        conn.close()    
            
        return
    
    
    def insert(self, table, user_name, value):
        '''
        D.insert(table, user_name, value) --> NONE
        Insets the values into the correct table. If the user name already exists
        it will only update the high score for that player.
        '''
        # inserting values
        
        conn = pysqlite.connect('high_scores.db')
        conn.text_factory = str
        
        cur = conn.cursor()
        
        
        if table == "Original":
            try:
                cur.execute('INSERT INTO Original VALUES("%s", %i)' %(user_name, value))
            
            except:
                cur.execute('UPDATE Original SET High_Score = %i WHERE User_Name = "%s"' %(value, user_name))
        
        
        elif table == "TimeTrial":
            try:
                cur.execute('INSERT INTO TimeTrial VALUES("%s", %i)' %(user_name, value))
            
            except:
                cur.execute('UPDATE TimeTrial SET High_Score = %i WHERE User_Name = "%s"' %(value, user_name))
    
        
        conn.commit()
        conn.close()
    
        return
    