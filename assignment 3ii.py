print('____QUESTION 3(ii)____')

class Book():
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print('Title:', self.title)
        print('Author:', self.author)
        print('Price:', self.price)
#creating instances
book1 = Book('Harvest of thorns', 'Shimmer Chinodya', 10)
book2 = Book(' Rutendo The Chief gradndaughter', 'Collet Mutangadura', 15)
print('[BOOKS]')
book1.display_details()
book2.display_details()
