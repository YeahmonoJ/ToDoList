import time
import keyboard
import os


def MainMenu(sleep_value):
    print("Welcome To Jimmy's To-Do-List")
    time.sleep(sleep_value)

    print("1. Add to List")
    time.sleep(sleep_value)

    print("2. Remove from List")
    time.sleep(sleep_value)

    print("3. Print List")
    time.sleep(sleep_value)
    
    while True:
        selection = int(input("Enter the corresponding number to select a process (ESC to exit): "))
        if selection == 1:
            CreateOrAddFile(sleep_value)
            break


def CreateOrAddFile(sleep_value):
    time.sleep(sleep_value)
    created_file = str(input("Enter a name for the file: "))
    text_conversion = created_file + '.txt'
    lines = []
        
    if check_if_file_exist(text_conversion):
        time.sleep(sleep_value)
        print("File already exist!")

    
        with open(text_conversion, 'r') as File:

            for i in File:
                lines.append(i.strip())
            File.close()
        FileAdd(text_conversion, lines)

    else:
        time.sleep(sleep_value)
        print("File does not exist")
        
        time.sleep(sleep_value)
        print("Creating File......")
        FileAdd(text_conversion, lines)

    

def FileAdd(file_name,lines):
    task_number = 0
    lst_correction = []

    try:
        with open(file_name, 'w') as File:
            while True:
                task_number = len(lines) + 1
                
                user_input = str(input("Enter a task! (If your done just hit ENTER or ESC by itself to Quit): "))
                if not user_input:
                    for i in range(len(lines)):
                        lst_correction.append(lines[i]+ "\n")
                    File.writelines(lst_correction)
                    print(task_number)
                    break

                lines.append(str(task_number) +'. ' + user_input)
                

                

    except IOError:
        print("Error: Failed to open file! ")
    except FileNotFoundError:
        print("Error: File not found")
    except PermissionError:
        print("Error: Permission denied")
    except IsADirectoryError:
        print("Error: Invalid txt file")
    except FileExistsError:
        print("Error: File already Exist")
    except NotADirectoryError:
        print("Error: Invalid Directory")
    except Exception as e:
        print("Error: Something went wrong!", e)


def check_if_file_exist(file_path):
    return os.path.exists(file_path)


def main():
    sleep_value = 1
    MainMenu(sleep_value)


if __name__ == '__main__':
    main()