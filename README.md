ShortUrls
=========

Create short urls from regular ones. Project using Python 2.7, Flask, PostgreSQL and SQLAlchemy.
Project deployed on Heroku at <a href="http://bazub-shorturl.herokuapp.com/">this link</a>

How it works
------------

When you are on the main page, you are presented with an input form and a submit button. Put the url you want shortened inside the input form (it currently accepts only full links e.g. 'http://example.com' and not just 'example.com').

You will then be redirected to a new page, where you will see the long url, and the short url. The short url is stored in a database, so you can also use it at a later time.

It might happen to not be able to provide a short url for the url you provided, in which case you will get a message saying so.

The short url will always be in the following format: ```http://bazub-shorturl.herokuapp.com/slink/******``` where the 6 stars are replaced by lowercase english letters, and the numbers from 0 to 5.

How it works (technical details)
------------

1. The url you provide is transformed into md5, which will produce a 128-bit hash value (a 32 digits long hex number). 
2. The result is then split into 4 equal parts.
3. Each part is then transformed into a 6-digit code (that uses a-z & 0-5).
4. The first 6-digit code which hasn't been used yet will be used as the short-link code for the url you provided.
5. If your url is not in the database, it is stored.

Known Issues (FAQ)
-----------

1. After I add a url, the page gives me a shorter url than the one I provided.

  The app currently ignores anything that is after an "?" or other special characters in the url you provide.
  
2. The short url takes me to a "Page not found".
 
  That most likely means that the long url used to create is not a url or it wasn't used correctly when transformed to a short url (e.g. example.com was used instead of http://example.com)

3. The short url takes me to a "Internal Server Error".

  That means that the url doesn't currently exist in the database (will take care of that in future updates) or that there is an error with the servers.

If you have any questions <a href="mailto:bazu_b@yahoo.com">Contact me!</a>