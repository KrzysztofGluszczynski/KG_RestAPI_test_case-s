import unittest
import cat_requests
import time


class SportlyCatTest2(unittest.TestCase):

    def setUp(self):
        self.base_line_site = "http://ip.jsontest.com/"
        self.site_url = "https://cat-fact.herokuapp.com"

    def test_sportlyCatTest3(self):
        print("Step 1. Get base site response time")
        start_time = time.time()
        for i in range(10):
            cat_requests.sendRequest(self.base_line_site, "")
        base_time = time.time() - start_time
        print("Time to perform 10 requests to baseline site:"+str(base_time))

        print("Step 2. Get response time for Cat site")
        start_time = time.time()
        for i in range(10):
            cat_requests.sendRequest(self.site_url, "/facts/random")
        cat_time = time.time() - start_time
        print("Time to perform 10 requests to cat site:"+str(cat_time))

        print("Step 3. Compare times and check if results are inside KPI range")
        print("Baseline time: "+str(base_time)+"\n" +
              "Cat site time: "+str(cat_time)+"\n" +
              "Difference: "+str(cat_time-base_time))
        # Check if cat site response time is lower then baseline site response time + 10 seconds
        if cat_time > base_time + 10:
            self.fail("Cat site response time is higher then baseline site response time + 10 seconds")
        # Check if cat site response time is lower or equal then 15 seconds
        if cat_time > 15:
            self.fail("Cat site response time is higher then 15 seconds")
        print("KPI success parameters within boundaries")

        # Sleep for better logs
        time.sleep(1)


if __name__ == "__main__":
    unittest.main()
