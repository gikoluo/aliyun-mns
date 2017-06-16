#!/usr/bin/env python
#coding=utf8
# Copyright (C) 2015, Alibaba Cloud Computing

#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import simple_http_notify_endpoint
import sys
import ssl

__version__ = "1.0.3"
class SimpleHttpsNotifyEndpoint(simple_http_notify_endpoint.SimpleHttpNotifyEndpoint):
    server_version = "SimpleHttpsNotifyEndpoint/" + __version__
    access_log_file = "access_log"

    RSA_PRIVATE_KEY = "\n-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQC7UKbXif9YkFQAghYs0CEZL066Sy2YbEKHdVm1OqmIHHY9CV9s\nFeCMD9HbbDwsBA2XQsVb7NP5MRydwTCpwCOBpntr0w94PuE+Q8TcLSHxgoqqI29s\nzF0xyRXjAJFabzu2sei8RySLw57C64lWIOxPrWsi+GHQK0XcFU7JfFACIQIDAQAB\nAoGBAKtDfZia2vYN2FAyoLXOgkS1pWTdsc2oRlf16tSx0ynY5B7AgBeiFRHasQTP\nfGC+P/LqIOsAqXsw9Toj1iuOuqaSBYpuCHFMe/dxrEAPXXA7GCMwW3lDeSfMinHV\nrjLTDMhZRLN+jT5QvlkOBNibaZSc3bmCwmGbkEeREkDGD+fFAkEA6A/pQQfT25ip\nAKHh2VOIzfOpiBfC0sci6ZF845kh5GxyFUAeq+hjUUx+ihzI7eIqKrkY+41eYz73\nSGhwuBkmhwJBAM6jGWNv0PgxcLs+sGa55BL53KuiVjIONxOhKrk3OfoF+i8jY7c7\ngUE3kgckcx7FZY323kjGSwX626+jvyRdFBcCQDv9kQEcsun75wSg1K/H5n/HU7Y4\n3kZ68E2NLMnxlk9ksYFI2CT8qGAl9DhkBJVqeBgfTZQKEbJ6Xpa7WRheeBUCQQDE\nS5oFpSYdcFIH/lBy9aodALFJdqhtWqWlhxff5P+1bNIyz2qdmPB7tL+K+2xE0f5c\nMyUMexqv7pOdMW+Vqro3AkAVx3pYn7e1YqMM40jI0J+CqyhXYZ2esiWvBylS+FUN\nY6WOonIAv774LIURaTplcAMuOAj6VDHpVmSDVvnVMgEu\n-----END RSA PRIVATE KEY-----"
    CERTIFICATE = "\n-----BEGIN CERTIFICATE-----\nMIIDbDCCAtWgAwIBAgIJALKoPicL21iaMA0GCSqGSIb3DQEBBQUAMIGBMQswCQYD\nVQQGEwJDTjERMA8GA1UECBMIWmhlamlhbmcxETAPBgNVBAcTCEhhbmd6aG91MQ8w\nDQYDVQQKDAZBbGluCAgxEzARBgNVBAsTCkFwc2FyYSBPU1MxDDAKBgNVBAMTA09T\nUzEYMBYGCSqGSIb3DQEJARYJYWxleC5rcQgIMB4XDTE0MDgyMDA4MjM1NVoXDTE1\nMDgyMDA4MjM1NVowgYExCzAJBgNVBAYTAkNOMREwDwYDVQQIEwhaaGVqaWFuZzER\nMA8GA1UEBxMISGFuZ3pob3UxDzANBgNVBAoMBkFsaW4ICDETMBEGA1UECxMKQXBz\nYXJhIE9TUzEMMAoGA1UEAxMDT1NTMRgwFgYJKoZIhvcNAQkBFglhbGV4LmtxCAgw\ngZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBALtQpteJ/1iQVACCFizQIRkvTrpL\nLZhsQod1WbU6qYgcdj0JX2wV4IwP0dtsPCwEDZdCxVvs0/kxHJ3BMKnAI4Gme2vT\nD3g+4T5DxNwtIfGCiqojb2zMXTHJFeMAkVpvO7ax6LxHJIvDnsLriVYg7E+tayL4\nYdArRdwVTsl8UAIhAgMBAAGjgekwgeYwHQYDVR0OBBYEFMuRh/onWCJ+geGxBp6Y\nMEugx/0HMIG2BgNVHSMEga4wgauAFMuRh/onWCJ+geGxBp6YMEugx/0HoYGHpIGE\nMIGBMQswCQYDVQQGEwJDTjERMA8GA1UECBMIWmhlamlhbmcxETAPBgNVBAcTCEhh\nbmd6aG91MQ8wDQYDVQQKDAZBbGluCAgxEzARBgNVBAsTCkFwc2FyYSBPU1MxDDAK\nBgNVBAMTA09TUzEYMBYGCSqGSIb3DQEJARYJYWxleC5rcQgIggkAsqg+JwvbWJow\nDAYDVR0TBAUwAwEB/zANBgkqhkiG9w0BAQUFAAOBgQA/8bbaN0Zwb44belQ+OaWj\n7xgn1Bp7AbkDnybpCB1xZGE5sDSkoy+5lNW3D/G5cEQkMYc8g18JtEOy0PPMKHvN\nmqxXUOCSGTmiqOxSY0kZwHG5sMv6Tf0KOmBZte3Ob2h/+pzNMHOBTFFd0xExKGlr\nGr788nh1/5YblcBHl3VEBA==\n-----END CERTIFICATE-----"

    def setup(self):
        tmpkeyfile = "rsa_private_key_checkhttp.pem"
        tmpcertfile = "x509_public_certificate_checkhttp.pem"
        open(tmpkeyfile, 'w').write(self.RSA_PRIVATE_KEY)
        open(tmpcertfile, 'w').write(self.CERTIFICATE)
        SSLSocket = ssl.wrap_socket(self.request,server_side=True, keyfile=tmpkeyfile, certfile=tmpcertfile,ssl_version=ssl.PROTOCOL_SSLv23)
        self.rfile = SSLSocket.makefile('rb', self.rbufsize)
        self.wfile = SSLSocket.makefile('wb', self.wbufsize)

if __name__ == "__main__":
    port = int(sys.argv[1]) if sys.argv[1:] else 8081
    msg_type = sys.argv[2] if sys.argv[2:] else "XML"
    simple_http_notify_endpoint.main(port, SimpleHttpsNotifyEndpoint, msg_type, "https://")
