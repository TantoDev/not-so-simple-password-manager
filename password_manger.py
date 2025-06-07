
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
		self.mastervault = {}
		self.filename = 'vault.json'
		self.masterfile = 'mastervault.json'
		self.loadfile()
		self.loadlock()

# prevent empty response from user	
	def safe_input(self,prompt, var_name="This field"):
		field = input(prompt).strip()
		while True:
			if not field:
				print(f"\n {var_name} cannot be empty!")
				field = input(prompt).strip()
			else:
				return field
		
	def addCredential(self):
		title = self.safe_input(" Enter the title: ")
		username = self.safe_input(" Enter your username: ")
		password = self.safe_input(" Enter your password: ")
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
			search_term = self.safe_input("\n Enter a search term: ")
			for cred in self.vault:
				if search_term.lower() in cred.title.lower() or search_term.lower() in cred.name:
					print(f"\n {cred.title} \n Username: {cred.name} \n Password: {cred.password}")
					found = True
			if not found:
				print("\n The entry doesn't exist in your vault")

# deletes credentials
	def delete(self):
		found = False
		if not self.vault:
			print("\n Your vault is empty!")
		else:
			word = self.safe_input("\n Enter the title of the credential you wish to delete: ")
			for cred in self.vault:
				if word.lower() == cred.title.lower():
					self.vault.remove(cred)
					self.savefile()
					print(f"\n {word} credential removed from vault!")
					found = True
			if not found:
				print("\n The entry doesn't exist in your vault")

# clears vault	
	def clear(self):
		if not self.vault:
			print("\n Your vault is empty!")
		else:
			reply = input("\n Are you sure you want to clear your vault? Y/N: ").lower().strip()
			if reply in ['yes','y']:
				self.vault.clear()
				self.savefile()
				print("\n Vault has been cleared!")
			elif reply in ['no','n']:
				print("\n Phew! Vault still intact")
			else:
				print('\n Invalid response! Please type Y or N')

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
		except (FileNotFoundError, json.JSONDecodeError, TypeError):
			self.vault = []
			
# saves the master password
	def savelock(self):
		with open(self.masterfile, 'w') as f:
			json.dump(self.mastervault,f)

# retrieves master password for authentication	
	def loadlock(self):
		try:
			with open(self.masterfile,'r') as f:
				self.mastervault = json.load(f)
		except (FileNotFoundError, json.JSONDecodeError, TypeError):
			self.mastervault = {}

# menu interface			
	def display_menu(self):
		menu_text = '''
 Simple Password Manager~©
 1. Add Credential
 2. View Vault
 3. Search
 4. Delete Credential
 5. Clear Vault
 6. Exit
'''

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
					myVault.clear()
				elif response == '6':
					print("\n  Have a nice day!\n")
					break
				else:
					print("\nInvalid input!")						
			except ValueError:
				print("Enter a numerical value")
# runs if first time running the program
	def register(self):
		self.mastervault['name'] = self.safe_input("\n Enter your name: ")
		self.savelock()
		print(f"\n Hi {self.mastervault['name']}, \n\n To start using your password manager you need to first create your master password.\n\n It would be required every time you try to access your vault.")
		while True:
			password = self.safe_input("\n Enter your Master Password: ")
			self.mastervault['password'] = self.safe_input("\n Confirm Password: ")
			if password == self.mastervault['password']:
				self.savelock()
				print("\n Password set successfully!")
				while True:
					reply = self.safe_input("\n Enter master password to continue: ")
					if reply == self.mastervault['password']:
						print("\n Verified!")
						self.display_menu()
						return 	
					else:
						print(f"\n Wrong password! Try again: ")
			else:
				print("\n Passwords dont match! Try again.")

# runs for every other time
	def resume(self):
		set_password = True
		print(f"\n Welcome back {self.mastervault['name']}!" )	
		while True:
			reply = self.safe_input("\n Enter master password to continue: ")
			if self.mastervault.get('password'):			
				if reply == self.mastervault['password']:
					print("\n Verified!")
					self.display_menu()
					return 
				else:
					print(f"\n Wrong password! Try again: ")
			else:
				print("\n Oops! seems like you haven't yet created your master password.\n No worries, try creating one now.")
				while True:
					password = self.safe_input("\n Enter your Master Password: ")
					self.mastervault['password'] = self.safe_input("\n Confirm Password: ")
					if password == self.mastervault['password']:
						self.savelock()
						print("\n Password set successfully!")
						while True:
							reply = self.safe_input("\n Enter your master password to continue: ")
							if reply == self.mastervault['password']:
								print("\n Verified!")
								self.display_menu()
								return 
					else:
						print("\n Passwords dont match! Try again.")

# Runs register() on first run, otherwise resume().
	def run(self):
		if not self.mastervault:
			self.register()
		else:
			self.resume()
	
							
myVault = Vault()
myVault.run()	

		
	
