import sys
import usb.core
import usb.util

#help(usb.core)
# Reading usb devices

dev = usb.core.find(find_all=True) 

sims = []

simVendorId = 0x19a2
simProductId = 0x5000

for cfg in dev:
    if cfg.idVendor == simVendorId and cfg.idProduct == simProductId:
        sims.append(cfg)

# If the sim100 is not found
if not sims:
    raise ValueError('SIM100 not found')

for sim in sims: 
   # print(usb.util.get_string(sim,256,1))
    file = open("WriteSDD.bat","a")
    file.write("..\\PackageLoaderUSB\\jre\\bin\\java -Djava.library.path=./dll/ -jar ..\\PackageLoaderUSB\\lib\\cltool.jar download")
    file.write(str(sim.idProduct) + "\n")
    file.write(str(sim.idVendor) + "\n")
    
    file.close()