from menu import Menu
from actions import StudentManager

def main():
    manager = StudentManager()
    menu = Menu(manager)
    menu.run()

if __name__ == '__main__':
    main()