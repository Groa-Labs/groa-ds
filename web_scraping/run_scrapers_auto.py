from dotenv import load_dotenv
from util import run_IMDB_scraper

load_dotenv()
#First arg -- reviewid to scrape from
#Second arg -- reviewid to scrape till
#Third arg --  Number of reviews to be stored in each s3 file
run_IMDB_scraper(1, 12,2)
