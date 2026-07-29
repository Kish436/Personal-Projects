import sqlite3 #A library which allows us to connect to a database

class DBFunctions:

    def __init__(self):

        self.DBName = 'PlumberBookingSystemProject.db' #The name of the database
        self.conn = None
        self.cursor = None

    def CreateDatabase(self): #Creating a connection to the database

        try:
            self.conn = sqlite3.connect(self.DBName) #provides a connection to the database
            self.cursor = self.conn.cursor() #lets us manipulate rows in a database and acts as a pointer

            print('cursor set')

        except sqlite3.Error as e: #if any error is encountered while trying to create the connection to the database
            print(e)

    def CreateUserTable(self): #Creating the user table

        UserTableScript = '''CREATE TABLE IF NOT EXISTS Users (
                             CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
                             Firstname TEXT NOT NULL,
                             Surname TEXT NOT NULL,
                             Email TEXT NOT NULL,
                             Postcode TEXT NOT NULL,
                             Username TEXT NOT NULL,
                             Password TEXT NOT NULL,
                             Issue TEXT NOT NULL);'''

        #SQL for creating the table if it has not been created already with appropriate datatypes

        try:
            self.cursor.execute(UserTableScript) #using the cursor to execute the SQL and creating the table

        except sqlite3.Error as e: #if any errors are encountered when trying to create the table
            print(e)

    def CreatePlumberTable(self): #Creating the plumber table

        PlumberTableScript = '''CREATE TABLE IF NOT EXISTS Plumbers (
                                PlumberID INTEGER PRIMARY KEY AUTOINCREMENT,
                                Firstname TEXT NOT NULL,
                                Surname TEXT NOT NULL,
                                Email TEXT NOT NULL,
                                Postcode TEXT NOT NULL,
                                Username TEXT NOT NULL,
                                Password TEXT NOT NULL,
                                CertNo TEXT NOT NULL,
                                ReviewTotal REAL NOT NULL,
                                NoOfReviews INTEGER NOT NULL,
                                AvgReview REAL NOT NULL,
                                Skill TEXT NOT NULL,
                                StandardFee REAL NOT NULL,
                                HourlyRate REAL NOT NULL,
                                DailyRate REAL NOT NULL,
                                StartOfDay TEXT NOT NULL,
                                EndOfDay TEXT NOT NULL);'''

        #SQL for plumber table if it has not been created with appropriate datatypes

        try:
            self.cursor.execute(PlumberTableScript) #Using the cursor to execute the SQL statement and create the table

        except sqlite3.Error as e: #if any errors encountered when trying to create this table
            print(e)

    def CreateMeetingTable(self):

        #creates the Meetings table if it does not exist with the following primary and foreign key constraints
        MeetingScript = '''CREATE TABLE IF NOT EXISTS Meetings (
                           MeetingID INTEGER PRIMARY KEY AUTOINCREMENT,
                           PlumberID INTEGER NOT NULL,
                           CustomerID INTEGER NOT NULL,
                           Date TEXT NOT NULL,
                           Time TEXT NOT NULL,
                           ExpandedIssue BLOB NOT NULL,
                           Status TEXT NOT NULL,
                           FOREIGN KEY ("CustomerID") REFERENCES "Users"("CustomerID"),
                           FOREIGN KEY ("PlumberID") REFERENCES "Plumbers"("PlumberID"))'''

        try:
            self.cursor.execute(MeetingScript) #attempts to create the Meetings table

        except sqlite3.Error as e: #handles any errors with creating the table
            print(e)

    def AddUser(self, firstname, surname, email, postcode, username, password):
        
        #script adds a customer to the database
        Script = '''Insert into Users (Firstname, Surname, Email, Postcode, Username, Password, Issue)
                    Values(?,?,?,?,?,?,'n')'''

        #parameters decided by information entered by the customer
        DataList = [firstname, surname, email, postcode, username, password]

        #executes sql script and commits changes to the database
        self.cursor.execute(Script, DataList)
        self.conn.commit()

    def AddPlumber(self, firstname, surname, email, postcode, username, password, CertNo):

        #inserts the plumber into the database
        Script = '''Insert into Plumbers (Firstname, Surname, Email, Postcode, Username, Password, CertNo, ReviewTotal,
                    NoOfReviews, AvgReview, Skill, StandardFee, HourlyRate, DailyRate, StartOfDay, EndOfDay)
                    Values(?,?,?,?,?,?,?,0,0,0.0,'n','0.0','0.0','0.0','n','n')'''

        #parameters decided by information entered by the plumber
        DataList = [firstname, surname, email, postcode, username, password, CertNo]

        #executes sql script and commits any changes to the database
        self.cursor.execute(Script, DataList)
        self.conn.commit()


    def getAllPlumberCertNos(self):

        #gets all the certification numbers from the existing plumbers
        Script = '''SELECT CertNo FROM Plumbers'''

        #executes the sql script and returns CertNos which is an array of all certification numbers 
        self.cursor.execute(Script)
        CertNos = self.cursor.fetchall()

        certNos = []

        for row in CertNos:
            certNos.append(row[0])

        return certNos

    def FindUser(self, username, password):
        
        #Selects a customer from the database with the username and password entered in the login screen
        Script = '''SELECT CustomerID FROM Users WHERE Username = ? AND Password = ?'''

        #parameters of the username and password entered by the customer logging in
        DataList = [username, password]

        #executes the sql script and returns the customerID of the customer
        self.cursor.execute(Script, DataList)
        UserID = self.cursor.fetchall()

        return UserID
        

    def FindPlumber(self, username, password, certNo):

        #Selects a customer from the database with the username and password entered in the login screen
        Script = '''SELECT PlumberID FROM Plumbers WHERE Username = ? AND Password = ? AND CertNo = ?'''

        #parameters of the username, password and certification number entered by the customer logging in
        DataList = [username, password, certNo]

        #executes the sql script and returns the plumberID of the plumber
        self.cursor.execute(Script, DataList)
        PlumberID = self.cursor.fetchall()

        return PlumberID

    def getCustomerUsernames(self):
        
        #gets all customer usernames from the Customer Table
        Script = '''SELECT Username FROM Users'''

        self.cursor.execute(Script)

        Usernames = self.cursor.fetchall()

        return Usernames #returns an array of customer usernames

    def getAllPlumberUsernames(self):

        #gets all plumber usernames from the Plumbers table 
        Script = '''SELECT Username FROM Plumbers'''

        self.cursor.execute(Script)
        
        Usernames = self.cursor.fetchall()

        return Usernames #returns an array of plumber usernames

    def AddIssue(self, CID, Issue):

        #adds the issue logged by the customer to their record in the Customer table
        Script = '''UPDATE Users SET Issue = ? WHERE CustomerID = ?'''

        #parameters of the issue and customerID to be able to add the issue to the correct record
        DataList = [Issue, CID]

        #executes sql script and commits any changes made to the database
        self.cursor.execute(Script, DataList)
        self.conn.commit()

    def AddSkill(self, plumberID, Skill):

        #adds the plumber skill area to their record
        Script = '''UPDATE Plumbers SET Skill = ? WHERE PlumberID = ?'''

        #parameters of the skill area and plumberID to ensure the skill gets added to the correct plumber
        DataList = [Skill, plumberID]

        #executes the sql script and commits any changes to the database
        self.cursor.execute(Script, DataList)
        self.conn.commit()

    def getIssue(self, CID):

        #gets the Issue the customer currently has logged
        Script = '''SELECT Issue FROM Users WHERE CustomerID = ?'''

        #parameter is the customerID of the user currently using the system
        dataList = [CID]

        #executes sql script and returns the issue 
        self.cursor.execute(Script, dataList)
        Issue = self.cursor.fetchall()

        return Issue

    def getPlumbers(self, Issue):

        #gets all information for the plumber recommendations table 
        Script = '''SELECT PlumberID, NoOfReviews, AvgReview, StandardFee, HourlyRate, DailyRate, StartOfDay, EndOfDay FROM Plumbers WHERE Skill = ?'''

        #parameter is the issue logged by the customer
        dataList = [Issue]

        #executes the sql and gets a list of tuples of plumbers with this information
        self.cursor.execute(Script, dataList)
        plumbers = self.cursor.fetchall()

        #splits the list of tuples into a list of dictionaries 
        Plumbers = []

        length = len(plumbers)

        for i in range(0, length):
            plumber = plumbers[i]

            PlumberDict = {'PlumberID' : plumber[0],
                           'NoOfReviews': plumber[1],
                           'AvgReview' : plumber[2],
                           'StandardFee' : plumber[3],
                           'HourlyRate' : plumber[4],
                           'DailyRate' : plumber[5],
                           'Start' : plumber[6],
                           'End' : plumber[7]}

            Plumbers.append(PlumberDict)

        #returns the list of dictionaries
        return Plumbers

    def getAllCompletedMeetings(self, CustomerID):

        #gets the completed meetings which a customer can leave a review for 
        Script = '''SELECT MeetingID, PlumberID, Date, Time FROM Meetings WHERE CustomerID = ? and Status = "Completed"'''
        DataList = [CustomerID]

        #executes sql and stores the list of tuples in MeetingsCompleted
        self.cursor.execute(Script, DataList)
        MeetingsCompleted = self.cursor.fetchall()

        #creates list of dictionaries for all completed meetings and returns this
        Meetings = []

        for row in MeetingsCompleted:

            MeetingDict = {'MeetingID' : row[0],
                           'PlumberID' : row[1],
                           'Date' : row[2],
                           'Time' : row[3]}
                           

            Meetings.append(MeetingDict)


        return Meetings

    def getAverageReview(self, plumberID):

        #gets the average review of a particular plumber
        Script = '''SELECT AvgReview FROM Plumbers WHERE PlumberID = ?'''
        DataList = [plumberID]

        self.cursor.execute(Script, DataList)
        AR = self.cursor.fetchall()
        AR = AR[0][0]

        #returns the extracted Average review
        return AR

    def getNoOfReviews(self, PlumberID):

        #gets the number of reviews a plumber has from the Plumbers table based on the plumberID of the plumber part of the completed meeting
        Script = '''SELECT NoOfReviews FROM Plumbers WHERE PlumberID = ?'''
        DataList = [PlumberID]

        #executes sql and extracts the number of reviews to return
        self.cursor.execute(Script, DataList)
        NR = self.cursor.fetchall()
        NR = NR[0][0]

        return NR

    def getReviewTotal(self, PlumberID):

        #gets the review total of a plumber from the Plumbers table based on the plumberID of the plumber part of the completed meeting
        Script = '''SELECT ReviewTotal FROM Plumbers WHERE PlumberID = ?'''
        DataList = [PlumberID]

        #executes sql and extracts the review total to return
        self.cursor.execute(Script, DataList)
        RT = self.cursor.fetchall()
        RT = RT[0][0]

        return RT

    def updateReview(self, PlumberID, NoOfReviews, ReviewTotal, AverageReview):

        #updates the review data of a plumber based on the review given by the customer
        Script = '''UPDATE Plumbers SET ReviewTotal = ?, NoOfReviews = ?, AvgReview = ? WHERE PlumberID = ?'''
        DataList = [ReviewTotal, NoOfReviews, AverageReview, PlumberID]

        #executes sql and commits any changes made to the database
        self.cursor.execute(Script, DataList)
        self.conn.commit()

    def updateMeetingStatus(self, newMeetingStatus, MeetingID):

        #updates the meeting status for the meeting with any given meetingID
        Script = '''UPDATE Meetings SET Status = ? WHERE MeetingID = ?'''
        DataList = [newMeetingStatus, MeetingID]


        #executes the sql and commits any changes to the database
        self.cursor.execute(Script, DataList)
        self.conn.commit()

        
    def AddPendingMeeting(self, CustomerID, PlumberID, Date, Time, Issue, status):

        #adds a pending meeting request to the database
        Script = '''INSERT INTO Meetings (PlumberID, CustomerID, Date, Time, ExpandedIssue, Status)
                    Values(?,?,?,?,?,?)'''

        #converts any dates and times entered to a string
        Date = str(Date)
        Time = str(Time)

        DataList = [PlumberID, CustomerID, Date, Time, Issue, status]

        #executes sql and commits any changes to the database
        self.cursor.execute(Script, DataList)
        self.conn.commit()

    def getAllAcceptedMeetings(self, CustomerID):

        #separate scripts to extract all meeting dates and times involving that customer
        ScriptDates = '''SELECT Date FROM Meetings WHERE CustomerID = ?'''
        ScriptTimes = '''SELECT Time FROM Meetings WHERE CustomerID = ?'''
    
        DataList = [CustomerID]

        #executes both sql scripts and returns the list of dates and times
        self.cursor.execute(ScriptDates, DataList)
        Dates = self.cursor.fetchall()

        self.cursor.execute(ScriptTimes, DataList)
        Times = self.cursor.fetchall()

        return Times, Dates

    def getAppointmentData(self, customerID):

        #gets all informations regarding meetings a customer has had or any that are pending
        Script = '''SELECT MeetingID, PlumberID, Date, Time, Status FROM Meetings WHERE CustomerID = ?'''
        DataList = [customerID]

        #executes sql and stores a list of tuples in ApptData
        self.cursor.execute(Script, DataList)
        ApptData = self.cursor.fetchall()

        #creates a list of dictionaries for each meeting and returns this
        Appointments = []

        for row in ApptData:

            MeetingDict = {'MeetingID' : row[0],
                           'PlumberID' : row[1],
                           'Date' : row[2],
                           'Time' : row[3],
                           'Status' : row[4]}
            Appointments.append(MeetingDict)

        return Appointments

    def getAllMeetingIDsCustomer(self, customerID):

        #gets all valid meetingIDs regarding an individual customer which are eligible to be cancelled
        Script = '''SELECT MeetingID FROM Meetings WHERE CustomerID = ? AND (Status = "Accepted" OR Status = "Pending")'''
        DataList = [customerID]

        #executes sql and stores a list of tuples in MeetingIDs
        self.cursor.execute(Script, DataList)
        MeetingIDs = self.cursor.fetchall()

        #creates a list of dictionaries for each meetingID and returns this
        Meetings = []

        for row in MeetingIDs:
            MeetingID = int(row[0])
            Meetings.append(MeetingID)

        return Meetings

    def getAllPendingMeetingIDs(self, customerID):

        #gets all valid meetingIDs regarding an individual customer which are eligible to be cancelled
        Script = '''SELECT MeetingID FROM Meetings WHERE CustomerID = ? AND Status = "Pending"'''
        DataList = [customerID]

        #executes sql and stores a list of tuples in MeetingIDs
        self.cursor.execute(Script, DataList)
        MeetingIDs = self.cursor.fetchall()

        #creates a list of dictionaries for each meetingID and returns this
        Meetings = []

        for row in MeetingIDs:
            MeetingID = int(row[0])
            Meetings.append(MeetingID)

        return Meetings


    def getAllMeetingIDsPlumber(self, plumberID):

        #gets all MeetingIDs which can be cancelled for a specific plumber
        Script = '''SELECT MeetingID FROM Meetings WHERE PlumberID = ? AND Status = "Accepted"'''
        DataList = [plumberID]

        #executes sql and stores a list of tuples in MeetingIDs
        self.cursor.execute(Script, DataList)
        MeetingIDs = self.cursor.fetchall()

        #creates a list of dictionaries for each meetingID and returns this
        Meetings = []

        for row in MeetingIDs:
            MeetingID = int(row[0])
            Meetings.append(MeetingID)

        return Meetings

    def getMeetingInfo(self, MeetingID):

        #gets the specific date and time of a particular meeting
        Script = '''SELECT Date, Time FROM Meetings WHERE MeetingID = ?'''
        DataList = [MeetingID]

        #executes sql and extracts the date and time to return
        self.cursor.execute(Script, DataList)
        DateAndTime = self.cursor.fetchall()

        DateAndTime = DateAndTime[0]
        
        return DateAndTime

    def getMeetingForCancellation(self, customerID):

        #gets all pending meeting requests for a customer to check if any have expired
        Script = '''SELECT MeetingID, Date, Time FROM Meetings WHERE CustomerID = ? AND Status = "Pending"'''
        DataList = [customerID]

        #executes sql and stores list of tuples
        self.cursor.execute(Script, DataList)
        MeetingInfo=self.cursor.fetchall()

        #creates a list of dictionaries for all meetings
        Meetings = []

        for row in MeetingInfo:

            Meeting = {'MeetingID' : row[0],
                       'Date' : row[1],
                       'Time' : row[2]}

            Meetings.append(Meeting)

        return Meetings

    def getMeetingForCancellationP(self, plumberID):

        #gets all meetings for a plumber which are pending to check if any are expired
        Script = '''SELECT MeetingID, Date, Time FROM Meetings WHERE PlumberID = ? AND Status = "Pending"'''
        DataList = [plumberID]

        #executes sql and stores a list of tuples in MeetingInfo
        self.cursor.execute(Script, DataList)
        MeetingInfo=self.cursor.fetchall()

        #creates a list of dictionaries for all meetings
        Meetings = []

        for row in MeetingInfo:

            Meeting = {'MeetingID' : row[0],
                       'Date' : row[1],
                       'Time' : row[2]}

            Meetings.append(Meeting)

        return Meetings
    
    def removePlumber(self, plumberID):

        #removes a plumber from the Plumbers table
        Script = '''DELETE FROM Plumbers WHERE PlumberID = ?'''
        DataList = [plumberID]

        #executes sql and commits any changes to the database
        self.cursor.execute(Script, DataList)
        self.conn.commit()

    def AddPlumberOtherInfo(self, plumberID, skill, HR, DR, SF, sTime, eTime):

        #adds all information collected in this class 
        Script = '''UPDATE Plumbers SET Skill = ?, HourlyRate = ?, DailyRate = ?, StandardFee = ?,
                    StartOfDay = ?, EndOfDay = ? WHERE PlumberID = ?'''
        DataList = [skill, HR, DR, SF, sTime, eTime, plumberID]

        #executes sql and commits any changes to the database
        self.cursor.execute(Script, DataList)
        self.conn.commit()


    def getPending(self, plumberID):

        #uses an inner join method to access all information regarding meetings for a plumber to accept or reject from multiple tables
        Script = '''SELECT Meetings.MeetingID, Users.CustomerID, Users.Postcode, Meetings.Date, Meetings.Time, Meetings.ExpandedIssue
                    FROM Users
                    INNER JOIN Meetings ON Users.CustomerID = Meetings.CustomerID
                    WHERE Meetings.PlumberID = ? AND Meetings.Status = "Pending"'''
        DataList = [plumberID]

        #executes sql and stores list of tuples in Data
        self.cursor.execute(Script, DataList)
        Data = self.cursor.fetchall()

        #creates a list of dictionaries for all meetings and returns this
        Meetings = []

        for row in Data:
            Meeting = {'MeetingID' : row[0],
                       'CID' : row[1],
                       'Postcode' : row[2],
                       'Date' : row[3],
                       'Time' : row[4],
                       'Issue' : row [5]}

            Meetings.append(Meeting)

        return Meetings

    def getPendingMeetingIDs(self, plumberID):

        #gets all meetingIDs for pending meetings regarding a specific plumber
        Script = '''SELECT MeetingID FROM Meetings WHERE PlumberID = ? AND Status = "Pending"'''
        DataList = [plumberID]

        #executes sql and stores list of tuples in MeetingIDs
        self.cursor.execute(Script, DataList)
        MeetingIDs = self.cursor.fetchall()

        #creates a list of dictionaries for all meetings and returns this
        MIDs = []
        for row in MeetingIDs:
            MIDs.append(row[0])

        return MIDs

    def getAccepted(self, plumberID):

        #gets all accepted meeting information from the meetings table and the customer postcode from different tables using inner join
        Script = '''SELECT Meetings.MeetingID, Users.CustomerID, Users.Postcode, Meetings.Date, Meetings.Time, Meetings.ExpandedIssue
                    FROM Users
                    INNER JOIN Meetings ON Users.CustomerID = Meetings.CustomerID
                    WHERE Meetings.PlumberID = ? AND Meetings.Status = "Accepted"'''
        DataList = [plumberID]

        #executes sql and stores list of tuples in Data
        self.cursor.execute(Script, DataList)
        Data = self.cursor.fetchall()

        #creates a list of dictionaries for all meetings and returns this
        Meetings = []

        for row in Data:
            Meeting = {'MeetingID' : row[0],
                       'CID' : row[1],
                       'Postcode' : row[2],
                       'Date' : row[3],
                       'Time' : row[4],
                       'Issue' : row [5]}

            Meetings.append(Meeting)

        return Meetings

    def UpdatePricing(self, plumberID, SF, HR, DR):

        #updates the plumber pricing figures based on inputs given
        Script = '''UPDATE Plumbers SET StandardFee = ?, HourlyRate = ?, DailyRate = ? WHERE PlumberID = ?'''
        Datalist = [SF, HR, DR, plumberID]

        #executes sql and 
        self.cursor.execute(Script, Datalist)
        self.conn.commit()


    def close(self):
        #closes the connection to the database
        self.conn.close()

        self.conn = None
        self.cursor = None
           



                
                    
                    

