import json
import boto3
import base64
import time

s3 = boto3.client('s3')
def lambda_handler(event, context):
    start_time = time.time()
    bucket = 'api123'
    key = 'cheetah_beta_118_0_49.data.cfs.bin'
    data = s3.get_object(Bucket=bucket, Key=key)
    content = data['Body'].read()
    #value = content.decode('utf8')
    encodedZip = base64.b64encode(content)
    endata = encodedZip.decode('ascii')
    #decodedZip = base64.b64decode(endata)
    #dedata = decodedZip.decode('ascii')
    # print(str(dedata))
    #print(endata)
    complete_data =[]
    filecount = 0
    chunks, chunk_size = len(endata), len(endata)//400
    print(chunks)
    print(chunk_size)
    n = 400
    packet = 0
    for i in range(0, len(endata), n):
            packet = packet+1
            dict_data = {
                "version": "1.0.0",
                 "type": "MCU",
                 "current_packet": packet,
                 "total_packets": chunk_size,
                 "psyload": [endata[i:i + 400]]
               }
            complete_data.append(dict_data)
    print("--- %s seconds ---" % (time.time() - start_time))
    return(complete_data)
