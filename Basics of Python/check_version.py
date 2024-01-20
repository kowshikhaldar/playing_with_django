import platform

def main():
    myinfo()

def myinfo():
    print("System:", platform.system())
    print("Platform:", platform.platform())
    print("OS Version:", platform.version())
    print("Architecture:", platform.architecture())
    print("Machine:", platform.machine())
    print("Processor:", platform.processor())
    print("Python Version:", platform.python_version())
    print("Python Compiler:", platform.python_compiler())
    print("Python Build:", platform.python_build())
    print("PC name:", platform.node())
    print(f"Release: {platform.release()}") #using fstring

if __name__=="__main__":
    main()
