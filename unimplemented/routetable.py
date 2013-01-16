import re

#from pysnmp.entity.rfc3413.oneliner import cmdgen

#s = r'(%s)' % ('(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.)\
#{3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)') 
#pattern = re.compile(s)
#file = 'routers.txt'
#s = open(file).read()
#i = 0
router_list = []
while True:
    match = pattern.search(s, i)
    if match:
        router_list.append(match.group(1))
        i = match.end() + 1
    else:
        break

class router:
    def __init__(self, who):
        self.name = who

    routetable = {}

router1 = router(router_list[0])

cmdGen = cmdgen.CommandGenerator()
errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.nextCmd(
    cmdgen.CommunityData('test-agent', public, 0),
    cmdgen.UdpTransportTarget((router1.name, 161)),
    (1,3,6,1,2,1,4,21,1,1))

if errorIndication:
        print errorIndication
else:
    if errorStatus:
            print '%s at %s\n' % (errorStatus.prettyPrint(),varBindTable[-1][int(errorIndex)-1])
    else:
        for varBindTableRow in varBindTable:
            for oid, val in varBindTableRow:
                 print varBindTableRow

RouteTable = {
    "ipRouteDest":      (1, 3, 6, 1, 2, 1, 4, 21, 1, 1),
    "ipRouteIfIndex":   (1, 3, 6, 1, 2, 1, 4, 21, 1, 2),
    "ipRouteNextHop":   (1, 3, 6, 1, 2, 1, 4, 21, 1, 7),
    "ipRouteType":      (1, 3, 6, 1, 2, 1, 4, 21, 1, 8),
    "ipRouteMask":      (1, 3, 6, 1, 2, 1, 4, 21, 1, 11),
}

def hex2dec(mack):
    return int(mack, 16)

def convertIp(hexip):
    ip = map(hex, map(ord, hexip))
    ip = map(hex2dec, ip)
    ip = re.sub("\,", ".",re.sub("\'|\[|\]|\s","", str(ip)))
    return ip

def walk(host, community, oid):
    cmdGen = cmdgen.CommandGenerator()
    errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.nextCmd(
        cmdgen.CommunityData('test-agent', community, 0),
        cmdgen.UdpTransportTarget((host, 161)), oid)

    if errorIndication:
        print errorIndication
    else:
        if errorStatus:
            print '%s at %s\n' % (errorStatus.prettyPrint(),varBindTable[-1][int(errorIndex)-1])
        else:
            val = []
            for varBindTableRow in varBindTable:
                for oid in varBindTableRow:                               
                    try:
                        val.append(convertIp(varBindTableRow[0][1]))
                    except:
                        val.append(str(varBindTableRow[0][1]))
    return val
ipRouteDest = walk(router1.name, community, RouteTable["ipRouteDest"])
ipRouteIfIndex = walk(router1.name, community, RouteTable["ipRouteIfIndex"])
ipRouteNextHop = walk(router1.name, community, RouteTable["ipRouteNextHop"])
ipRouteType = walk(router1.name, community, RouteTable["ipRouteType"])
ipRouteMask = walk(router1.name, community, RouteTable["ipRouteMask"])

table = zip(ipRouteIfIndex, ipRouteNextHop, ipRouteType, ipRouteMask)
routetable = dict(zip(ipRouteDest, table))
    
print routetable
