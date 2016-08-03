#!/usr/bin/env ruby

require 'webrick'

port = ENV['PORT'] || 4000

server = WEBrick::HTTPServer.new(Port: port, DocumentRoot: Dir.pwd)

Signal.trap('SIGINT') { server.shutdown }
server.start
