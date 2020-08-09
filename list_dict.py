
class MyList(list):
    def __init__(self,args=None):
        if args:
            self.extend(args)
        # print("List Obj Created Successfully!")
    def remove_same_content(self,inplace=True):
        empty_list=[]
        for a in self:
            if a not in empty_list:
                empty_list.append(a)
        if inplace:
            self.clear()
            self.extend(empty_list)
            return self
        else:
            return empty_list
    def append_args(self,*args):
        for arg in args:
            self.append(arg)

class MyDict(dict):
    def __init__(self,**kw):
        self.update(kw)
        # print("Dict Object Has Been Created Succesfully.")
    def __getattr__(self,key):
        return self[key]


