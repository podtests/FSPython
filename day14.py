def findDivision(num1):
    try: # always
        #f1 = #read from file & get num1 value
        res = 100/num1
    except FileNotFoundError as e: # if error occurs
        print('Inside FileNotFoundError Handle block')
        print(f'Error info: {e}')
    except ZeroDivisionError  as e: 
        print('Inside ZeroDivisionError Handle block')
        print(f'Error info: {e}')
        num1 = 10
        res = 100/num1  
    except Exception as e:
        print('I was not abel to catch excption in any of the above block, so this would help me to catch those here!')
    else: #only runs if no error occured
        print('I am in else block')
    finally: # always
        print('Everything should be fine now!')    
      # handle the file      
    return res

def findOutput(num1):
    
    return findDivision(num1)

print(findOutput(4))

print("Hello to EveryOne!")