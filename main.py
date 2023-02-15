import os

answer = input("Are you on arch linux right now? [y/N] ")
if answer.lower() != "y":
    answer = ""
    print("You have to install arch linux in order to use this script!")
    exit(1)

answer = input("Good! do you have yay installed? [y/N] ")
if answer.lower() != "y":
    answer = ""
    print("Please install yay to continue!")
    exit(1)

print("Starting installation proccess")
os.system("yay -S vmware-workstation --noconfirm")
os.system("sudo systemctl enable --now vmware-networks-configuration.service && sudo systemctl enable --now vmware-usbarbitrator.service && sudo systemctl enable --now vmware-networks-server.service")
print("VMware workstation installed successfully!")
print("Installing license key")
os.system("sudo /usr/lib/vmware/bin/vmware-vmx-debug --new-sn MC60H-DWHD5-H80U9-6V85M-8280D")
print("License key install successfully!")

print("\nVMware installation completed!")