import dns
import dns.resolver
import time

my_resolver = dns.resolver.Resolver()

# 8.8.8.8 is Google's public DNS server
my_resolver.nameservers = ['20.150.142.142']

answer = my_resolver.query('google.com')

result = dns.resolver.resolve('.com', 'A')

for ipval in result:
  print('IP', ipval.to_text())

t_end = time.time() + 60 * 15
while time.time() < t_end:

    #Do the function but I still need to do it.