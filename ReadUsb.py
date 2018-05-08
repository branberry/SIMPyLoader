import sys
import usb.core
import usb.util
import os
from subprocess import Popen

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

    # making sure that we get an actual serial number for the device
    if serialNum is not None:
        # Creating the individual batch files
        file = open(batchPath + serialNum + ".bat","w")

        ################################################################
        #    This is the batch file's information for each sim         #  
        ################################################################
        file.write("..\\PackageLoaderUSB\\jre\\bin\\java -Djava.library.path=./dll/ -jar ..\\PackageLoaderUSB\\lib\\cltool.jar download ")
        file.write("\"-if=SICK SERVICE:DIV05_SERVICE@USB?COLA2\" ")  
        file.write("\"-usbpath=\\\\?//\\usb#vid_19a2&pid_5000#" + serialNum + "#{40f8d7c6-6856-483d-ac31-dc646ca2d89b}\"")
        file.write(" -descriptions=SDD/sim100.sdd -file=SDD_Manifest\\SIM100manifestsdd.spk")
        file.close()

# looping through the batch file directory
for batchFile in os.listdir(batchPath):
    # Creating the string for the path of the batch file
    path = os.getcwd() + "\\batchfiles\\" + batchFile

    # Opening the batch file and displaying that information to the console
    p = Popen(path)
