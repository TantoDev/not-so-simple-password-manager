import json

class Credential:
	def __init__(self, title, username, password):
		self.title = title
		self.name = username
		self.password = password

# converts data to storable format 
	def to_dict(self):
		return {'title': self.title,'username': self.name, 'password': self.password}

# converts data back to object format
	@staticmethod
	def from_dict(data):
			return Credential(data['title'],data['username'],data['password'])
				
class Vault:
	def __init__(self):
		self.vault = []
		self.filename = 'vault.json'
		self.loadfile()
		
	def addCredential(self):
		title = input(" Enter the title: ")
		username = input(" Enter your username: ")
		password = input(" Enter your password: ")
		myCred = Credential(title,username, password)
		self.vault.append(myCred)
		self.savefile()
		print("\n Saved to vault!")
		
	def viewAll(self):
		if not self.vault:
			print("\n Your vault is empty!")
		else:
			print("\n  Saved credentials:")
			for cred in self.vault:
				print(f"\n  {cred.title}\n  --------")

# search credentials and handles case sensitivy	
	def search(self):
		if not self.vault:
			print("\n Your vault is empty!")
		else:
			found = False
			search_term = input("\n Enter a search term: ")
			for cred in self.vault:
				if search_term.lower() in cred.title.lower() or search_term.lower() in cred.name:
					print(f" {cred.title} \n Username: {cred.name} \n Password: {cred.password}")
					found = True
			if not found:
				print("\n The entry doesn't exist in your vault")

# deletes credentials
	def delete(self):
		found = False
		if not self.vault:
			print("\n Your vault is empty!")
		else:
			word = input("\n Enter the title of the credential you wish to delete: ")
			for cred in self.vault:
				if word.lower() == cred.title.lower():
					self.vault.remove(cred)
					self.savefile()
					print(f"\n {word} credential removed from vault!")
					found = True
			if not found:
				print("\n The entry doesn't exist in your vault")

# saves user data				
	def savefile(self):
		data = [(cred.to_dict()) for cred in self.vault]
		with open(self.filename,'w') as f:
			json.dump(data,f)

# retrives saved data			
	def loadfile(self):
		try:
			with open(self.filename,'r') as f:
				data = json.load(f)
				self.vault = [(Credential.from_dict(item)) for item in data]
		except FileNotFoundError:
			self.vault = []
		except json.JSONDecodeError:
			self.vault = []
		except TypeError:
			self.vault = []
			
myVault = Vault()	
menu_text = '''
 Simple Password Manager~©
 1. Add Credential
 2. View Vault
 3. Search
 4. Delete Credential
 5. Exit
'''
# menu interface
while True:
	try:
		response = input(menu_text+"\n Select your choice: ").strip()
		if response == '1':
			myVault.addCredential()
		elif response == '2':
			myVault.viewAll()
		elif response == '3':
			myVault.search()
		elif response == '4':
			myVault.delete()
		elif response == '5':
			print("\nHave a nice day!\n")
			break
		else:
			print("\nInvalid input!")						
	except ValueError:
		print("Enter a numerical value")

    
