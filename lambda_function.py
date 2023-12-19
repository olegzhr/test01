import os
import json
import redis
import base64

def lambda_handler(event, context):
    
    redis_host = os.environ['RedisAddressEnvName']
    redis_port = 6379
    redis_password = ""
    respons_redis = ""
    
    output = []
    
    try:
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

    except Exception as e:
        print(e)
    
    for record in event['records']:
        # Do custom processing on the payload here
        
        payload = base64.b64decode(record['data'])
        
        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': record['data']
        }
        output.append(output_record)
        
        try:
            r.rpush('altprobe_aws', payload)
            
        except Exception as e:
            print(e)
            

    return {'records': output}

    
    
    
    
