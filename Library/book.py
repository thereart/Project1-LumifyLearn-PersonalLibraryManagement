
class Book:
    def __init__(self, title, author):
        
        self.title = title
        self.author = author
        self.is_available = True
        
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def borrow(self):
        if self.is_available == True: 
            return True
        else: self.is_available == False
        return False 
    
    def return_book(self):
        self.is_available = True
        