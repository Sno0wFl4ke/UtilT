def settings():
    print(">> Settings")
    print("1) Download Paths")
    print("2) other Settings")
    print("3) Exit ")
    s = input("What would you like to change?")
    match s:
        case '1':
            download_paths()
        case '2':
            other_settings()
        case '3':
            exit()
        case _:
            print("Invalid option")

def download_paths():
    print ("Download Path")
