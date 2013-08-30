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
    #Invalid policy element-400
    try:
        bucket=conn.create_bucket(arg[0])
        policy='{"Wersion":"2012-10-17","ource":"arn:aws:s3:::'+arg[0]+'/*"}]}';
        bucket.set_policy(policy)
        
    except S3ResponseError,e:
        Expectexception(e,400)
        
    #print " - S_Neg_Policy Serial Test Done !"