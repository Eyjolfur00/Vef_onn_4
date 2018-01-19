from bottle import *
import os

@route('/')
def index():
    return """
    <!DOCTYPE html>
           <html>
               <head>
                   <title>Verkefni1</title>
                   <meta charset="utf-8">
               </head>
               <body>
                   <h1>Sidur</h1>
                   <ul>
                       <li><a href="/1">forsida</a></li>
                       <li><a href="/2">totierkoolkid</a></li>
                       <li><a href="/3">supremehere</a></li>
                   </ul>

                </body>
           </html>
            """
@route('/<nr>')
def index(nr):
    if nr =="0":
        return """
    <!DOCTYPE html>
           <html>
               <head>
                   <title>Verkefni1</title>
                   <meta charset="utf-8">
               </head>
               <body>
                   <h1>Sidur</h1>
                   <ul>
                       <li><a href="/1">forsida</a></li>
                       <li><a href="/2">totierkoolkid</a></li>
                       <li><a href="/3">supremehere</a></li>
                   </ul>

                </body>
           </html>
            """
    
    if nr=='1':
        return """
    <!DOCTYPE html>
           <html>
               <head>
                   <title>Verkefni1</title>
                   <meta charset="utf-8">
               </head>
               <body>
                   <h1>Forsíða</h1>
                   <ul>
                       <li><a href="/0">Sidur</a></li>
                       <li><a href="/2">totierkoolkid</a></li>
                       <li><a href="/3">supremehere</a></li>
                   </ul>
            """

    if nr=='2':
        return """
    <!DOCTYPE html>
           <html>
               <head>
                   <title>Verkefni1</title>
                   <meta charset="utf-8">
               </head>
               <body>
                   <h1>TotierKOOLkid </h1>
                   <ul>
                       <li><a href="/0">Sida</a></li>
                       <li><a href="/1">Forsíða</a></li>
                       <li><a href="/3">supremehere</a></li>
                   </ul>
            """
    if nr=='3':
        return """
    <!DOCTYPE html>
           <html>
               <head>
                   <title>Verkefni1</title>
                   <meta charset="utf-8">
               </head>
               <body>
                   <h1>Supremehere</h1>
                   <ul>
                       <li><a href="/0">Sída</a></li>
                       <li><a href="/1">forsida</a></li>
                       <li><a href="/2">totierkoolkid</a></li>
                   </ul>
            """


run(host="localhost", port=8080, debug = True)


