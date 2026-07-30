from tkinter import *
from datetime import datetime, timedelta
from NEA_SQL import DBFunctions
from tkinter import ttk


class chooseType:

    def __init__(self):

        self.Screen1 = Tk() #assigns the variable root to having the attributes of Tk()

        self.Screen1.geometry('400x400') #Creates the 400x400 grid
        self.Screen1.title('Plumber or User') #title of the Interface
        self.Screen1.config(bg = '#00008B') #background colour of blue

        self.Type = None

        self.CreateObjects() #call to the CreateObjects method
    def CustomerPressed(self):

        self.Screen1.destroy() #destroys this root to remove it from the screen
        self.Type = '0'
        LoginOrRegister(self.Type) #calls the next class

    def PlumberPressed(self):

        self.Screen1.destroy() #destroys this root to remove it from the screen
        self.Type = '1'
        LoginOrRegister(self.Type)#calls the next class

    def CreateObjects(self):

        Plumber = Button( self.Screen1,
                               text = 'Plumber',
                               font = ('Courir', 20),
                               command = lambda: self.PlumberPressed()) #button which is created for the user to be able to select if they are a plumber 
        Customer = Button( self.Screen1,
                               text = 'Customer',
                               font = ('Courir', 20),
                               command = lambda: self.CustomerPressed()) #button which is created for the user to be able to select if the are a client
        HeadingLabel = Label( self.Screen1,
                            text = 'Are you a:',
                            fg = 'yellow',
                            bg = '#00008B',
                            font = ('Courir', 20, 'italic', 'bold') ) #label that makes it clear as to what to do on this screen

        #places tkinter objects onto the window
        HeadingLabel.place(x=60, y=70)
        Plumber.place(x=75, y=150)
        Customer.place(x = 200, y=150)

class LoginOrRegister:

    def __init__(self, Type):

        self.LorR = Tk() #assigns the Tkinter methods to be able to be used by self.root

        self.Type = Type #assigns the value returned by the previous class to the container Type

        self.LorR.geometry('400x400')
        self.LorR.title('Login or Register')

        self.LorR.config(bg = '#00008B') #Creates a user interface and lays out its attributed

        self.CreateObjects() #Call to the method 'CreateObjects' for the objects to be created

    def LoginPressed(self): #What happens if the login button is pressed

        if self.Type == '0':
            self.LorR.destroy() #deletes the current screen to prepare for next
            LoginCustomer() #Type '0' represents the current person is a Client

        elif self.Type == '1':
            self.LorR.destroy() 
            LoginPlumber() #Type '1' represents the current person is a plumber

    def RegisterPressed(self): #What happens when the register button is pressed

        #Types are the same as self.LoginPressed()
        
        if self.Type == '0':
            self.LorR.destroy()
            RegisterCustomer()

        elif self.Type == '1':
            self.LorR.destroy()
            RegisterPlumber()

    def Back(self):
        self.LorR.destroy()
        chooseType()
            
    def CreateObjects(self):

        #label indicates the purpose of the screen
        TitleLabel = Label( self.LorR,
                            text = 'Login or Register?',
                            fg = 'yellow',
                            bg = '#00008B',
                            font = ('Courir', 30, 'italic', 'bold'))

        Login = Button( self.LorR,
                             text = 'Login',
                             font = ('Courir', 20),
                             command = lambda: self.LoginPressed()) #Creates a login button

        Register = Button( self.LorR,
                                text = 'Register',
                                font = ('Courir', 20),
                                command = lambda: self.RegisterPressed()) #Creates a register button

        Back = Button( self.LorR,
                            text = 'Back',
                            font = ('Courir', 10),
                            command = self.Back)

        #places tkinter objects onto the window
        TitleLabel.place(x = 30, y = 50)

        Login.place(x=70, y=170)
        Register.place(x=190, y=170)

        Back.place(x = 10, y = 350)

        #Places both buttons at specific coordinates on the interface

class RegisterCustomer:

    def __init__(self):

        self.RC = Tk() #Creates another interface used by the user to create a new account

        self.RC.geometry('1000x750')
        self.RC.title('Register User')
        self.RC.config(bg = '#00008B')

        #establishes a connection to the database 

        self.DB = DBFunctions()
        self.DB.CreateDatabase()
        self.DB.CreateUserTable()

        self.CreateObjects()

    def EnterPressed(self):

        ##Checks if the input is Valid
        firstname = self.Firstname.get()
        surname = self.Lastname.get()
        email = self.Email.get()
        postcode = self.Postcode.get()
        username = self.Username.get()
        password = self.Password.get()
        Cpassword = self.ConfirmPassword.get() #gets all data entered by user
        counter = 0 #will be used to check the number of errors in the code
        usernames = self.DB.getCustomerUsernames() #used to check if anyone with this username is already in the system
        #presence, format, and length checks
        if firstname == '' or firstname.isalpha() == False: 
            counter = counter + 1
            #changes the yellow labels for the entry boxes to red and to 'INVALID' to indicate an error
            self.FnLabel.config(fg = '#FF0000', text = 'INVALID')
            self.FnLabel.after(500, lambda: self.FnLabel.config(fg = 'yellow', text = 'Firstname:')) 
                
        if surname == '' or surname.isalpha() == False:
            counter = counter + 1
            self.LnLabel.config(fg = '#FF0000', text = 'INVALID')
            self.LnLabel.after(500, lambda: self.LnLabel.config(fg = 'yellow', text = 'Lastname:'))

        if ('@' not in email) or (email == '') or email.isdigit() == True:
            counter = counter + 1
            self.ELabel.config(fg = '#FF0000', text = 'INVALID')
            self.ELabel.after(500, lambda: self.ELabel.config(fg = 'yellow', text = 'Email:'))

        if (len(postcode) > 9) or (postcode == '') or (postcode.isalnum() == False):
            counter = counter + 1
            self.PCLabel.config(fg = '#FF0000', text = 'INVALID')
            self.PCLabel.after(500, lambda: self.PCLabel.config(fg = 'yellow', text = 'Postcode:'))

        if (username == '') or (username.isdigit() == True) or username in usernames :
            counter = counter + 1
            self.UnLabel.config(fg = '#FF0000', text = 'INVALID')
            self.UnLabel.after(500, lambda: self.UnLabel.config(fg = 'yellow', text = 'Usename:'))

        if (password.isalnum() == False) or (password == '') or len(password) < 12:
            counter = counter + 1
            self.PWLabel.config(fg = '#FF0000', text = 'INVALID')
            self.PWLabel.after(500, lambda: self.PWLabel.config(fg = 'yellow', text = 'Password:'))

        if (Cpassword != password) or (Cpassword == ''):
            counter = counter + 1
            self.CPWLabel.config(fg = '#FF0000', text = 'INVALID')
            self.CPWLabel.after(500, lambda: self.CPWLabel.config(fg = 'yellow', text = 'Confirm Password:'))

        if counter == 0:
            #if no errors encountered with the data entered then adds user to the database
            self.DB.AddUser(firstname, surname, email, postcode, username, password) 
            self.RC.destroy() #destroys the current screen as it is no longer needed
            self.DB.close() #closes the database connection since the code will now jump to the next screen in a different class
            LoginCustomer()
                            
    def ClearPressed(self):

        #Removes all data entered into these fields the instance the clear button is pressed

        self.Firstname.delete(0, END) #(0, END) allows us to delete the emtire entry
        self.Lastname.delete(0, END)
        self.Email.delete(0, END)
        self.Postcode.delete(0, END)
        self.Password.delete(0, END)
        self.ConfirmPassword.delete(0, END)

    def Back(self):
        self.RC.destroy()
        self.DB.close()
        LoginOrRegister('0') #goes back to the previous screen. '0' indicates that this user is a customer not a plumber

    def CreateObjects(self):

        #Creates entry objects in which users will be able to enter their details in

        self.Firstname = Entry( self.RC,
                                width = 100,
                                borderwidth = 5)

        self.Lastname = Entry( self.RC,
                                width = 100,
                                borderwidth = 5)

        self.Email = Entry( self.RC,
                            width = 100,
                            borderwidth = 5)

        self.Postcode = Entry( self.RC,
                               width = 100,
                               borderwidth = 5)

        self.Username = Entry( self.RC,
                               width = 100,
                               borderwidth = 5)


        self.Password = Entry( self.RC,
                               width = 100,
                               borderwidth = 5)

        self.ConfirmPassword = Entry( self.RC,
                               width = 100,
                               borderwidth = 5)

        #Creates clear and enter button so that user can either remove all data from the field
        #or they can choose to attempt to proceed to the next stage/return to the previous screen

        Enter = Button( self.RC,
                             text = 'Enter',
                             font = ('Courir', 20),
                             command = lambda: self.EnterPressed())

        Clear = Button( self.RC,
                             text = 'Clear',
                             font = ('Courir', 20),
                             command = lambda: self.ClearPressed())

        Back = Button( self.RC,
                            text = 'Back',
                            font = ('Courir', 10),
                            command = lambda: self.Back())


        #Creates labels for unambiguity of what each field is for

        self.RegisterLabel = Label( self.RC,
                                    text = 'Register',
                                    fg = 'yellow',
                                    bg = '#00008B',
                                    font = ('Courir', 30, 'italic', 'bold'))

        self.FnLabel = Label( self.RC,
                              text = 'Firstname: ',
                              fg = 'yellow',
                              bg = '#00008B',
                              font = ('Courir', 10))

        self.LnLabel = Label( self.RC,
                              text = 'Lastname: ',
                              fg = 'yellow',
                              bg = '#00008B',
                              font = ('Courir', 10))

        self.ELabel = Label( self.RC,
                             text = 'Email: ',
                             fg = 'yellow',
                             bg = '#00008B',
                             font = ('Courir', 10))

        self.PCLabel = Label( self.RC,
                              text = 'Post Code: ',
                              fg = 'yellow',
                              bg = '#00008B',
                              font = ('Courir', 10))

        self.UnLabel = Label( self.RC,
                              text = 'Username: ',
                              fg = 'yellow',
                              bg = '#00008B',
                              font = ('Courir', 10))

        self.PWLabel = Label( self.RC,
                              text = 'Password: ',
                              fg = 'yellow',
                              bg = '#00008B',
                              font = ('Courir', 10))

        self.PasswordInfo = Label( self.RC,
                                    text = 'Must be minimum 12 Characters and alpha numeric',
                                    fg = 'yellow',
                                    bg = '#00008B',
                                    font = ('Courir', 10, 'italic'))

        self.CPWLabel = Label( self.RC,
                              text = 'Confirm Password: ',
                              fg = 'yellow',
                              bg = '#00008B',
                              font = ('Courir', 10))

        #Places the labels in a vertical column one after another

        self.RegisterLabel.place(x = 100, y = 100)
        self.Firstname.place(x = 160, y = 200)
        self.Lastname.place(x = 160, y = 250)
        self.Email.place(x = 160, y = 300)
        self.Postcode.place(x = 160, y = 350)
        self.Username.place(x = 160, y = 400)
        self.Password.place(x = 160, y = 450)
        self.ConfirmPassword.place(x = 160, y = 520)

        #Places the entry blocks to correspond with the positions of their labels

        self.FnLabel.place(x = 30, y = 200)
        self.LnLabel.place(x = 30, y = 250)
        self.ELabel.place(x = 30, y = 300) 
        self.PCLabel.place(x = 30, y = 350)
        self.UnLabel.place(x = 30, y = 400)
        self.PWLabel.place(x = 30, y = 450)
        self.PasswordInfo.place(x = 160, y = 485)
        self.CPWLabel.place(x = 30, y = 520)

        #Places the Clear and Enter buttons onto the interface 

        Clear.place(x = 150, y = 590)
        Enter.place(x = 350, y = 590)
        Back.place(x = 10, y = 700)


