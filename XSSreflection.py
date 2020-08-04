
import click
import urllib.request
import urllib.parse as urlparse
from urllib.parse import parse_qs
import requests
from tqdm import tqdm

@click.command()
@click.option('-f','--file')
@click.option('-o','--output')
@click.option('-m','--mark')
def main(file,output,mark):
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
            newurl=res.geturl()
            page=requests.get(newurl)
            if(mark in page.text):
                if(output is not None):
                    o.write(newurl+"\n")
                tqdm.write(newurl)


    f.close()
    if(output is not None):
        o.close()

if(__name__=='__main__'):
    main()
