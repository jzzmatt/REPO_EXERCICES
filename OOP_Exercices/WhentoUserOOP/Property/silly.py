class Silly:
    def _get_silly(self):
        print("Your are getting silly")
        return self._silly

    def _set_silly(self, value):
        print("Your are making silly {}".format(value))
        self._silly = value


    def _del_silly(self):
        print("Whoah, you killed silly!")
        del self._silly


    silly = property(_get_silly, _set_silly, _del_silly, "This is the property of silly attribute")



s = Silly()
print(s)
s.silly = "funny"
print(s)
s.silly
del s.silly


