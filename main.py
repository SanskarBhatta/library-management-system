import os
os.system('cls')
class Library:
    def __init__(self):
        self.book=[]
        self.no_of_books=0
    
    def add_books(self):
        # self.name=book_name
        n=int(input("How many books u wanna keep?"))
        for i in range(n):
            r=i+1
            if 11 <= r % 100 <= 13:
                suffix="th"
            else:
                match r % 10:
                    case 1: suffix = 'st'
                    case 2: suffix = 'nd'
                    case 3: suffix = 'rd'
                    case _: suffix = 'th'
            book_name=str(input(f"Enter ur {i+1}{suffix} book:"))
            self.book.append(book_name)
            self.no_of_books+=1
    def show_info(self):
        print(f"\n📊 Total books in library: {self.no_of_books}")
        print("----------------------------")
        for i in range(len(self.book)):
            print (f"{i+1}.\n{self.book[i]}")

my_library = Library()
my_library.add_books()
my_library.show_info()
