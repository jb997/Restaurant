class Menu(object):
    def __init__(self):
        self.starters = {"Soup": 6.00, "Bruschetta": 5.00, "Meatballs": 8.00, "Garlic Flatbread": 4.00}
        self.mains = {"lasagne": 11.00, "pizza": 9.50, "penne al ragu": 9.00, "risotto": 10.00}
        self.desserts = {"tirimasu": 7.00, "gelato": 5.00, "lemon possett": 5.50, "Hazelnut Dream": 6.00}

    def select_course(self, course_name, options):
        print "Please see our " + course_name + " options below."
        for key in options:
            print key
        print ""
        choice = raw_input("Choose your " + course_name + ". ")
        while choice not in options:
            print "Unfortunately, this is not something we currently serve.\nPlease choose something on the menu.\n"
            choice = raw_input("Choose your " + course_name + ". ")
        print "You selected " + choice + "\n"
        return choice


    def meal(self):
        starter = self.select_course("starter", self.starters)
        main = self.select_course("main", self.mains)
        dessert = self.select_course("dessert", self.desserts)
        total = self.starters[starter] + self.mains[main] + self.desserts[dessert]
        tip = total * 1.10
        print "Total: ${:.2f}\nTotal plus tip: ${:.2f}".format(total, tip)


menu = Menu()
menu.meal()