class RegisterPlumber:

    def __init__(self):

        self.RP = Tk() #Creates another interface used by the user to create a new account

        self.RP.geometry('1200x750')
        self.RP.title('Register User')
        self.RP.config(bg = '#00008B')

        self.DB = DBFunctions() #new database connection
        self.DB.CreateDatabase()
        self.DB.CreatePlumberTable() #creates the plumber table if it has not already been created (required when the first plumber enters into the system)

        self.CreateObjects()

    def ClearPressed(self):

        #Removes all data entered into these fields the instance the clear button is pressed

        self.Firstname.delete(0, END) #(0, END) allows us to delete the entire entry
        self.Lastname.delete(0, END)
        self.Email.delete(0, END)
        self.Postcode.delete(0, END)
        self.Username.delete(0, END)
        self.Password.delete(0, END)
        self.ConfirmPassword.delete(0, END)
        self.CIG_CerfictateNo.delete(0, END)

    def Back(self):
        self.RP.destroy() #destroys the registration window
        self.DB.close() #closes the database connection
        LoginOrRegister('1') #returns to the login and registration selection page as a plumber

    def EnterPressed(self):

        #gets the certification board of the plumber to use in the validation
        Board = self.CertBoard.get()

        #gets all data entered by user
        firstname = self.Firstname.get()
        surname = self.Lastname.get()
        email = self.Email.get()
        postcode = self.Postcode.get()
        username = self.Username.get()
        password = self.Password.get()
        Cpassword = self.ConfirmPassword.get()
        CertNo = self.CertNo.get()

        #counter being 0 at the end of the method indicates that no errors have been found 
        counter = 0

        usernames = self.DB.getAllPlumberUsernames() #this variable holds the same purpose as that in the RegisterCustomer class

        #checks done here are all the same as in the RegisterCustomer class
        
        if firstname == '' or firstname.isalpha() == False:
            counter = counter + 1
            self.FnLabel.config(fg = '#FF0000', text = 'INVALID')
            self.FnLabel.after(500, lambda: self.FnLabel.config(fg = 'yellow', text = 'Firstname:'))
                
        if surname == '' or surname.isalpha() == False:
            counter = counter + 1
            self.LnLabel.config(fg = '#FF0000', text = 'INVALID')
            self.LnLabel.after(500, lambda: self.LnLabel.config(fg = 'yellow', text = 'Lastname:'))

        if ('@' not in email) or (email == '') or email.isdigit() == True:
            counter = counter + 1
            self.ELabel.config(fg = '#FF0000', text = 'INVALID')
            self.ELabel.after(500, lambda: self.ELabel.config(fg = 'yellow', text = 'Email:'))

        if (len(postcode) > 7) or (postcode == '') or (postcode.isalnum() == False):
            counter = counter + 1
            self.PCLabel.config(fg = '#FF0000', text = 'INVALID')
            self.PCLabel.after(500, lambda: self.PCLabel.config(fg = 'yellow', text = 'Postcode:'))

        if (username == '') or (username.isdigit() == True) or username in usernames:
            counter = counter + 1
            self.UnLabel.config(fg = '#FF0000', text = 'INVALID')
            self.UnLabel.after(500, lambda: self.UnLabel.config(fg = 'yellow', text = 'Usename:'))

        if (password.isalnum() == False) or (password == '') or len(password) < 12:
            counter = counter + 1
            self.PWLabel.config(fg = '#FF0000', text = 'INVALID')
            self.PWLabel.after(500, lambda: self.PWLabel.config(fg = 'yellow', text = 'Password:'))

        if (Cpassword != password) or (Cpassword == ''):
            counter = counter + 1
            self.CPWLabel.config(fg = '#FF0000', text = 'INVALID')
            self.CPWLabel.after(500, lambda: self.CPWLabel.config(fg = 'yellow', text = 'Confirm Password:'))


        CertNos = self.DB.getAllPlumberCertNos() #used to check if there is a plumber with that certificate number in the system already
        #checks the certification board the plumber has selected
        #performs length, presence and format checks on the certification ID 

        if Board == 'CIG':
            if len(CertNo) != 29 or CertNo.isalnum() == False or CertNo[7] != '/' or CertNo[12] != '-' or CIG[15] != '/' or CIG[22] != '/':
                counter = counter + 1
                self.CertNoLabel.config(fg = '#FF0000', text = 'INVALID')
                self.CertNoLabel.after(500, lambda: self.CertNoLabel.config(fg = 'yellow', text = 'Cert No:'))
            else:
                if CertNo in CertNos:
                    counter = counter + 1
                    self.CertNoLabel.config(fg = '#FF0000', text = 'INVALID')
                    self.CertNoLabel.after(500, lambda: self.CIGLabel.config(fg = 'yellow', text = 'Cert No:'))

        elif Board == 'BPEC':
            if len(CertNo) != 5 or CertNo.isdigit() == False:
                counter = counter + 1
                self.CertNoLabel.config(fg = '#FF0000', text = 'INVALID')
                self.CertNoLabel.after(500, lambda: self.CertNoLabel.config(fg = 'yellow', text = 'Cert No:'))
            else:
                if CertNo in CertNos:
                    counter = counter + 1
                    self.CertNoLabel.config(fg = '#FF0000', text = 'INVALID')
                    self.CertNoLabel.after(500, lambda: self.CIGLabel.config(fg = 'yellow', text = 'Cert No:'))

        elif Board == 'CSCS':
            if len(CertNo) != 6 or CertNo.isdigit() == False:
                counter = counter + 1
                self.CertNoLabel.config(fg = '#FF0000', text = 'INVALID')
                self.CertNoLabel.after(500, lambda: self.CertNoLabel.config(fg = 'yellow', text = 'Cert No:'))
            else:
                if CertNo in CertNos:
                    counter = counter + 1
                    self.CertNoLabel.config(fg = '#FF0000', text = 'INVALID')
                    self.CertNoLabel.after(500, lambda: self.CIGLabel.config(fg = 'yellow', text = 'Cert No:'))
                
        if counter == 0:
            self.DB.AddPlumber(firstname, surname, email, postcode, username, password, CertNo)
            PlumberID = self.DB.FindPlumber(username, password, CertNo)
            PlumberID = PlumberID[0][0] #extracts the plumberID removing it from the list format it was returned in
            self.RP.destroy()
            self.DB.close()
            #passes the plumberID to the next class to ensure all info collected now is added to the correct plumber
            collectPlumberInfo(PlumberID)

    def CreateObjects(self):

        #Creates entry objects in which users will be able to enter their details in

        self.Firstname = Entry( self.RP,
                                width = 100,
                                borderwidth = 5)

        self.Lastname = Entry( self.RP,
                                width = 100,
                                borderwidth = 5)

        self.Email = Entry( self.RP,
                            width = 100,
                            borderwidth = 5)

        self.Postcode = Entry( self.RP,
                               width = 100,
                               borderwidth = 5)

        self.Username = Entry( self.RP,
                               width = 100,
                               borderwidth = 5)


        self.Password = Entry( self.RP,
                               width = 100,
                               borderwidth = 5)

        self.ConfirmPassword = Entry( self.RP,
                               width = 100,
                               borderwidth = 5)

        self.CertNo = Entry( self.RP,
                                    width = 100,
                                    borderwidth = 5)

        #Enables plumbers to select which board they belong to in terms of their certificate issuer

        self.CertBoard = StringVar(self.RP, value = 'CIG')

        certBoardLabel = Label( self.RP,
                                text = 'Select Certification Board:',
                                fg = 'yellow',
                                bg = '#00008B',
                                font = ('Courir', 10))

        CIG = Radiobutton( self.RP,
                             text = 'City and Guilds',
                             font = ('Courir', 10),
                             variable = self.CertBoard,
                             value = 'CIG')

        BPEC = Radiobutton( self.RP,
                             text = 'BPEC',
                             font = ('Courir', 10),
                             variable = self.CertBoard,
                             value = 'BPEC')

        CSCS = Radiobutton( self.RP,
                             text = 'CSCS',
                             font = ('Courir', 10),
                             variable = self.CertBoard,
                             value = 'CSCS')

        #Creates clear and enter button so that user can either remove all data from the field
        #or they can choose to attempt to proceed to the next stage, or return to the previous screen

        Enter = Button( self.RP,
                             text = 'Enter',
                             font = ('Courir', 20),
                             command = lambda: self.EnterPressed())

        Clear = Button( self.RP,
                             text = 'Clear',
                             font = ('Courir', 20),
                             command = lambda: self.ClearPressed())

        Back = Button( self.RP,
                            text = 'Back',
                            font = ('Courir', 10),
                            command = lambda: self.Back())

        #Creates labels for unambiguity of what the screen/each entry box is for, and for any formats required

        self.RegisterLabel = Label( self.RP,
                                    text = 'Register',
                                    fg = 'yellow',
                                    bg = '#00008B',
                                    font = ('Courir', 30, 'italic', 'bold'))
        self.FnLabel = Label( self.RP,
                              text = 'Firstname: ',
                              fg = 'yellow',
                              bg = '#00008B',
                              font = ('Courir', 10))
        self.LnLabel = Label( self.RP,
                              text = 'Lastname: ',
                              fg = 'yellow',
                              bg = '#00008B',
                              font = ('Courir', 10))
        self.ELabel = Label( self.RP,
                             text = 'Email: ',
                             fg = 'yellow',
                             bg = '#00008B',
                             font = ('Courir', 10))
        self.PCLabel = Label( self.RP,
                              text = 'Post Code: ',
                              fg = 'yellow',
                              bg = '#00008B',
                              font = ('Courir', 10))
        self.UnLabel = Label( self.RP,
                              text = 'Username: ',
                              fg = 'yellow',
                              bg = '#00008B',
                              font = ('Courir', 10))        
        self.PWLabel = Label( self.RP,
                              text = 'Password: ',
                              fg = 'yellow',
                              bg = '#00008B',
                              font = ('Courir', 10))
        self.CPWLabel = Label( self.RP,
                              text = 'Confirm Password: ',
                              fg = 'yellow',
                              bg = '#00008B',
                              font = ('Courir', 10))
        self.CertNoLabel = Label( self.RP,
                               text = 'Cert No: ',
                               fg = 'yellow',
                               bg = '#00008B',
                               font = ('Courir', 10))
        self.PasswordInfo = Label( self.RP,
                            text = 'Must be minimum 12 Characters and alpha numeric',
                            fg = 'yellow',
                            bg = '#00008B',
                            font = ('Courir', 10, 'italic'))

        #places the certification options onto the window
        certBoardLabel.place(x=1000, y=150)
        CIG.place(x=1000, y=220)
        BPEC.place(x=1000, y=270)
        CSCS.place(x=1000, y=320)
        
        #Places the labels in a vertical column one after another

        self.RegisterLabel.place(x = 100, y = 100)
        self.Firstname.place(x = 180, y = 200)
        self.Lastname.place(x = 180, y = 250)
        self.Email.place(x = 180, y = 300)
        self.Postcode.place(x = 180, y = 350)
        self.Username.place(x = 180, y = 400)
        self.PasswordInfo.place(x = 210, y = 480)
        self.Password.place(x = 180, y = 450)
        self.ConfirmPassword.place(x = 180, y = 520)
        self.CertNo.place(x = 180, y = 570)

        #Places the entry blocks to correspond with the positions of their labels

        self.FnLabel.place(x = 30, y = 200)
        self.LnLabel.place(x = 30, y = 250)
        self.ELabel.place(x = 30, y = 300)
        self.PCLabel.place(x = 30, y = 350)
        self.UnLabel.place(x = 30, y = 400)
        self.PWLabel.place(x = 30, y = 450)
        self.CPWLabel.place(x = 30, y = 520)
        self.CertNoLabel.place(x = 30, y = 570)

        #Places the Clear and Enter buttons onto the interface 

        Clear.place(x = 150, y = 610)
        Enter.place(x = 350, y = 610)
        Back.place(x =10, y = 700)
                             
class LoginCustomer:

    def __init__(self):

        #Creating and customising a user interface referred to by self.root which possesses all method of Tk()

        self.LC = Tk()

        self.LC.geometry('1000x500')
        self.LC.title('Login Client')
        self.LC.config(bg = '#00008B')

        self.counter = 1 #used to track how many login attempts have been made

        self.DB = DBFunctions()
        self.DB.CreateDatabase()
        self.DB.CreateUserTable()

        self.CreateObjects() #Call to self.CreateObjects() to create the buttons and other objects

    def EnterPressed(self):

        if self.counter == 3:
            BlockedLabel = Label( self.LC,
                                  text = 'All 3 attempts used',
                                  font = ('Courir', 15),
                                  bg = '#00008B',
                                  fg = '#FF0000')

            BlockedLabel.place(x = 500, y = 370)
            BlockedLabel.after(1000, lambda: self.LC.destroy()) #if all attempts used, close the system for the user     

        Username = self.Username.get()
        Password = self.Password.get()

        CustomerID = self.DB.FindUser(Username, Password) #attempts to find the user's customerID based on the username and password entered

        if len(CustomerID) != 1:
            CustomerLabel = Label( self.LC,
                               text = 'User not found',
                               font = ('Courir', 10),
                               fg = '#FF0000',
                               bg = '#00008B')
            CustomerLabel.place(x=850, y=170)
            CustomerLabel.after(500, lambda: CustomerLabel.destroy())

            self.counter = self.counter + 1 #counts the attempt and stores it in self.counter
 

        else:
            #if user is valid, send the user to the customer dashboard 
            self.CustomerID = CustomerID[0][0]
            self.DB.close()
            self.LC.destroy()
            CustomerDashboard(self.CustomerID)

    def ClearPressed(self):

        self.Username.delete(0, END)
        self.Password.delete(0, END)

    def Back(self):
        self.LC.destroy()
        self.DB.close()
        LoginOrRegister('0') #indicates this is a customer who is still using the system using '0'

    def CreateObjects(self):

        Clear = Button( self.LC,
                             text = 'Clear',
                             font = ('Courir', 20),
                             command = lambda: self.ClearPressed()) #Button to clear fields

        Enter = Button( self.LC,
                             text = 'Enter',
                             font = ('Courir', 20),
                             command = lambda: self.EnterPressed()) #Button to confirm details

        Back = Button( self.LC,
                            text = 'Back',
                            font = ('Courir', 10),
                            command = lambda: self.Back()) #button to go back to the previous window

        LoginLabel = Label( self.LC,
                                 text = 'Login',
                                 fg = 'yellow',
                                 bg = '#00008B',
                                 font = ('Courir', 30, 'italic', 'bold')) #Label to indicate the purpose of the screen

        self.Username = Entry( self.LC,
                               width = 100,
                               borderwidth = 5 ) #Creates an entry field within which the user can enter their username 

        self.Password = Entry( self.LC,
                               width = 100,
                               borderwidth = 5 ) #Creates an entry field within which the user can enter their password

        UnLabel = Label( self.LC,
                              text = 'Username: ',
                              fg = 'yellow',
                              bg = '#00008B',
                              font = ('Courir', 10))

        PwLabel = Label( self.LC,
                              text = 'Password: ',
                              fg = 'yellow',
                              bg = '#00008B',
                              font = ('Courir', 10))





        #Places all the buttons in their appropriate places on the GUI

        Clear.place(x = 100, y = 250)
        Enter.place(x = 250, y = 250)
        Back.place(x = 10, y = 450)

        LoginLabel.place(x = 100, y = 100)

        self.Username.place(x = 100, y = 150)
        self.Password.place(x = 100, y = 200)

        UnLabel.place(x = 20, y = 150)
        PwLabel.place(x = 20, y = 200)       


