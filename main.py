import random
import time

def generate_random_date(start_date, end_date):
    print("Generating a random date between", start_date, "and", end_date)
    randomGenerator = random.Random()
    dateFormat = '%m/%d/%Y'
    start_time = time.mktime(time.strptime(start_date, dateFormat))
    end_time = time.mktime(time.strptime(end_date, dateFormat))
    random_time = randomGenerator.randint(int(start_time), int(end_time))
    random_date = time.strftime(dateFormat, time.localtime(random_time))