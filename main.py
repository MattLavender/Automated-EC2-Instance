import os,parser,json,io,time,request
import boto3,botocore
from time import sleep
import sys



# Import AWS Credential File
# Temporary, use this path
AWSCredential_FilePath='/root/.aws/credentials'
try:
    with open(AWSCredential_FilePath) as f:
        print('Your Credential:')
        for line in f:
            print('\t'+line.strip())
except FileNotFoundError as FileError:
    print("Credential File Error:",FileError)
    sys.exit(1)

# Import AWS Config File
# Temporary, use this path
AWSConfig_FilePath='/root/.aws/config'
try:
    with open(AWSConfig_FilePath) as f:
        print('Your AWS Config:')
        for line in f:
            print('\t'+line.strip())
except FileNotFoundError as FileError:
    print("AWS Config File Error:",FileError)
    sys.exit(1)



# Import EC2 Configuration File
EC2_ConfiguationFilePath='/work/Automated-EC2-Instance/EC2-Instance-config.json'
try:
    with open(EC2_ConfiguationFilePath) as f:
        print('Your Configuration:')
        JSON_EC2_ConfigFile=json.load(f)
        print(JSON_EC2_ConfigFile)
except (FileExistsError,FileNotFoundError) as FileError:
    print("Configuration File Error:",FileError)
# Connect to AWS
try:
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    print('Connection Successful')
except botocore.exceptions.ClientError as ConnectError:
    print(ConnectError)
    sys.exit(1)

# Create EC2-Instance

print('='*40)
print('Create new EC2-Instance')
print('='*40)
ec2_resource=boto3.resource('ec2')
instance = ec2_resource.create_instances(
    ImageId = 'ami-0615132a0f36d24f4',
    MinCount = 1,
    MaxCount = 1,
    InstanceType = 't2.micro',
    KeyName = 'Csi@dvtk',
    SubnetId = 'subnet-3a5aad72',
    ## Added
    # Vpc = 'vpc-3ee8fa59'
)
print (instance[0].id)
