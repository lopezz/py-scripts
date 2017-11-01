# -*- coding: utf-8 -*-
"""
HTML crawler to get all the iframe src's of a url list

author slopez - lopezcardona24@gmail.com
version 0.1
"""

import urllib2
from bs4 import BeautifulSoup

def geturls(filename):
    """
    takes a txt file as argument containing the urls and store its contents line by line in a list
    """
    with open(filename) as k:
        content = k.readlines()
    k.close()
    content = [x.strip() for x in content]
    return content


def getiframes(url, output_filename):
    """
    Opens and parse an url to find if there is any iframe tags. Also prints the iframe src
    """
    with open(output_filename, 'a') as outfile:
        print "Analyzing ", url, "..."
        outfile.write("Analyzing " + url + "...\n")

        page = urllib2.urlopen(url).read()
        soup = BeautifulSoup(page, "html.parser")
        total_iframes = 0
        src_list = []

        for iframe in soup.find_all('iframe'):
            src = iframe.get('src')
            if not iframe.get('src').startswith("//www.googletagmanager.com"):
                total_iframes += 1
                src_list.append(src + "\n")
        print "total_iframes in this url: ", total_iframes
        outfile.write("total_iframes in this url: " + str(total_iframes) + "\n")
        print "Iframe urls: "
        outfile.write("Iframe urls: \n")
        for src in src_list:
            print src
            outfile.write(src)
        print "\n"
        outfile.write("\n")


URL_LIST = geturls('urls.txt')
OUTPUT_FILE = 'output.txt'

for target_url in URL_LIST:
    getiframes(target_url, OUTPUT_FILE)
