import sys
print("\nhello world\n")
get_input_1 = input()
print("\nget input : %s\n" % get_input_1)
get_input_2 = sys.stdin.readlines()
print("\nget input : %s\n" % get_input_2[0])
sys.stdout.flush()