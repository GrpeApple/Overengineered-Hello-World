def createClass(createClass_boolean):
    if createClass_boolean == True:
        global Hello_World_Class
        class Hello_World_Class:
            def __init__(self, tuple_string, print_boolean):
                self.tuple_string = tuple_string
                self.print_boolean = print_boolean
                self.output = []
            def print_tuple_string(self, print_tuple_boolean):
                if self.print_boolean == True:
                    if print_tuple_boolean:
                        for i in self.tuple_string:
                            self.output.append(i)
def initialize(initialize_boolean, return_boolean):
    if initialize_boolean:
        createClass(True)
        H = 'H'
        e = 'e'
        l = 'l'
        second_l = 'l'
        o = 'o'
        space = ' '
        W = 'W'
        second_o = 'o'
        r = 'r'
        third_l = 'l'
        d = 'd'
        exclamation_mark = '!'
        list_string = []
        list_string.append(H)
        list_string.append(e)
        list_string.append(l)
        list_string.append(second_l)
        list_string.append(o)
        list_string.append(space)
        list_string.append(W)
        list_string.append(second_o)
        list_string.append(r)
        list_string.append(third_l)
        list_string.append(d)
        list_string.append(exclamation_mark)
        boolean = True
        hello_world = Hello_World_Class(tuple(list_string), boolean)
        hello_world.print_tuple_string(True)
        if return_boolean:
            return hello_world.output
def print_string(print_string_boolean):
    if print_string_boolean:
        empty=''
        for output in initialize(True, True):
            print(output, end=empty)
print_string(True)

