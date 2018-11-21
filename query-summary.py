#!/usr/bin/env python
#query-summary.py
#Author:K0walski

import shodan
import sys

API_KEY = 'YOUR_API'

FACETS = [
    'org',
    'domain',
    'port',
    'asn',
    ('country',10),
]

FACETS_TITLES ={
    'org': 'Top 5 Organizations',
    'domain': 'Top 5 Domains',
    'port': 'Top 5 Ports',
    'asn': 'Top 5 Autonomous Sysyems',
    'country': 'Top 10 Countries',
}

#Input validation
if len(sys.argv) == 1:
    print 'Usage: %s <search query>' % sys.argv[0]
    sys.exit(1)

try:
    api = shodan.Shodan(API_KEY)
    #Setup the api
    query =' '.join(sys.argv[1:])

    result = api.count(query,facets=FACETS)

    print 'Shodan Summary Information'
    print 'Query: %s' % query
    print 'Total Results: %s\n' % result['total']

    #Print the summary info from the facets
    for facet in result['facets']:
        print FACETS_TITLES[facet]

        for term in result['facets'][facet]:
            print '%s: %s' % (term['value'],term['count'])

    #Print an empty line between summary info
    print ''

except Exception,e:
    print 'Error: %s' % e
    sys.exit(1)

'''
Sample Output

============================
./query-summary.py waf

Shodan Summary Information
Query: waf
Total Results: 128104

Top 5 Organizations
Enzu: 8379
DXTL Tseung Kwan O Service: 7995
Psychz Networks: 7082
Peg Tech: 5642
EGIHosting: 4769
Top 5 Domains
scalabledns.com: 6722
psychz.net: 2105
ceranetworks.com: 981
multacom.com: 729
amazonaws.com: 666
Top 10 Countries
US: 68496
CN: 30017
HK: 18902
ZA: 5597
RU: 488
KR: 455
DE: 304
SG: 291
AT: 138
TR: 94
Top 5 Ports
80: 106611
443: 8892
8080: 4182
8443: 2019
8081: 682
Top 5 Autonomous Sysyems
as35916: 8981
as18978: 8379
as40676: 8210
as15003: 8099
as134833: 4103

'''
