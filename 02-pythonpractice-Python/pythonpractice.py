"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""

class Classy(object):
    def __init__(self):
        self.items = []

    def addItem(self,x):
        self.items.append(x)
        # print(items)

    def classiness(self):
        sum = 0
        # print(items)
        for i in self.items:
            if i == "tophat":
                sum = sum + 2
            elif i == "bowtie":
                sum = sum + 4
            elif i == "monocle":
                sum = sum + 5
            else :
                sum = sum
        return sum



