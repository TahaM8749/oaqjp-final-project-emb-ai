import unittest
import json
from emotion_detection import emotion_detector  

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        result_1 = emotion_detector('I am glad this happened')
        self.assertIn('joy', result_1)
        self.assertIn('dominant_emotion', result_1)
        self.assertEqual(result_1['dominant_emotion'], 'joy')
       
        result_2 = emotion_detector('I am really mad about this')
        self.assertIn('anger', result_2)
        self.assertIn('dominant_emotion', result_2)
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertIn('disgust', result_3)
        self.assertIn('dominant_emotion', result_3)
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        result_4 = emotion_detector('I am so sad about this')
        self.assertIn('sadness', result_4)
        self.assertIn('dominant_emotion', result_4)
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertIn('fear', result_5)
        self.assertIn('dominant_emotion', result_5)
        self.assertEqual(result_5['dominant_emotion'], 'fear')

if __name__ == "__main__":
    unittest.main()