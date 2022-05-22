from termcolor import colored
import datetime
from random import randint


def link_finder(scraped, daily):
    # Getting that day's date
    date = datetime.date.today().strftime("%d/%m/%Y")

    # Getting the length of the database
    lengthdb = scraped.count_documents({})
    print(colored(f'Found {lengthdb} documents...', 'green'))

    if lengthdb > 0:
        # Quarrying everything
        all = []
        for document in scraped.find():
            all.append(document)

        # Chosing a random document
        length = len(all)
        i = randint(0, length-1)
        chosenDoc = all[i]

        # Extracting link and index from the doc
        link = chosenDoc['link']
        index = chosenDoc['index']
        print(index)
        # Inserting the index with today's date
        no_repeat = {
            'Date': date,
            'index': index
        }

        daily.insert_one(no_repeat)

        # Deleting the entry from the main database
        scraped.delete_one({'index': index})
    else:
        link = None
        print(colored('The database is empty...', 'red'))

    return link


