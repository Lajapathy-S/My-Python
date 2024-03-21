class computer :
    def __init__(self,name,cpu,os):
        self.name = name 
        self.cpuname = self.cpu(cpu)
        self.osname = self.os(os)
    def __str__(self) :
        # return 'name :'+self.name+'\ncpu name :'+self.cpuname.get_make()+'\nos name:'+self.osname.get_os
        return 'The cpu name is ' +self.cpuname.get_make()+'\nThe computer name is '+self.name +'\nThe os name is '+self.osname.get_os()

    class cpu:
        def __init__(self,make) :
            self.make = make
        def get_make(self):
            return self.make
    class os:
        def __init__(self,os) :
            self.os = os
        def get_os(self):
            return self.os


c1 = computer('IBM','Intel','windows') 
print(c1)
# print('the computer name is : ',c1.name) 
# print('the computer cpu name is : ',c1.cpuname)
# print('the computer os name is : ',c1.osname)
