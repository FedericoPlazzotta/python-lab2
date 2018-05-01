def new_task():
    print("Insert new task: ")
    task=input()
    to_do_manager.append(task)

def remove_task():
    print("what would you like to remove?")
    to_be_removed = input()
    to_do_manager.remove(to_be_removed)

if __name__ == '__main__':
    to_do_manager=[]
    choice=0
    while(choice!="4"):
        print("""  digit your choice: 
                    1. insert a new task (a string of text);
                    2. remove a task (by typing its content, exactly);
                    3. show all existing tasks, sorted in alphabetic order;
                    4. close the program.
                """)
        choice = input()
        if(choice=="1"):
            new_task()
        elif(choice=="2"):
            remove_task()
        elif(choice=="3"):
            to_do_manager.sort()
            print(to_do_manager)
        elif(choice=="4"):
            print(to_do_manager)
            print("programme successfully completed")


        else:
            print("invalid choice, try again!")