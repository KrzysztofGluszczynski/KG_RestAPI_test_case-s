import unittest
import cat_requests
import time


class SportlyCatTest4(unittest.TestCase):

    def setUp(self):
        self.site_url = "https://cat-fact.herokuapp.com"

    def test_sportlyCatTest4(self):
        print("Step 1. Perform requests every 5 seconds for 30 minutes")
        test_time = 1800                    # Seconds
        test_interval = 5                   # Seconds
        start_time = time.time()
        for i in range(int(test_time/test_interval)):
            print("Sending request nr "+str(i+1))
            fact = cat_requests.sendRequest(self.site_url, "/facts/random")
            if len(fact) > 6:
                print("Request nr "+str(i+1)+" Success")
            else:
                self.fail("Request nr "+str(i+1)+" Failure")
            # Calculating sleep time, so requests are sent every 5 seconds.
            time.sleep((start_time+5*(i+1))-time.time())

        # Sleep for better logs
        time.sleep(1)


if __name__ == "__main__":
    unittest.main()
