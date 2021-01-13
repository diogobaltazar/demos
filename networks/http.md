HTTP := Hypertext transfer protocol between two agents: the *client* and the *server*.   
The agents communicate through *requests*. The format for the requests is well-defined by the HTTP.

HTTP format [src-1](https://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html) [src-2](https://www.tutorialspoint.com/http/http_requests.htm)
+ ``request-line`` := ``<method.resource><SP><uri.resource><SP><version.http><CRLF>``
+ [`header`]
+ ``<CRLF>``
+ [`<body.message>`]

``<method.resource>`` is in [`GET`,`HEAD`,`POST`,`PUT`,`DELETE`,`TRACE`,`CONNECT`]
|``<method.resource>``||example|
|---|---|---|
|`GET`|retrieve data|GET http://www.w3.org/pub/WWW/TheProject.html HTTP/1.1|
|`HEAD`|transfers the status line and the header section only||
|[`POST`]|send data through the message body rather than through parameters in the query string||
|[`PUT`]|replace all the current representations of the target resource with the uploaded content. Idempotent operation. Send data through the message body rather than through parameters in the query string||
|[`PATCH`]|Replace some of the current representations of the target resource with the uploaded content. Non-idempotent operation. Send data through the message body rather than through parameters in the query string. ||
|[`DELETE`]|remove current representations of the target resource||
|[`CONNECT`]|establishes a tunnel to the server||
|[`OPTIONS`]|communication options for the target resource||
|[`TRACE`]|message loop back test ||

GET
    GET /hello.htm HTTP/1.1
    User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)
    Host: www.tutorialspoint.com
    Accept-Language: en-us
    Accept-Encoding: gzip, deflate
    Connection: Keep-Alive

POST
    POST /cgi-bin/process.cgi HTTP/1.1
    User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)
    Host: www.tutorialspoint.com
    Content-Type: application/x-www-form-urlencoded
    Content-Length: length
    Accept-Language: en-us
    Accept-Encoding: gzip, deflate
    Connection: Keep-Alive

    licenseID=string&content=string&/paramsXML=string

POST

    POST /cgi-bin/process.cgi HTTP/1.1
    User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)
    Host: www.tutorialspoint.com
    Content-Type: text/xml; charset=utf-8
    Content-Length: length
    Accept-Language: en-us
    Accept-Encoding: gzip, deflate
    Connection: Keep-Alive

    <?xml version="1.0" encoding="utf-8"?>
    <string xmlns="http://clearforest.com/">string</string>

# PYTHON
[see](https://2.python-requests.org/en/v1.0.0/api/)