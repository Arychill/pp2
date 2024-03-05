import json

with open('/Users/argynmoldabek/Desktop/pp2/lab4/sample-data.json', 'r') as file:
    data = json.load(file)

interfaces = data.get('imdata', [])

print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for interface in interfaces:
    attributes = interface.get('l1PhysIf', {}).get('attributes', {})
    dn = attributes.get('dn', '')
    description = attributes.get('descr', '')
    speed = attributes.get('speed', 'inherit')
    mtu = attributes.get('mtu', '')

    
    print("{:<50} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))
