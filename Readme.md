Technical Assignment: Run Selenium Test on BrowserStack
We’d like you to build a script demonstrating skills in web scraping, API integration, and text processing using the Selenium framework (any language of your choice). Follow the steps below:

Visit the website El País, a Spanish news outlet.
Ensure that the website's text is displayed in Spanish.
Scrape Articles from the Opinion Section:
    Navigate to the Opinion section of the website.
    Fetch the first five articles in this section.
    Print the title and content of each article in Spanish.
    If available, download and save the cover image of each article to your local machine.
Translate Article Headers:
    Use a translation API of your choice, such as:
    Google Translate API
    Rapid Translate Multi Traduction API
    Translate the title of each article to English.
    Print the translated headers.
Analyze Translated Headers:
    From the translated headers, identify any words that are repeated more than twice across all headers combined.
    Print each repeated word along with the count of its occurrences.
Cross-Browser Testing:
    Run the solution locally to verify functionality.
    Once validated, execute the solution on BrowserStack across 5 parallel threads, testing across a combination of desktop and mobile browsers.
    Submission: Kindly upload your completed assignment source code to GitHub within the next 3 days.


Notes:
1 avoid time.sleep
2 specific xpaths
(By.XPATH,'//section[@data-dtm-region="portada_apertura"]')