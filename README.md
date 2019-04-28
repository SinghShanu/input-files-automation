# input-files-automation
Small modular automation program in python 3 to demonstrate use of REST API calls, file generation and manipulation on windows/linux
Main functions that are performed as part of this program:
  api_data_fetcher.py --> script to fetch json data by hitting third-aprty API endpoints
  input_files_creator.py --> script to generate data input files with json format in a particular windows directory
  file_zipper_utility.py --> script to generate a zip file comprising of all json input files and checking integrity
  backup_replace_input_files.py --> script to take backup of original zip file from server location and replacing it with newly created zip file
  starter_script.py --> main program starting point with decalarations and function calls
