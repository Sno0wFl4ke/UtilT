import sys
from classmodules.classmodule import MyClass
from funcmodules.downloader import func_downloader

def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))

    func_downloader('Downloader')

    my_object = MyClass('Thomas')
    my_object.say_name()

if __name__ == '__main__':
    main()
