import dns
import dns.resolver

my_resolver = dns.resolver.Resolver()

# 8.8.8.8 is Google's public DNS server
my_resolver.nameservers = ['20.150.142.142']

answer = my_resolver.query('google.com')

result = dns.resolver.resolve('.com', 'A')

for ipval in result:
  print('IP', ipval.to_text())
