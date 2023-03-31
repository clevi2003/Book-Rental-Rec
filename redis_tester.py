from book_redis import BookAPI
import time
import random


def main():


    api = BookAPI()

    # adds book data
    api.add_book(file_name="cleanbooks.csv")

    # adds ratings data
    api.add_rating(file_name="cleanratings.csv")
    print(api.get_users_ratings(8))
    print(api.get_users_who_rated(1552041778))



if __name__ == '__main__':
    main()
