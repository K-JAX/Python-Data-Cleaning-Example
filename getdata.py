import urllib.request
import os.path as path
import time

def get_file_age(file):
	return time.time() - path.getmtime(file)

day = 86400

if get_file_age('Datasets/owid-covid-data.csv') > day:
	print('Beginning file download wtih urllib2...')
	url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
	urllib.request.urlretrieve(url, 'Datasets/owid-covid-data.csv')