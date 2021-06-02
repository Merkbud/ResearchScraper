# importing the module
from googlesearch import search
from newspaper.article import ArticleException
import xlsxwriter
import newspaper
import time
from newspaper import Article
from newspaper import Config
from urllib.error import HTTPError
user_agent = 'Edg/90.0.818.62'
config = Config()
config.browser_user_agent = user_agent

# creating the excel document
outWorkbook = xlsxwriter.Workbook("Archivaldata.xlsx")
outSheet = outWorkbook.add_worksheet()
x=503
# stored queries in a list

query_list = ["site:wsj.com before:2014","site:wired.com before:2014 ","site:newyorker.com before:2014","site:theverge.com before:2014","site:digitaltrends.com before:2014","site:techcrunch.com before:2014","site:nytimes.com before:2014","site:bloomberg.com before:2014","site:coindesk.com before:2014","site:forbes.com before:2014"]

# save the company name in a variable
crypto_name = " Dogecoin "

# iterate through different keywords, search and print

for j in query_list:
        for i in search(j+crypto_name,  tld='com', lang='en', num=100, start=0, stop=10, pause=60):
                x=x+1
                try:
                
                        page = Article(i, config=config)
                        page.download()
                        page.parse()
                        outSheet.write(0,0,"URL")
                        outSheet.write(0,1,"Author")
                        outSheet.write(0,2,"Publication date")
                        outSheet.write(0,3,"Publication")
                        outSheet.write(0,4,"Headline")
                        outSheet.write(0,5,"Cryptocurrency")
                        outSheet.write(x,0,i)
                        outSheet.write(x,1,str(page.authors))
                        outSheet.write(x,2,str(page.publish_date))
                        outSheet.write(x,3,str(j))
                        outSheet.write(x,4,str(page.title))
                        outSheet.write(x,5,str(crypto_name))
                        print(i)
                        time.sleep(10)
                except ArticleException as ae:
                        print(ae)
                        continue
                except HTTPError as e:
                        print(e)
                        continue

outWorkbook.close()