class LoginPlumber:

    def __init__(self): #initialises the attribues which are local to the class

        self.LP = Tk()
        self.counter = 1 #counter serves the same purpose as the LoginCustomer class

        #Creates the user interface base and assigns background colour, the title and the size
        self.LP.geometry('1000x500')
        self.LP.title('.......LOGIN.......')
        self.LP.config(bg = '#00008B')

        self.DB = DBFunctions()
        self.DB.CreateDatabase()
        self.DB.CreatePlumberTable()

        self.CreateObjects() #Call to self.CreateObject which creates the buttons and the labels and other objects on the interface

    def EnterPressed(self):

        if self.counter == 3:
            BlockedLabel = Label( self.LP,
                                  text = 'All 3 attempts used',
                                  font = ('Courir', 15),
                                  bg = '#00008B',
                                  fg = '#FF0000')

            BlockedLabel.place(x = 500, y = 370)
            BlockedLabel.after(1000, lambda: self.LP.destroy()) #closes the system for the user if all three attempts used

        #Gets the data entered into the username and password entry fields from self.CreateObjects
        username = self.Username.get()
        password = self.Password.get()
        certNo = self.Certificate.get()
        PlumberID = self.DB.FindPlumber(username, password, certNo)#attempts to find the plumber in the database using information which is unique

        #checks if there is a plumber existing with these credentials
        if len(PlumberID) != 1:
            PlumberLabel = Label( self.LP,
                               text = 'Plumber not found',
                               font = ('Courir', 10),
                               fg = '#FF0000',
                               bg = '#00008B')
            PlumberLabel.place(x=850, y=210)
            PlumberLabel.after(1000, lambda: PlumberLabel.destroy())

            self.counter = self.counter + 1

        else:
            #gets the plumberID and goes to the Plumber dashboard, closing the database connection and the login window
            self.plumberID = PlumberID[0][0]
            self.DB.close()
            self.LP.destroy()
            PlumberDashboard(self.plumberID)


    def clearPressed(self):

        #Clears all the data entered into the fields

        self.Username.delete(0, END) 
        self.Password.delete(0, END)
        self.Certificare.delete(0, END)

    def Back(self):
        self.LP.destroy()
        self.DB.close()
        LoginOrRegister('1') #indicates that the user is still a plumber

    def CreateObjects(self):

        self.Username = Entry( self.LP,
                          width = 100,
                          borderwidth = 5 ) #Entry field where user can type their username

        self.Password = Entry( self.LP,
                          width = 100,
                          borderwidth = 5 ) #Entry field where user can type their password

        self.Certificate = Entry( self.LP,
                                  width = 100,
                                  borderwidth = 5) #Entry field where user can type their certification number

        usernameLabel = Label( self.LP,
                                    text = 'Username: ',
                                    bg = '#00008B',
                                    fg = 'yellow',
                                    font = ('Courir', 10, 'italic', 'bold')) #indicates which field to enter the username in
        passwordLabel = Label( self.LP,
                                    text = 'Password: ',
                                    bg = '#00008B',
                                    fg = 'yellow',
                                    font = ('Courir', 10, 'italic', 'bold')) #indicates which field to enter the password in
        certificateLabel = Label( self.LP,
                                    text = 'City And Guilds Certificate No: ',
                                    bg = '#00008B',
                                    fg = 'yellow',
                                    font = ('Courir', 10, 'italic', 'bold')) #indicates which field to enter the ceretification number in

        Label_LOGIN = Label( self.LP,
                        text = "LOGIN",
                        bg = "#00008B",
                        fg = "yellow",
                        font = ("Courier", 40, "italic", "bold")) #indicates the purpose of the entire GUI page

        Button_enter = Button( self.LP,
                           text = "Enter",
                           font = ("Courier", 20),
                           command = lambda: self.EnterPressed() ) #Allows the user to confirm their details

        Button_clear = Button( self.LP,
                           text = "Clear",
                           font = ("Courier", 20),
                           command = lambda: self.clearPressed() ) #Allows the user to clear all the data in all fields


        Back = Button( self.LP,
                            text = 'Back',
                            font = ('Courir', 10),
                            command = lambda: self.Back()) #Returns the user back to the previous window
 


        #Placing each object for the interface onto the root 

        self.Username.place(x = 210, y = 130)
        self.Password.place(x = 210, y = 170)
        self.Certificate.place(x = 210, y = 210)

        usernameLabel.place(x = 70, y = 130)
        passwordLabel.place(x = 70, y = 170)
        certificateLabel.place(x = 3, y = 210)

        Label_LOGIN.place(x = 150, y = 50)

        
        Button_enter.place(x = 250, y = 250)

        Button_clear.place(x = 100, y = 250)

        Back.place(x = 10, y = 450)

        return

class collectPlumberInfo:

    def __init__(self, PlumberID):

        self.plumberID = PlumberID
        #will be used to indicate whether the plumber has entered a valid area of expertise
        self.skills = ['Boiler', 'Radiator', 'Taps', 'Water cylinder/tank', 'Toilet', 'Pipes' ] 

        self.Collect = Tk()
        self.Collect.geometry('800x700')
        self.Collect.title('Collect Info')
        self.Collect.config(bg = '#00008B')

        self.DB = DBFunctions()
        self.DB.CreateDatabase()

        self.CreateObjs()

    def CreateObjs(self):

        #Creates Tkinter objects for this window

        CollectLabel = Label( self.Collect,
                              text = 'Additional Information:',
                              fg = 'yellow',
                              bg = '#00008B',
                              font = ('Courir', 20, 'bold', 'italic'))

        SkillLabel = Label( self.Collect,
                            text = 'Enter Expertise (not number):',
                            fg = 'yellow',
                            bg = '#00008B',
                            font = ('Courir', 15, 'bold', 'italic'))

        self.skill = Entry( self.Collect,
                            width = 40,
                            borderwidth = 5)

        skill1 = Label( self.Collect,
                              text = '1. Boiler',
                              font = ('Courir', 10),
                              fg = 'yellow',
                              bg = '#00008B')
        
        skill2 = Label( self.Collect,
                              text = '2. Radiator',
                              font = ('Courir', 10),
                              fg = 'yellow',
                              bg = '#00008B')
        skill3 = Label( self.Collect,
                              text = '3. Taps',
                              font = ('Courir', 10),
                              fg = 'yellow',
                              bg = '#00008B')

        skill4 = Label( self.Collect,
                              text = '4. Water cylinder/tank',
                              font = ('Courir', 10),
                              fg = 'yellow',
                              bg = '#00008B')

        skill5 = Label( self.Collect,
                              text = '5. Toilets',
                              font = ('Courir', 10),
                              fg = 'yellow',
                              bg = '#00008B')

        skill6 = Label( self.Collect,
                              text = '6. Pipes',
                              font = ('Courir', 10),
                              fg = 'yellow',
                              bg = '#00008B')

        #Entry boxes to enter typical start/end times

        self.startTime = Entry( self.Collect,
                                width = 40,
                                borderwidth = 5)

        self.endTime = Entry( self.Collect,
                              width = 40,
                              borderwidth = 5)



        StartTimeLabel = Label( self.Collect,
                            text = 'Enter your typical daily starting time:',
                            fg = 'yellow',
                            bg = '#00008B',
                            font = ('Courir', 15, 'bold', 'italic'))

        EndTimeLabel = Label( self.Collect,
                            text = 'Enter your typical daily finishing time:',
                            fg = 'yellow',
                            bg = '#00008B',
                            font = ('Courir', 15, 'bold', 'italic'))

        Back = Button( self.Collect,
                       text = 'Back',
                       font = ('Courir', 10),
                       command = lambda: self.Back())

        Enter = Button( self.Collect,
                        text = 'Enter',
                        font = ('Courir', 12),
                        command = lambda: self.Enter())

        #Entry boxes to enter pricing scheme
        self.HRate = Entry( self.Collect,
                            width = 10,
                            borderwidth = 5)

        self.DRate = Entry( self.Collect,
                            width = 10,
                            borderwidth = 5)

        self.SFee = Entry( self.Collect,
                            width = 10,
                            borderwidth = 5)

        HRLabel = Label( self.Collect,
                         text = 'Hourly Rate:',
                         fg = 'yellow',
                         bg = '#00008B',
                         font = ('Courir', 10))

        DRLabel = Label( self.Collect,
                         text = 'Daily Rate:',
                         fg = 'yellow',
                         bg = '#00008B',
                         font = ('Courir', 10))


        SFLabel = Label( self.Collect,
                         text = 'Standard Fee:',
                         fg = 'yellow',
                         bg = '#00008B',
                         font = ('Courir', 10))
        
        #places each object onto the new screen
        CollectLabel.place(x=100, y=20)
        SkillLabel.place(x=20, y=140)
        self.skill.place(x=20, y=200)
        skill1.place(x=70, y=250)
        skill2.place(x=70, y=300)
        skill3.place(x=70, y=350)
        skill4.place(x=70, y=400)
        skill5.place(x=70, y=450)
        skill6.place(x=70, y=500)
        StartTimeLabel.place(x=350, y=100)
        self.startTime.place(x=350, y=150)
        EndTimeLabel.place(x=350, y=250)
        self.endTime.place(x=350, y=300)
        self.HRate.place(x=350, y=500)
        self.DRate.place(x=460, y=500)
        self.SFee.place(x=570, y=500)
        HRLabel.place(x=350, y=425)
        DRLabel.place(x=450, y=425)
        SFLabel.place(x=550, y=425)
        Back.place(x=10, y=650)
        Enter.place(x=300, y=600)

    def Back(self):

        #if the plumber chooses to go back to the registration screen, it removes any details previously entered in the registration part
        self.DB.removePlumber(self.plumberID) 
        self.DB.close()
        self.Collect.destroy()
        RegisterPlumber()

    def Enter(self):

        #gets all data from entry boxes and sets time format for converting times to datetime objects
        StartTime = self.startTime.get()
        EndTime = self.endTime.get()
        skill = self.skill.get()
        DR = self.DRate.get()
        HR = self.HRate.get()
        SF = self.SFee.get()
        timeFormat = '%H:%M'
        try:
            #attempts to convert the prices to float as a type check
            DR = float(DR)
            HR = float(HR)
            SF = float(SF)

            #checks if the times provided are valid times by attempting to convert them into a datetime object
            STime = datetime.strptime(StartTime, timeFormat)
            ETime = datetime.strptime(EndTime, timeFormat)

            
            #checks if the skill area entered matches to one in the list self.skills
            if skill in self.skills:
                skill = skill.lower()

                #updates the record with the correct plumberID to have this information stored there
                self.DB.AddPlumberOtherInfo(self.plumberID, skill, HR, DR, SF, StartTime, EndTime) 
                self.DB.close()
                self.Collect.destroy()
                PlumberDashboard(self.plumberID) #moves to the plumber dashboard for this user 

            else:
                #displays an error message to indicate the skill entered isnt valid
                errorLabel = Label( self.Collect,
                                    text = 'Skill is not part of the given list',
                                    fg = 'red',
                                    bg = '#00008B',
                                    font = ('Courir', 10))
                errorLabel.place(x=50, y=550)
                errorLabel.after(1000, lambda: errorLabel.destroy()) 

        except ValueError:
            #gives the user a prompt to ensure all information is entered in a valid format
            errorLabel = Label( self.Collect,
                                    text = 'Please ensure times are in HH:MM format, and rates/fees in the correct form',
                                    fg = 'red',
                                    bg = '#00008B',
                                    font = ('Courir', 10))
            errorLabel.place(x=50, y=550)
            errorLabel.after(1000, lambda: errorLabel.destroy())

