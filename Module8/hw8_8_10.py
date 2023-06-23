import collections
from collections import Counter
ips = [
    "85.157.172.253", "192.168.16.2",
    "10.10.10.1", "8.8.8.8",
    "85.157.172.253", "10.10.10.1",
    "10.10.10.1", "85.157.172.253",
    "192.168.16.55", "192.168.15.3"
    ]
ips_list = collections.namedtuple("ips", "counter")
def get_count_visits_from_ip(ips):
    ip_count = collections.Counter(ips)
    return ip_count

print(get_count_visits_from_ip(ips))

def get_frequent_visit_from_ip(ips):
    ip_count = collections.Counter(ips)
    ip_tuple=ip_count.most_common()
    #print(ip_count1.most_common())
    return ip_tuple

#ips_1=(get_count_visits_from_ip(ips))
print(get_frequent_visit_from_ip(ips))