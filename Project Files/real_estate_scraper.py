'''
Name of file: real_estate_scraper.py
Date created: August 29, 2018
Date last updated: September 25, 2018
Created by: James Ingram
Purpose of Program: Scrape real estate data from Zillow.com, parse it with BeautifulSoup, and write the output to a csv file
'''
# imports necessary pacakges, libraries, and dependencies
from bs4 import BeautifulSoup
import unicodecsv as csv
import codecs
import datetime
import os
import logging

# Web scraping from live website if !robots.txt
# from urllib import request
# html = request.urlopen(pageurl).read().decode('utf-8')
# soup = BeautifulSoup(html, 'html.parser')

def main_menu():
	# To avoid scraping data from live web server each page was downloaded onto localhost
	# Data from zillow.com, search term = "Albany, NY"
	alb_urls = ["apage1.html", "apage2.html", "apage3.html", "apage4.html", "apage5.html", "apage6.html", "apage7.html", "apage8.html", "apage9.html", "apage10.html", "apage11.html", "apage12.html", "apage13.html", "apage14.html", "apage15.html", "apage16.html", "apage17.html", "apage18.html", "apage19.html", "apage20.html"]
	# Data from zillow.com, search term = "Binghamton, NY"
	bing_urls = ["bpage1.html", "bpage2.html", "bpage3.html", "bpage4.html", "bpage5.html", "bpage6.html", "bpage7.html", "bpage8.html", "bpage9.html", "bpage10.html", "bpage11.html", "bpage12.html", "bpage13.html", "bpage14.html", "bpage15.html", "bpage16.html", "bpage17.html", "bpage18.html", "bpage19.html"]
	# Data from zillow.com, search term = "Buffalo, NY"
	buff_urls = ["bupage1.html", "bupage2.html", "bupage3.html", "bupage4.html", "bupage5.html", "bupage6.html", "bupage7.html", "bupage8.html", "bupage9.html", "bupage10.html", "bupage11.html", "bupage12.html", "bupage13.html", "bupage14.html", "bupage15.html", "bupage16.html", "bupage17.html", "bupage18.html", "bupage19.html", "bupage20.html"]
	# Data from zillow.com, search term = "Syracuse, NY"
	syr_urls = ["spage1.html", "spage2.html", "spage3.html", "spage4.html", "spage5.html", "spage6.html", "spage7.html", "spage8.html", "spage9.html", "spage10.html", "spage11.html", "spage12.html", "spage13.html", "spage14.html", "spage15.html", "spage16.html", "spage17.html", "spage18.html", "spage19.html", "spage20.html"]

	# create empty list to store data from scraped html documents
	properties_list = []
	# set initial count to 0
	writecount = 0
	# create date format to append to .csv filename
	now = datetime.datetime.today().strftime("%m%d%y")

	# function to scrape data from saved html documents
	def pagescraper(url):
		# reads html document
		f = codecs.open(url, 'r')
		# use BeautifulSoup to parse html
		soup = BeautifulSoup(f, 'html.parser')
		# finds div and class tags associated with desired data
		all = soup.find_all("div",{"class":"zsg-photo-card-content"})
		# iterates through data to extract desired fields. If data is missing, makes it null value and sends debug report to log file
		for item in all:
			try:
				raw_title = item.find("h4").text
			except:
				raw_title = None
				logging.debug("Listing title not found")
			try:
				raw_address = item.find("span",{"itemprop":"streetAddress"}).text
			except:
				raw_address = None
				logging.debug("Listing address not found")
			try:
				raw_city = item.find("span",{"itemprop":"addressLocality"}).text.lstrip().lower().title()
			except:
				raw_city = None
				logging.debug("Listing city not found")
			try:
				raw_state = item.find("span",{"itemprop":"addressRegion"}).text
			except:
				raw_state = None
				logging.debug("Listing state not found")
			try:
				raw_zip_code = str(item.find("span",{"itemprop":"postalCode"}).text)
			except:
				raw_zip_code = None
				logging.debug("Listing zip code not found")
			try:
				raw_price = int(item.find("span",{"class":"zsg-photo-card-price"}).text.replace("$","").replace(",",""))
			except:
				raw_price = None
				logging.debug("Listing price not found")
			try:
				raw_bed_info = int(item.find("span",{"class":"zsg-photo-card-info"}).text.split()[0])
			except:
				raw_bed_info = None
				logging.debug("Listing bedroom data not found")
			try:
				raw_bath_info = int(item.find("span",{"class":"zsg-photo-card-info"}).text.split()[3])
			except:
				raw_bath_info = None
				logging.debug("Listing bathroom data not found")
			try:
				raw_sqft_info = int(item.find("span",{"class":"zsg-photo-card-info"}).text.split()[6].replace(",",""))
			except:
				raw_sqft_info = None
				logging.debug("Listing area data not found")
			
			# append items to properties list
			properties = {
			'title':raw_title,
			'address':raw_address,
			'city':raw_city,
			'state':raw_state,
			'zip_code':raw_zip_code,
			'price':raw_price,
			'beds':raw_bed_info,
			'baths':raw_bath_info,
			'area':raw_sqft_info,
			'region':fname
			}
			properties_list.append(properties)
		return properties_list

	# creates log file and sets logging parameters
	logging.basicConfig(
		filename='real_estate.log',
		level=logging.DEBUG, 
		format='%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s', 
		datefmt="%Y-%m-%d %H:%M:%S")
	try:
		os.system('cls')
	except:
		os.system('clear')

	print("Real Estate Scraper\n")
	print("Choose city:\n")
	def menu(list,question):
		for item in list:
			print(1 + list.index(item), item)
		return input(question)
	while True:
		items = ["Albany, NY", "Binghamton, NY", "Buffalo, NY", "Syracuse, NY"]
		choice = menu(items,"\nPlease make a selection from the list above:\n>")
		try:
			choice = int(choice)
			break
		except:
			print("Invalid selection, please try again\n")
			continue
	print()

	# User makes a selection
	if choice == 1:
		urls = alb_urls
		fname = "albany"
	elif choice == 2:
		urls = bing_urls
		fname = "binghamton"
	elif choice == 3:
		urls = buff_urls
		fname = "buffalo"
	elif choice == 4:
		urls = syr_urls
		fname = "syracuse"
	else:
		main_menu()

	try:
		os.system('cls')
	except:
		os.system('clear')
	print("Reading html files from:")
	filecount = 0
	# iterates through list of html documents and runs pagescraper function
	for url in urls:
		print(url)
		pagescraper(url)
		filecount +=1
	print(filecount, "files successfully read!")

	print("\nWriting records to file...")
	fh = open("properties-" + fname + "-" + now + ".csv", "wb")
	# writes extracted data to .csv file
	try:
		with fh as csvfile:
			fieldnames = ['title','address','city','state','zip_code','price','beds','baths','area','region']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			for row in properties_list:
				writecount += 1
				writer.writerow(row)
			fh.close()
			logging.info("Records successfully written to file")
			print(writecount, "records written to 'properties-" + fname + "-" + now +".csv'")
	except:
		logging.debug("Records not written to file")
		print("Error: records could not be written to file!")
		quit()
	rescrape = input("\nWould you like to load more files?\n>")
	if rescrape.lower().startswith("y"):
		main_menu()
	else:
		analyze = input("\nWould you like to analyze the records now?\n>")
		if analyze.lower().startswith("y"):
			os.system("python real_estate_analyzer.py")
		else:
			print('\nTo analyze the records, run "real_estate_analyzer.py"')
			print("Goodbye!")
			quit()

###############################
# Program execution begins here
###############################
main_menu()
