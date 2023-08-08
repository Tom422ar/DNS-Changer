import subprocess

def configure_dns(dns1, dns2):
    try:
        # Setting the first DNS
        subprocess.run(['netsh', 'interface', 'ipv4', 'set', 'dns', 'name="Wi-Fi"', 'static', dns1, 'both'])

        # Setting the second DNS
        subprocess.run(['netsh', 'interface', 'ipv4', 'add', 'dns', 'name="Wi-Fi"', dns2, 'index=2'])

        print("Setting has been setted successfully.")
    except Exception as e:
        print("error while setting DNS", e)

def reset_dns():
    try:
        # Clearing Setted DNS
        subprocess.run(['netsh', 'interface', 'ipv4', 'delete', 'dns', 'name="Wi-Fi"', 'all'])

        print("The DNS Setting has been cleared.")
    except Exception as e:
        print("Error while Clearing DNS:", e)

if __name__ == "__main__":
    option = input("Please Make One of This Options\n\n\t1) Setting DNS\n\t2) Clearing DNS\n : ")

    if option == "1":
        dns1 = input(" Please Enter first DNS : ")
        dns2 = input(" Please Enter the Second DNS : ")
        configure_dns(dns1, dns2)
    elif option == "2":
        reset_dns()
    else:
        print("invalid choice.")
