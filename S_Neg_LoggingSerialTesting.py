from client import conn
from boto.exception import S3ResponseError
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
    #log-delivery group need WRITE & READ_ACP permissions - 400
    try:
        bucket=conn.create_bucket(arg[0])
        bucket.enable_logging(arg[0], 'loglog-')
    except S3ResponseError,e:
        Expectexception(e,400)
    
    #Target Bucket not exist-404
    try:
        bucket.enable_logging('nosuchbucket', 'loglog-')
    except S3ResponseError,e:
        Expectexception(e,400)
        
    conn.delete_bucket(arg[0]) 
    #print " - S_Neg_Logging Serial Test Done !"