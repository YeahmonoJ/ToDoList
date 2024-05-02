import time
import os
import re


def MainMenu(sleep_value: int) -> int:
    """
    Displays a menu for a To-do list App

    Parameters:
    sleep_value (int): The duration to sleep between printing each menu item.

    Returns: 
    selection (int): The Users selection from the dial menu 
    selection: needs to be a value from 1 to 3
    """
    
    print("Welcome To Jimmy's To-Do-List")
    time.sleep(sleep_value)
                     
    print()
    print("1. Add to List")
    time.sleep(sleep_value)

    print()
    print("2. Remove from List")
    time.sleep(sleep_value)

    print()
    print("3. Print List")
    time.sleep(sleep_value)
    
    while True:
        try:
            print()
            selection = int(input("Enter the corresponding number to select a process (ESC to exit): "))
            
            if selection >= 1 and selection <= 3:
                return selection
        
            else:

                time.sleep(sleep_value)
                print()
                print("Invalid Number, choose a number between 1 and 3")

        except ValueError:
            time.sleep(sleep_value)
            print()
            print("Invalid input, please enter a number between 1 and 3")


def CreateOrAddFile(sleep_value):
    """
    This function will check if the file already exist or not 
    If file exist then the file will be opened
    If file does not exist it will be created then opened 
    
    """
    time.sleep(sleep_value)
    print()
    created_file = str(input("Enter a name for the file: "))

    text_conversion = created_file + '.txt'
    lines = []
        
    if check_if_file_exist(text_conversion):
        time.sleep(sleep_value)
        print()
        print("File already exist!")

    
        with open(text_conversion, 'r') as File:

            for i in File:
                lines.append(i.strip())
            File.close()
        FileAdd(text_conversion, lines)

    else:
        time.sleep(sleep_value)
        print()
        print("File does not exist")
        
        time.sleep(sleep_value)
        print()
        print("Creating File......")
        FileAdd(text_conversion, lines)
    

def FileAdd(file_name,lines):
    task_number = 0
    lst_correction = []

    try:
        with open(file_name, 'w') as File:
            while True:
                task_number = len(lines) + 1
                
                print()
                user_input = str(input("Enter a task! (If your done just hit ENTER or ESC by itself to Quit): "))
                
                if not user_input:
                    
                    for i in range(len(lines)):
                        lst_correction.append(lines[i]+ "\n")
                    
                    File.writelines(lst_correction)
                    
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


def RemoveALine(sleep_value):
    lines = []
    temp_lines = []
    nums = 0


    while(True):
        try:
            time.sleep(sleep_value)
            print()
            created_file = str(input("Enter a name for the file: "))
            text_conversion = created_file + '.txt'
    
        except ValueError:
            time.sleep(sleep_value)
            print()
            print("Invalid input")

        if check_if_file_exist(text_conversion):
            time.sleep(sleep_value)
            print()
            print("File does exist")
            break
        else:
            time.sleep(sleep_value)
            print()
            print("That file does not exist, Enter a valid file name") 

    with open(text_conversion, 'r') as File:
        for i in File:
            lines.append(i.strip())
        File.close()
        print(lines)

    while(True):

        try:
            print()
            removal = input("Choose the corresponding number to the line that you would like to remove (Press ENTER to escape: )")
            
            if removal == "":

                with open(text_conversion, 'w') as File:

                    for i in range(len(lines)):
                        temp_lines.append(lines[i] + '\n')
                    
                    File.writelines(temp_lines)
                    break
            
            removal =int(removal)

            if removal > len(lines):
                print()
                print("Out of bounds")

            elif removal == 0:
                print()
                print("value to Low!")

            else:
                del lines[removal-1]
                for i in range(removal-1, len(lines)):
                    result = re.search(r'^([^.]*)\.', lines[i]) 
                    char_num_after_period = len(result.group(1))
                    
                    corrected_line = lines[i][0:char_num_after_period]
                    nums = int(corrected_line) - 1
                    lines[i] = str(nums) + lines[i][char_num_after_period:]
                print(lines)
            
        except ValueError:
            print()
            print("Not a valid Int")

def ReadFile(sleep_value):
    time.sleep(sleep_value)
    print()
    created_file = str(input("Enter a name for the file: "))

    text_conversion = created_file + '.txt'
        
    if check_if_file_exist(text_conversion):
        time.sleep(sleep_value)
        print()
        
        with open(text_conversion, 'r') as File:
            for line in File:
                print(line.strip())




def main():
    sleep_value = 1
    main_menu = MainMenu(sleep_value)
    if main_menu == 1:
        CreateOrAddFile(sleep_value)
    
    elif main_menu == 2:
        RemoveALine(sleep_value)
    
    elif main_menu == 3:
        ReadFile(sleep_value)
    
    else:
        print("Something went wrong! ")
        


if __name__ == '__main__':
    main()