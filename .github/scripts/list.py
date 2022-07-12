import os
import sys
import utilities
import json

list = os.getenv('LIST')
list = list.strip('][').split(',')
specfiles = []
for file in list:
  if(file.split('/')[-1]=="spec.json"):
    specfiles.append(file)
print(specfiles)
if(len(specfiles)==0):
  sys.exit(0)
utilities.run_shell_command('ls')
os.chdir('./packager/')
utilities.run_shell_command('mvn clean package')
os.chdir('../')
utilities.run_shell_command('java -cp "packager/target/lib/*:packager/target/*" io.cdap.hub.Tool build')
utilities.run_shell_command('ls')
f = open("./packages.json", "r")
l = json.loads(f.read())
print(l)