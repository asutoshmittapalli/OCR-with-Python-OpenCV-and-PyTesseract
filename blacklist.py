custom_config = r'-c tessedit_char_blacklist=abcdefghijklmnopqrstuvwxyz --psm 6'
pytesseract.image_to_string(img, config=custom_config)
