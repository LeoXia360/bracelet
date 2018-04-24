from botocore.vendored import requests

switch = 0
hue = 0
vinyl = 0 
def lambda_handler(event, context):
    global vinyl
    global hue
    if(event["gesture"] == "0"): 
        if(hue == 0):
            hue = 1
        else: 
            hue = 0
        return "p"

    elif(event["gesture"] == "1"):
        global switch
        headers = {'Content-Type': 'application/json'}
        if (switch == 0): 
            data = '{"method":"passthrough", "params": {"deviceId": "800655B6B068CE49D0B446E32F86F56C19311152", "requestData": "{\\"system\\":{\\"set_relay_state\\":{\\"state\\":1}}}" }}'
            switch = 1
        else: 
            switch = 0
            data = '{"method":"passthrough", "params": {"deviceId": "800655B6B068CE49D0B446E32F86F56C19311152", "requestData": "{\\"system\\":{\\"set_relay_state\\":{\\"state\\":0}}}" }}'
        requests.post('https://use1-wap.tplinkcloud.com/?token=03546e31-A7XmhafFphGZ2NCjAYmzy1v', headers=headers, data=data)
    elif(event["gesture"] == "2"):
        headers = {'Content-Type': 'application/json'}
        if (vinyl == 0): 
            data = '{"method":"passthrough", "params": {"deviceId": "80065F035FCA08C63C68971D8C07927E18665D3F", "requestData": "{\\"system\\":{\\"set_relay_state\\":{\\"state\\":1}}}" }}'
            vinyl = 1
        else: 
            vinyl = 0
            data = '{"method":"passthrough", "params": {"deviceId": "80065F035FCA08C63C68971D8C07927E18665D3F", "requestData": "{\\"system\\":{\\"set_relay_state\\":{\\"state\\":0}}}" }}'
        requests.post('https://use1-wap.tplinkcloud.com/?token=03546e31-A7XmhafFphGZ2NCjAYmzy1v', headers=headers, data=data)
    elif(event["gesture"] == "3"):
        print("gesture3")
    return 1