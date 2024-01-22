# EDGAR
Free tools for the efficient and consistent retrieval of corporate and financial data from the SEC. 

# What is EDGAR?

EDGAR is a database of corporate filings maintained by the United States Securities and Exchange Commission (SEC). These filings contain a wealth of quantitative and qualitative information on every legal entity that issues non-exempt securities in the United States. Whether you are looking to study the fundamentals of your favorite stocks, or to track the corporate webs weaved by a person or company of interest, EDGAR is the place to do it.

But there's a catch. 

To _programatically_ access EDGAR data in a consistent and reliable manner is a complex problem. Most people who have found solutions to this problem charge a fee for it, or only provide a limited free access to the obtained data. Thanks to funding from investigative journalism organization Bellingcat, I was able to devote six months to studying the EDGAR database, determining the most likely use cases for researchers and investors, and building tools that can help people exploit this incredible, free resource.

# Table of Cleaned Financial Data

I've built a table containing most income statement, balance sheet, and cash flow statement data for every company traded publicly in the U.S. This table is updated periodically, and [available here for download as a .CSV file](https://edgar.marketinference.com/). You can open this file in EXCEL, use it as a data source for your own code, or use my simple Python script to access time series for the desired data points. 

The current table is created by the following method:

  - Monthly bulk download of all company facts data from EDGAR (this is the data set accessed by the official APIs)
  - Scraping of all calculation sheets related to each filing associated with a publicly traded company
  - Create a dictionary matching the most commonly used GAAP tags with a plain English term 
  - For a given company, for each year:
    - Determine what GAAP tags are listed under each cashflow / income / balance sheet headings (or whatever alternative terms the company happens to use) in the calculation sheet 
    - For each tag:
      - Obtain all the data associated with the tag in the company's bulk download folder for the desired year, and the preceding one 
      - Determine whether the data is duration or point in time
      - Identify quarterly and yearly values based on the time data associated with each data point
      - Recalculate all quarterly values if the reported ones are cumulative
      - Calculate Q4 value
      - Create cleaned and sorted time series
      - Isolate the value for the considered year (or calculate trailing twelve month value based on preceding four quarters for this year if the company hasn't reported yet)
    - For some particularly problematic data points such as debts I use addition between related data points to ensure consistency (this is why the debt amounts are not always perfectly accurate, but almost always in the ballpark)
    - Match the GAAP tags with their plain English term
    - Keep a database of orphan tags, and add them into the dictionary, manually
   
The quality of any programatically produced finacial dataset is not going to be as accurate or as complete as a S&P Global or Bloomberg subscription. The dataset I have created is of comparable accuracy to what you can find on Yahoo Finance, but spans a wider time frame, and is good enough for me to use in my own projects such as [Market Inference](https://www.marketinference.com/) and [Graham](https://graham.marketinference.com/info). 

I believe we can keep improving this dataset – with your help! Please report inconsistencies to me and I will do my best to improve the existing method. I also am designing an entirely new method that I will implement early next year, based on the scraping of tables embedded in yearly/quarterly reports. 

# Text Search all EDGAR Filings

If you're interested in finding all the documents mentioning a certain person or a phrase in the EDGAR database, you can do that via text search. The problem is that there is no way to programmatically access the results. As a solution, I've built a [search and scraping script](EDGAR_text_search.py) in Python that allows you to search for up to 3 distinct phrases, to modify the desired time frame, and to search only quarterly/yearly reports if desired. Note that the method I have created is reliable up to the limit of 10,000 search results. So I recommend doing a few manual searches first to tailor the parameters until you get an acceptable quantity of results.

The script will give you a .CSV table with the date, name of the company, place of registration, place of business, ticker symbol, filing type, filing link, and document link. 

Let me know how it works! In a few months I will provide an updated version that automatically breaks over-ambitious searches into manageable time frames, and I will also try to include whatever other reasonable suggestions I receive. 

# RSS Feed Customizer

EDGAR has three RSS feeds, and I wrote a [RSS feed parsing script](EDGAR_RSS_custom.py)  that allows you to filter the feed to return only company/tickers of interest. The output is similar to the text search script in that it returns a .CSV with the name of the company, place of registration, place of business, ticker symbol, filing type, filing link, and document link. Here too, I would be happy to improve the tool according to your proposals. 




