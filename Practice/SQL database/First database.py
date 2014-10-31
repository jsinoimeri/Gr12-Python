from sqlite3 import dbapi2 as pysqlite

conn = pysqlite.connect('leaugue.db')
conn.text_factory = str

cur = conn.cursor()

try:
    cur.execute('CREATE TABLE Density (Province TEXT, Population INTEGER, Land_Area REAL)')
except:
    cur.execute('DROP TABLE Density')
    cur.execute('CREATE TABLE Density (Province TEXT, Population INTEGER, Land_Area REAL)')


cur.execute(('INSERT INTO Density VALUES("%s", %i, %f)') %("Newfoundloand and Labrador", 505469, 370494.89))
cur.execute(('INSERT INTO Density VALUES("%s", %i, %f)') %("Prince Edward Island", 135851, 5683.91))
cur.execute(('INSERT INTO Density VALUES("%s", %i, %f)') %("Nova Scotia", 913462, 52917.46))
cur.execute(('INSERT INTO Density VALUES("%s", %i, %f)') %("New Brunswick", 729997, 71355.12))
cur.execute(('INSERT INTO Density VALUES("%s", %i, %f)') %("Quebec", 7546131, 1356366.78))
cur.execute(('INSERT INTO Density VALUES("%s", %i, %f)') %("Ontario", 12160282, 907573.82))
cur.execute(('INSERT INTO Density VALUES("%s", %i, %f)') %("Manitoba", 1148401, 552369.96))
cur.execute(('INSERT INTO Density VALUES("%s", %i, %f)') %("Saskatchewan", 968157, 588276.09))
cur.execute(('INSERT INTO Density VALUES("%s", %i, %f)') %("Alberta", 3290350, 640044.57))
cur.execute(('INSERT INTO Density VALUES("%s", %i, %f)') %("British Columbia", 4113487, 924815.43))
cur.execute(('INSERT INTO Density VALUES("%s", %i, %f)') %("Yukon", 30372, 474711.02))
cur.execute(('INSERT INTO Density VALUES("%s", %i, %f)') %("Northwest Territories", 41464, 1140834.90))
cur.execute(('INSERT INTO Density VALUES("%s", %i, %f)') %("Nunavut", 29474, 1932254.97))

conn.commit()

cur.execute('SELECT * FROM Density')

records = cur.fetchall()

for record in records:
    print "%s %i %.2f" %(record[0], record[1], record[2])

print "\n"
cur.execute('SELECT Population FROM Density')

population = cur.fetchall()

for pop in population:
    print "%i" %(pop)

print "\n"    
cur.execute('SELECT Province FROM Density WHERE Population < 1000000')

population = cur.fetchall()

for pop in population:
    print "%s" %(pop)
    
print "\n"    
cur.execute('SELECT Province FROM Density WHERE Population < 1000000 or Population > 5000000')

population = cur.fetchall()

for pop in population:
    print "%s" %(pop)

print "\n"    
cur.execute('SELECT Province FROM Density WHERE Population > 1000000 and Population < 5000000')

population = cur.fetchall()

for pop in population:
    print "%s" %(pop)
    
print "\n"    
cur.execute('SELECT Province FROM Density WHERE Land_Area > 200000')

areas = cur.fetchall()

for area in areas:
    print "%s" %(area)

print "\n"    
cur.execute('SELECT * FROM Density')

records = cur.fetchall()

for record in records:
    print "%s %.2f" %(record[0], record[1] / record[2])

cur.execute('UPDATE Density SET Population = 12160283 WHERE Province = "Ontario"')

conn.close()