banner = '''
                                                                                                                                                                                          
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣾⣿⠟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣧⡈⠛⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⡿⠛⢁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⡿⠟⢁⣤⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⠟⢉⣠⠶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣴⣶⣿⠖⢀⣠⠾⣿⣿⠿⠋⣠⡴⠛⠁⠴⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠙⠋⣠⡴⠛⢁⡴⠞⠁⠀⠚⠉⠀⠀⠀⢰⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣤⠈⢁⣤⠞⢋⣤⡄⠀⠀⠀⠀⠀⠀⢠⣬⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠷⠀⠠⣾⣿⡿⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⠋⠀⠀⠀⠀⠀⠀⢀⡆⢸⣿⣿⠀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣉⣁⡀⠀⠀⠀⠀⠀⠀⣀⣉⣀⣀⣀⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠁⠀⠀⠀
---------------------------------------------
                D0nk3y M1ssil3
         "Push botton to fire donkeys"
'''
print(banner)

import subprocess

# Ask the user whether they are using the local or remote system
system_choice = input("Are you using the local system or the remote system? (local/remote): ")

if system_choice.lower() == "local":
    # Gather information for airodump-ng on the local system
    file_name = input("Enter the file name: ")
    interface = input("Enter the wireless interface: ")
    mac_address = input("Enter the target network MAC address: ")
    channel = input("Enter the channel number: ")

    # Construct the airodump-ng command for local execution
    airodump_cmd = f"airodump-ng --bssid {mac_address} --channel {channel} -w {file_name} {interface}"

    try:
        # Execute the command locally
        subprocess.run(airodump_cmd, shell=True, check=True)
    except subprocess.CalledProcessError:
        print("An error occurred while executing the command.")
elif system_choice.lower() == "remote":
    # Gather information for remote system (Pi)
    pi_ip = input("Enter the Pi's IP address: ")
    username = input("Enter the SSH username: ")
    password = input("Enter the SSH password: ")
    pi_interface = input("Enter the wireless interface on the Pi: ")
    pi_mac_address = input("Enter the target network MAC address: ")
    pi_channel = input("Enter the channel number: ")
    file_name = input("Enter the file name: ")

    # Construct the airodump-ng command for remote execution
    airodump_cmd = f"airodump-ng --bssid {pi_mac_address} --channel {pi_channel} -w {file_name} {pi_interface}"

    try:
        # Use SSH to connect to the remote system (Pi) and execute the command
        ssh_command = f"ssh {username}@{pi_ip} '{airodump_cmd}'"
        subprocess.run(ssh_command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print("An error occurred while executing the command on the remote system.")
else:
    print("Invalid choice. Please select 'local' or 'remote'.")

