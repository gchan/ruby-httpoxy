#!/usr/bin/env ruby

require 'webrick'

server = WEBrick::HTTPServer.new(Port: 4000, DocumentRoot: Dir.pwd)

Signal.trap('SIGINT') { server.shutdown }
server.start
