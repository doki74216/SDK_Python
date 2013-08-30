import os
import time
import ACLSerialTesting
import BucketLoggingSerialTesting
import BucketSerialTesting
import LifecycleSerialTesting
import MPUSerialTesting
import ObjectSerialTesting
import PolicySerialTesting
import VersioningSerialTesting
import WebsiteSerialTesting
import Neg_ACLSerialTesting
import Neg_BucketSerialTesting
import S_Neg_lifecycleSerial
import S_Neg_LoggingSerialTesting
import S_Neg_ObjectSerialTesting
import S_Neg_PolicySerialTesting

#Change test buckets' name here
buckets=["allentest1","allentest2","allentest3"] 

print "S3 Python SDK Serial Test-\nbucketname1: "+buckets[0]+" ,bucketname2: "+buckets[1]
print "-----------------------------------------------------------------------"
 
# os.system('echo ACLSerialTesting ')
# ACLSerialTesting.main(buckets);
# time.sleep(5)
#   
# os.system('echo BucketLoggingSerialTesting ')
# BucketLoggingSerialTesting.main(buckets);
# time.sleep(5)
#    
# os.system('echo BucketSerialTesting ')
# BucketSerialTesting.main(buckets);
# time.sleep(5)
#    
# os.system('echo LifecycleSerialTesting ')
# LifecycleSerialTesting.main(buckets);
# time.sleep(5)
#    
os.system('echo MPUSerialTesting ')
MPUSerialTesting.main(buckets);
time.sleep(5)
#    
# os.system('echo ObjectSerialTesting ')
# ObjectSerialTesting.main(buckets);
# time.sleep(5)
#    
# os.system('echo PolicySerialTesting ')
# PolicySerialTesting.main(buckets);
# time.sleep(5)
#    
# os.system('echo VersioningSerialTesting ')
# VersioningSerialTesting.main(buckets);
# time.sleep(5)
#    
# os.system('echo WebsiteSerialTesting ')
# WebsiteSerialTesting.main(buckets);
# time.sleep(5)
#  
#  
# #Negative_test
#   
# os.system('echo Neg_ACLSerialTesting ')
# Neg_ACLSerialTesting.main(buckets);
# time.sleep(5)
#   
# os.system('echo Neg_BucketSerialTesting ')
# Neg_BucketSerialTesting.main(buckets); 
# time.sleep(5)
#   
# os.system('echo S_Neg_lifecycleSerial ')
# S_Neg_lifecycleSerial.main(buckets);
# time.sleep(5)
#   
# os.system('echo S_Neg_LoggingSerialTesting ')
# S_Neg_LoggingSerialTesting.main(buckets);
# time.sleep(5)
#    
# os.system('echo S_Neg_ObjectSerialTesting ')
# S_Neg_ObjectSerialTesting.main(buckets);
# time.sleep(5)
#    
# os.system('echo S_Neg_PolicySerialTesting ')
# S_Neg_PolicySerialTesting.main(buckets);

os.system('echo S3 Python SDK Serial Test Done!')