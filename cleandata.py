import pandas as pd

BOOKS = 'books.csv'
RATINGS = 'ratings.csv'

def main():
    ratings = pd.read_csv(RATINGS, delimiter=';', encoding='utf-8')
    ratings.columns = ["userId", 'isbn', "rating"]
    ratings = ratings[ratings['rating'] != 0]
    df = ratings['isbn'].value_counts().to_frame()
    df.columns = ['count']
    # list of isbns to remove
    remove = df.index[df['count'] == 1].tolist()
    ratings = ratings[~ratings['isbn'].isin(remove)]
    ratings.to_csv('cleanratings.csv', index=False)

    books = pd.read_csv(BOOKS, delimiter=';', encoding='utf-8')
    books.columns = ['isbn', 'title', "author", "pubYear", "publisher", "imageS", "imageM", "imageL"]
    books.drop(['pubYear', 'publisher', "imageS", "imageL"], axis=1, inplace=True)
    books = books[~books['isbn'].isin(remove)]
    books.to_csv('cleanbooks.csv', index=False)



if __name__ == '__main__':
    main()