import random
import json
import fbchat
import time

username = "E-MAIL" #Replace this field with the e-mail of the account you want to use
passW = "PASSWORD" #Replace this field with the account's password
client = fbchat.Client(username, passW)
i = 0
def main():
    Givers = ['Name1', 'Name2', 'Name3', 'Name4', 'Name5', 'Name6', 'Name7', 'Name8', 'Name9', 'Name10', 'Name11', 'Name12', 'Name13', 'Name14', 'Name15', 'Name16', 'Name17', 'Name18', 'Name19', 'Name20', 'Name21', 'Name22', 'Name23', 'Name24', 'Name25', 'Name26', 'Name27']
    Receivers = ['Name1', 'Name2', 'Name3', 'Name4', 'Name5', 'Name6', 'Name7', 'Name8', 'Name9', 'Name10', 'Name11', 'Name12', 'Name13', 'Name14', 'Name15', 'Name16', 'Name17', 'Name18', 'Name19', 'Name20', 'Name21', 'Name22', 'Name23', 'Name24', 'Name25', 'Name26', 'Name27']
    PairsDict = { }
    cnt = 0
    InUse = 0
    Fine = False
    Fin = True

    for x in Givers:    
        InUse = random.randint(0,len(Receivers)-1)                
        while Receivers[InUse] == 99:
            InUse = random.randint(0,len(Receivers)-1)
            if InUse == 99:
                continue 
        PairsDict[cnt] = {Givers[cnt] : Receivers[InUse]}    
        cnt += 1
        Receivers[InUse] = 99
    for item in PairsDict.items():
        rec = json.dumps(item[1]).split('{')[1].split(':')[1].split('}')[0].split('"')[1]
        sndr = json.dumps(item[1]).split('{')[1].split(':')[0].split('"')[1]
        print(sndr + ' is ' + rec + '\'s secret santa!')
    #print(json.dumps(item[1]).split('{')[1].split(':')[0])
    #print(json.dumps(item[1]).split('{')[1].split(':')[1].split(' ')[1].split('}')[0])
        if rec == sndr:
            print('retry')
            Fin = False
            main()
            break    
    if Fin:      
        for item in PairsDict.items():            
            rec = json.dumps(item[1]).split('{')[1].split(':')[1].split(' ')[1].split('}')[0].split('"')[1]
            sndr = json.dumps(item[1]).split('{')[1].split(':')[0].split('"')[1]
             # -WARNING- A LOOT OF ELIF STATEMENTS INCOMING, plese don't kill me :) -WARNING- #
            if sndr == 'Name1':
                client.sendMessage(rec, thread_id= 'TODO: GET userid VALUE FROM FACEBOOK PROFILE PAGE SOURCE')  
            elif sndr == 'Name2':
                client.sendMessage(rec, thread_id= 'TODO: GET userid VALUE FROM FACEBOOK PROFILE PAGE SOURCE')  
            elif sndr == 'Name3':
                client.sendMessage(rec, thread_id= 'TODO: GET userid VALUE FROM FACEBOOK PROFILE PAGE SOURCE')  
            elif sndr == 'Name4':
                client.sendMessage(rec, thread_id= 'TODO: GET userid VALUE FROM FACEBOOK PROFILE PAGE SOURCE')  
            elif sndr == 'Name5':
                client.sendMessage(rec, thread_id= 'TODO: GET userid VALUE FROM FACEBOOK PROFILE PAGE SOURCE')  
            elif sndr == 'Name6':
                client.sendMessage(rec, thread_id= 'TODO: GET userid VALUE FROM FACEBOOK PROFILE PAGE SOURCE')  
            elif sndr == 'Name7':
                client.sendMessage(rec, thread_id= 'TODO: GET userid VALUE FROM FACEBOOK PROFILE PAGE SOURCE')  
            elif sndr == 'Name8':
                client.sendMessage(rec, thread_id= 'TODO: GET userid VALUE FROM FACEBOOK PROFILE PAGE SOURCE')  
            elif sndr == 'Name9':
                client.sendMessage(rec, thread_id= 'TODO: GET userid VALUE FROM FACEBOOK PROFILE PAGE SOURCE')  
            elif sndr == 'Name10':
                client.sendMessage(rec, thread_id= 'TODO: GET userid VALUE FROM FACEBOOK PROFILE PAGE SOURCE')  
            elif sndr == 'Name11':
                client.sendMessage(rec, thread_id= 'TODO: GET userid VALUE FROM FACEBOOK PROFILE PAGE SOURCE')  
            elif sndr == 'Name12':
                client.sendMessage(rec, thread_id= 'TODO: GET userid VALUE FROM FACEBOOK PROFILE PAGE SOURCE')  
            elif sndr == 'Name13':
                client.sendMessage(rec, thread_id= 'TODO: GET userid VALUE FROM FACEBOOK PROFILE PAGE SOURCE')  
            elif sndr == 'Name14':
                client.sendMessage(rec, thread_id= 'TODO: GET userid VALUE FROM FACEBOOK PROFILE PAGE SOURCE')  
            elif sndr == 'Name15':
                client.sendMessage(rec, thread_id= 'TODO: GET userid VALUE FROM FACEBOOK PROFILE PAGE SOURCE')  
            elif sndr == 'Name16':
                client.sendMessage(rec, thread_id= 'TODO: GET userid VALUE FROM FACEBOOK PROFILE PAGE SOURCE')  
            elif sndr == 'Name17':
                client.sendMessage(rec, thread_id= 'TODO: GET userid VALUE FROM FACEBOOK PROFILE PAGE SOURCE')  
            elif sndr == 'Name18':
                client.sendMessage(rec, thread_id= 'TODO: GET userid VALUE FROM FACEBOOK PROFILE PAGE SOURCE')  
            elif sndr == 'Name19':
                client.sendMessage(rec, thread_id= 'TODO: GET userid VALUE FROM FACEBOOK PROFILE PAGE SOURCE')  
            elif sndr == 'Name20':
                client.sendMessage(rec, thread_id= 'TODO: GET userid VALUE FROM FACEBOOK PROFILE PAGE SOURCE')  
            elif sndr == 'Name21':
                client.sendMessage(rec, thread_id= 'TODO: GET userid VALUE FROM FACEBOOK PROFILE PAGE SOURCE')  
            elif sndr == 'Name22':
                client.sendMessage(rec, thread_id= 'TODO: GET userid VALUE FROM FACEBOOK PROFILE PAGE SOURCE')  
            elif sndr == 'Name23':
                client.sendMessage(rec, thread_id= 'TODO: GET userid VALUE FROM FACEBOOK PROFILE PAGE SOURCE')  
            elif sndr == 'Name24':
                client.sendMessage(rec, thread_id= 'TODO: GET userid VALUE FROM FACEBOOK PROFILE PAGE SOURCE')  
            elif sndr == 'Name25':
                client.sendMessage(rec, thread_id= 'TODO: GET userid VALUE FROM FACEBOOK PROFILE PAGE SOURCE')  
            elif sndr == 'Name26':
                client.sendMessage(rec, thread_id= 'TODO: GET userid VALUE FROM FACEBOOK PROFILE PAGE SOURCE')  
            elif sndr == 'Name27':
                client.sendMessage(rec, thread_id= 'TODO: GET userid VALUE FROM FACEBOOK PROFILE PAGE SOURCE')  
            time.sleep(5)                                
main()
