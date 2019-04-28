import json, os
from api_data_fetcher import simple_get, log_error
from requests.exceptions import RequestException

def create_input_files(base_url, url_set, directory):
	"""
	"""
	try:
		if os.path.exists(directory):
			for url in url_set:
				if simple_get(url) is not None:
					with open(directory+'data_'+url[len(base_url):]+'.json', 'w') as outfile:
						json.dump(simple_get(url), outfile)
				else:
					return False
					break
			return True
		else:
			return False
	
	except RequestException as e:
		log_error('Error during requests to {0} : {1}'.format(url, str(e)))
		return None
		
					