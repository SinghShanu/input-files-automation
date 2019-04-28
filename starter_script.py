from file_zipper_utility import zip_input_files
from backup_replace_input_files import create_zip_backup, replace_zip_file
from api_data_fetcher import log_error
from requests.exceptions import RequestException

base_url = 'https://jsonplaceholder.typicode.com/'
url_set = (base_url+'posts', base_url+'comments', base_url+'albums', base_url+'photos', base_url+'todos', base_url+'users')
input_files_directory = 'D:\\dev\\data_upload_automation\\input_files\\'
zip_file_directory = 'D:\\dev\\data_upload_automation\\'
resourceName = 'Custom_Resource_Test'
resource_directory = 'C:\\InputFileLocation\\'

def main():
	"""
	"""
	try:
		print("Program to fetch data from API and zip json files")
		print("Process Starting...")
		if zip_input_files(base_url, url_set, resourceName, input_files_directory):
			print("Latest API json files zipped successfully")
			print("Proceeding with taking backup of resource files on server...")
			if create_zip_backup(resource_directory, resourceName) and replace_zip_file(zip_file_directory, resource_directory, resourceName):
				print("Backup and replace completed successfully!!!")
			else:
				print("Something went wrong in backup and replace file utility!!!")
		else:
			print("Something went wrong in file zipper utility!!!")
	
	except RequestException as e:
		log_error('Error during requests to {0} : {1}'.format(url, str(e)))
		return None
	
	
if __name__ == "__main__":
	main()