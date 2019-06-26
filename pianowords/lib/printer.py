from escpos.printer import Usb
#from pythonosc import dispatcher
#from pythonosc import osc_server



virtual = True
virtual = False

if virtual:
    class p():
        def text(t):
            print(t)
else:
#	p = Usb(0x04b8, 0x0202, 0)
    p = Usb(0x067b, 0x2305, 0)
        #profile="TM-T88III")


#disp = dispatcher.Dispatcher()
#def print_volume_handler(unused_addr, args, volume):
#          print("[{0}] ~ {1}".format(args[0], volume))
#          print(unused_addr)
#          print(args)
#          print(volume)
#          print("----------------")


#def oscserver():

	#disp.map("/filter", print)
#	disp.map("/volume", print_volume_handler, "Volume")
	# dispatcher.map("/logvolume", print_compute_handler, "Log volume", math.log)
#	server = osc_server.ThreadingOSCUDPServer(("127.0.0.1", 1337), disp)
#	print("Serving on {}".format(server.server_address))
#	server.serve_forever()

#oscserver()


p.text("Hello World\n")

from escpos import *

#import escpos


StarLC20 = printer.File("/dev/usb/lp0")
# Print text
StarLC20.text("Hello World\n")
# Print image
#Epson.image("logo.gif")
# Print QR Code
#Epson.qr("You can readme from your smartphone")
# Print barcode
#Epson.barcode('1324354657687','EAN13',64,2,'','')
# Cut paper
#Epson.cut()
 


StarLC20.text("              |\\\n")
StarLC20.text("           |--|/----------------,~\-123-PIANO--(#)--------\n")
StarLC20.text("           |--|---4-------------|~'------------|----------\n")
StarLC20.text("           |-/|.-------|~~~~|--/|-----|~~~~|--/|----------\n")
StarLC20.text("           |(-|-)-4---_|---_|--\|----_|---_|--\|----------\n")
StarLC20.text("           |-`|'-----(_)--(_)-------(_)--(_)--------------\n")
StarLC20.text("             \|")