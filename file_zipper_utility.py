import zipfile, os
from input_files_creator import create_input_files
from api_data_fetcher import log_error
from requests.exceptions import RequestException

def zip_input_files(base_url, url_set, resourceName, directory):
	"""
	"""
	try:
		if create_input_files(base_url, url_set, directory):
			with zipfile.ZipFile(resourceName+'.zip', 'w', zipfile.ZIP_DEFLATED) as zip:
				rootdir = os.path.basename(directory)
				
				for dirpath, dirnames, files in os.walk(directory):
					for filename in files:
						#print(filename)
						filepath = os.path.join(dirpath, filename)
						parentpath = os.path.relpath(filepath, directory)
						arcname = os.path.join(rootdir, parentpath)
						zip.write(filepath, arcname)
			return True
		else:
			#print("Something went wrong while creating input files")
			return False	
	
	except RequestException as e:
		log_error('Error during requests to {0} : {1}'.format(url, str(e)))
		return None
	