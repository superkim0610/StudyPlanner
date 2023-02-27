import time

class studyTime:
    """
    Data type class used to define time.\n

    <Set time to given time>\n
    * studyTime(yyyy, mm, dd, hour, min, sec)\n
    * studyTime().setTime(yyyy, mm, dd, hour, min, sec)\n

    <Set time to present time>\n
    * studyTime(now=True)\n
    * studyTime().setTime(now=True)\n

    <Initialize time>\n
    * studyTime()\n
    * studyTime().setTime()\n

    <Get time data>\n
    * studyTime.time() -> (yyyy, mm, dd, hour, min, sec)
    """

    def __init__(self, year:int=0, mon:int=0, mday:int=0, hour:int=0, minute:int=0, sec:int=0, now:bool=False):
        self.setTime(year, mon, mday, hour, minute ,sec, now=now)

    def __repr__(self) -> str:
        return f"<{self.year}-{self.mon:02d}-{self.mday:02d} {self.hour:02d}:{self.minute:02d}:{self.sec:02d}>"
    
    def __eq__(self, other:object):
        return self.time() == other.time()

    def setTime(self, year:int=0, mon:int=0, mday:int=0, hour:int=0, minute:int=0, sec:int=0, now:bool=False):
        if now == True:
            t = time.localtime()
            self.setTime(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min ,t.tm_sec)
        else:
            self.year  = year
            self.mon = mon
            self.mday = mday
            self.hour = hour
            self.minute = minute
            self.sec = sec

    def time(self):
        return (self.year, self.mon, self.mday, self.hour, self.minute, self.sec)

class studyEvent:
    def __init__(self, subjectName:str, startTime:studyTime=studyTime(), finishTime:studyTime=studyTime()):
        self.subjectName = subjectName
        self.startTime = startTime
        self.finishTime = finishTime

    def setSubjectName(self, subjectName):
        self.setSubjectName = subjectName

    def setStartTime(self):
        pass

    def setFinishTime(self):
        pass

def main():
    pass

if __name__ == "__main__":
    main()