class University():

    # object constructor (__init__ method)
    def __init__(self):
        # object attributes (object features)
        self.name = 'CUE'    

    def set_name(self,name):
        self.name=name

    # object methods (object behaviors)
    def print_name(self):  
        print(self.name)

a=University()
a.print_name()
a.set_name('MIT')
a.print_name()