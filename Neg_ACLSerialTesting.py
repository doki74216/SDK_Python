from boto.s3.connection import S3Connection
from boto.exception import S3ResponseError
from boto.s3.bucket import Bucket
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
    #fake Accessey
    try:
        conn = S3Connection('123','KsfrFsMZpRnNEDa6XTcimwzdc9/qpyobSDCWc/Ft')
        conn.create_bucket(arg[0])
    except S3ResponseError, e:
        Expectexception(e,403)
    #fake SecretKey
    try:
        conn = S3Connection('AKIAJSVJQLDTTJ4JATAA','123')
        conn.create_bucket(arg[0])
    except S3ResponseError, e:
        Expectexception(e,403)
    #Nosuch user
    try:
        conn=  S3Connection('AKIAJSVJQLDTTJ4JATAA','KsfrFsMZpRnNEDa6XTcimwzdc9/qpyobSDCWc/Ft')
        bucket=conn.create_bucket(arg[0])
        bucket.add_email_grant('FULL_CONTROL', '123@abc.def')
    except S3ResponseError, e:
        Expectexception(e,400)
    #Nosuch user 
    try:
        bucket.add_user_grant('FULL_CONTROL', '123')
    except S3ResponseError, e:
        Expectexception(e,400)
    
# print " - Neg_ACL Serial Test done !"
    

 
    