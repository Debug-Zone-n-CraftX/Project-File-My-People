import file


def select():
    while True:
        print()
        print("1 Add Content To File")
        print("2 Show file content")
        print("3 Remove file Content")
        print("4 Exit Program")
        choice = int(input("Select Your Choice : "))

        if choice == 1:
            
            count = int(input("Enter the number of contact to Add : "))
            for i in range(1,count+1):
                content = input("Enter the name & Number : ")
                file.file_write(content)
            print(i,"Content Added Successfully")
            break

        elif choice == 2:
            print()
            print("Content of File :-")
            file.show_file()
        
        elif choice == 3:
            print()
            file.clear_file()
            print("File is Cleared")

        elif choice == 4:
            print("Exiting ....")
            break
 
        else:
            print("Invalid Input")

select() 
