from variables import *
from functions import *
import cv2
import pytesseract


def read_screenshot(path):

    # read image & standard preprocessing
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.bitwise_not(image)

    def crop_img(img, scale=1.0):
        center_x, center_y = img.shape[1] / 2, img.shape[0] / 2
        width_scaled, height_scaled = img.shape[1] * scale, img.shape[0] * scale
        left_x, right_x = center_x - width_scaled / 2, center_x + width_scaled / 2
        top_y, bottom_y = center_y - height_scaled / 2, center_y + height_scaled / 2
        img_cropped = img[int(top_y):int(bottom_y), int(left_x):int(right_x)]
        return img_cropped

    def crop_left(img, scale=1.0):
        center_x, center_y = img.shape[1] / 2, img.shape[0] / 2
        width_scaled, height_scaled = img.shape[1] * scale, img.shape[0]
        width_unscaled = img.shape[1]
        left_x, right_x = center_x - width_scaled / 2, center_x + width_unscaled / 2
        top_y, bottom_y = center_y - height_scaled / 2, center_y + height_scaled / 2
        img_cropped = img[int(top_y):int(bottom_y), int(left_x):int(right_x)]
        return img_cropped

    if path == PATH_RSI or path == PATH_STOCHASTIC:

        # standard preprocessing & resize image
        retval, image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)
        image = cv2.resize(image, (100, 100), interpolation=cv2.INTER_CUBIC)

        # convert to gray, and threshold
        th, threshed = cv2.threshold(image, 240, 255, cv2.THRESH_BINARY_INV)

        # morph-op to remove noise
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
        morphed = cv2.morphologyEx(threshed, cv2.MORPH_CLOSE, kernel)

        # find the max-area contour
        cnts = cv2.findContours(morphed, cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)[-2]
        cnt = sorted(cnts, key=cv2.contourArea)[-1]
        # print(cnt)
        # crop and save it
        x, y, w, h = cv2.boundingRect(cnt)
        dst = img_cropped = image[y:y + h, x:x + w]
        img_cropped = crop_left(img_cropped, 0.6)
        img_cropped = crop_img(img_cropped, 0.8)
        cv2.imwrite(PATH_STOCHASTIC, img_cropped)

        config = '--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789'
        text = pytesseract.image_to_string(img_cropped, config=config)
        text = ''.join(i for i in text if i.isdigit())
        if len(text) > 0:
            text = int(text)
            if text >= 0 and text <= 100: print(text)
            else: end_program(error=True)
        else: end_program(error=True)

    elif path == PATH_TEST or path == PATH_PRICE:
        print("I am called here")
        image = cv2.resize(image, (0, 0), fx=20, fy=20)
        retval, image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)

        if path == PATH_EARNINGS:
            config = '--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789,.'
        elif path == PATH_TEST:
            config = '--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789,.'
        elif path == PATH_PRICE:
            config = '--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789.'

        text = pytesseract.image_to_string(image, config=config)
        text = ''.join(i for i in text if i.isdigit() or i == '.')

        if len(text) > 0: print(int(float(text)))
        else: end_program(error=True)


read_screenshot(path='ss\\test.png')
