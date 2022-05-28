import unittest

from pencilvania.pencilvania import main

QR_CODE_IMAGE_PATH = 'test/images/qr_code.png'

class QrCodeTest(unittest.TestCase):
    def test_qr_code(self):
        main(image_path=QR_CODE_IMAGE_PATH)


if __name__ == "__main__":
    unittest.main()
