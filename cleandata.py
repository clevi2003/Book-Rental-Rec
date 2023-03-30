import pandas as pd

BOOKS = 'books.csv'
RATINGS = 'ratings.csv'

def main():
    books = pd.read_csv(BOOKS, delimiter=';', encoding='utf-8')
    books.columns = ['isbn', 'title',"author", "pubYear","publisher","imageS","imageM","imageL"]
    books.drop(['pubYear', 'publisher', "imageS", "imageL"], axis=1, inplace=True)
    books.to_csv('cleanbooks.csv', index=False)

    ratings = pd.read_csv(RATINGS, delimiter=';', encoding='utf-8')
    ratings.columns = ["userId", 'isbn', "rating"]
    ratings = ratings[ratings['rating'] != 0]
    ratings.to_csv('cleanratings.csv', index=False)



if __name__ == '__main__':
    main()