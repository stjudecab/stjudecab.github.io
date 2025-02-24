#!/usr/bin/env python
#!/usr/bin/env pypy
#########################################################################
# Copyright (c) 2020-~ Beisi Xu && St Jude
# This source code is released for free distribution under the terms of the
# Attribution-NonCommercial-ShareAlike 4.0 International (cc)
#*Author:       Beisi Xu < xubeisi [at] gmail DOT com >
# File Name: bibtex_organizer.py            Created Time: Mon Feb 22 00:43:52 CST 2021
#########################################################################

from __future__ import print_function
import re, os, sys, shutil
from string import *
import argparse
import time

import urllib.request
import bibtexparser

dbsamptext = """@article{2019_NatNeurosci_yang,
  title = {Differentiation of Human Pluripotent Stem Cells into Neurons or Cortical Organoids Requires Transcriptional Co-Regulation by {{UTX}} and {{53BP1}} Cofi},
  author = {Yang, Xiaoyang and Xu, Beisi and Mulvey, Brett and Evans, Myron and Jordan, Samuel and Wang, Yong-Dong and Pagala, Vishwajeeth and Peng, Junmin and Fan, Yiping and Patel, Arishna and Peng, Jamy C.},
  year = {2019},
  month = mar,
  volume = {22},
  pages = {362--373},
  issn = {1546-1726},
  doi = {10.1038/s41593-018-0328-5},
  abstract = {An interaction between UTX and 53BP1, which occurs in humans but not mice, promotes neurogenic gene expression that underlies neuronal differentiation and cortical development, perhaps providing insight into human-specific neurodevelopment.},
  copyright = {2019 The Author(s), under exclusive licence to Springer Nature America, Inc.},
  file = {files/5226/Yang et al. - 2019 - Differentiation of human pluripotent stem cells in.pdf;files/5225/s41593-018-0328-5.html},
  journal = {Nat Neurosci},
  language = {en},
  number = {3},
  pmcid = {PMC6511450},
  pmid = {30718900}
}"""

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
headers = {'User-Agent': user_agent}
apiurl_jabref = "https://abbreviso.toolforge.org/a/"
apiurl_pmc = "https://www.ncbi.nlm.nih.gov/pmc/articles/"

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def journal2abbr_jabref(journal):
    url = apiurl_jabref + urllib.parse.quote(journal)
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        theabbr = response.read()
    return str(theabbr.replace(b",",b".").decode("utf-8"))

def getPMCFig1(entry):
    url = apiurl_pmc + entry['pmcid']
    req = urllib.request.Request(url, headers=headers)
    #import pdb; pdb.set_trace()
    try:
        with urllib.request.urlopen(req) as response:
            page = response.read()
    except:
        sys.stderr.write("getPMCFig1: %s Error\n" % url)
        return entry
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page)
    tags = soup.findAll('img')
    igot = 0
    for tag in tags:
        if re.search("/bin/",tag['src']):
            igot += 1
            suf = tag['src'].split(".")[-1]
            newname = ".".join([ "Highlight", entry['ID'], "fig1", suf])
            if os.path.isfile(newname):
                sys.stderr.write("getPMCFig1: Skip Figure %s\n" % (newname))
                entry['fig1'] = newname
                break
            url = re.sub("/pmc/.*","",apiurl_pmc) + tag['src']
            try:
                req = urllib.request.Request(url, headers=headers)
                with urllib.request.urlopen(req) as response:
                    with open(newname, 'b+w') as f:
                        f.write(response.read())
                entry['fig1'] = newname
                break
            except:
                sys.stderr.write("getPMCFig1: %s Figure %d Error\n" % (url, igot))
    return entry

def checkstdinout(file,inorout="in",info="file"):
    if file in [ "-", None ] or file.replace("std","") == inorout:
        if inorout == "out":
            fff = sys.stdout
        else:
            fff = sys.stdin
    elif not os.path.isfile(file) and inorout == "in":
        sys.stderr.write("%s not exist %s\n" % (file, info))
        sys.exit(0)
    elif inorout == "out":
        if file.split('.')[-1] == 'gz':
            import gzip
            fff = gzip.open(file,'w')
        else:
            fff = open(file,'w')
    elif inorout == "append":
        if file.split('.')[-1] == 'gz':
            import gzip
            fff = gzip.open(file,'a')
        else:
            fff = open(file,'a')
    elif inorout == "in":
        if file.split('.')[-1] == 'gz':
            import gzip
            fff = gzip.open(file,'r')
        else:
            fff = open(file,'r')
    return fff



def main(argv):
    parser = argparse.ArgumentParser(description="%prog [options] -f filein -o fileout -m mode ",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-f", "--filein", action="store", type=str,
                      dest="fin", help="in file name,.gz would gzip, none|stdin|- means stdin", metavar="<file>")
    parser.add_argument("-o", "--fileout", action="store", type=str,
                      dest="fout", help="out file name,.gz would gzip, none|stdout|- means stdout", metavar="<string>")
    parser.add_argument("-m", "--mode", action="store", type=str,
                      dest="mode", help="abbr(get Journal Abbreviation),fig get 1st figure from PMC", metavar="<string>",default="abbr,fig")
    opt = parser.parse_args()
    if len(argv) < 2:
        parser.print_help()
        sys.exit(0)

    ffin = checkstdinout(opt.fin,"in","--filein")
    if os.path.isfile(opt.fin) and opt.fout == None:
        opt.fout = ".".join(opt.fin.split(".")[:-1] + [ "clean", "bib"])
    ffout = checkstdinout(opt.fout,"out","--fileout")
    
    modes = opt.mode.split(",")
    bibtex_database = bibtexparser.bparser.BibTexParser(common_strings=True).parse_file(ffin)
    for entry in bibtex_database.entries:
        if "abbr" in modes:
            abbr = journal2abbr_jabref(entry['journal'])
            entry['abbr'] = abbr
            sys.stderr.write (" ".join(["Abbr      :", entry['abbr'], "##", entry['journal'], "##", entry['year']]) + "\n")
        if "fig" in modes:
            if 'pmcid' in entry:
                entry = getPMCFig1(entry)

    #    print (entry.journal, entry.year)

    bibtexparser.dump(bibtex_database,ffout)

if __name__ == "__main__":
    main(sys.argv)


