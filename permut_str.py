def permutation(string):
	def rec(string_,arr,new_string):
		for i in range(len(string_)):
			if arr[i]==0:
				arr[i]=1
				rec(string_,arr,new_string+string_[i])
				arr[i]=0
		if len(new_string)==len(string_):
			print(new_string)
	rec(string,[0]*len(string),"")

string = input("Enter string ")
print("All permutation of string is: ")
permutation(string)