class PlumberDashboard:

    def __init__(self, plumberID):

        self.plumberID = plumberID

        #Creates the plumber dashboard
        self.PD = Tk()
        self.PD.geometry('1800x800')
        self.PD.title('Plumber Dashboard')
        self.PD.config(bg = '#00008B')

        #creates the meeting table (needed for the first meeting since the table won't exist if no meetings have been made)
        self.DB = DBFunctions()
        self.DB.CreateDatabase()
        self.DB.CreateUserTable()
        self.DB.CreateMeetingTable() 

        self.checkForPastMeetings()
        self.CreateDashboard()

    def CreateDashboard(self):

        #The table which will show any upcoming appointments a plumber has with the relevant information
        self.Appointments = ttk.Treeview(self.PD, columns = ('CID', 'Postcode', 'date', 'time', 'ExpandedIssue'))
        self.Appointments.heading('#0', text = 'MeetingID')
        self.Appointments.heading('CID', text = 'CustomerID')
        self.Appointments.heading('Postcode', text = 'Postcode')
        self.Appointments.heading('date', text = 'Appointment Date')
        self.Appointments.heading('time', text = 'Appointment Time')
        self.Appointments.heading('ExpandedIssue', text = 'Issue message')

        #Creates the buttons which will contain the functionalities of the dashboard
        CancelBooking = Button( self.PD,
                              text='Cancel booking',
                              font=('Courir', 15),
                              command = lambda: self.cancel())

        UpdatePricing = Button( self.PD,
                                   text='Update Pricing',
                                   font=('Courir', 15),
                                   command = lambda: self.updatePrices())
        Pending = Button( self.PD,
                            text = 'Pending meetings',
                            font = ('Courir', 15),
                            command = lambda: self.AccOrRej())

        Completed = Button( self.PD,
                            text = 'Mark meeting as completed',
                            font = ('Courir', 15),
                            command = lambda: self.MarkAsCompleted())

        logout = Button( self.PD,
                              text='logout',
                              font=('Courir', 10),
                              command = lambda: self.logout())

        #label to indicate this is the main dashboard
        DashboardLabel = Label( self.PD,
                                     text='Plumber Dashboard',
                                     fg = 'yellow',
                                     bg = '#00008B',
                                     font = ('Courir', 30, 'italic', 'bold'))

        #Displaying the plumber's average review
        AVGReviewLabel = Label( self.PD,
                                     text='Average Review:',
                                     fg = 'yellow',
                                     bg = '#00008B',
                                     font = ('Courir', 10, 'bold'))
        AR = str(round(self.DB.getAverageReview(self.plumberID), 2))
        self.AVGReview = Label( self.PD,
                           text = AR+'/5',
                           fg = 'yellow',
                           bg = '#00008B',
                           font = ('Courir', 10, 'bold'))

        #places all tkinter objects onto the dashboard screen
        self.Appointments.place(x=10, y=200)
        logout.place(x=10, y=700)
        UpdatePricing.place(x=1220, y=200)
        CancelBooking.place(x=1220, y=260)
        Pending.place(x=1220, y=320)
        Completed.place(x=1220, y=380)
        DashboardLabel.place(x=50, y=100)
        AVGReviewLabel.place(x=1400, y=260)
        self.AVGReview.place(x=1450, y=300)
        

        #calls this method to fill the Appointment table with any upcoming appointments
        self.FillUpcomingTable()

    def refreshReview(self):

        AR = str(round(self.DB.getAverageReview(self.plumberID), 2))
        self.AVGReview.config(text = AR+'/5')
        

    def updatePrices(self):

        #removes the dashboard window from the user's screen and creates the new window for updating prices
        self.PD.withdraw() 

        self.UPrice = Tk()
        self.UPrice.geometry('700x500')
        self.UPrice.config(bg = '#00008B')

        #Entry boxes which will be used to enter the new pricing scheme
        self.USF = Entry( self.UPrice,
                            width = 25,
                            borderwidth = 5)
        self.UHR = Entry( self.UPrice,
                            width = 25,
                            borderwidth = 5)
        self.UDR = Entry( self.UPrice,
                            width = 25,
                            borderwidth = 5)
        
        #Labels to indicate the purpose of the screen/entry boxes        
        PriceLabel = Label( self.UPrice,
                         text = 'Update Pricing: ',
                         font = ('Courir', 20, 'bold', 'italic'),
                         fg = 'yellow',
                         bg = '#00008B')
        SF = Label( self.UPrice,
                         text = 'Standard Fee: ',
                         font = ('Courir', 10),
                         fg = 'yellow',
                         bg = '#00008B')
        HR = Label( self.UPrice,
                         text = 'Hourly Rate: ',
                         font = ('Courir', 10),
                         fg = 'yellow',
                         bg = '#00008B')
        DR = Label( self.UPrice,
                         text = 'Daily Rate: ',
                         font = ('Courir', 10),
                         fg = 'yellow',
                         bg = '#00008B')
        
        #Enter and close button to either return to the dashboard, or confirm new prices
        Enter = Button( self.UPrice,
                         text = 'Enter',
                         font = ('Courir', 10),
                         command = lambda: self.EnterPrices())

        close = Button( self.UPrice,
                         text = 'Back',
                         font = ('Courir', 10),
                         command = lambda: self.closeUPrice())
 
        #places objects onto the window
        PriceLabel.place(x=50, y=20)
        SF.place(x=30, y=120)
        HR.place(x=30, y=200)
        DR.place(x=30, y=280)
        self.USF.place(x=130, y=120)
        self.UHR.place(x=130, y=200)
        self.UDR.place(x=130, y=280)
        Enter.place(x=180, y=350)
        close.place(x=10, y=450)

    def EnterPrices(self):

        #retrieves all data entered into the entry boxes
        SF = self.USF.get()
        HR = self.UHR.get()
        DR = self.UDR.get()
        try:
            #Attempts to convert each price to a float as a type check
            SF = float(SF)
            HR = float(HR)
            DR = float(DR)

            if SF>=0 and HR>0 and DR>0: #checks all prices are above zero or at least zero
                self.DB.UpdatePricing(self.plumberID, SF, HR, DR)
                Valid = Label( self.UPrice,
                               text = 'Pricing Updated',
                               bg = '#00008B',
                               fg = '#FF0000',
                               font = ('Courir', 10))
                Valid.place(x=405,y=200)
                Valid.after(500, lambda: Valid.destroy()) #displays that the prices have been updated
                self.closeUPrice() #calls this method to close the UPrice window
            
        except ValueError:
            #if prices are invalid and not of the correct type, an error label will appear
            Error = Label( self.UPrice,
                           text = 'Prices should either be in integer or decimal format',
                           bg = '#00008B',
                           fg = '#FF0000',
                           font = ('Courir', 10))
            Error.place(x=375,y=200)
            Error.after(1000, lambda: Error.destroy()) 

    def FillUpcomingTable(self):

        #deletes any existing information in the Appointments table
        for appt in self.Appointments.get_children():
            self.Appointments.delete(appt) 

        #gets all the appt information for that plumber 
        ApptInfo = self.DB.getAccepted(self.plumberID)

        try:
            #attempts to add this information to the Appointments table
            length = len(ApptInfo)
            for i in range(0, length):
                Appt = ApptInfo[i]
                Data = (Appt['MeetingID'], Appt['CID'], Appt['Postcode'], Appt['Date'], Appt['Time'], Appt['Issue'])
                self.Appointments.insert('', '0', text  = Data[0], values = Data[1:])
            
        except:
            pass

    def closeUPrice(self):

        self.UPrice.withdraw() #removes the window from the user's screen
        self.PD.deiconify() #reopens the plumber dashboard
        self.checkForPastMeetings() #will be explained later within the method
        self.refreshReview() #refreshes the plumber review

    def BackCancel(self):

        self.CancelWindow.withdraw() #removes the window from the user's screen
        self.PD.deiconify() #reopens the plumber dashboard
        self.checkForPastMeetings() #will be explained later within the method
        self.FillUpcomingTable() #updates the Appointments table on the dashboard
        self.refreshReview() #refreshes the plumber review

    def cancel(self):

        self.PD.withdraw() #removes the plumber dashboard from the user's screen

        #creates the cancellation window
        self.CancelWindow = Tk()
        self.CancelWindow.geometry('400x250')
        self.CancelWindow.title('Cancel Booking')
        self.CancelWindow.config(bg = '#00008B')

        #MeetingID entry box for the user to enter the ID of the meeting they wish to cancel
        self.MeetingIDCancel = Entry( self.CancelWindow,
                                      width = 20,
                                      borderwidth = 5)

        
        #Enter and Back buttons to either confirm the meeting to cancel or to return to the plumber dashboard
        Enter = Button( self.CancelWindow,
                        text = 'Enter',
                        font = ('Courir', 10),
                        command = lambda: self.AttemptToCancel())

        Back = Button( self.CancelWindow,
                       text = 'Back',
                       font = ('Courir', 10),
                       command = lambda: self.BackCancel())

        #Labels identify the purpose of the window/entry box
        CancelLabel = Label( self.CancelWindow,
                             text = 'Cancel Meeting:',
                             fg = 'yellow',
                             bg = '#00008B',
                             font = ('Courir', 25, 'bold', 'italic'))


        MeetingIDLabel = Label(self.CancelWindow,
                             text = 'MeetingID:',
                             fg = 'yellow',
                             bg = '#00008B',
                             font = ('Courir', 10))

        
        #places the tkinter objects onto the CancelWindow
        self.MeetingIDCancel.place(x=130, y=100)
        Enter.place(x=280, y=100)
        Back.place(x=10, y=200)
        CancelLabel.place(x=20, y=30)
        MeetingIDLabel.place(x=10, y=100)

    def AttemptToCancel(self):

        #retrieves the MeetingID entered by the user
        MeetingID = self.MeetingIDCancel.get()
        #outlines the date and time format which the information in the meeting table is stored as
        date_format = '%Y-%m-%d'
        time_format = '%H:%M:%S'

        try:
            #converts the meetingID to an integer and attempts to see if it is a valid meeting that is allocated to this particular plumber
            MeetingID = int(MeetingID)
            MeetingIDs = self.DB.getAllMeetingIDsPlumber(self.plumberID)
            if MeetingID in MeetingIDs:
                #extracts that meeting date and time and converts them to datetime objects
                DateAndTime = self.DB.getMeetingInfo(MeetingID)
                Date = str(DateAndTime[0])
                Time = str(DateAndTime[1])
                Date = datetime.strptime(Date, date_format).date()
                Time = datetime.strptime(Time, time_format).time()

                #gets the current date and time
                currentDateTime = datetime.now()
                currentDate = currentDateTime.date()
                currentTime = currentDateTime.time()

                #checks if the current date is the same as the meeting date 
                if currentDate == Date:

                    #creates timedelta objects for both the current and meeting times, and subtracts them and extracts the absolute value, ignorong any negative values 
                    currentDelta = timedelta(hours = currentTime.hour, minutes = currentTime.minute)
                    MeetingDelta = timedelta(hours = Time.hour, minutes = Time.minute)

                    if currentDelta > MeetingDelta:
                        timeDiff = abs(currentDelta-MeetingDelta)

                        #if the times are less than 2 hours apart, the cancellation is not allowed
                        if timeDiff < timedelta(hours=2):
                            errorLabel = Label( self.CancelWindow,
                                            text = 'Cancellations must be made two hours in advance',
                                            bg = '#00008B',
                                            fg = '#FF0000',
                                            font = ('Courir', 10))
                            errorLabel.place(x=20,y=160)
                            errorLabel.after(500, lambda: errorLabel.destroy())

                        #if the times are more than two hours apart, it is allowed and the status of the meeting is changed to cancelled
                        else:
                            ValidLabel = Label( self.CancelWindow,
                                            text = 'Meeting cancelled',
                                            bg = '#00008B',
                                            fg = '#FF0000',
                                            font = ('Courir', 10))
                            ValidLabel.place(x=20,y=160)
                            ValidLabel.after(1000, lambda: ValidLabel.destroy())
                            status = 'Cancelled'
                            self.DB.updateMeetingStatus(status, MeetingID)

                    else:
                        errorLabel = Label( self.CancelWindow,
                                            text = 'This meeting has already passed',
                                            bg = '#00008B',
                                            fg = '#FF0000',
                                            font = ('Courir', 10))
                        errorLabel.place(x=20,y=160)
                        errorLabel.after(500, lambda: errorLabel.destroy())

                        
                #if the current date is greater than the meeting date, this means the meeting date is past and cannot be cancelled and displays an error label 
                elif currentDate > Date:
                    errorLabel = Label( self.CancelWindow,
                                        text = 'Meeting date already passed',
                                        bg = '#00008B',
                                        fg = '#FF0000',
                                        font = ('Courir', 10))
                    errorLabel.place(x=20,y=160)
                    errorLabel.after(500, lambda: errorLabel.destroy())

                #if the current date is less than the meeting date, the meeting can be cancelled
                else:
                    ValidLabel = Label( self.CancelWindow,
                                        text = 'Meeting cancelled',
                                        bg = '#00008B',
                                        fg = '#FF0000',
                                        font = ('Courir', 10))
                    ValidLabel.place(x=20,y=160)
                    ValidLabel.after(1000, lambda: ValidLabel.destroy())
                    status = 'Cancelled'
                    self.DB.updateMeetingStatus(status, MeetingID)
                    
            #if the meetingID is not valid for this specific plumber, an error label is shown
            else:
                errorLabel = Label( self.CancelWindow,
                                        text = 'MeetingID is not valid',
                                        bg = '#00008B',
                                        fg = '#FF0000',
                                        font = ('Courir', 10))
                errorLabel.place(x=20,y=160)
                errorLabel.after(500, lambda: errorLabel.destroy())                

        #an error label is shown if there are any errors with the type of the meetingID
        except ValueError:
            errorLabel = Label( self.CancelWindow,
                                        text = 'Ensure all data is of a valid type',
                                        bg = '#00008B',
                                        fg = '#FF0000',
                                        font = ('Courir', 10))
            errorLabel.place(x=20,y=160)
            errorLabel.after(500, lambda: errorLabel.destroy())

    def AccOrRej(self):

        #removes the plumber dashboard from the user's screen
        self.PD.withdraw()

        #Creates the new accept or reject window
        self.AorR = Tk()
        self.AorR.geometry('1600x800')
        self.AorR.title('Accept or Reject')
        self.AorR.config(bg = '#00008B')

        #Creates a table to show all the pending meetings a plumber has
        self.pending = ttk.Treeview(self.AorR, columns = ('CustomerID', 'Postcode', 'Date', 'Time', 'Issue'))
        self.pending.heading('#0', text = 'MeetingID')
        self.pending.heading('CustomerID', text = 'CustomerID')
        self.pending.heading('Postcode', text = 'Postcode')
        self.pending.heading('Date', text = 'Date')
        self.pending.heading('Time', text = 'Time')
        self.pending.heading('Issue', text = 'Expanded Issue')

        #Entry box used to enter the meetingID of the meeting to accept or reject
        self.MeetingIDAorR = Entry( self.AorR,
                                    width = 20,
                                    borderwidth = 5)
        
        #Buttons to either accept or reject the meeting, or to go back to the dashboard
        Accept = Button( self.AorR,
                         text = 'Accept',
                         font = ('Courir', 20),
                         command = lambda: self.Accept())

        Reject = Button( self.AorR,
                         text = 'Reject',
                         font = ('Courir', 20),
                         command = lambda: self.Reject())

        Back = Button( self.AorR,
                       text = 'Back',
                       font = ('Courir', 10),
                       command = lambda: self.BackAorR())

        #Labels which indicate the purpose of the window/entry boxes
        MeetingIDLabel = Label( self.AorR,
                                text = 'MeetingID: ',
                                fg = 'yellow',
                                bg = '#00008B',
                                font = ('Courir', 10))

        AorRLabel = Label( self.AorR,
                           text = 'Accept or Reject',
                           fg = 'yellow',
                           bg = '#00008B',
                           font = ('Courir', 25, 'bold', 'italic'))

        #places tkinter objects onto the AorR window
        self.pending.place(x=50, y=120)
        AorRLabel.place(x=100, y=20)
        Accept.place(x=30, y=500)
        Reject.place(x=190, y=500)
        MeetingIDLabel.place(x=50, y=400)
        self.MeetingIDAorR.place(x=135, y=400)
        Back.place(x=10, y=700)
        self.FillPendingTable()

    def FillPendingTable(self):

        #deletes anything which was already held in this table
        for appt in self.pending.get_children():
            self.pending.delete(appt)

        #gets new pending meeting information
        PendingInfo = self.DB.getPending(self.plumberID)

        try:
            #attempts to add all pending meetings to the Pending table
            length = len(PendingInfo)
            for i in range(0, length):
                Appt = PendingInfo[i]
                Data = (Appt['MeetingID'], Appt['CID'], Appt['Postcode'], Appt['Date'], Appt['Time'], Appt['Issue'])
                self.pending.insert('', '0', text  = Data[0], values = Data[1:])
            
        except:
            pass
        
    def logout(self):
        
        self.PD.destroy() #destroys the plumber dashboard
        self.DB.close() #closes the database connection
        LoginPlumber() #returns the user to the login screen

    def Accept(self):

        try:
            #attempts to convert the meetingID entered to an integer, and retrieves all the meetingIDs that have status pending for this plumber
            MeetingID = int(self.MeetingIDAorR.get())
            MeetingIDs = self.DB.getPendingMeetingIDs(self.plumberID)

            #if the MeetingID is assigned to this plumber and the status of the meeting is Pending, update the status to Accepted
            if MeetingID in MeetingIDs:
                status = "Accepted"
                self.DB.updateMeetingStatus(status, MeetingID)
                AcceptedLabel = Label( self.AorR,
                                    text = 'Meeting Accepted',
                                    fg = '#FF0000',
                                    bg = '#00008B',
                                    font = ('Courir', 10))
                AcceptedLabel.place(x=1300, y=550)
                AcceptedLabel.after(1000, lambda: AcceptedLabel.destroy())

               #if it is not assigned to this plumber, displays an error message saying the entered MeetingID is not valid 
            else:
                errorLabel = Label( self.AorR,
                                        text = 'MeetingID not Valid',
                                        fg = '#FF0000',
                                        bg = '#00008B',
                                        font = ('Courir', 10))
                errorLabel.place(x=1300, y=550)
                errorLabel.after(1000, lambda: errorLabel.destroy())

        #if the meetingID is not of the correct type, displays an error message
        except ValueError:
            errorLabel = Label( self.AorR,
                                    text = 'MeetingID is not an integer',
                                    fg = '#FF0000',
                                    bg = '#00008B',
                                    font = ('Courir', 10))
            errorLabel.place(x=1300, y=550)
            errorLabel.after(1000, lambda: errorLabel.destroy())

    def Reject(self):

        try:
            #Checks if MeetingID is an integer, and gets all Pending MeetingIDs 
            MeetingID = int(self.MeetingIDAorR.get())
            MeetingIDs = self.DB.getPendingMeetingIDs(self.plumberID)

            #checks if MeetingID is assigned to that plumber and is a pending meeting
            if MeetingID in MeetingIDs:
                #Sets this meeting status to rejected and displays a label on the screen to indicate this
                status = "Rejected"
                self.DB.updateMeetingStatus(status, MeetingID)
                RejectedLabel = Label( self.AorR,
                                    text = 'Meeting Rejected',
                                    fg = '#FF0000',
                                    bg = '#00008B',
                                    font = ('Courir', 10))
                RejectedLabel.place(x=1300, y=550)
                RejectedLabel.after(1000, lambda: RejectedLabel.destroy())

               #if it is not assigned to this plumber, displays an error message saying the entered MeetingID is not valid 
            else:
                errorLabel = Label( self.AorR,
                                        text = 'MeetingID not Valid',
                                        fg = '#FF0000',
                                        bg = '#00008B',
                                        font = ('Courir', 10))
                errorLabel.place(x=1300, y=550)
                errorLabel.after(1000, lambda: errorLabel.destroy())

                
        except ValueError:
            #shows an error on the screen if the MeetingID cannot be converted to integer
            errorLabel = Label( self.AorR,
                                    text = 'MeetingID is not an integer',
                                    fg = '#FF0000',
                                    bg = '#00008B',
                                    font = ('Courir', 10))
            errorLabel.place(x=1300, y=550)
            errorLabel.after(1000, lambda: errorLabel.destroy())
        
    def BackAorR(self):

        self.AorR.withdraw() #removes the Accept or reject window from the user's screen
        self.PD.deiconify() #brings the Plumber Dashboard back onto the screen
        self.checkForPastMeetings() #Checks for any pending meetings which have expired
        self.FillUpcomingTable() #updates the Appointments table on the dashboard
        self.refreshReview() #refreshes the plumber review
        
    def MarkAsCompleted(self):

        #Remove the plumber dashboard and creates the window to mark a meeting as completed
        self.PD.withdraw() 

        self.Completed = Tk()
        self.Completed.geometry('1900x700')
        self.Completed.title('Accept or Reject')
        self.Completed.config(bg = '#00008B')

        self.accepted = ttk.Treeview(self.Completed, columns = ('CustomerID', 'Postcode', 'Date', 'Time'))
        self.accepted.heading('#0', text = 'MeetingID')
        self.accepted.heading('CustomerID', text = 'CustomerID')
        self.accepted.heading('Postcode', text = 'Postcode')
        self.accepted.heading('Date', text = 'Date')
        self.accepted.heading('Time', text = 'Time')

        #Entry box to allow the meetingID of the meeting to mark as completed
        self.C_MeetingID = Entry( self.Completed,
                                    width = 20,
                                    borderwidth = 5)

        #links to the function that validates if it can be marked as completed
        Completed = Button( self.Completed,
                         text = 'Completed',
                         font = ('Courir', 10),
                         command = lambda: self.CompletedMeetings())
        
        #Describes what the screen/entry box is for 
        MeetingIDLabel = Label( self.Completed,
                                text = 'MeetingID: ',
                                fg = 'yellow',
                                bg = '#00008B',
                                font = ('Courir', 10))

        CompletedLabel = Label( self.Completed,
                           text = 'Mark as Completed: ',
                           fg = 'yellow',
                           bg = '#00008B',
                           font = ('Courir', 20, 'bold', 'italic'))

        Back = Button( self.Completed,
                       text = 'Back',
                       font = ('Courir', 10),
                       command = lambda: self.BackCompleted())
        
        #places Tkinter objects onto the Completed window
        self.accepted.place(x=50, y=120)
        CompletedLabel.place(x=20, y=20)
        Completed.place(x=1300, y=200)
        MeetingIDLabel.place(x=1100, y=100)
        self.C_MeetingID.place(x=1100, y=200)
        Back.place(x=10, y=550)
        self.FillAcceptedTable()

    def CompletedMeetings(self):

        #date and time formats which will be used when converting meeting date and time to datetime objects
        Date_format = '%Y-%m-%d'
        Time_format = '%H:%M:%S'

        try:
            #Attempts to convert MeetingID to an integer and extracts all accepted meetingIDs from the acceptedInfo variable above
            MeetingID = self.C_MeetingID.get()
            MeetingID = int(MeetingID)
            length = len(self.acceptedInfo)
            MeetingIDs = []
            for i in range(0, length):
                appt = self.acceptedInfo[i]
                ApptMeetingID = appt['MeetingID']
                MeetingIDs.append(ApptMeetingID)

            #checks MeetingID entered by user is part of the accepted meetingIDs, and finding the date and time of the meeting entered 
            if MeetingID in MeetingIDs:
                for i in range(0, length):
                    appt = self.acceptedInfo[i]
                    if appt['MeetingID'] == MeetingID:
                        MeetingDate = appt['Date']
                        MeetingTime = appt['Time']

                #converting meeting date and time to datetime objects, and getting the current date and tome
                MeetingDate = datetime.strptime(MeetingDate, Date_format).date()
                MeetingTime = datetime.strptime(MeetingTime, Time_format)
                MTime = MeetingTime.time()
                
                current = datetime.now()
                CTime = current.time()
                CDate = current.date()

                #if the current date is after the meeting date, meeting cannot be marked as completed
                if CDate < MeetingDate:
                    errorLabel = Label( self.Completed,
                                    text = 'Meeting date not passed yet',
                                    fg = 'red',
                                    bg = '#00008B',
                                    font = ('Courir', 10))
                    errorLabel.place(x=1300, y=250)
                    errorLabel.after(1000, lambda: errorLabel.destroy())

                #if the current date is equal to the meeting date, check times
                elif CDate == MeetingDate:
                    currentDelta = timedelta(hours = CTime.hour, minutes = CTime.minute)
                    MeetingDelta = timedelta(hours = MTime.hour, minutes = MTime.minute)
                    if MeetingDelta < currentDelta:
                        timeDiff = abs(currentDelta-MeetingDelta)
                        #if the current time is after the meeting time, cannot cancel meeting
                        if timeDiff < timedelta(hours=1):
                            errorLabel = Label( self.Completed,
                                            text = 'Must be done at least an hour after the meeting',
                                            fg = 'red',
                                            bg = '#00008B',
                                            font = ('Courir', 10))
                            errorLabel.place(x=1120, y=250)
                            errorLabel.after(1000, lambda: errorLabel.destroy())

                        else:
                            #marks meeting as completed in the database and shows that the meeting has been cancel
                            status = 'Completed'
                            self.DB.updateMeetingStatus(status, MeetingID)
                            Completed = Label( self.Completed,
                                            text = 'Marked as completed',
                                            fg = 'red',
                                            bg = '#00008B',
                                            font = ('Courir', 10))
                            Completed.place(x=1300, y=250)
                            Completed.after(1000, lambda: Completed.destroy())


                else:
                    #marks meeting as completed in the database and shows that the meeting has been cancel
                    status = 'Completed'
                    self.DB.updateMeetingStatus(status, MeetingID)
                    Completed = Label( self.Completed,
                                        text = 'Marked as completed',
                                        fg = 'red',
                                        bg = '#00008B',
                                        font = ('Courir', 10))
                    Completed.place(x=1300, y=250)
                    Completed.after(1000, lambda: Completed.destroy())
                    self.BackCompleted()

            else:
                #if the MeetingID is of a valid type but doesn't exist for the plumber
                errorLabel = Label( self.Completed,
                                    text = 'MeetingID is invalid',
                                    fg = 'red',
                                    bg = '#00008B',
                                    font = ('Courir', 10))
                errorLabel.place(x=1300, y=250)
                errorLabel.after(1000, lambda: errorLabel.destroy())

        #if there are any errors with the MeetingID entered an error message is displayed         
        except ValueError:
            errorLabel = Label( self.Completed,
                                        text = 'invalid MeetingID',
                                        fg = 'red',
                                        bg = '#00008B',
                                        font = ('Courir', 10))
            errorLabel.place(x=1300, y=250)
            errorLabel.after(1000, lambda: errorLabel.destroy()) 

    def FillAcceptedTable(self):

        #removes the appointments in the table currently

        for appt in self.accepted.get_children():
            self.accepted.delete(appt)

        #gets all accepted meetings for the plumber 
        self.acceptedInfo = self.DB.getAccepted(self.plumberID)

        try:
            #attempts to add the meeting information to the table 
            length = len(self.acceptedInfo)
            for i in range(0, length):
                Appt = self.acceptedInfo[i]
                Data = (Appt['MeetingID'], Appt['CID'], Appt['Postcode'], Appt['Date'], Appt['Time'], Appt['Issue'])
                self.accepted.insert('', '0', text  = Data[0], values = Data[1:])
        
        except:
            pass

    def BackCompleted(self):
        self.Completed.withdraw() #removes the Completed window from the user's screen
        self.PD.deiconify() #displays the plumber dashboard again
        self.checkForPastMeetings() #checks for any pending meeting requests that have expired
        self.FillUpcomingTable() #updates the Appointments table on the dashboard
        self.refreshReview() #refreshes the plumber review


    def checkForPastMeetings(self):

        #format for the meeting dates and times to be converted to datetime objects
        date_format = '%Y-%m-%d'
        time_format = '%H:%M:%S'

        #gets all meetingIDs, dates and times for any pending meeting requests, and the current date and time
        MeetingDatesTimes = self.DB.getMeetingForCancellationP(self.plumberID)
        currentDateTime = datetime.now()
        currentDate = currentDateTime.date()
        currentTime = currentDateTime.time()

        #checks if there are no current pending meeting requests
        if MeetingDatesTimes == []:
            pass

        else:
            #iterates through all dates and times for all pending meetings
            for Meeting in MeetingDatesTimes:
                #extracts date and time of meeting and converts to datetime objects
                Date = Meeting['Date']
                Time = Meeting['Time']
                Date = datetime.strptime(Date, date_format).date()
                Time = datetime.strptime(Time, time_format).time()
                #if the current date is after the meeting date - set to cancelled
                if currentDate > Date:
                    MeetingID = Meeting['MeetingID']
                    status = 'Cancelled'
                    self.DB.updateMeetingStatus(status, MeetingID)
                    
                #if current date is equal to the meeting date  
                elif currentDate == Date:
                    #if the current time is after the meeting time - set to cancelled
                    if currentTime > Time:
                        MeetingID = Meeting['MeetingID']
                        status = 'Cancelled'
                        self.DB.updateMeetingStatus(status, MeetingID)

