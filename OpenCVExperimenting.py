import cv2 as cv
import numpy as np
import threading
import tkinter as tk

class MotionDetection:
    def __init__(self):
        self.contourLastLength = None
        self.count = 1
        self.contour = None
        self.liveflag = True

    def showLive(self):
        if not hasattr(self, "t2") or not self.t2.is_alive():
            self.liveflag = False
            self.t2 = threading.Thread(target=self.LiveFeed, daemon=True)
            self.t2.start()

    def hideLive(self):
        self.liveflag = True  # signal thread to stop
        if hasattr(self, "t2"):
            self.t2.join(timeout=2)
        cv.destroyAllWindows()

    def LiveFeed(self):
        kernel = np.ones((3,3), dtype=np.uint8)
        cap = cv.VideoCapture(0)

        if not cap.isOpened():
            print('Cannot open camera')
            return

        ret, frameLast = cap.read()
        gray_last = cv.cvtColor(frameLast, cv.COLOR_BGR2GRAY)

        while not self.liveflag:
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            graydiff = cv.absdiff(gray, gray_last)
            graydiff = cv.medianBlur(graydiff, 3)
            mask = cv.adaptiveThreshold(graydiff, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 3)
            mask = cv.medianBlur(mask, 3)
            mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)

            gray_last = gray

            contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
            cv.drawContours(frame, contours, -1, (127, 127, 63), 2)

            cv.imshow("frame", frame)
            cv.imshow("mask", mask)

            if cv.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv.destroyAllWindows()

    def Interface(self):
        root = tk.Tk()
        root.geometry("200x300")

        tk.Button(root, text="Show Live", command=self.showLive).pack()
        tk.Button(root, text="Hide Live", command=self.hideLive).pack()

        root.mainloop()


if __name__ == "__main__":
    md = MotionDetection()
    md.Interface()
    
