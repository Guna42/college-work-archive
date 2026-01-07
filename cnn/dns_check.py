import dns.resolver
for s in dns.resolver.Resolver().nameservers:
    print("DNS Server:", s)
