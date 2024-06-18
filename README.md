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
<td>Response in text field is at least 6 characters long.</td>
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
<td>Response in text field is at least 6 characters long.</td>
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
<td>10 requests sent with responses from baseline site received</td>
</tr>
<tr>
<td>2</td>
<td>Send requests to cat site</td>
<td>10 requests sent with responses received</td>
</tr>
<tr>
<td>3</td>
<td>Compare times and check if results are inside KPI range</td>
<td>Cat site response time is lower then baseline site response time + 10 seconds<br>
    Cat site response time is lower or equal then 15 seconds
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
<td>Every 5 seconds we receive response on our request</td>
</tr>
</table>

    
