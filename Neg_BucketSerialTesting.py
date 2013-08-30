from boto.exception import S3ResponseError
from client import conn
from xml.dom import minidom

def Expectexception(e,code):
    if(e.status != code):
        print"Expected Status Code :"+repr(code)+", get another Exception...";
        xmldoc = minidom.parseString(e.body)
        itemlist = xmldoc.getElementsByTagName('Message')
        print "Status Code: " + repr(e.status)
        print "Reason: " + repr(e.reason)
        print "Message: " + itemlist[0].childNodes[0].nodeValue
def main(arg):
    #too much buckets-400
    try:
        for index in range(105):
            #print "Create no."+repr(index)+" Bucket"
            conn.create_bucket('chtt'+repr(index))
    except S3ResponseError, e:
        Expectexception(e,400)
    
    #The specified bucket does not exist-404
    try:          
        for index in range(105):
            #print "Delete no."+repr(index)+" Bucket"
            conn.delete_bucket('chtt'+repr(index))
        
    except S3ResponseError, e:
        Expectexception(e,404)
    
    
    #The specified bucket does not exist 404-
    try:          
        bucket=conn.get_bucket('nosuchbucket')
    except S3ResponseError, e:
        Expectexception(e,404)
    
    #print " - Neg_Bucket Serial Test Done !"
        