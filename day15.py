
from dotenv import load_dotenv
import os
import sys
# list down all the environment variables
#print(os.environ) # output is of dictionary like object

# Get specific env variable
#print(os.environ["PATH"])
#print(os.getenv("PATH"))

#os.environ["PodTestKey"] = "hjgfakjfhqkjr23467gfafg3748fyhje" 
#print(os.environ["PodtestKey"])

envType =  sys.argv[1]  #   envtype
envfilepath = ".env."+str(envType)

print(envfilepath)
load_dotenv(envfilepath) # .env
print(os.environ["PodtestKey"])




