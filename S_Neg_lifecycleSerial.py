import boto.s3
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
    #Overlapping prefixs-400
    try:
        bucket=conn.create_bucket(arg[0])
        expire=boto.s3.lifecycle.Expiration(date='2020-10-17T00:00:00.000Z')
        lifecycle_config = boto.s3.lifecycle.Lifecycle()
        lifecycle_config.add_rule('testLC1', 'gg', 'Enabled',1)
        lifecycle_config.add_rule('testLC2', 'gghh', 'Enabled',expire)
        
        bucket.configure_lifecycle(lifecycle_config)
        result=bucket.get_lifecycle_config()
        for rules in result:
            print "Rule ID: "+rules.id
            print "prefix: "+rules.prefix
            print "Expiration: "+repr(rules.expiration)
        
        print "Clean up.."
        bucket.delete_lifecycle_configuration()
        conn.delete_bucket(bucket)
        
    except S3ResponseError, e:
        Expectexception(e,400)
    
    #Expire date form error-400    
    try:
        bucket=conn.create_bucket(arg[0])
        expire=boto.s3.lifecycle.Expiration(date='2020-10-17')
        lifecycle_config = boto.s3.lifecycle.Lifecycle()
        lifecycle_config.add_rule('testLC2', 'gghh', 'Enabled',expire)
        
        bucket.configure_lifecycle(lifecycle_config)
        result=bucket.get_lifecycle_config()
        for rules in result:
            print "Rule ID: "+rules.id
            print "prefix: "+rules.prefix
            print "Expiration: "+repr(rules.expiration)
        
        print "Clean up.."
        bucket.delete_lifecycle_configuration()
        conn.delete_bucket(bucket)
    except S3ResponseError, e:
        Expectexception(e,400)
        
    #print " - Lifecycle Serial Test Done !"
    