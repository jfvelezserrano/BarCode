import csv
import cv2
from barcode_recognizer import Code39Recognizer
import unittest

class MakeTests(unittest.TestCase):

    def __procesar(self, file_name, x, y, width, height, groundtruth):
        img = cv2.imread("groundtruth/"+file_name)
        result = self.recognizer.recognize(img, x, y, width, height)
        self.test += 1
        if result == groundtruth:
            self.success += 1

    @classmethod
    def setUpClass(cls):
        cls.recognizer = Code39Recognizer()

    def test_SuccessRate(self):
        self.success = 0
        self.test = 0
        with open('groundtruth/via_project_2Mar2021_18h59m.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_counter = 0
            for row in csv_reader: 
                if line_counter > 0:
                    file_name = row[0]
                    x = int(row[4])
                    y = int(row[5])
                    width = int(row[6])
                    height = int(row[7])
                    result = row[8]
                    self.__procesar(file_name, x, y, width, height, result)
                line_counter += 1            
        success_rate = self.success / self.test
        print("Success rate: " + str(success_rate))
        self.assertGreater(success_rate, 0.9)



if __name__ == "__main__":
    unittest.main()


