import subprocess                  # Python'dan kali linux kodları çalıştırma kütüphanesi
import optparse as opt             # to give input to the program
import re                          # Regex Library
import random                      # For random numbers
from termcolor import colored      # For string color
from time import sleep             # wait..

 


def control_interface(interface,module):
    
    if interface == "eth0":
        ifc = subprocess.check_output(["ifconfig"])
        ifc_regex = re.search(r"eth0",str(ifc))
        
        
        if str(interface) == ifc_regex.group(0):
             print(f"Interface: {interface} -->", colored("OK","green"))
        
        if module == "random":
            random_mac(interface)
        elif module == "manuel":
            manuel_mac(interface)
        else:
            print("invalid Module")


    elif interface == "wlan0":
        ifc = subprocess.check_output(["ifconfig"])
        ifc_regex = re.search(r"wlan0",str(ifc))
        
        
        if str(interface) == ifc_regex.group(0):
            print(f"Interface: {interface} -->", colored("OK","green"))
        
        if module == "random":
            random_mac(interface)
        elif module == "manuel":
            manuel_mac(interface)
        else:
            print("invalid Module")
		
    else:
        print("Invaild interface")




def random_mac(interface):

    a = random.randint(00,99)
    b = random.randint(00,99)
    c = random.randint(00,99)
    d = random.randint(00,99)
    e = random.randint(00,99)
    f = random.randint(00,99)
    
    adress =  f"{a}:{b}:{c}:{d}:{e}:{f}"
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",adress])
    control_mac(interface,adress)



def manuel_mac(interface):
  
    print(colored("Please use valid area codes","red"))
    address = str(input("mac: "))

    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether", address])
    control_mac(interface,address)


def control_mac(interface,a):
   
   ifconfig = subprocess.check_output(["ifconfig",interface])
   new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))                        # (Regex format,Varriable to apply)
   

   if new_mac.group(0) == a:
       subprocess.call(["ifconfig",interface,"up"])
       print("Mac address:", new_mac.group(0), "--> ",colored("OK","green"))                  # string expression to get result
       
   
   else:
       print(colored("Mac address not accepted. Automatically assigning mac address", "blue"))
       random_mac(interface)


        
print(colored(">>>>","red") + " Sarp Cahnger Started " + colored("<<<<","red"))
sleep(0.5)
print(colored(">>>>","red") + " By Hacker Sarp " + colored("<<<<","red") + "\n" + colored(">>>>","red") + " https://github.com/4sarp " + colored("<<<<","red") + "\n\n\n")
sleep(0.7)

                                                                         # We create the parser.
                                                                         # We add our options with the parser
                                                                         # Finally, we tell where to assign the given value using the option.
                                                                         # dest = Destination 
                
parse_object = opt.OptionParser()                                                           
parse_object.add_option("-m","--module", dest = "module", help = " Selected of |random| or |manuel|")                            
parse_object.add_option("-i","--interface",dest = "interface", help = " Choose network connection line")                           
 
(user_inputs, arguments) = parse_object.parse_args()
control_interface(user_inputs.interface,user_inputs.module)




