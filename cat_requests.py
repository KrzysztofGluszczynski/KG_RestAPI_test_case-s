import requests


def sendRequest(site_url, endpoint, parameters=""):
    """
        Function to send requests to target site.
        :param
            site_url    string      URL for target site
            endpoint    string      endpoint for target site url
            parameters string      parameters to add to target site url
        :return
            response from request in form of JSON
    """
    request = site_url + endpoint
    if len(parameters) > 0:
        request += "?" + parameters
    response = requests.get(request)
    return response.json()
