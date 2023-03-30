from book_redis import BookAPI
import time
import random


def main():


    api = BookAPI()

    # Insert new following
    api.add_book(file_name="cleanbooks.csv")

    # Post a new tweet
    api.add_rating(file_name="cleanratings.csv")
    print(api.get_user_ratings(8))



if __name__ == '__main__':
    main()
