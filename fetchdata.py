import json
class Emp:

    def __init__(self):
        self.__data = None
    def connect(self,file1):
        with open(file1) as f1:
            self.__data=json.load(f1)
    def retrievedata(self,ename):
        for e in self.__data['emp']:
            if e['name'] == ename:
                return e