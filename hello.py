
import dns.resolver
import time

def check_dns_records(domain):
    record_types = ['A', 'CNAME', 'MX', 'TXT']
    results = {}

    for record_type in record_types:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            results[record_type] = [answer.to_text() for answer in answers]
        except dns.resolver.NoAnswer:
            results[record_type] = []
        except dns.resolver.NXDOMAIN:
            results[record_type] = 'Domain does not exist'
        except Exception as e:
            results[record_type] = f'Error: {e}'

    return results

def main():
    domain = input("Enter the domain name to check: ")
    print(f"Checking DNS records for {domain}...")
    
    while True:
        results = check_dns_records(domain)
        print(f"DNS records for {domain}:")
        for record_type, records in results.items():
            print(f"{record_type} records: {records}")
        
        print("Sleeping for 30 minutes before next check...")
        time.sleep(1800)  # Wait for 30 minutes before the next check

if __name__ == "__main__":
    main()
