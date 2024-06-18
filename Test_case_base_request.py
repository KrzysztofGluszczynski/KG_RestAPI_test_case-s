import unittest
import cat_requests
import time


class SportlyCatTest1(unittest.TestCase):

    def setUp(self):
        self.site_url = "https://cat-fact.herokuapp.com"

    def test_sportlyCatTest1(self):
        print("Step 1. Send request for random cat fact with default parameters")
        fact = cat_requests.sendRequest(self.site_url, "/facts/random")["text"]
        print("Fact: \""+fact+"\"")
        if len(fact) > 6:
            print("Step 1. Success")
        else:
            self.fail("Step 1. Response in text field was less then 6 characters long.")

        # Sleep for better logs
        time.sleep(1)


if __name__ == "__main__":
    unittest.main()