class CustomerDashboard:

    def __init__(self, customerID):

        #customerID from the login screen
        self.CustomerID = customerID

        #a list of valid issue areas 
        self.issues = ['boiler', 'radiator', 'taps', 'water cylinder/tank', 'toilet', 'pipes' ]

        #creates the main customer dashboard
        self.CD = Tk()
        self.CD.geometry('1500x600')
        self.CD.title('Customer Dashboard')
        self.CD.config(bg = '#00008B')

        #creates a connection to the database 
        self.DB = DBFunctions()
        self.DB.CreateDatabase()
        self.DB.CreateMeetingTable()
        self.DB.CreatePlumberTable()

        self.checkForPastMeetings()

        self.CreateDashboard()

    def CreateDashboard(self):

        #creates the table which contains all meeting requests, upcoming meetings, rejected meetings and completed meetings
        self.Appointments = ttk.Treeview(self.CD, columns = ('PlumberID', 'date', 'time', 'status'))
        self.Appointments.heading('#0', text = 'MeetingID')
        self.Appointments.heading('PlumberID', text = 'PlumberID')
        self.Appointments.heading('date', text = 'Appointment Date')
        self.Appointments.heading('time', text = 'Appointment Time')
        self.Appointments.heading('status', text = 'Appointment Status')


        #buttons for each of the different functionalities of the system
        CancelBooking = Button( self.CD,
                              text='Cancel booking',
                              font=('Courir', 20),
                              command = lambda: self.cancel())

        logIssue = Button( self.CD,
                                   text='Update issue',
                                   font=('Courir', 20),
                                   command = lambda: self.LogIssue())

        logout = Button( self.CD,
                              text='logout',
                              font=('Courir', 10),
                              command = lambda: self.logout())

        MakeBooking = Button( self.CD,
                                   text = 'Make Booking',
                                   font = ('Courir', 20),
                                   command = lambda: self.PlumberRecommendations())

        Review = Button( self.CD,
                         text = 'Leave Review',
                         font = ('Courir', 20),
                         command = lambda: self.LeaveReview())

        #shows the purpose of the screen
        DashboardLabel = Label( self.CD,
                                     text='Customer Dashboard',
                                     fg = 'yellow',
                                     bg = '#00008B',
                                     font = ('Courir', 30, 'italic', 'bold'))
        
        #places the tkinter objects onto the CD window
        self.Appointments.place(x=50, y=200)
        logout.place(x=10, y=550)
        logIssue.place(x=1200, y=200)
        CancelBooking.place(x=1200, y=275)
        MakeBooking.place(x=1200, y=350)
        Review.place(x=1200, y=425)
        DashboardLabel.place(x=50, y=100)

        self.updateTable()

    def LeaveReview(self):

        #removes the customer dashboard from the user's screen
        self.CD.withdraw()

        #creates the review window
        self.ReviewWindow = Tk()
        self.ReviewWindow.geometry('1500x400')
        self.ReviewWindow.title('Review a Plumber')
        self.ReviewWindow.config(bg = '#00008B')
        
        #creates a table which displays the meetings that can be reviewed e.g. their current status is completed
        self.Completed = ttk.Treeview(self.ReviewWindow, columns = ('PlumberID', 'date', 'time'))
        self.Completed.heading('#0', text = 'MeetingID')
        self.Completed.heading('PlumberID', text = 'PlumberID')
        self.Completed.heading('date', text = 'Appointment Date')
        self.Completed.heading('time', text = 'Appointment Time')

        #creates entry boxes to allow the user to enter the meetingID and review they would like to leave 
        self.MeetingIDReview = Entry( self.ReviewWindow,
                           width = 20,
                           borderwidth = 5)

        self.ReviewValue = Entry( self.ReviewWindow,
                        width = 20,
                        borderwidth = 5)

        #buttons to either return to the customer dashboard, or attempt to leave a review
        Back = Button( self.ReviewWindow,
                       text = 'Back',
                       font = ('Courir', 10),
                       command = lambda: self.BackReview())

        Enter = Button( self.ReviewWindow,
                        text = 'Enter',
                        font = ('Courir', 10),
                        command = lambda: self.EnterReview())

        #labels to explai the purpose of the dashboard/entry boxes
        WindowLabel = Label( self.ReviewWindow,
                             text = 'Leave Plumber Review',
                             font = ('Courir', 30, 'bold', 'italic'),
                             fg = 'yellow',
                             bg = '#00008B')

        MeetingIDLabel = Label( self.ReviewWindow,
                                text = 'MeetingID: ',
                                font = ('Courir', 10),
                                fg = 'yellow',
                                bg = '#00008B')
        
        ReviewLabel = Label( self.ReviewWindow,
                                text = 'Review out of 5: ',
                                font = ('Courir', 10),
                                fg = 'yellow',
                                bg = '#00008B')

        #places the tkinter objects onto the ReviewWindow 
        Back.place(x=10, y=350)
        self.MeetingIDReview.place(x=120, y=200)
        self.ReviewValue.place(x=120, y=250)
        MeetingIDLabel.place(x=20, y=200)
        ReviewLabel.place(x=20, y=250)
        WindowLabel.place(x=30, y=80)
        Enter.place(x=280, y=250)
        self.Completed.place(x=500, y=100)

        #Fills the Completed table 
        self.FillReviewTable()

    def BackReview(self):

        self.ReviewWindow.withdraw() #removes the review screen from the user's screem
        self.CD.deiconify() #re-displays the customer dashboard
        self.ClearAppts() #clears the Appointments table
        self.checkForPastMeetings() #cancels any expired pending requests
        self.updateTable() #updates the Appointments table with any new information

    def FillReviewTable(self):

        #gets all completed meetings and finds out how many there are
        self.Meetings = self.DB.getAllCompletedMeetings(self.CustomerID)
        length = len(self.Meetings)

        #iterates through the list of completed meetings and adds each to the Completed table
        for a in range(0, length):
            Meeting = self.Meetings[a]
            data = (Meeting['MeetingID'], Meeting['PlumberID'], Meeting['Date'], Meeting['Time'])
            self.Completed.insert('', '0', text = data[0], values = data[1:])

    def EnterReview(self):

        #retrieves the MeetingID and Review entered
        MeetingID = self.MeetingIDReview.get()
        Review = self.ReviewValue.get()

        try:
            #attempts to check if MeetingID is an integer and Review is a float
            MeetingID = int(MeetingID)
            Review = float(Review)

            #finds out how many completed meetings there are and attempts to match the entered MeetingID with one from the list
            length = len(self.Meetings)
            Meeting = ''
            for i in range(0, length):
                TempMeeting = self.Meetings[i]
                if MeetingID == TempMeeting['MeetingID']:
                    Meeting = TempMeeting

            #checks a valid meeting was found
            if Meeting == '':
                errorLabel = Label( self.ReviewWindow,
                                    text = 'Meeting does not exist for you',
                                    fg = 'red',
                                    bg = '#00008B',
                                    font = ('Courir', 10))
                errorLabel.place(x=40, y=320)
                errorLabel.after(1000, lambda: errorLabel.destroy())
            
            else:
                #extracts the plumberID from the Meeting 
                PlumberID = Meeting['PlumberID']
                #if the review is between 0 and 5 inclusive, gets the no of reviews and the review total for the plumber 
                if Review >= 0 and Review <= 5:
                    NR = int(self.DB.getNoOfReviews(PlumberID))
                    RT = float(self.DB.getReviewTotal(PlumberID))
                    #if these were extracted successfully from the database
                    if NR != None and RT != None:
                        #add one to the number of reviews and add the review to the review total
                        NR = NR + 1
                        RT = RT + Review
                        #calculate a new average review and add to the database
                        AverageReview = RT/NR
                        self.DB.updateReview(PlumberID, NR, RT, AverageReview)
                        #change the meeting status to indicate it has now been reviewed, and closes the review window 
                        newMeetingStatus = 'Completed and Reviewed'
                        self.DB.updateMeetingStatus(newMeetingStatus, MeetingID)

                        self.BackReview()
                        
                #if the review is greater than 5 or lower than 0
                else:
                    errorLabel = Label( self.ReviewWindow,
                                    text = 'No completed meeting with this plumber or review is not between 0-5 inclusive',
                                    fg = 'red',
                                    bg = '#00008B',
                                    font = ('Courir', 10))
                    errorLabel.place(x=40, y=320)
                    errorLabel.after(1000, lambda: errorLabel.destroy())
                    
                    
        #if there are any errors in casting variables, exception handles it through displaying an error label 
        except ValueError:
            errorLabel = Label( self.ReviewWindow,
                                    text = 'Review information must be an integer or decimal and the MeetingID must be an integer',
                                    fg = 'red',
                                    bg = '#00008B',
                                    font = ('Courir', 10))
            errorLabel.place(x=10, y=320)
            errorLabel.after(1000, lambda: errorLabel.destroy())
                    
        

    def updateTable(self):

        #gets all Appointment data for the Appointments table 
        ApptInfo = self.DB.getAppointmentData(self.CustomerID)

        try:
            #attempts to fill the Appointments table with the ApptInfo
            length = len(ApptInfo)
            for i in range(0, length):
                Appt = ApptInfo[i]
                Data = (Appt['MeetingID'], Appt['PlumberID'], Appt['Date'], Appt['Time'], Appt['Status'])
                self.Appointments.insert('', '0', text  = Data[0], values = Data[1:])
            
        except:
            pass

    def LogIssue(self):
        #removes the customer dashboard from the user's screen
        self.CD.withdraw()
        #creates the window for logging an issue
        self.LogIssues = Tk()
        self.LogIssues.geometry('600x600')
        self.LogIssues.config(bg = '#00008B')
        #an entry box to allow the user to enter their issue area
        self.Issue = Entry( self.LogIssues,
                            width = 25,
                            borderwidth = 5)
        #labels to display the areas of expertise and the purpose of the window/entry box
        option1 = Label( self.LogIssues,
                              text = '1. Boiler',
                              font = ('Courir', 20),
                              fg = 'yellow',
                              bg = '#00008B')
        option2 = Label( self.LogIssues,
                              text = '2. Radiator',
                              font = ('Courir', 20),
                              fg = 'yellow',
                              bg = '#00008B')
        option3 = Label( self.LogIssues,
                              text = '3. Taps',
                              font = ('Courir', 20),
                              fg = 'yellow',
                              bg = '#00008B')
        option4 = Label( self.LogIssues,
                              text = '4. Water cylinder/tank',
                              font = ('Courir', 20),
                              fg = 'yellow',
                              bg = '#00008B')
        option5 = Label( self.LogIssues,
                              text = '5. Toilets',
                              font = ('Courir', 20),
                              fg = 'yellow',
                              bg = '#00008B')
        option6 = Label( self.LogIssues,
                              text = '6. Pipes',
                              font = ('Courir', 20),
                              fg = 'yellow',
                              bg = '#00008B')
        Problem = Label( self.LogIssues,
                         text = 'Please select the nature of your problem: ',
                         font = ('Courir', 20, 'bold', 'italic'),
                         fg = 'yellow',
                         bg = '#00008B')

        Description = Label( self.LogIssues,
                             text = 'Please enter the word not the number',
                             font = ('Courir', 8, 'italic'),
                             fg = 'yellow',
                             bg = '#00008B')

        #either attempts to log the issue or return to the dashboard
        Enter = Button( self.LogIssues,
                         text = 'Enter',
                         font = ('Courir', 10),
                         command = lambda: self.EnterIssue())

        close = Button( self.LogIssues,
                         text = 'Back',
                         font = ('Courir', 10),
                         command = lambda: self.CloseIssue())
 

        #places the tkinter objects onto the LogIssues window
        Problem.place(x=20, y=50)
        self.Issue.place(x=100, y=150)
        option1.place(x=100, y=220)
        option2.place(x=100, y=260)
        option3.place(x=100, y=300)
        option4.place(x=100, y=340)
        option5.place(x=100, y=380)
        option6.place(x=100, y=420)
        Description.place(x=100, y=180)
        Enter.place(x=320, y=150)
        close.place(x=10, y=550)

    def CloseIssue(self):

        self.LogIssues.withdraw() #removes the LogIssues window from the screen
        self.CD.deiconify() #re-displays the customer dashboard to the user
        self.ClearAppts() #clears the Appointments table
        self.checkForPastMeetings() #cancels any expired meeting requests
        self.updateTable() #updates the Appointments table with any new information

    def EnterIssue(self):

        try:

            #gets the issue entered by the user and converts it to lowercase
            Issue = str(self.Issue.get())
            Issue = Issue.lower()
            #checks to see if the issue is part of any of the issue areas accepted by the system
            if Issue in self.issues:
                #adds the issue and calls the CloseIssue screen to go back to the plumber dashboard
                self.DB.AddIssue(self.CustomerID, Issue)
                Valid = Label( self.LogIssues,
                               text = 'Issue logged',
                               bg = '#00008B',
                               fg = '#FF0000',
                               font = ('Courir', 10))
                Valid.place(x=375,y=150)
                Valid.after(500, lambda: Valid.destroy())
                self.CloseIssue()
                
            else:
                Error = Label( self.LogIssues,
                               text = 'Not Valid',
                               bg = '#00008B',
                               fg = '#FF0000',
                               font = ('Courir', 10))
                Error.place(x=375,y=150)
                Error.after(500, lambda: Error.destroy())

        except ValueError:
            Error = Label( self.LogIssues,
                           text = 'Ensure the entered issue is entered as text',
                           bg = '#00008B',
                           fg = '#FF0000',
                           font = ('Courir', 10))
            Error.place(x=375,y=150)
            Error.after(500, lambda: Error.destroy())            


    def ClearAppts(self):

        #clears the Appointments table
        for appt in self.Appointments.get_children():
            self.Appointments.delete(appt)

    def BackCancel(self):

        self.CancelWindow.withdraw() #removes the cancel window from the user's screen
        self.CD.deiconify() #re-displays the customer dashboard 
        self.ClearAppts() #clears the Appointments table
        self.checkForPastMeetings() #cancels any expired meeting requests
        self.updateTable() #updates Appointments table with new information
    
    def cancel(self):

        #removes the customer dashboard from the user's screen
        self.CD.withdraw()


        #creates the window for cancelling meetings
        self.CancelWindow = Tk()
        self.CancelWindow.geometry('400x250')
        self.CancelWindow.title('Cancel Booking')
        self.CancelWindow.config(bg = '#00008B')

        self.MeetingIDCancel = Entry( self.CancelWindow,
                                      width = 20,
                                      borderwidth = 5)

        #Buttons to either attempt to cancel meetings or return to the main dashboard 
        Enter = Button( self.CancelWindow,
                        text = 'Enter',
                        font = ('Courir', 10),
                        command = lambda: self.AttemptToCancel())

        
        Back = Button( self.CancelWindow,
                       text = 'Back',
                       font = ('Courir', 10),
                       command = lambda: self.BackCancel())

        #labels explaining the purpose of the window/entry box
        MeetingIDLabel = Label(self.CancelWindow,
                             text = 'MeetingID:',
                             fg = 'yellow',
                             bg = '#00008B',
                             font = ('Courir', 10))

        CancelLabel = Label( self.CancelWindow,
                             text = 'Cancel Meeting:',
                             fg = 'yellow',
                             bg = '#00008B',
                             font = ('Courir', 25, 'bold', 'italic'))

        #places the tkinter objects onto the CancelWindow 
        self.MeetingIDCancel.place(x=130, y=100)
        Enter.place(x=280, y=100)
        Back.place(x=10, y=200)
        CancelLabel.place(x=20, y=30)
        MeetingIDLabel.place(x=10, y=100)

    def AttemptToCancel(self):

        #retrieves the MeetingID entered by the user
        MeetingID = self.MeetingIDCancel.get()
        #outlines the date and time format which the information in the meeting table is stored as
        date_format = '%Y-%m-%d'
        time_format = '%H:%M:%S'

        try:
            #converts the meetingID to an integer and attempts to see if it is a valid meeting that is allocated to this particular customer
            MeetingID = int(MeetingID)
            MeetingIDs = self.DB.getAllMeetingIDsCustomer(self.CustomerID)
            if MeetingID in MeetingIDs:
                #extracts that meeting date and time and converts them to datetime objects
                DateAndTime = self.DB.getMeetingInfo(MeetingID)
                Date = str(DateAndTime[0])
                Time = str(DateAndTime[1])
                Date = datetime.strptime(Date, date_format).date()
                Time = datetime.strptime(Time, time_format).time()

                #gets the current date and time
                currentDateTime = datetime.now()
                currentDate = currentDateTime.date()
                currentTime = currentDateTime.time()

                #checks if the current date is the same as the meeting date
                if currentDate == Date:
                    #creates timedelta objects for both the current and meeting times, and subtracts them and extracts the absolute value, ignorong any negative values
                    currentDelta = timedelta(hours = currentTime.hour, minutes = currentTime.minute)
                    MeetingDelta = timedelta(hours = Time.hour, minutes = Time.minute)
                    if MeetingDelta < currentDelta:
                        timeDiff = abs(currentDelta-MeetingDelta)
                        #gets all pending MeetingIDs to see if a time constraint needs to be applied when attempting to cancel the meeting
                        PendingMeetings = self.DB.getAllPendingMeetingIDs(self.CustomerID)
                        #if the times are less than 2 hours apart and the meeting has , the cancellation is not allowed
                        if timeDiff < timedelta(hours=2) and MeetingID not in PendingMeetings:
                            errorLabel = Label( self.CancelWindow,
                                            text = 'Cancellations must be made 2 hour in advance',
                                            bg = '#00008B',
                                            fg = '#FF0000',
                                            font = ('Courir', 10))
                            errorLabel.place(x=20,y=160)
                            errorLabel.after(500, lambda: errorLabel.destroy())
                            
                        #if the times are more than two hours apart, it is allowed and the status of the meeting is changed to cancelled
                        else:
                            CLabel = Label( self.CancelWindow,
                                            text = 'Meeting cancelled',
                                            bg = '#00008B',
                                            fg = '#FF0000',
                                            font = ('Courir', 10))
                            CLabel.place(x=20,y=160)
                            CLabel.after(500, lambda: CLabel.destroy())
                            status = 'Cancelled'
                            self.DB.updateMeetingStatus(status, MeetingID)

                #if the current date is greater than the meeting date, this means the meeting date is past and cannot be cancelled and displays an error label        
                elif currentDate > Date:
                    errorLabel = Label( self.CancelWindow,
                                        text = 'Meeting date already passed',
                                        bg = '#00008B',
                                        fg = '#FF0000',
                                        font = ('Courir', 10))
                    errorLabel.place(x=20,y=160)
                    errorLabel.after(500, lambda: errorLabel.destroy())

                #if the current date is less than the meeting date, the meeting can be cancelled
                else:
                    CLabel = Label( self.CancelWindow,
                                        text = 'Meeting cancelled',
                                        bg = '#00008B',
                                        fg = '#FF0000',
                                        font = ('Courir', 10))
                    CLabel.place(x=20,y=160)
                    CLabel.after(500, lambda: CLabel.destroy())
                    status = 'Cancelled'
                    self.DB.updateMeetingStatus(status, MeetingID)

            #if the meetingID is not valid for this specific customer, an error label is shown
            else:
                errorLabel = Label( self.CancelWindow,
                                        text = 'MeetingID is not valid',
                                        bg = '#00008B',
                                        fg = '#FF0000',
                                        font = ('Courir', 10))
                errorLabel.place(x=20,y=160)
                errorLabel.after(500, lambda: errorLabel.destroy())                

        #an error label is shown if there are any errors with the type of the meetingID
        except ValueError as e:
            print(e)
            errorLabel = Label( self.CancelWindow,
                                        text = 'Ensure all data is of a valid type',
                                        bg = '#00008B',
                                        fg = '#FF0000',
                                        font = ('Courir', 10))
            errorLabel.place(x=20,y=160)
            errorLabel.after(500, lambda: errorLabel.destroy())                
                                

    def logout(self):
        self.CD.destroy() #destroys the customer dashboard
        self.DB.close() #closes the connection to the database
        LoginCustomer() #returns the user to the login page

    def PlumberRecommendations(self):

        #removes the customer dashboard from the user's screen
        self.CD.withdraw()

        #creates the window to show plumber recommendations
        self.PlumbersWindow = Tk()
        self.PlumbersWindow.geometry('1600x850')
        self.PlumbersWindow.title('Plumber recommendations')
        self.PlumbersWindow.config(bg = '#00008B')

        #buttons to either go back to the dashboard, or continue to booking a plumber
        close = Button( self.PlumbersWindow,
                             text = 'Back',
                             font = ('Courir', 10),
                             command = lambda: self.closeRecPage())

        Book = Button( self.PlumbersWindow,
                            text = 'Book',
                            font = ('Courir', 30),
                            command = lambda: self.MakeAppt())


        close.place(x = 10, y = 750)
        Book.place(x = 550, y = 530)

        #label states the purpose of the screen
        PlumberRecLabel = Label( self.PlumbersWindow,
                             text = 'Plumber Recommendations',
                             fg = 'yellow',
                             bg = '#00008B',
                             font = ('Courir', 25, 'italic', 'bold'))

        PlumberRecLabel.place(x = 100, y = 50)
                            

        #a table to show the plumber recommendations with all relevant information
        self.PlumberRecs = ttk.Treeview(self.PlumbersWindow, columns = ('NoOfReviews', 'AvgReview', 'StandardFee', 'HourlyRate', 'DailyRate', 'S/E'))
        self.PlumberRecs.heading('#0', text = 'PlumberID')
        self.PlumberRecs.heading('NoOfReviews', text = 'Number of reviews')
        self.PlumberRecs.heading('AvgReview', text = 'Average Review')
        self.PlumberRecs.heading('StandardFee', text = 'Standard Fee')
        self.PlumberRecs.heading('HourlyRate', text = 'Hourly Rate')
        self.PlumberRecs.heading('DailyRate', text = 'Daily Rate')
        self.PlumberRecs.heading('S/E', text = 'Start/End times')

        self.PlumberRecs.place(x=5, y=175)

        #the variable which controls which option the user wishes to filter the plumbers by
        self.Order = StringVar( self.PlumbersWindow, value = 'AR')

        #label indicating the purpose of the radio buttons below
        SortingLabel = Label( self.PlumbersWindow,
                               text = 'Sort by:',
                               fg = 'yellow',
                               bg = '#00008B',
                               font = ('Courir', 10, 'italic', 'bold'))

        SortingLabel.place(x = 1420, y = 175)

        #radio buttons to allow the plumbers to be filtered either by pricings or reviews
        RadioButtonAR = Radiobutton( self.PlumbersWindow,
                                              text = 'Average Reviews',
                                              font = ('Courir', 7),
                                              variable = self.Order,
                                              value = 'AR')
        RadioButtonSF = Radiobutton( self.PlumbersWindow,
                                              text = 'Standard Fee',
                                              font = ('Courir', 7),
                                              variable = self.Order,
                                              value = 'SF')
        RadioButtonHR = Radiobutton( self.PlumbersWindow,
                                              text = 'Hourly Rate',
                                              font = ('Courir', 7),
                                              variable = self.Order,
                                              value = 'HR')
        RadioButtonDR = Radiobutton( self.PlumbersWindow,
                                              text = 'Daily Rate',
                                              font = ('Courir', 7),
                                              variable = self.Order,
                                              value = 'DR')

        RadioButtonAR.place(x = 1420, y = 230)
        RadioButtonSF.place(x = 1420, y = 285)
        RadioButtonHR.place(x = 1420, y = 340)
        RadioButtonDR.place(x = 1420, y = 395)

        #button is used by the user to update any changes to the radio buttons
        UpdateTable = Button( self.PlumbersWindow,
                                   text = 'update table',
                                   font = ('Courir', 10),
                                   command = lambda: self.RefreshTable())

        UpdateTable.place(x = 1420, y = 470)
                                
        #a scroll bar for the plumber recommendations table 
        scrollbar = ttk.Scrollbar( self.PlumbersWindow,
                                   orient = 'vertical',
                                   command = self.PlumberRecs.yview)
        self.PlumberRecs.configure(yscrollcommand = scrollbar.set)
        scrollbar.place(x=1400, y=175, height=227)

        #gets the issue the customer has entered and retrieves all plumbers in the database who have this as their area of expertise
        Issue = self.DB.getIssue(self.CustomerID)
        if len(Issue) == 1 and Issue != 'n':
            Issue = Issue[0][0]
            self.plumbers = self.DB.getPlumbers(Issue)

        #if no issue found, an error label is displayed
        else:
            errorLabel = Label( self.PlumbersWindow,
                                text = 'Issue Not Yet Logged',
                                bg = '#00008B',
                                fg = 'red',
                                font = ('Courir', 10))
            self.PlumbersWindow.after(500, command = lambda: errorLabel.destroy)

        #automatically filters the options by reviews initially
        self.OrderByReviews()

    def RefreshTable(self):

        #gets the value of the radio button selected, and calls the appropriate function to sort results by
        value = self.Order.get()

        if value == 'AR':
            self.OrderByReviews()
        elif value == 'SF':
            self.OrderByStandardFee()
        elif value == 'HR':
            self.OrderByHourlyRate()
        elif value == 'DR':
            self.OrderByDailyRate()

    def OrderByReviews(self):

        #removes anything currently in the PlumberRecs table
        for plumber in self.PlumberRecs.get_children():
            self.PlumberRecs.delete(plumber)

        length = len(self.plumbers)

        #uses a bubble sort algorithm in order to sort the plumbers by average review
        for i in range(0, length):
            for j in range(0, length-1):
                CurrentPlumber = self.plumbers[j]
                nextPlumber = self.plumbers[j+1]
                if CurrentPlumber['AvgReview'] > nextPlumber['AvgReview']:
                    self.plumbers[j] = nextPlumber
                    self.plumbers[j+1] = CurrentPlumber

        #adds the plumbers to the table
        for a in range(0, length):
            plumber =self.plumbers[a]
            #creates a string containing both the plumber's start and end time
            timeStr = str(plumber['Start']) +' / ' + str(plumber['End'])
            #outlines the data to be added, and adds a £ sign to any prices, and rounds the AvgReview to 2dp
            AverageReview = round(plumber['AvgReview'], 2)
            data = (plumber['PlumberID'], plumber['NoOfReviews'], AverageReview, '£' + str(plumber['StandardFee']), '£' + str(plumber['HourlyRate']), '£' + str(plumber['DailyRate']), timeStr)
            self.PlumberRecs.insert('', '0', text = data[0], values = data[1:])

    def OrderByStandardFee(self):

        #removes anything currently in the PlumberRecs table
        for plumber in self.PlumberRecs.get_children():
            self.PlumberRecs.delete(plumber)

        length = len(self.plumbers)

        #uses a bubble sort algorithm in order to sort the plumbers by standard fee
        for i in range(0, length):
            for j in range(0, length-1):
                CurrentPlumber = self.plumbers[j]
                nextPlumber = self.plumbers[j+1]
                if CurrentPlumber['StandardFee'] < nextPlumber['StandardFee']:
                    self.plumbers[j] = nextPlumber
                    self.plumbers[j+1] = CurrentPlumber

        #adds the plumbers to the table
        for a in range(0, length):
            plumber =self.plumbers[a]
            #creates a string containing both the plumber's start and end time
            timeStr = str(plumber['Start']) + ' / ' + str(plumber['End'])
            #outlines the data to be added, and adds a £ sign to any prices, and rounds the AvgReview to 2dp
            AverageReview = round(plumber['AvgReview'], 2)
            data = (plumber['PlumberID'], plumber['NoOfReviews'], AverageReview, '£' + str(plumber['StandardFee']), '£' + str(plumber['HourlyRate']), '£' + str(plumber['DailyRate']), timeStr)
            self.PlumberRecs.insert('', '0', text = data[0], values = data[1:])

    def OrderByHourlyRate(self):

        #removes anything currently in the PlumberRecs table
        for plumber in self.PlumberRecs.get_children():
            self.PlumberRecs.delete(plumber)

        length = len(self.plumbers)

        #uses a bubble sort algorithm in order to sort the plumbers by hourly rate
        for i in range(0, length):
            for j in range(0, length-1):
                CurrentPlumber = self.plumbers[j]
                nextPlumber = self.plumbers[j+1]
                if CurrentPlumber['HourlyRate'] < nextPlumber['HourlyRate']:
                    self.plumbers[j] = nextPlumber
                    self.plumbers[j+1] = CurrentPlumber

        #adds the plumbers to the table
        for a in range(0, length):
            plumber =self.plumbers[a]
            #creates a string containing both the plumber's start and end time
            timeStr = str(plumber['Start']) + ' / ' + str(plumber['End'])
            #outlines the data to be added, and adds a £ sign to any prices, and rounds the AvgReview to 2dp
            AverageReview = round(plumber['AvgReview'], 2)
            data = (plumber['PlumberID'], plumber['NoOfReviews'], AverageReview, '£' + str(plumber['StandardFee']), '£' + str(plumber['HourlyRate']), '£' + str(plumber['DailyRate']), timeStr)
            self.PlumberRecs.insert('', '0', text = data[0], values = data[1:])

    def OrderByDailyRate(self):

        #removes anything currently in the PlumberRecs table
        for plumber in self.PlumberRecs.get_children():
            self.PlumberRecs.delete(plumber)

        length = len(self.plumbers)

        #uses a bubble sort algorithm in order to sort the plumbers by daily rate
        for i in range(0, length):
            for j in range(0, length-1):
                CurrentPlumber = self.plumbers[j]
                nextPlumber = self.plumbers[j+1]
                if CurrentPlumber['DailyRate'] < nextPlumber['DailyRate']:
                    self.plumbers[j] = nextPlumber
                    self.plumbers[j+1] = CurrentPlumber

        #adds the plumbers to the table
        for a in range(0, length):
            plumber = self.plumbers[a]
            #creates a string containing both the plumber's start and end time
            timeStr = str(plumber['Start'] + ' / ' + plumber['End'])
            #outlines the data to be added, and adds a £ sign to any prices, and rounds the AvgReview to 2dp
            AverageReview = round(plumber['AvgReview'], 2)
            data = (plumber['PlumberID'], plumber['NoOfReviews'], AverageReview, '£' + str(plumber['StandardFee']), '£' + str(plumber['HourlyRate']), '£' + str(plumber['DailyRate']), timeStr)
            self.PlumberRecs.insert('', '0', text = data[0], values = data[1:])

        
    def closeRecPage(self):

        self.PlumbersWindow.withdraw() #removes the plumber recommendations window from the user's screen
        self.CD.deiconify() #re-displays the customer dashboard
        self.ClearAppts() #clears the Appointments table 
        self.checkForPastMeetings() #cancels any expired meeting requests
        self.updateTable() #updates Appointments table with new information

    def MakeAppt(self):

        #closes the plumber recommedation window 
        self.PlumbersWindow.withdraw()

        #creates the window to enter booking information to make a meeting request
        self.Booking = Tk()
        self.Booking.geometry('700x500')
        self.Booking.title('Booking')
        self.Booking.config(bg = '#00008B')

        #labels to indicate the purpose of the screen/entry boxes
        RequestBookingLabel = Label( self.Booking,
                                     text = 'Request a booking: ',
                                     fg = 'yellow',
                                     bg = '#00008B',
                                     font = ('Courir', 25, 'bold', 'italic'))

        PIDLabel = Label( self.Booking,
                          text = 'PlumberID: ',
                          fg = 'yellow',
                          bg = '#00008B',
                          font = ('Courir', 10))

        DateLabel = Label( self.Booking,
                          text = 'Date: ',
                          fg = 'yellow',
                          bg = '#00008B',
                          font = ('Courir', 10))
        
        TimeLabel = Label( self.Booking,
                          text = 'Time: ',
                          fg = 'yellow',
                          bg = '#00008B',
                          font = ('Courir', 10))
        
        IssueLabel = Label( self.Booking,
                          text = 'Issue: ',
                          fg = 'yellow',
                          bg = '#00008B',
                          font = ('Courir', 10))

        #labels which indicate the format to enter dates and times in 
        DateFormatLabel = Label( self.Booking,
                                 text = 'dd/mm/yyyy',
                                 font = ('Courir', 10, 'italic'),
                                 fg = 'yellow',
                                 bg = '#00008B')

        TimeFormatLabel = Label( self.Booking,
                                 text = 'hh:mm',
                                 font = ('Courir', 10, 'italic'),
                                 fg = 'yellow',
                                 bg = '#00008B')                                 

        #entry boxes for the user to enter the plumberID, date, time and elaboration of their issue
        self.PlumberIDMA = Entry( self.Booking,
                                width = 20,
                                borderwidth = 5)
        self.dateMA = Entry( self.Booking,
                           width = 20,
                           borderwidth = 5)

        self.timeMA = Entry( self.Booking,
                           width = 20,
                           borderwidth = 5)

        self.ExpandedIssue = Entry( self.Booking,
                                    width = 80,
                                    borderwidth = 5)

        #either attempts to make a booking request, or returns the user to the plumber recommendation window
        Enter = Button( self.Booking,
                             text = 'Enter',
                             font = ('Courir', 20),
                             command = lambda: self.AttemptToBook())

        Back = Button( self.Booking,
                       text = 'Back',
                       font = ('Courir', 10),
                       command = lambda: self.BackBook())

        #places the tkinter objects onto the Booking window 
        Back.place(x=10, y=450)
        RequestBookingLabel.place(x=30, y=50)
        self.PlumberIDMA.place(x=120, y=150)
        PIDLabel.place(x=20, y=150)
        DateLabel.place(x=20, y=200)
        TimeLabel.place(x=20, y=250)
        DateFormatLabel.place(x=270, y=200)
        TimeFormatLabel.place(x=270, y=250)
        IssueLabel.place(x=20, y=300)
        self.dateMA.place(x=120, y=200)
        self.timeMA.place(x=120, y=250)
        self.ExpandedIssue.place(x=120, y=300)
        Enter.place(x=350, y=350)    

    def BackBook(self):
        
        self.Booking.withdraw() #removes the booking window from the user's screen
        self.PlumbersWindow.deiconify() #re-displays the plumber recommendations window
        self.ClearAppts() #clears the Appointments table
        self.checkForPastMeetings() #cancels any expired meeting requests
        self.updateTable() #updates the Appointments table with any new information

        
    def AttemptToBook(self):

        #outlines the format for the Date and Time strings to be converted to when made into datetime objects
        Date_format = '%d/%m/%Y'
        Time_format = '%H:%M:%S'
        #gets the Date and Time entered into the entry boxes
        Date = self.dateMA.get()
        Time = self.timeMA.get()
        Time = Time + ':00' 

        try:
            #converts Date and Time into datetime objects using the formats outlined above
            Date = datetime.strptime(Date, Date_format).date()
            Time = datetime.strptime(Time, Time_format).time()

            #gets the current date and time
            currentDateTime = datetime.now()
            currentDate = currentDateTime.date()
            currentTime = currentDateTime.time()

            #if the current date is the same as the date requested by the user
            if currentDate == Date:
                #converts the inputted and current times to timedelta objects and calculates the absolute difference between the two values 
                currentDelta = timedelta(hours = currentTime.hour, minutes = currentTime.minute)
                InputDelta = timedelta(hours = Time.hour, minutes = Time.minute)
                if InputDelta > currentDelta:
                    timeDiff = abs(currentDelta-InputDelta)
                    #if the times are within two hour, the booking request cannot be made and a suitable error message is displayed
                    if timeDiff < timedelta(hours=2):
                        errorLabel = Label( self.Booking,
                                            text = 'Bookings must be made two hours in advance',
                                            bg = '#00008B',
                                            fg = '#FF0000',
                                            font = ('Courir', 10))
                        errorLabel.place(x=375,y=150)
                        errorLabel.after(1000, lambda: errorLabel.destroy())

                    else:
                        #counter checks if there is already a meeting at this time. counter remaining at 0 after the for loop indicates there is no meeting at this time and date
                        counter = 0
                        #gets all the current meeting times and dates regarding this customer 
                        currentMeetingTimes, currentMeetingDates = self.DB.getAllAcceptedMeetings(self.CustomerID)
                        for i in range(0, len(currentMeetingTimes)):
                            TempTime = currentMeetingTimes[i][0]
                            TempDate = currentMeetingDates[i][0]
                            if TempDate == Date and TempTime == Time:
                                counter = counter + 1

                        #if there is a meeting already with this for this customer - an error label is displayed   
                        if counter > 0:
                            errorLabel = Label( self.Booking,
                                            text = 'You already have a meeting at this time',
                                            bg = '#00008B',
                                            fg = '#FF0000',
                                            font = ('Courir', 10))
                            errorLabel.place(x=375,y=150)
                            errorLabel.after(1000, lambda: errorLabel.destroy())

                        #if there are no meetings for this customer with this date and time
                        else:
                            #extracts all plumberIDs from the plumber recommendations variable self.plumbers and adds it to the list PlumberIDs
                            PlumberIDs = []
                            length = len(self.plumbers)
                            for i in range(0, length):
                                plumber = self.plumbers[i]
                                PlumberIDs.append(plumber['PlumberID'])

                            #gets the plumberID entered by the user and checks if it is part of the PlumberIDs list
                            PlumberID = int(self.PlumberIDMA.get())
                            if PlumberID in PlumberIDs:
                                #if it is, then get the expanded issue entered by the user and add all this information to the meetings table in the database with status pending
                                issue = str(self.ExpandedIssue.get())
                                status = 'Pending'
                                self.DB.AddPendingMeeting(self.CustomerID, PlumberID, Date, Time, issue, status)
                                #label to indicate the meeting has been requested
                                MeetingReqLabel = Label( self.Booking,
                                                         text = 'Meeting Requested',
                                                         bg = '#00008B',
                                                         fg = '#FF0000',
                                                         font = ('Courir', 10))
                                MeetingReqLabel.place(x=375, y=150)
                                MeetingReqLabel.after(1000, lambda: MeetingReqLabel.destroy())
                                self.BackBook()

                            else:
                                #if the plumberID was not found in the plumber recommendations table - error message displayed
                                errorLabel = Label( self.Booking,
                                                text = 'PlumberID is invalid',
                                                bg = '#00008B',
                                                fg = '#FF0000',
                                                font = ('Courir', 10))
                                errorLabel.place(x=375,y=150)
                                errorLabel.after(1000, lambda: errorLabel.destroy())

                else:
                    errorLabel = Label( self.Booking,
                                                text = 'PlumberID is invalid',
                                                bg = '#00008B',
                                                fg = '#FF0000',
                                                font = ('Courir', 10))
                    errorLabel.place(x=375,y=150)
                    errorLabel.after(1000, lambda: errorLabel.destroy())

                
            elif currentDate > Date:
                #if the current date is after the date entered - a meeting cannot be made and so an error message is displayed
                errorLabel = Label( self.Booking,
                                    text = 'Invalid Date',
                                    bg = '#00008B',
                                    fg = '#FF0000',
                                    font = ('Courir', 10))
                errorLabel.place(x=375,y=150)
                errorLabel.after(1000, lambda: errorLabel.destroy())
            

            else:
                #counter checks if there is already a meeting at this time. counter remaining at 0 after the for loop indicates there is no meeting at this time and date
                counter = 0
                #gets all the current meeting times and dates regarding this customer
                currentMeetingTimes, currentMeetingDates = self.DB.getAllAcceptedMeetings(self.CustomerID)
                for i in range(0, len(currentMeetingTimes)):
                    TempTime = currentMeetingTimes[i][0]
                    TempDate = currentMeetingDates[i][0]
                    if TempDate == Date and TempTime == Time:
                        counter = counter + 1

                #if there is a meeting already with this for this customer - an error label is displayed
                if counter > 0:
                    errorLabel = Label( self.Booking,
                                    text = 'You already have a meeting at this time',
                                    bg = '#00008B',
                                    fg = '#FF0000',
                                    font = ('Courir', 10))
                    errorLabel.place(x=375,y=150)
                    errorLabel.after(1000, lambda: errorLabel.destroy())

                #if there are no meetings for this customer with this date and time
                else:
                    #extracts all plumberIDs from the plumber recommendations variable self.plumbers and adds it to the list PlumberIDs
                    PlumberIDs = []
                    length = len(self.plumbers)
                    for i in range(0, length):
                        plumber = self.plumbers[i]
                        PlumberIDs.append(plumber['PlumberID'])

                    #gets the plumberID entered by the user and checks if it is part of the PlumberIDs list
                    PlumberID = int(self.PlumberIDMA.get())
                    if PlumberID in PlumberIDs:
                        #if it is, then get the expanded issue entered by the user and add all this information to the meetings table in the database with status pending
                        issue = str(self.ExpandedIssue.get())
                        status = 'Pending'
                        self.DB.AddPendingMeeting(self.CustomerID, PlumberID, Date, Time, issue, status)
                        #label to indicate the meeting has been requested
                        MeetingReqLabel = Label( self.Booking,
                                                     text = 'Meeting Requested',
                                                     bg = '#00008B',
                                                     fg = '#FF0000',
                                                     font = ('Courir', 10))
                        MeetingReqLabel.place(x=375, y=150)
                        MeetingReqLabel.after(1000, lambda: MeetingReqLabel.destroy())
                        self.BackBook()

                    else:
                        #if the plumberID was not found in the plumber recommendations table - error message displayed
                        errorLabel = Label( self.Booking,
                                        text = 'PlumberID is invalid',
                                        bg = '#00008B',
                                        fg = '#FF0000',
                                        font = ('Courir', 10))
                        errorLabel.place(x=375,y=150)
                        errorLabel.after(1000, lambda: errorLabel.destroy())

                
        #exception handles any errors with casting values 
        except ValueError:
            errorLabel = Label( self.Booking,
                                    text = 'Please ensure data entered is in the correct format',
                                    bg = '#00008B',
                                    fg = '#FF0000',
                                    font = ('Courir', 10))
            errorLabel.place(x=375,y=50)
            errorLabel.after(500, lambda: errorLabel.destroy())

    def checkForPastMeetings(self):

        #format for the meeting dates and times to be converted to datetime objects
        date_format = '%Y-%m-%d'
        time_format = '%H:%M:%S'

        #gets all meetingIDs, dates and times for any pending meeting requests, and the current date and time
        MeetingDatesTimes = self.DB.getMeetingForCancellation(self.CustomerID)
        currentDateTime = datetime.now()
        currentDate = currentDateTime.date()
        currentTime = currentDateTime.time()

        #checks if there are no current pending meeting requests
        if MeetingDatesTimes == []:
            pass

        else:
            #iterates through all dates and times for all pending meetings
            for Meeting in MeetingDatesTimes:
                #extracts date and time of meeting and converts to datetime objects
                Date = Meeting['Date']
                Time = Meeting['Time']
                Date = datetime.strptime(Date, date_format).date()
                Time = datetime.strptime(Time, time_format).time()
                #if the current date is after the meeting date - set to cancelled
                if currentDate > Date:
                    MeetingID = Meeting['MeetingID']
                    status = 'Cancelled'
                    self.DB.updateMeetingStatus(status, MeetingID)
                    
                #if current date is equal to the meeting date
                elif currentDate == Date:
                    #if the current time is after the meeting time - set to cancelled
                    if currentTime > Time:
                        MeetingID = Meeting['MeetingID']
                        status = 'Cancelled'
                        self.DB.updateMeetingStatus(status, MeetingID)
                

chooseType()

        

        
