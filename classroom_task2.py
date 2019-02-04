class ipcal():
	def _init_(self,ip=[0,0,0,0],nm=[0,0,0,0]):
		self.ip=ip
		self.nm=nm
	def printip(self):
		print(self.ip)
	def printnm(self):
		print(self.nm)
myip=ipcal([192,168,1,1],[255,255,255,0])
myip.printip()
mynm.printnm()
