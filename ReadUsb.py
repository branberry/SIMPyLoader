import sys
import usb.core

# Reading usb devices
dev = usb.core.find(find_all=True)
Sims = []
# Loop through eafch device and print trhe product ids in both hex and decimal
for cfg in dev:
    if cfg.idVendor == 6562 and cfg.idProduct == 20480:
        Sims.append(cfg)

for sim in Sims:
    #print(sim)
    file = open("WriteSDD.bat","a")

    file.write(str(sim.idProduct) + "\n")
    file.write(str(sim.idVendor) + "\n")
    
    file.close()