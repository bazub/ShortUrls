'''
Created on Nov 28, 2012

@author: Bogdan
'''
from sqlalchemy.engine import create_engine
import hashlib
engine = create_engine('postgresql+psycopg2://postgres:test123@localhost/shorts')
def long2short(url):
    base32='abcdefghijklmnopqrstuvwxyz012345'
    url=url.lower()
    m=hashlib.md5()
    m.update(url)
    output=[]
    for i in range(0,4):
        output.append("")
        subHex=m.hexdigest()[i*8:i*8+8]
        intval=0x3FFFFFFF & int(subHex,16)
        out=''
        for j in range(0,6):
            val=0x0000001F & intval
            out=out+base32[val]       
            intval= intval>>5
        output[i]=output[i]+out
    return output
def check_if_long_exists(longLink):
    connection= engine.connect()
    result=connection.execute("SELECT * FROM shorturls WHERE long=%s",longLink)
    connection.close()
    return result.rowcount
def get_first_not_used(shortLink):
    connection=engine.connect()
    result=connection.execute("SELECT * FROM shorturls WHERE short=%s",shortLink)
    connection.close()
    return result.rowcount
def insert_new_pair(shortLink,longLink):
    connection=engine.connect()
    connection.execute("INSERT INTO shorturls (short,long) VALUES(%s,%s)", shortLink, longLink)
    connection.close()
def get_short_for_long(longLink):
    connection=engine.connect()
    result=connection.execute("SELECT * FROM shorturls WHERE long=%s",longLink)
    connection.close()
    for row in result:  #only executes 1 operation, but didn't spend time to think of a more clever solution
        return row['short'] 
def get_long_url(shortLink):
    connection=engine.connect()
    result=connection.execute("SELECT * FROM shorturls WHERE short=%s",shortLink)
    if result.rowcount==0:
        return 1
    for row in result:
        return row["long"]