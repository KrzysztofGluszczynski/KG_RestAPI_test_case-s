import unittest
import cat_requests
import time


class SportlyCatTest2(unittest.TestCase):

    def setUp(self):
        self.site_url = "https://cat-fact.herokuapp.com"

    def test_sportlyCatTest1(self):
        print("Step 1. Send request for random cat fact with : dog and 2 facts")
        facts = cat_requests.sendRequest(self.site_url, "/facts/random", parameters="animal_type=dog&amount=2")
        print("Facts array: \""+str(facts)+"\"")
        if len(facts) == 2 and len(facts[0]["text"]) > 6 and  len(facts[1]["text"]) > 6:
            print("Step 1. Success")
        else:
            self.fail("Step 1. Number of responses is different then 2 or responses are shorter then 6 characters.")
        # Sleep for better logs
        time.sleep(1)


if __name__ == "__main__":
    unittest.main()
