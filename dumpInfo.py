

def dumpInfo(flow):
   # do something
   dict = flow.__dict__
   print "[Flow Info]"
   print "Host:" + dict["Host"]
   print "method:" + dict["method"]
   print "protocol:" + dict["protocol"]
   print "[Request Info]"
   print "request start time:" + dict["requestStartTime"]
   print "request end time:" + dict["requestEndTime"]
   print "request body:" + dict["requestBody"]
   headers = dict["requestHeaders"]
   for k in headers.keys():
      print "request header: " + k + " = " + headers[k][0]
   print "[Response Info]"
   print "response code:",dict["responseCode"]
   print "response start time:" + dict["responseStartTime"]
   print "response end time:" + dict["responseEndTime"]
   print "response body:" + dict["responseBody"]
   headers = dict["responseHeaders"]
   for k in headers.keys():
      print "response header: " + k + " = " + headers[k][0]

def request(context, flow):
   # do nothing
   dict = flow.__dict__
   request = flow.request
   dict["Host"] = str(request.host)
   dict["method"] = str(request.method)
   dict["protocolVersion"] = str(request.httpversion)
   dict["protocol"] = str(request.scheme)
   dict["requestStartTime"] = str(request.timestamp_start)
   dict["requestEndTime"] = str(request.timestamp_end)
   dict["requestHeaders"] = request.headers
   dict["requestBody"] = request.get_decoded_content()

def response(context, flow):
   dict = flow.__dict__
   response = flow.response
   dict["responseCode"] = response.code
   dict["responseStartTime"] = str(response.timestamp_start)
   dict["responseEndTime"] = str(response.timestamp_end)
   dict["responseHeaders"] = response.headers
   dict["responseBody"] = response.get_decoded_content()
 
   dumpInfo(flow)
