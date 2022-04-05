#!/usr/bin/env python3
import os
import json
import time
def main():
    path="/usr/share/websites/chatting"
    messagelength=2000
    while 1:
        accountsfile=open(f'{path}/accounts/accounts.json','r')
        accounts=json.loads(accountsfile.read())
        if(os.listdir(f'{path}/channels')):
            for i in os.listdir(f'{path}/channels'):
                if(os.path.isfile(f'{path}/messages/{i}')):
                    
                    message=open(f'{path}/channels/{i}','r')
                    channel=open(f'{path}/messages/{i}','r')
                    
                    channelmessages=json.loads(channel.read())
                    tmpmssg=json.loads(message.read())
                    if(tmpmssg["content"]!="" and len(tmpmssg["content"])<messagelength):
                        exists=False
                        index=0
                        for j in range(len(accounts)):
                            if(accounts[j]["username"]==tmpmssg["author"]):
                                exists=True
                                index=j
                        if (exists):
                            if("password" in tmpmssg):
                                if(tmpmssg["password"]==accounts[index]["password"]):
                                    print(f'{tmpmssg["author"]}: {tmpmssg["content"]}')
                                    tmpmssg={
                                        "date":tmpmssg["date"],
                                        "author":tmpmssg["author"],
                                        "content":tmpmssg["content"]
                                    }
                                    channelmessages["messages"].append(tmpmssg)
                                    open(f'{path}/messages/{i}','w').write(json.dumps(channelmessages))
                                else:
                                    print("Auth failed")
                            else:
                                print("No password supplied")
                        else:
                            print(f'{tmpmssg["author"]}: {tmpmssg["content"]}')
                            channelmessages["messages"].append(tmpmssg)
                            open(f'{path}/messages/{i}','w').write(json.dumps(channelmessages))
                    
                    channel.close()
                    message.close()
                else:
                    print("Channel created: "+i.strip(".json"))
                    open(f'{path}/messages/{i}','x').write(open(f'{path}/channels/{i}','r').read())
                os.remove(f'{path}/channels/{i}')
        
        if(os.listdir(f'{path}/createaccount')):
            print('Processing account creation request')

            for i in os.listdir(f'{path}/createaccount'):

                newaccount=open(f'{path}/createaccount/{i}','r').read()
                newaccount=json.loads(newaccount)
                exists=False
                for j in accounts:
                    if(j["username"]==newaccount["username"]):
                        exists=True
                if(not exists):
                    if(newaccount["username"] and newaccount["password"]):
                        print(f'{newaccount["username"]} created an account')
                        accounts.append(newaccount)
                        open(f'{path}/accounts/accounts.json','w').write(json.dumps(accounts))
                else:
                    print(f'User tried to overwrite account {newaccount["username"]}')
                os.remove(f'{path}/createaccount/{i}')
        accountsfile.close()
        time.sleep(1)
main()
'''while 1:
    try:
        main()
    except KeyboardInterrupt:
        print("Shutting down backend...")
        break
    except Exception as e:
        print(e)
'''
