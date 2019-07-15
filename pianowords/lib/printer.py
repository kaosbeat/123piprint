from escpos import *
# from escpos.printer import Usb,Serial, Dummy
#import escpos

# d = Dummy()
# print(d.text("test"))
# StarLC20 = printer.File("/dev/usb/lp0", profile="Simple")
# StarLC20 = printer.Dummy()
# StarLC20 = printer.File("/dev/usb/lp0", auto_flush=False)
StarLC20 = printer.File("/dev/usb/lp0")
# escpos.Escpos(profile = "Simple")
# printer.Escpos(profile = "Simple")
# StarLC20 = printer.Usb(0x067b,0x2305,0, profile="Simple")
# StarLC20 = printer.Network("localhost",  port=4242, timeout=300, profile = "Simple")
# StarLC20.hw("INIT")
# StarLC20.hw("RESET")
# StarLC20._raw("111".encode())
# Print text
onlinebytes = b"\x11"
offlinebytes = b"\x13"
bellbytes = b"\x07"
StarLC20._raw(bellbytes)
# StarLC20.flush()

# StarLC20.text("Hello World\n")
# StarLC20.flush()
# Print image
#Epson.image("logo.gif")
# Print QR Code
#Epson.qr("You can readme from your smartphone")
# Print barcode
#Epson.barcode('1324354657687','EAN13',64,2,'','')
# Cut paper
#Epson.cut()
 


# StarLC20.text("              |\\\n")
# StarLC20.text("           |--|/----------------,~\-123-PIANO--(#)--------\n")
# StarLC20.text("           |--|---4-------------|~'------------|----------\n")
# StarLC20.text("           |-/|.-------|~~~~|--/|-----|~~~~|--/|----------\n")
# StarLC20.text("           |(-|-)-4---_|---_|--\|----_|---_|--\|----------\n")
# StarLC20.text("           |-`|'-----(_)--(_)-------(_)--(_)--------------\n")
# StarLC20.text("             \|")

# StarLC20.close()


def openPrinter():
    # StarLC20.open()
    global StarLC20
    onlinebytes = b"\x11"
    StarLC20._raw(onlinebytes)

def closePrinter():
    global StarLC20
    offlinebytes = b"\x13"
    StarLC20._raw(offlinebytes)
    # StarLC20.close()
    # StarLC20._raw()

def PrintWord(word):
    global StarLC20
    StarLC20.text(word)
    StarLC20.flush()


def NextLine():
    global StarLC20
    StarLC20.text("\n") 
    StarLC20.flush()