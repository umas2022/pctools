
import sys
import subprocess

path_7z = sys.argv[1]
path_in = sys.argv[2] 
path_out = sys.argv[3] 
password = sys.argv[4]

print("path_7z: " + path_7z)
print("path_in: " + path_in)
print("path_out: " + path_out)
print("password: " + password)

subprocess.run([path_7z, 'a', path_out,"-p"+password, path_in])

# wait_here = input("\npress enter to exit ...")