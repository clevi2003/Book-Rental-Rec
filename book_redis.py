"""
API for Redis
"""
import redis
from datetime import date
import datetime

class BookAPI:

    def __init__(self, host='localhost', port=6379, db=0, decode_responses=True):
        self.r = redis.Redis(host=host, port=port, db=db)
        self.r.flushall()

    def add_rating(self, file_name):
        """Creates hash for each user and their ratings"""
        with open(file_name, "r") as file:
            # skipping header of csv file
            headers = file.readline()
            while True:
                rating = file.readline().strip().split(',')
                # stops if reached the end of file
                if len(rating) < 2:
                    break
                # adds book rating to user's hash of ratings (isbn: rating)
                self.r.hset(str(rating[0]), mapping={rating[1]: rating[2]})

    def add_book(self, file_name):
        """Creates hashes containing book info,
         creates lists of all books by a given author,
         creates set of all isbns with same title"""
        # opening csv file and reading it
        with open(file_name, "r") as file:
            # header of csv file
            headers = file.readline()
            while True:
                book_lst = file.readline().strip().split(",")
                print(book_lst)
                # stops if reached the end of file
                if len(book_lst) < 2:
                    break

                # adds book information to hash, named by isbn
                self.r.hset(f'{headers[0]}:{book_lst[0]}', mapping={headers[1]: book_lst[1], headers[2]: book_lst[2], headers[3]: book_lst[3], 'availability': 1})
                # adds isbn to author list
                #self.r.lpush(book_lst[2], str(book_lst[0]))
                # adds isbn to book title set
                self.r.sadd(book_lst[1], book_lst[0])

    def rent_book(self, user, isbn):
        """rents book by creating hash"""
        today = date.today().strftime('%Y-%m-%d')
        week = today + datetime.timedelta(days=7)
        self.r.hset(f'{user}:{isbn}',
                    mapping={'rentDate': today, 'returnDate': week, 'overdue': 0})

    def get_user_ratings(self, user):
        # gets list of user's ratings
        user_ratings = self.r.hgetall(user)
        return user_ratings