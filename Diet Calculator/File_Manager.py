class File:

    #format = [(key type, num lines need),
    #          (type, num lines needed),
    #          ...]
    def __init__(self, format):
        
        self.elemType = elementType

        self.elem_lines = 0;
        self.types = []
        for item in format:
            self.elem_lines = self.elem_lines + item[1]
            self.types.append(item[0])

    #element = [key, obj, ...]
    #element should match the given format
    def add_elem(self, element):

        self.elem_check(element)

    #get an element
    def get_elem(self, key):

        print("get")
        
        
    def elem_check(self, element):

        if len(element) == len(self.types):
            for i in range(0, len(element)):
                if not type(element[i]) == type(self.types[i]):
                    print("element types dont match format types")
                    exit();
        else:
            print("element length doesnt match types length")
            exit();



