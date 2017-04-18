#Python 2.6.9
#input data will come from test case data in 'inputData.txt'
#output data will be placed in the 'outputFile.html' file

#A's 1 to n/3 (floor)
#B's (n/3 (floor) + 1) to 2 * n/3(floor)
#F's n/10
#C's = eager above n/10
#D's = lazy above n/10
#Just FYI: This grading scale can produce a way for someone to make a 50% in the class but due to his/her
    # eagerness, he or she can still get a C. Alternatively, this also means that someone who made an 80%
    # in class can get a D because they were marked lazy


class Student:
    def __init__(self, s_id, fName, lName, perGrade, tieFactor):
        self.s_id = s_id
        self.fName = fName
        self.lName = lName
        self.perGrade = perGrade
        self.tieFactor = tieFactor
        self.letterGrade = 'F' #automatically assign F for easier data manipulation later
        #self.location = location
    def getID(self):
        return(self.s_id)
    def getFName(self):
        return(self.fName)
    def getLName(self):
        return(self.lName)
    def getPerGrade(self):
        return(self.perGrade)
    def getTieFactor(self):
        return(self.tieFactor)
    def getLetterGrade(self):
        return(self.letterGrade)
#    def getLocation(self):
#        return(self.location)


inputData = open('input.txt', 'r+')
splitData = inputData.read().split()
inputData.close()
fileSize = len(splitData) #finds file size
i=0 #used for while loop
j=0 #used for testing
k=0 #used for grade assignment loops
l=0 #used to write html file
studentList = []

#while loop to create student objects
while (i < fileSize):
    studentList.append(Student(splitData[i], splitData[i+1], splitData[i+2], splitData[i+3], splitData[i+4]))
    #ensures no index out of bounds errors
    try:
        i+=5
    except:
        pass
    #ignores the location data and ensures no index out of bounds errors
    try:
        while (len(splitData[i]) != 9):
            i+=1
    except:
        break

#sorts list by primarily grade, then last name, then tieFactor
studentPerGradeList = sorted(studentList, key=lambda studentList: (studentList.getPerGrade(),
                                                                   studentList.getLName(),
                                                                   [(-ord(c) for c in studentList.getTieFactor())]), reverse=True)

#gets number of A's list
lenAList = len(studentPerGradeList)//3
#gets number of B's list
lenBList = 2 * lenAList
#gets number of F's list
lenFList = -(-len(studentPerGradeList)//10)

#assigns A's to proper students. For loop is (inclusive, exclusive) so no need for (lenAList - 1)
for k in range(0, lenAList):
    studentPerGradeList[k].letterGrade = 'A'
#assign B's to proper students. For loop is (inclusive, exclusive) so no need for (lenBList - 1)
for k in range(lenAList, lenBList):
    studentPerGradeList[k].letterGrade = 'B'
#assign C's and D's to proper students based on their rank in the class.
for k in range(lenBList, len(studentPerGradeList)-lenFList):
    if (studentPerGradeList[k].getTieFactor() == 'E'):
        studentPerGradeList[k].letterGrade = 'C'
    else:
        studentPerGradeList[k].letterGrade = 'D'

#sort list alphabetically with letter grades now assigned
studSortedOutput = sorted(studentPerGradeList, key=lambda studentPerGradeList: (studentPerGradeList.getLName(),
                                                                                studentPerGradeList.getFName(),
                                                                                studentPerGradeList.getLetterGrade()), reverse=False)
#initial html code
html_str1 = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Professor Haskell Grading Sheet</title>

</head>
<body>
    <table border=1>
     <tr>
       <th>Student ID</th>
       <th>First Name</th>
       <th>Last Name</th>
       <th>Grade</th>
     </tr>
     <indent>
        Professor Haskell Grading Sheet
"""

#loop through data set to populate list and write html code
html_str2 = ''
for l in range(0, len(studSortedOutput)):
    html_str2+=('<tr>')
    html_str2+='\n  <td>' + studSortedOutput[l].getID() +'</td>'
    html_str2+='\n  <td>' + studSortedOutput[l].getFName() +'</td>'
    html_str2+='\n  <td>' + studSortedOutput[l].getLName() + '</td>'
    html_str2+='\n  <td>' + studSortedOutput[l].getLetterGrade() + '</td>'
    html_str2+=('\n</tr>\n')

#closing html code from html_str1
html_str3 = """
     </indent>
    </table>
</body>
"""

#opens html file with write capability
Html_file= open("output.html","w")
#writes the three strings
Html_file.write(html_str1 + html_str2 + html_str3)
#closes html file for better encompassed program
Html_file.close()