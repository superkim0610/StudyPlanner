import time

class sTime:
    """
    Data type class used to define time.\n

    <Set time to given time>\n
    * sTime(yyyy, mm, dd, hour, min, sec)\n
    * sTime().setTime(yyyy, mm, dd, hour, min, sec)\n

    <Set time to present time>\n
    * sTime(now=True)\n
    * sTime().setTime(now=True)\n

    <Set time by tuple data>\n
    * sTime(tuple_data)\n
    * sTime().setTime(tuple_data)\n

    <Initialize time>\n
    * sTime()\n
    * sTime().setTime()\n

    <Return time data>\n
    * sTime.time() -> (yyyy, mm, dd, hour, min, sec)
    """

    def __init__(self, year:int=0, mon:int=0, mday:int=0, hour:int=0, minute:int=0, sec:int=0, data:tuple=None, now:bool=False):
            self.setTime(year, mon, mday, hour, minute ,sec, data=data, now=now)

    def __repr__(self) -> str:
        return f"<{self.year}-{self.mon:02d}-{self.mday:02d} {self.hour:02d}:{self.minute:02d}:{self.sec:02d}>"
    
    def __eq__(self, other:object):
        return self.time() == other.time()
    
    def __add__(self, other:object):
        s = self.time()
        o = other.time()
        r = (s[i] + o[i] for i in range(6))
        return sTime(data=r)

    def __sub__(self, other:object):
        s = self.time()
        o = other.time()
        r = (s[i] - o[i] for i in range(6))
        return sTime(data=r)

    def setTime(self, year:int=0, mon:int=0, mday:int=0, hour:int=0, minute:int=0, sec:int=0, data:tuple=None, now:bool=False):
        if now == True:
            t = time.localtime()
            self.setTime(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min ,t.tm_sec)
        elif data is not None:
            self.setTime(*data)
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
    """
    class studyEvent is the object can save the data about study event.
    for example, subject name, start time, finish time, comment
    """
    def __init__(self, subjectName:str, startTime:sTime=sTime(), finishTime:sTime=sTime(), comment:list=[]):
        self.subjectName = subjectName
        self.startTime = startTime
        self.finishTime = finishTime
        self.studyingTime = self.finishTime - self.startTime
        self.comment = comment

    def setSubjectName(self, subjectName:str):
        self.setSubjectName = subjectName

    def setStartTime(self, startTime:sTime=sTime(), now:bool=False):
        if now == True:
            self.startTime = sTime(now=True)
        else:
            self.startTime = startTime
        self.studyingTime = self.finishTime - self.startTime

    def setFinishTime(self, finishTime:sTime=sTime(), now:bool=False):
        if now == True:
            self.finishTime = sTime(now=True)
        else:
            self.finishTime = finishTime
        self.studyingTime = self.finishTime - self.startTime

    def addComment(self, commentName:str, commentContent:str=""):
        """
        for example, comment = [['name1', 'content1'], ['name2', 'content2'], ...]
        """
        self.comment.append([commentName, commentContent])

class dayStudyEvent:
    def __init__(self):
        self.studyEventList = []
        self.dayStudyingTime = sTime()
    
    def addStudyEvent(self, studyEvent):
        pass

class sTodo:
    """
    <Todo status>
    * None (literally mean none, blank)
    * Done
    * Almost
    * Missed
    """
    def __init__(self, todoName:str, todoSubjectName:str, todoStatus:str="None", todoDate:sTime=sTime(now=True)):
        self.todoName = todoName
        self.todoSubjectName = todoSubjectName
        self.todoStatus = todoStatus
        self.todoDate = todoDate

    def changeName(self, todoName:str):
        self.todoName = todoName

    def changeSubjectName(self, todoSubjectName:str):
        self.todoSubjectName = todoSubjectName

    def changeStatus(self, todoStatus:str):
        self.todoStatus = todoStatus

    def changeDate(self, todoDate:sTime):
        self.todoDate = todoDate

class sSubject:
    def __init__(self, subjectName:str, subjectColor:str):
        self.subjectName = subjectName
        self.subjectColor = subjectColor
        # self.totalTime = sTime()

    def changeName(self, newName:str):
        self.subjectName = newName

    def changeColor(self, newColor:str):
        self.subjectColor = newColor

def main():
    # test (sTime operating)
    a = sTime(data=(0,1,2,3,4,5))
    b = sTime()
    b.setTime(data=(3,5,6,7,8,9))
    print(b-a)
    print((b-a).time())

if __name__ == "__main__":
    main()