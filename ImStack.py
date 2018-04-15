#Exercise No. 6 - STACK
#Maria Loren I. Ignacio
#https://github.com/lorenignacio/python-activities
#lorenignacio00@gmail.com
#This program sorts all my Subjects by name and time

class ImStack:
    def __init__(self):
        self.items = ["BsCoe Elective 3 6:00pm-9:00pm",
                      "Data Structures and Algorithm Analysis 6:00pm-9:00pm",
                      "Computer Seminar and Field Trips 6:00pm-9:00pm",
                      "Total Quality Management in Computer Engineering 6:00pm-9:00pm",
                      "Engineering Economy 7:30am-10:00am",
                      "Environmental Engineering 2:00pm-4:00pm",]
        
        self.items2 = sorted(self.items)  #to peek the sorted items in the original list
        self.items3 = self.items2[::-1]   #to peek the reversed original list

    def sort(self):
        return sorted(self.items2)
    def reverse(self):
        return self.items2[::-1]
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peekname(self):
        return self.items3[len(self.items)-1]
    def peeknamenext(self):
        return self.items3[len(self.items)-2]
    def peektimenext(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)




if __name__ == "__main__":
    loren = ImStack()
    print ("Second Semester 2017-2018")
    print "Maria Loren I. Ignacio",loren.size(),"subjects"
    x = input("Sort by:\n1. Subject\n2. Time\n\tEnter : ")
    if x == 1:
        while loren.size() >= 2:
            print "Subjects",loren.peekname()
            print "Next subject is ",loren.peeknamenext(), "\n - - - - - -  "
            loren.pop()
    elif x == 2:
        while loren.size() >= 2:
            print "Displaying is ",loren.peektime()
            print "Next subject is ", loren.peektimenext(), "\n - - - - - - "
            loren.pop()
    else:
        print "INVALID!"
        



