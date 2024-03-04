from calendar import *
import datetime
try:
    from tkinter import *   # Python 3.x
except:
    from Tkinter import *   # Python 2.x


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid(row=0, column=0, sticky='news')
        DateNow = datetime.datetime.now()
        self.month = int(DateNow.month)
        self.year = int(DateNow.year)
        self.createDaysOfWeekLabels()

        # Create frames and button controls for previous, current and next month.
        self.frameList = []    # List that contains the frame objects.
        self.buttonList = []   # List that contains the button objects.
        self.split()

    def split(self):
        month_name = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        leftArrow = Button(self, text="<", command=self.prevMonth)
        leftArrow.grid(row = 0, column = 0)
        rightArrow = Button(self, text=">", command=self.nextMonth)
        rightArrow.grid(row = 0, column = 1)
        for i in range(3):
            try:
                print i, "this is i"
                print self.month
                mFrame = Frame(self)
                self.createMonth(mFrame)
                self.frameList.append(mFrame)
                mButton = Button(self, text=month_name[self.month-1])
                mButton['command'] = lambda f=mFrame, b=mButton: self.showMonth(f, b)
                mButton.grid(row=1, column=i)
                # Grid each frame
                mFrame.grid(row=3, column=0, columnspan=7, sticky='news')
                if (i == 1):
                    mButton['relief'] = 'flat'
                else:
                    mButton.grid_remove()
                    # Remove all but the ith frame. More efficient to remove than forget and configuration is remembered.
                    mFrame.grid_remove()          
                self.buttonList.append(mButton)

            except:
                pass
        # Create year widget at top right of top frame
        label = Label(self, text=self.year)#displaying year
        label.grid(row=0, column=6)
        print "-------------------"

    def prevMonth(self):

        self.month -= 1
        print self.month, "this is month in PREV"
        if self.month <= 0:
            self.month = 12
            print self.month, "month inside forinif in PREVMONTH"
            self.year -= 1
        elif self.month >= 13:
            self.month = 0
            print self.month, "month inside forinelif in PREVMONTH"
            self.year += 1
        self.split()

    def nextMonth(self):

        self.month += 1
        print self.month, "this is month in NEXT"
        for frame in self.frameList:
            frame.grid_remove()

        if self.month <= -1:
            self.month = 11
            print self.month, "month inside forinif in NEXTMONTH"
            self.year -= 1
        elif self.month >= 13:
            self.month = 1
            print self.month, "month inside forinelif in NEXTMONTH"
            self.year += 1
        self.split()


    def createDaysOfWeekLabels(self):
        days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
        for i in range(7):
            label = Label(self, text=days[i], width = 3)
            label.grid(row = 2, column = i)

    def showMonth(self, mFrame, mButton):
        # Display all buttons normally
        for button in self.buttonList:
            button['relief'] = 'raised'

        # Set this month's button relief to flat
        mButton['relief'] = 'flat'

        # Hide all frames
        for mframe in self.frameList:
            mframe.grid_remove()

        mFrame.grid()

    def createMonth(self, mFrame):

        weekday, numDays = monthrange(self.year, self.month)
        week = 0
        for i in range(1, numDays + 1):
            button = Button(mFrame, text = str(i), width=3)
            button.grid(row = week, column = weekday)

            weekday += 1

            if weekday > 6:
                week += 1
                weekday = 0

mainWindow = Tk()
obj = Application(mainWindow)
mainWindow.mainloop()