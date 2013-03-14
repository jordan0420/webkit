import os
import mimetypes
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from cStringIO import StringIO

# recommended string building tech. from
# http://www.skymind.com/~ocrow/python_string/
#wrapped in a string builder class
class StringBuilder:
    def __init__(self):
        self.collection = StringIO()
    def append(self, string):
        self.collection.write(string)
    def toString(self):
        return self.collection.getvalue()

class DirectoryResolver:
    def __init__(self, path):
        self.path = path

    def convertpath_sep(self):
        x = str(self.path)
        x = x.replace("/","\\")
        if x.startswith("\\"):
            x = x.replace("\\","",1)
        return x
    def vdir_root(self):
        arg = self.convertpath_sep()
        if str(arg).find("\\") == -1:
            return str("")
        lst = str(arg).split("\\")
        if len(lst) == 0:
            return str("")
        result = lst[0]
        result = str(result)
        if result.find(".") != -1:
            return str("")
        return result
    
class VDirInfo:
    def __init__(self, vdir, localpath):
        self.vdir = vdir
        self.localpath = localpath

class VDirList:
    def __init__(self):
        self.list = []

    def add(self, vdir, localpath):
        x = VDirInfo(vdir,localpath)
        self.list.append(x)

    def count(self):
        return len(self.list)

    def get_path(self, requestPath):
        resolve = DirectoryResolver(requestPath)
        root = resolve.vdir_root()
        if root == str(""):
            return None
        for item in self.list:
            if item.vdir == root:
                x = str(resolve.convertpath_sep()).replace(root, item.localpath,1)
                return x;
        return None

class ResourceLocator:
    def __init__(self):
        self.vdir_list = VDirList()
    def get_local_path(self, requestedpath):
        return self.vdir_list.get_path(requestedpath)

class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        locator = ResourceLocator()
        locator.vdir_list.add("test","c:\\\\deploy\\")
        pth = locator.get_local_path(self.path)
        if os.path.exists(pth):
            self.send_response(200)
            
            self.send_header('Server','cx1193719-b')
            self.send_header('Content-type',    mimetypes.guess_type(pth))
            self.send_header('Accept-Ranges','bytes')
            self.end_headers()
            byte = 1
            builder = StringBuilder()
            f = open(pth,'rb')
            print f
            while byte != str(""):
                byte = f.read(1)
                if (byte != str("")):
                    builder.append(byte)
            self.wfile.write(builder.toString())
            f.close()
            print "done"
            return
        self.send_response(404)
        self.send_header('Server','cx1193719-b')
        self.send_header('Content-type',    'text/html')
        self.end_headers()
        print "file not found"
        self.wfile.write("File not found")
        
        
def main():
    try:
        server = HTTPServer(('', 8081), HttpHandler)
        print 'starting server'
        server.serve_forever()
    except KeyboardInterrupt:
        print 'shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()
