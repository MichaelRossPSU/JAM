import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import tornado.options

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, False)

class WSHandler(tornado.websocket.WebSocketHandler):

  def open(self):
    print 'user is connected.\n'

  def on_message(self, message):
        currentState = GPIO.input(11)
        print "Message received: {}".format(self.request.remote_ip)
        if message == "ledon":
                if currentState == True:
                        self.write_message("LED is already on!")
                else:
                        GPIO.output(11, True)
                        self.write_message("ON")
        elif message == "ledoff":
                if currentState == False:
                        self.write_message("LED already off!")
                else:
                        GPIO.output(11, False)
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