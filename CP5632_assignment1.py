_author_ = "prabhjot kaur"
'''
Name= Prabhjot kaur
Student id=13430639
Github link:-
'''
# Initialize the constants

def main():
    print("Reading List 1.0 - by Prabhjot kaur ")
    list_book = []
    displaymenu()
    load_books(list_book)
    choice = input("enter your choice").upper()
    print(choice)
    while choice != 'Q':
        if choice == 'R':
            print("Required books are as following")
            list_required(list_book)
        elif choice == 'C':
            print("completed books are as following")
            list_completebooks(list_book)
        elif choice == 'A':
            add_book(list_book)
        elif choice == 'M':
            mark_completebook(list_book)
        else:
            print("invalid input")
        choice = input("enter your choice").upper()
    totalbooks = 0
    for list in list_book:
            totalbooks += 1
    print("{} books are saved to books.csv".format(totalbooks))
    print("Have a nice day")
            #displaymenu()


# end of main()
'''This function is for displaying a menu to user
'''

def displaymenu():
    print("Menu:")
    print("R - List required books")
    print("C - List completed books")
    print("A - Add new book")
    print("M - Mark a book as completed")
    print("Q - Quit")

'''This function is used for loading a list of book from books.csv file
FUNCTION load_books(list_book):
    temp_file <- open("books.csv", "r")
    for line in temp_file:
        count=0
        list_book.append(line.strip().split(','))
       # OUTPUT line
ENDFUNCTION

    ENDFOR
'''
def load_books(list_book):
    temp_file = open("books.csv", "r")
    for line in temp_file:
        count=0
        list_book.append(line.strip().split(','))
       # print(line)

'''This function is for displaying the list of completed books
FUNCTION list_completebooks(list_book):
    totalpages <- 0
    count <- 0
    numofbooks=-0
    for list in list_book:
        IF list_book[count][3] = 'c':
            OUTPUT "{}. {:<50s} by {:<50s}{:>4s} pages".format(count,list_book[count][0], list_book[count][1], list_book[count][2])
                                                       ENDFOR
            numofbooks += 1
            totalpages += int(list_book[count][2])
        ENDIF
        count += 1
    ENDFOR
    OUTPUT "Total pages for {} books are {}: " .format(numofbooks,totalpages)
                       ENDFOR
    displaymenu()
ENDFUNCTION
'''
def list_completebooks(list_book):
    totalpages = 0
    count = 0
    numofbooks=-0
    for list in list_book:
        if list_book[count][3] == 'c':
            print("{}. {:<50s} by {:<50s}{:>4s} pages".format(count,list_book[count][0], list_book[count][1], list_book[count][2]))
            numofbooks += 1
            totalpages += int(list_book[count][2])
        count += 1
    print("Total pages for {} books are {}: " .format(numofbooks,totalpages))
    displaymenu()

'''This function is for displaying the list of required books'''
def list_required(list_book):
    totalpages = 0
    count = 0
    numofbooks=0
    for list in list_book:
        if list_book[count][3] == 'r':
            print("{}. {:<50s} by {:<50s}{:>4s} pages".format(count,list_book[count][0], list_book[count][1], list_book[count][2]))
            numofbooks+=1
            totalpages += int(list_book[count][2])
        count += 1

    if numofbooks == 0:
        print("no book")
    print("Total pages for {} books are {}: ".format(numofbooks, totalpages))
    displaymenu()

'''This function is used for adding a new book to the book list'''
def add_book(list_book):

    title = input("Title:")
    while title == '':
        print("Title cannot be blank")
        title = input("Title:")
    author=input("Author:")
    while author == '':
        print("author cannot be blank")
        author = input("author:")
    pages=0
    flag=0
    while flag ==0:
     try:
      while pages <=0:
         #print("pages must be greater than 0")
         pages=int(input("pages:"))

      flag=1
     except ValueError:
         print("Pages cannot be blank and Enter valid numer only")
         #pages=int(input("pages:"))
    list_book.append([title,author,str(pages),'r'])
    print("{} by {},({}pages)is added to reading list".format(title,author,str(pages)))
    print(list_book)
    book_file = open("Books.csv", "w")
    save_list(list_book)


'''This function is used to update the list of books with new changes'''
def save_list(list_book):
    book_file = open("Books.csv", "w")
    for list in list_book:
        for char in list:
            if char == 'r' or char == 'c':
                print(char, end='', file=book_file)
            else:
                print(char, end=',', file=book_file)
        print(file=book_file)
    book_file.close()

'''This function is used for marking book as completed'''
def mark_completebook(list_book):
    list_required(list_book)
    print("Enter the number of a book to mark as completed")
    try:
        num = int(input(">>>"))
        count = 0
        flag=0
        for list in list_book:
         count+=1
        while flag==0:
          while num>count :
            print("number of book u entered is not matched matched")
            num = int(input("enter the number of books marked as completed"))
          flag=1
        if list_book[num][3] == 'c':
            print("That book is already completed")
        else:
            list_book[num][3] = 'c'
            save_list(list_book)
            print("{} by {} marked as completed".format(list_book[num][0],list_book[num][1]))
    except ValueError:
        print("Invalid input; enter a valid number")
main()

