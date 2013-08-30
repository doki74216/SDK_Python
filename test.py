import boto.s3.connection
from boto.s3.connection import S3Connection
from boto.s3.key import Key
print("Hello world!");
access_key = 'AKIAJSVJQLDTTJ4JATAA'
secret_key = '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'
#to use custom host
#     conn2 = boto.connect_s3(
#             aws_access_key_id = access_key,
#             aws_secret_access_key = secret_key,
#             host = 'objects.dreamhost.com',
#             #is_secure=False,               # uncommmnt if you are not using ssl
#             calling_format = boto.s3.connection.OrdinaryCallingFormat(),
#             )

#Initiate connection without using boto.cfg
conn = S3Connection('AKIAJSVJQLDTTJ4JATAA','KsfrFsMZpRnNEDa6XTcimwzdc9/qpyobSDCWc/Ft')
#setting proxy if not using boto.cfg
conn.proxy='10.160.3.88'
conn.proxy_port='8080'

bucket = conn.create_bucket('chttest5')

print(bucket.list)

k = Key(bucket)
print(k)
k.key = 'foobar2'
k.set_contents_from_string('This is a test2 of S3')



# List Buckets
result = conn.get_all_buckets()
for b in result:
    print "Bucket :"+b.name
    for key in b.list():
        print " - "+key.name.encode('utf-8')

            
