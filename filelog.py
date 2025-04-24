import re

#Opens and reads the log file
with open('access.log', 'r') as file:
  log_lines = file.readlines()
  print(f"Total lines read: {len(log_lines)}")
  
  #Filters out BotPoke
  filtered_logs = [line for line in log_lines if '"BotPoke"' not in line]
  
#Make sure all instances of BotPoke is removed.
print(f"Number of remaining log entries: {len(filtered_logs)}")

ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'

#Extract all IP addresses from filtered logs
all_ips = re.findall(ip_pattern, '\n'.join(filtered_logs))

#Get unique IP addresses
unique_ips = set(all_ips)

print(f"Unique IP Addresses ({len(unique_ips)} found):")
#Outputs the unique ip's in a column
for i, ip in enumerate(sorted(unique_ips), 1):
    print(f"{ip:<15}", end="  ")
    #Start a new line every 5 ip's
    if i % 5 == 0: 
        print()



