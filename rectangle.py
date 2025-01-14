class rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadt = breadth
    def area(self):
            return self.length*self.breadth
    def perimeter(self):
            return 2*(self.length+self.breadth)
    def compare_area(self,other):
            if self.area()>other.area():
                return "first rectangle is larger"
            elif self.area()<other.area():
                return "second rectangle is larger"
            else:
                return "both rectangles are equal"
            length1=float(input("enter length of first rectangle"))
            breadth1=float(input("enter breadth of first rectangle"))
            rect1=rectangle(length1,breadth1)
            length2=float(input("enter length of second rectangle"))
            breadth2=float(input("enter breadth of second rectangle"))
            rect2=rectangle(length2,breadth2)
            print(f"area of first rectangle:{rect1.area()}perimeter:{rect1.perimeter()}")
            print(f"area of second rectangle:{rect2.area()}perimeter:{rect2.perimeter()}")
            print(rect1.compare_area(rect2))



