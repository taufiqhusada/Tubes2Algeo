import shutil
import os

#dijadiin satu folder dulu woy
source = r'PINS'
reference = r'Reference'
test = r'Test'

subfolders = os.listdir(source);

for folder in subfolders:
	path = os.path.join(source,folder)
	files = os.listdir(path)
	totalFiles = len(files) 
	print(totalFiles)
	cnt = 0;
	for file in files:
		print(os.path.join(path,file))
	for file in files:
		if (cnt>totalFiles/5):break;   
		shutil.move(os.path.join(path,file),os.path.join(test,file))
		cnt+=1;
	files = os.listdir(path)
	for file in files:
		shutil.move(os.path.join(path,file),os.path.join(reference,file)) 
	