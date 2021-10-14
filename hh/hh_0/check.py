from bs4 import BeautifulSoup
import requests
import csv
import os
import shutil

shutil.rmtree(".pages")
shutil.rmtree(".urls")