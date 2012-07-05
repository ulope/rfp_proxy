========================================
Radio Free Python Feed Proxy (and fixer)
========================================

This is a simple proxy for `Radio Free Python`_'s MP3 feed.

.. _`Radio Free Python`: http://radiofreepython.com/

Purpose
-------

The purpose is to make the feed usable by a wider range of podcatchers.

Problem
-------

In the original feed the url to the audio file contains spaces but when requested like this from the server returns a 404.
Escaping the spaces with `%20` fixes the problem. And that is all this proxy does :)

Live version
------------

An instance of this proxy is running at http://rfpproxy.ulo.pe, hosted on heroku.