#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
form="""
<head><title>test date alert</title>

<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
<style type="text/css">
body {background-color:#b0c4de;}
</style>
<META HTTP-EQUIV="content-type" CONTENT="text/html; charset=utf-8">
</head>
<body>
<div id="link" style="background-color:grey;height:500px;width:100px;float:left;color: orange;">
<b>Links</b><br />

<a href="mail.dhs.sg">dhs mail</a><br />
<a href="https://appengine.google.com/">google app engine</a></br>
<a href="http://www.dhs.sg/">DHS official website</a><br />
</div>

<center><img style="width: 200px; height: 200px; margin-top: 5px;" alt="dhs logo" src="/logo.jpg"></center>
<center><p style="color: red;"><b>DHS test date alert</b></p></center>
<center><form method="post">
	enter your name:<input type="text" name="name"><i>eg:liu.fengyuan</i>
	<br>
	<input type="submit"/>
</form></center>
<center><p style="color: green;">TODAY IS!!!</p><b><script language="javascript"> var date = new Date(); var day = date.getDay(); var month = date.getMonth(); var year = date.getYear(); if (year < 1000) { year =year+1900; } 
document.write(day + '/' + month + '/' + year); </script></b></center>
</div>
</body>
<div id="footer" style="background-color:black;clear:both;text-align:center;">
<b style="color: white;">&copy feng yuan</b>
</div>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form)


    def post(self):
        name=self.request.get('name')
        if name:
            self.response.out.write('hello '+name)
        else:
            self.response.out.write('enter your name please')
                                
        

app = webapp2.WSGIApplication([('/', MainHandler),],
                              debug=True)
