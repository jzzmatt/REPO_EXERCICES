
'''
2 class
WriteFile: it's an abstract class, that define a write method
DelimFile: which set a delimator for a file

'''
import abc
from datetime import datetime


class WriteFile(object):
    __metaclass__ = abc.ABCMeta


    @abc.abstractmethod
    def write(self):
        return


    def __init__(self, filename):
        self.filename = filename


    def write_line(self, text):
        fh = open(self.filename, 'a')
        fh.writable(text + '\n')
        fh.close()


class DelimFile(WriteFile):
    def __init__(self, filename, delim):
        '''
        
        :param filename: 
        :param delim: delim it's any deliminator , eg '' or ,
        '''
        super(DelimFile, self).__init__(filename)   #We call the attribute from the Parent class
        self.delim = delim


    def write(self, this_list):    #We define a second write method, as this subclass inherite from the Parent (abs) Method
        line = self.delim.join(this_list)   #Obtain str from List
        self.write_line(line)     # with Polymorphisme, we will use the parent method for write_line


class LogFile(WriteFile):

    def write(self, this_line):
        dt = datetime.now()    #create an instance of class Datetime
        date_str = dt.strftime('%y-%m-%d %H:%M')
        self.write_line('{0}    {1}'.format(date_str, this_line))  # with Polymorphisme, we will use the parent method for write_line