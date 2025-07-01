import dns.resolver
import dns.query
import dns.zone

def dns_enum(domain):
    try:
        # Query NS records
        answers = dns.resolver.resolve(domain, 'NS')
        ns_servers = [r.to_text() for r in answers]
        print(f"Name Servers for {domain}: {ns_servers}")

        # Attempt zone transfer on each NS server
        for ns in ns_servers:
            ns = ns.rstrip('.')
            print(f"Attempting zone transfer on {ns}...")
            try:
                zone = dns.zone.from_xfr(dns.query.xfr(ns, domain))
                names = zone.nodes.keys()
                print(f"Zone transfer successful! Records:")
                for n in names:
                    print(n.to_text())
            except Exception:
                print(f"Zone transfer failed on {ns}.")
    except Exception as e:
        print(f"DNS enumeration error: {e}")
