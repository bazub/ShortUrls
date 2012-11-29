'''
Created on Nov 27, 2012

@author: Bogdan
'''
import os
from flask import Flask,redirect
from flask.globals import request
from flask.templating import render_template
from l2s import long2short, check_if_long_exists, get_first_not_used,insert_new_pair, get_short_for_long, get_long_url
from sqlalchemy.engine import create_engine
import flask


app = Flask(__name__)
engine = create_engine('postgresql+psycopg2://*')
connection= engine.connect()
connection.execute("CREATE TABLE IF NOT EXISTS shorturls (short TEXT,long TEXT)")
connection.close()

@app.route('/')
def hello_world():
    return render_template('main.html')

@app.route('/link/<path:url>')
def return_short_url(url):
    url=str(url)
    ok=0 #flag to check if I could find a possible short link
    if not check_if_long_exists(url):
        output=long2short(url)
        for i in range(0,4):
            if not get_first_not_used(output[i]):
                insert_new_pair(output[i],url)
                ok=1 #found a short link for the current link
                break
        if ok:
            rv="Long link: "+url+"<br>Short link: http://bazub-shorturl.herokuapp.com/slink/"+output[i]
        else: 
            rv="Could not create a short link. Sorry!"
    else:
        short=str(get_short_for_long(url))
        rv="1Long link: "+url+"<br>Short link: http://bazub-shorturl.herokuapp.com/slink/"+short
    
    return rv
@app.route('/slink/<url>')
def return_long_url(url):
    rv=get_long_url(url)
    return redirect(rv)
    #return '<meta http-equiv="REFRESH" content="0;url='+rv+'">'

@app.route('/transform',methods=['POST'])
def redir_to_link():
    rv =str(flask.request.form['url'])
    return redirect("/link/"+rv)
    #return '<meta http-equiv="REFRESH" content="0;url=http://localhost:5000/link/'+rv+'">'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)