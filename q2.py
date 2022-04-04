class clockTime:
    def _init_(self):
        self.hours = self.setHours()
        self.minutes = self.setMinutes()
        self.seconds = self.setSeconds()

    def setHours(self,hours):
        self.hours = hours

    def setMinutes(self,minutes):
        self.minutes = minutes
    
    def setSeconds(self,seconds):
        self.seconds = seconds
    
    def setTime(self):
        tiime = "Time is: "+ self.hours+ ":" +self.minutes+ ":"+self.seconds
        return tiime

    def showTime(self):
        print(self.setTime())


hours = str(input("Enter hours: "))
minutes = str(input("Enter minutes: "))
seconds =  str(input("Enter seconds: "))

time = clockTime()
time.setHours(hours)
time.setMinutes(minutes)
time.setSeconds(seconds)
time.setTime()
time.showTime()


