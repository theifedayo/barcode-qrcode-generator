# import pyqrcode
# import png
# from pyqrcode import QRCode
  
  
# # String which represents the QR code
# s = "1232312"
  
# # Generate QR code
# url = pyqrcode.create(s)
  
# # Create and save the svg file naming "myqr.svg"
# url.svg("myqr.svg", scale = 8)
  
# # Create and save the png file naming "myqr.png"
# url.png('myqr.png', scale = 6)

# import EAN13 from barcode module
from barcode import EAN13
  
# import ImageWriter to generate an image file
from barcode.writer import ImageWriter
  
# Make sure to pass the number as string
number = '5901234123457'
  
# Now, let's create an object of EAN13
# class and pass the number
my_code = EAN13(number)

  
# Our barcode is ready. Let's save it.
my_code.save("new_code")