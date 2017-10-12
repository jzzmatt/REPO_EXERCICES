class MyError(Exception):   #inehrite from SuperClass Exception
    def __init__(self, *args):  #args here, match any value entered
        if args:
            self.message = args[0]

        else:
            self.message = None


    def __str__(self):
        print("Calling str")
        if self.message:
            return "Here's a MyError Exception with a message: {0}".format(self.message)
        else:
            return "Here's a MyError Exception"

raise MyError

raise MyError("Houston Mayday Mayday, we have a problem")
