import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import tornado.options

import RPi.GPIO as GPIO
relay = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay, GPIO.OUT)
GPIO.output(relay, False)

class WSHandler(tornado.websocket.WebSocketHandler):

  def open(self):
    print 'user is connected.\n'

  def on_message(self, message):
        currentState = GPIO.input(relay)
        print "Message received: {}".format(self.request.remote_ip)
        if message == "on":
                if currentState == True:
                        self.write_message("Alarm is already armed")
                else:
                        GPIO.output(relay, True)
                        self.write_message("ON")
        elif message == "off":
                if currentState == False:
                        self.write_message("Alarm is already disarmed")
                else:
                        GPIO.output(relay, False)
                        self.write_message("OFF")

  def on_close(self):
    print 'connection closed\n'

  def check_origin(self,origin):
        return True

application = tornado.web.Application([(r'/ws', WSHandler),])

if __name__ == "__main__":
  http_server = tornado.httpserver.HTTPServer(application)
  http_server.listen(8888)
  tornado.ioloop.IOLoop.instance().start()