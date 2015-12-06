"""parser.py: 

Parse the notepal post.

"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2015, Dilawar Singh and NCBS Bangalore"
__credits__          = ["NCBS Bangalore"]
__license__          = "GNU GPL"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

from lxml import etree
from lxml.html.soupparser import fromstring
import html2text


class NotepalParser( ):

    def __init__( self, feed ):
        self.feed = feed.decode ( errors = 'ignore' )
        self.htmlParser = etree.HTMLParser( )
        self.root = fromstring( self.feed )

    def get_post( self ):
        filteredTree =  etree.XPath( "//div[@class='content clearfix']" )
        res = self.root.find( ".//div[@class='content clearfix']")
        print("\n======================")
        print html2text.html2text( etree.tostring( res ))
        

