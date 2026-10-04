import qrcode
# Taking UPI_ID as a input

upi_id = input("enter the UPI ID = ")

# Explain the payment url format:
""" a payment url is an endpoint that contains the information required to initiate a payment.
The payment gateway validates these parameters like amount,currency,transaction ID, order and redirect url to the payment page.
"""

## upi://pay?pa=UPI_ID%apn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE
# Here pa -> parameters, apn-> user name
# Defining the payment url based on the UPI ID and payment app
# You can modify these urls based on the payments app you want to support

phonepe_url =f'upi//pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url =f'upi//pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url =f'upi//pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# Here mc is 'merchant code' if you have mc then write otherwise you can skip this code.

# Create QR codes for each payment apps
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# save the Qr code to image file (optional)
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

# Pillow as pil python library which can use for image processing.
# display the qr code
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()


