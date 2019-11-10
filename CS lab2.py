list1=[1,2,3,4,5,6,7,8,9]
list2=[17,1,5,7,9,16,45]

def common_num(num1,num2):
	end_num=[]
	for num in num1:
		if num in num2:
			end_num.append(num):
	return sum end_num
print(common_num(list1,list2))	


encoder_caesar={'a':'d','b':'e','c':'f','d':'g','e':'h','f':'i','g':'j','h':'k','i':'l','j':'m','k':'n','l':'o','m':'p','n':'q','o':'r','p':'s','q':'t','r':'u','s':'v','t':'w','u':'x','v':'y','w':'z','x':'a','y':'b','z':'c'}
def encoder