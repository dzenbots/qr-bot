import cv2


class QRReader:
    def __init__(self, filename=None):
        self.filename = filename

    def video_qr_reader(self):
        if not self.filename:
            cam = cv2.VideoCapture(0)
            detector = cv2.QRCodeDetector()
            while True:
                _, img = cam.read()
                data, bbox, _ = detector.detectAndDecode(img)
                if data:
                    cam.release()
                    cv2.destroyAllWindows()
                    return data
                if cv2.waitKey(1) == ord("Q"):
                    break
            cam.release()

    def picture_qr_reader(self):
        if self.filename:
            detector = cv2.QRCodeDetector()  # включаем  QRCode detector
            img = cv2.imread(self.filename)
            data, _, _ = detector.detectAndDecode(img)
            return None if data is None else data
