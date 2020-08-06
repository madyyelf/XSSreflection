
import click
import urllib.request
import urllib.parse as urlparse
from urllib.parse import parse_qs
import requests
from tqdm import tqdm
import time
import random

@click.command()
@click.option('-f','--file',required=True,type=str)
@click.option('-o','--output',type=str)
@click.option('-m','--mark',type=str)
@click.option('-s','--sleep',type=int)
@click.option('-h','--human',default=False, type=bool)
def main(file,output,mark,sleep,human):
    if(mark==None):
        mark="patataman"
    f=open(file,"r")
    if(output is not None):
        o=open(output,"w")
    count=len(f.readlines())
    f.seek(0)

    for url in tqdm(f,total=count,desc="Processant: ",unit="URLs"):
        u=urlparse.urlparse(url)
        parameters=parse_qs(u.query)

        for param in list(parameters):
            parameters=parse_qs(u.query)
            newparameters=parameters
            newparameters[param]=mark
            res = urllib.parse.ParseResult(scheme=u.scheme, netloc=u.hostname, path=u.path, params=u.params, query=urllib.parse.urlencode(newparameters), fragment=u.fragment)
            try:
                newurl=res.geturl()
                page=requests.get(newurl)
                if(mark in page.text):
                    if(output is not None):
                        o.write(newurl+"\n")
                        tqdm.write(newurl)
            except Exception:
                pass
            if(sleep is not None):
                time.sleep(sleep)
            if(human == True):
                time.sleep(random.randint(4,9))


    f.close()
    if(output is not None):
        o.close()

if(__name__=='__main__'):
    main()
