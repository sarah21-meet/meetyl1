class User():
	def __init__(self,name,email,password):
		self.name=name
		self.email=email
		self.password=password
		self.friends_list=[]
		self.posts=[]
	def add_friend(self,email):
		self.email=email
		self.friends_list.append(email)
		print("[name] has added [email] as a friend")
	def remove_friend(self,email):
		self.email=email
		self.friends_list.pop(email)
		print("[name] has removed [email] as a friend")
	def post(self,text):
		self.text=input()
		self.post.append(text)
		print("[name] has posted [text]")
	def get_userInfo():
		print("_______________")
		print("Name:[name]")
		print("Email:[email]")
		print("Password:[password]")
		print("Friend:[friends_list]")
		print("Posts:[post]")
		print("________________")