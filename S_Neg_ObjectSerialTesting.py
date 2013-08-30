from client import conn
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
    #Copy Source bucket not exist    
    try:
        bucket=Bucket()
        bucket=conn.create_bucket(arg[0])
        bucket2=conn.create_bucket(arg[1])    
        key=bucket.new_key('test.txt')
        key.set_contents_from_string("Hello World!")
        bucket2.copy_key('cptest','nosuchbucket','test.txt')
    except S3ResponseError,e:
        Expectexception(e,404)
        
    #Copy Source Key not exist
    try:    
        key=bucket.new_key('test.txt')
        key.set_contents_from_string("Hello World!")
        bucket2.copy_key('cptest',arg[0],'nosuchkey')
    except S3ResponseError,e:
        Expectexception(e,404)
    
    #print " - S_Neg_Object Serial Test Done !"