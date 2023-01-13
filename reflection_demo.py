
def new_method(self):
    print("It is a new method!")

def main():

    #dynamic importing module
    func_01_module = __import__("src.func_01",fromlist=["func_01"])
    print(func_01_module)

    '''
    test reflection
    '''
    #check if exist class[func01]
    if hasattr(func_01_module,"func01"):
        #build an instance of class[func01]
        func01 =  getattr(func_01_module,"func01")
        print(func01)

        #check if exist method[method_print]
        if hasattr(func01,"method_print"):
            #build a function of method[method_print]
            func01_method = getattr(func01,"method_print")
            func01_method(func01)
        else:
            pass

        #add new method to class[func01]
        setattr(func01,"new_method",new_method)

        if hasattr(func01,"new_method"):
            func01_newmethod = getattr(func01,"new_method")
            func01_newmethod(func01)

        #delete method added before
        delattr(func01,"new_method")
        result = "No!" if hasattr(func01,"new_method") else "Yes!"
        print(f"delete method: {result}")
    else:
        pass
    





if __name__=="__main__":
    main()