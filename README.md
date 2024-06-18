RestAPI testing<br>
    Cat facts site testing<br>
    Used applications:<br>
        - Windows               11 Pro<br>
        - Pycharm Community     2024.1.3<br>
        - Python                3.12.2<br>
        - requests              2.32.3<br>

Test case descriptions:
<table>
<tr><td align="center" colspan="3">
Test case 1 - Sending request for random fact without parameters
</td></tr>
<tr>
<td>Step ID:</td>
<td>Step description:</td>
<td>Expected result:</td>
</tr>
<tr>
<td>1</td>
<td>Send request for random cat fact with default parameters</td>
<td>Response in text field is at least 6 characters long.<br>
    Reason: I set expected length to at least 6 characters, as from experiments this was shortest fact I recieved and shorter facts don't make sense.
</td>
</tr>
</table>

<table>
<tr><td align="center" colspan="3">
Test case 2 - Sending request for random fact without parameters
</td></tr>
<tr>
<td>Step ID:</td>
<td>Step description:</td>
<td>Expected result:</td>
</tr>
<tr>
<td>1</td>
<td> Send request for random cat fact with parameters animal_type=cat and amount=2</td>
<td>Response in text field is at least 6 characters long.<br>
    Reason: I set expected length to at least 6 characters, as from experiments this was shortest fact I recieved and shorter facts don't make sense.
</td>
</tr>
</table>



<table>
<tr><td align="center" colspan="3">
Test case 3 - KPI for response time for cat site
</td></tr>
<tr>
<td>Step ID:</td>
<td>Step description:</td>
<td>Expected result:</td>
</tr>
<tr>
<td>1</td>
<td>Send requests to base site</td>
<td>10 requests sent with responses from baseline site received<br>
    Reason: 10 requests should give good view on response time and will not take long. I found baseline site for stable comarison, in case od different ping for different network that can run this test.
</td>
</tr>
<tr>
<td>2</td>
<td>Send requests to cat site</td>
<td>10 requests sent with responses received<br>
    Reason: 10 requests should give good view on response time and will not take long.</td>
</tr>
<tr>
<td>3</td>
<td>Compare times and check if results are inside KPI range</td>
<td>Cat site response time is lower then baseline site response time + 10 seconds<br>
    Cat site response time is lower or equal then 15 seconds<br>
    Reason: From testing base site response time was 2-3 seconds and cat site was 6-7 seconds. I made KPIs values to have big margin of error.
            Those can be refined based on requirements.
</td>
</tr>
</table>

<table>
<tr><td align="center" colspan="3">
Test case 4 - KPI for response time for cat site</td></tr>
<tr>
<td>Step ID:</td>
<td>Step description:</td>
<td>Expected result:</td>
</tr>
<tr>
<td>1</td>
<td>Perform requests every 5 seconds for 30 minutes</td>
<td>Every 5 seconds we receive response on our request<br>
    Reason: 5 seconds are long enought, to not overwhelm server and will be good for testing stablity of RestAPI. 30 minutes time was taken as good for short lenght stability test.</td>
</tr>
</table>

    
