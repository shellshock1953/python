""" proxy checker """
import urllib2
import socket

host_to_connected = 'http://uar.net'
hosts = []
hosts_file = open('proxy.hosts').readlines()

available_hosts = []

for host in hosts_file:
    try:
        host = host.rstrip()
        print("[\t%s\t]: Trying...") % host
        proxy_handler = urllib2.ProxyHandler({'http': host})
        opener = urllib2.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib2.install_opener(opener)
        req = urllib2.Request(host_to_connected)  # change the url address here
        sock = urllib2.urlopen(req, timeout=4)
        print("[\t%s\t]: Connected to %s") % (host, host_to_connected)
        print("[\t%s\t]: Second try") % host
        sock = urllib2.urlopen(req, timeout=4)
        print("[\t%s\t]: SUCCSESS!\n") % host
        available_hosts.append(host)
    except urllib2.URLError:
        print("[\t%s\t]: Unable to connect. Passing...\n") % host
    except socket.timeout, urllib2.HTTPError:
        print('[\t%s\t]: Time out\n') % host
print("\nList of available hosts:")
print available_hosts
