import zipfile, os, shutil
from datetime import datetime
from api_data_fetcher import log_error
from requests.exceptions import RequestException

def create_zip_backup(srcPath, resourceName):
	"""
	"""
	try:
		if os.path.exists(srcPath):
			if os.path.isfile(srcPath+resourceName+".zip"):
				#print("Original zip file present in this directory.")
				#print("Original File Name: "+resourceName+".zip")
				#print("Backup File Name: "+"BKP_"+resourceName+".zip_"+datetime.now().strftime("%Y_%m_%d-%H_%M_%S"))
				shutil.copy(srcPath+resourceName+".zip", srcPath+"BKP_"+resourceName+"_"+datetime.now().strftime("%Y_%m_%d-%H_%M_%S")+".zip")
			return True
		else:
			#print("Invalid directory error in create_zip_backup function...")
			return False
			
	except RequestException as e:
		log_error('Error during requests to {0} : {1}'.format(url, str(e)))
		return None

def replace_zip_file(srcPath, destPath, resourceName):
	"""
	"""
	try:
		if os.path.exists(srcPath) and os.path.exists(destPath) and os.path.isfile(destPath+resourceName+".zip"):
			#print("New updated zip file: "+srcPath)
			#print("Replace file location: "+destPath)
			os.unlink(destPath+resourceName+".zip")
			shutil.move(srcPath+resourceName+".zip", destPath)
			return True
		else:
			#print("Invalid directory error in replace_zip_file function or zip file doesn't exist...")
			return False
	except RequestException as e:
		log_error('Error during requests to {0} : {1}'.format(url, str(e)))
		return None