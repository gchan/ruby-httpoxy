#!/usr/bin/env ruby

keys = ENV.keys.join("\n")

require 'cgi'
require 'uri'

cgi = CGI.new

out = ""
out << "Enivornment Variables:\n"
out << keys + "\n\n"

out << "HTTP_PROXY env:\n"
out << "ENV['HTTP_PROXY']  > #{ENV["HTTP_PROXY"]}\n\n"

out << "net/http proxy check:\n"
out << "#{URI("http://www.google.com").find_proxy || "NONE!"}\n\n"

out << "`./go-proxy-check` (system command):\n#{`./go-proxy-check`}\n"

puts cgi.header
puts out
