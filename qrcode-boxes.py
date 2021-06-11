from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2

vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)
frame = vs.read()
frame = imutils.resize(frame, width=400)
barcodes = pyzbar.decode(frame)


for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
barcodeData = barcode.data.decode("utf-8")
barcodeType = barcode.type
text = "{} ({})".format(barcodeData, barcodeType)
cv2.putText(frame, text, (x, y - 10),
     cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
cv2.imshow("Barcode Reader", frame)
