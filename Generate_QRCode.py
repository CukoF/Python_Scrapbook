# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 14:35:10 2023

@author: selcu
"""

import pyqrcode
#import pypng
from pyqrcode import QRCode


# Create a target link in STR
target_link = "https://selchukhadzhaahmed.com/"

# Generate a QR Code
url = pyqrcode.create(target_link)

# Create and save the png file
url.png("SH_Website_QRCode.png", scale = 10)