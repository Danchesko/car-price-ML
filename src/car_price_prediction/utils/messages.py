SCRAPING_STARTED_MESSAGE = (
    "Scraped data was not found, scraping module" +
    " is being initialized with default/setted parameters")

SCRAPING_DATA_FOUND_MESSAGE = ("Scraped data was found, parameters " +
                       "will be created based on found data")

LOADING_RAW_DATA_MESSAGE = "Loading raw/scraped data..."

ESTIMATOR_TRAINING_MESSAGE = "Training a model..."

SUCESS_MESSAGE = "Parameters succesfully created"


def num_of_failed_pages(list_of_pages):
    return ("%d pages were failed to scrape" % len(list_of_pages))
