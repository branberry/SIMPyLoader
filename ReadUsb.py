import sys
import usb.core
import usb.util
import os


# Reading usb devices
dev = usb.core.find(find_all=True) 

# list that holds the sim device objects
sims = []

simVendorId = 0x19a2
simProductId = 0x5000

for cfg in dev:
    if cfg.idVendor == simVendorId and cfg.idProduct == simProductId:
        sims.append(cfg)

# If the sim100 is not found
if not sims:
    raise ValueError('SIM100 not found')

# creates a directory to hold sim batch files if it does not already exist
batchPath = "batchfiles/"
if not os.path.exists(batchPath):
    os.makedirs(batchPath)
# create batch files for sim100
for sim in sims: 
    # Retrieve the string representation of the sim100
    serialNum = usb.util.get_string(sim,sim.iSerialNumber)
   # print(usb.util.get_string(sim,256,1))
    file = open(batchPath + serialNum + ".bat","w")
    file.write("..\\PackageLoaderUSB\\jre\\bin\\java -Djava.library.path=./dll/ -jar ..\\PackageLoaderUSB\\lib\\cltool.jar download ")
    file.write("\"-if=SICK SERVICE:DIV05_SERVICE@USB?COLA2\"")

    
    file.close()