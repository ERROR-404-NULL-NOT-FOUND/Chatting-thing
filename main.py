import os
import json
import time
def main():
    path="/usr/share/websites/chatting"
    while 1:
        if(os.listdir(f'{path}/channels')):
            for i in os.listdir(f'{path}/channels'):
                if(os.path.isfile(f'{path}/messages/{i}')):
                    
                    message=open(f'{path}/channels/{i}','r')
                    channel=open(f'{path}/messages/{i}','r')
                    
                    channelmessages=json.loads(channel.read())
                    tmpmssg=json.loads(message.read())

                    print(f'{tmpmssg["author"]}: {tmpmssg["content"]}')
                    channelmessages["messages"].append(tmpmssg)
                    open(f'{path}/messages/{i}','w').write(json.dumps(channelmessages))
                    
                    channel.close()
                    message.close()
                else:
                    print("Channel created: "+i.strip(".json"))
                    open(f'{path}/messages/{i}','x').write(open(f'{path}/channels/{i}','r').read())
                os.remove(f'{path}/channels/{i}')
    time.sleep(1)
while 1:
    try:
        main()
    except KeyboardInterrupt:
        print("Shutting down backend...")
        break
    except:
        pass