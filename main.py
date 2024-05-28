from PokemonTypes import PokemonType
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.utils import get_color_from_hex

Builder.load_file('main_layout.kv')

class MainLayout(Widget):
	toggleModern=-1
	primaryType=-1
	secondaryType=-1

	toggleModernButton = ObjectProperty(None)
	toggleAlteredButton = ObjectProperty(None)
	spinnerPrimaryType = ObjectProperty(None)
	spinnerSecondaryType = ObjectProperty(None)
	labelTimes4Weak = ObjectProperty(None)
	labelTimes2Weak = ObjectProperty(None)
	labelNeutral = ObjectProperty(None)
	labelTimes2Resist = ObjectProperty(None)
	labelTimes4Resist = ObjectProperty(None)
	labelImmune = ObjectProperty(None)


	def __init__(self, **kwargs):
		super(MainLayout, self).__init__(**kwargs)

		self.createTypeList()

		self.spinnerSecondaryType.values.append(self.typeNone.name)
		for t in self.alteredTypeList:
			self.spinnerPrimaryType.values.append(t.name)
			self.spinnerSecondaryType.values.append(t.name)
		
		self.spinnerPrimaryType.values.sort()
		self.spinnerSecondaryType.values.sort()
	

	def toggleVersion(self):

		if self.toggleModernButton.state == 'down':
			self.toggleModern = 1
			self.chooseType()
			return

		if self.toggleAlteredButton.state == 'down':
			self.toggleModern = 0
			self.chooseType()
			return

		self.toggleModern = -1
		self.chooseType()

	def chooseType(self):

		typeList = []

		if self.toggleModern == 0:
			typeList = self.alteredTypeList
		else:
			typeList = self.modernTypeList

		for t in typeList:
			if t.name==self.spinnerPrimaryType.text:
				if self.primaryType != -1:
					self.spinnerSecondaryType.values.append(self.primaryType.name)
				self.primaryType=t
				self.spinnerSecondaryType.values.remove(t.name)
			if t.name==self.spinnerSecondaryType.text:
				if self.secondaryType != -1:
					if self.secondaryType.name != 'None':
						self.spinnerPrimaryType.values.append(self.secondaryType.name)
				self.secondaryType=t
				self.spinnerPrimaryType.values.remove(t.name)
			if self.spinnerSecondaryType.text == 'None':
				if self.secondaryType != -1:
					if self.secondaryType.name != 'None':
						self.spinnerPrimaryType.values.append(self.secondaryType.name)
				self.secondaryType=self.typeNone

		self.spinnerPrimaryType.values.sort()
		self.spinnerSecondaryType.values.sort()

		self.calculate()
		

	def calculate(self):

		if self.toggleModern == -1 or self.secondaryType == -1 or self.primaryType == -1:
			self.resetText()
			return

		times4Weak=[]
		times2Weak=[]
		if self.toggleModern==0:
			neutral=self.alteredTypeList.copy()
		else:
			neutral=self.modernTypeList.copy()
		times2Resist=[]
		times4Resist=[]
		immune=[]

		for t in self.primaryType.weak:
			times2Weak.append(t)
			neutral.remove(t)
		for t in self.primaryType.resist:
			times2Resist.append(t)
			neutral.remove(t)
		for t in self.primaryType.immune:
			immune.append(t)
			neutral.remove(t)

		for t in self.secondaryType.weak:
			if t in immune:
				pass
			elif t in times2Weak:
				times4Weak.append(t)
				times2Weak.remove(t)
			elif t in times2Resist:
				neutral.append(t)
				times2Resist.remove(t)
			else:
				times2Weak.append(t)
				neutral.remove(t)
		for t in self.secondaryType.resist:
			if t in immune:
				pass
			elif t in times2Resist:
				times4Resist.append(t)
				times2Resist.remove(t)
			elif t in times2Weak:
				neutral.append(t)
				times2Weak.remove(t)
			else:
				times2Resist.append(t)
				neutral.remove(t)
		for t in self.secondaryType.immune:
			immune.append(t)
			if t in times2Weak:
				times2Weak.remove(t)
			if t in neutral:
				neutral.remove(t)
			if t in times2Resist:
				times2Resist.remove(t)




		strTimes4Weak='4x weak: '
		if times4Weak:
			strTimes4Weak=strTimes4Weak+'[b]'+times4Weak[0].name+'[/b]'
			times4Weak.pop(0)
		while times4Weak:
			strTimes4Weak=strTimes4Weak+', '+'[b]'+times4Weak[0].name+'[/b]'
			times4Weak.pop(0)
		strTimes2Weak='2x weak: '
		if times2Weak:
			strTimes2Weak=strTimes2Weak+'[b]'+times2Weak[0].name+'[/b]'
			times2Weak.pop(0)
		while times2Weak:
			strTimes2Weak=strTimes2Weak+', '+'[b]'+times2Weak[0].name+'[/b]'
			times2Weak.pop(0)
		strNeutral='Neutral: '
		if neutral:
			strNeutral=strNeutral+'[b]'+neutral[0].name+'[/b]'
			neutral.pop(0)
		while neutral:
			strNeutral=strNeutral+', '+'[b]'+neutral[0].name+'[/b]'
			neutral.pop(0)
		strTimes2Resist='2x resist: '
		if times2Resist:
			strTimes2Resist=strTimes2Resist+'[b]'+times2Resist[0].name+'[/b]'
			times2Resist.pop(0)
		while times2Resist:
			strTimes2Resist=strTimes2Resist+', '+'[b]'+times2Resist[0].name+'[/b]'
			times2Resist.pop(0)
		strTimes4Resist='4x resist: '
		if times4Resist:
			strTimes4Resist=strTimes4Resist+'[b]'+times4Resist[0].name+'[/b]'
			times4Resist.pop(0)
		while times4Resist:
			strTimes4Resist=strTimes4Resist+', '+'[b]'+times4Resist[0].name+'[/b]'
			times4Resist.pop(0)
		strImmune='Immune: '
		if immune:
			strImmune=strImmune+'[b]'+immune[0].name+'[/b]'
			immune.pop(0)
		while immune:
			strImmune=strImmune+', '+'[b]'+immune[0].name+'[/b]'
			immune.pop(0)

		self.labelTimes4Weak.text=strTimes4Weak
		self.labelTimes2Weak.text=strTimes2Weak
		self.labelNeutral.text=strNeutral
		self.labelTimes2Resist.text=strTimes2Resist
		self.labelTimes4Resist.text=strTimes4Resist
		self.labelImmune.text=strImmune

	def createTypeList(self):
		anormal=PokemonType('Normal')
		afighting=PokemonType('Fighting')
		aflying=PokemonType('Flying')
		apoison=PokemonType('Poison')
		aground=PokemonType('Ground')
		arock=PokemonType('Rock')
		abug=PokemonType('Bug')
		aghost=PokemonType('Ghost')
		asteel=PokemonType('Steel')
		afire=PokemonType('Fire')
		awater=PokemonType('Water')
		agrass=PokemonType('Grass')
		aelectric=PokemonType('Electric')
		apsychic=PokemonType('Psychic')
		aice=PokemonType('Ice')
		adragon=PokemonType('Dragon')
		adark=PokemonType('Dark')
		afairy=PokemonType('Fairy')

		anormal.addTypeInteractions([afighting],[],[aghost])
		afighting.addTypeInteractions([aflying,apsychic,afairy],[arock,abug,adark],[])
		aflying.addTypeInteractions([arock,aelectric,aice],[afighting,abug,agrass],[aground])
		apoison.addTypeInteractions([aground,apsychic],[afighting,apoison,abug,agrass,afairy],[])
		aground.addTypeInteractions([awater,agrass,aice],[apoison,arock],[aelectric])
		arock.addTypeInteractions([afighting,aground,asteel,awater,agrass],[anormal,aflying,apoison,afire],[])
		abug.addTypeInteractions([aflying,arock,afire],[afighting,aground,agrass],[])
		aghost.addTypeInteractions([aghost,adark],[apoison,abug],[anormal,afighting])
		asteel.addTypeInteractions([afighting,aground,afire],[anormal,aflying,arock,abug,asteel,agrass,apsychic,aice,adragon,afairy],[apoison])
		afire.addTypeInteractions([aground,arock,awater],[abug,asteel,afire,agrass,aice,afairy],[])
		awater.addTypeInteractions([agrass,aelectric],[asteel,afire,awater,aice],[])
		agrass.addTypeInteractions([aflying,apoison,abug,afire,aice],[aground,awater,agrass,aelectric],[])
		aelectric.addTypeInteractions([aground],[aflying,asteel,aelectric],[])
		apsychic.addTypeInteractions([abug,aghost,adark],[afighting,apsychic],[])
		aice.addTypeInteractions([afighting,asteel,afire],[aground,awater,aice,adragon],[])
		adragon.addTypeInteractions([aice,adragon,afairy],[afire,awater,agrass,aelectric],[])
		adark.addTypeInteractions([afighting,abug,afairy],[aghost,adark],[apsychic])
		afairy.addTypeInteractions([apoison,asteel],[afighting,abug,adark],[adragon])

		self.alteredTypeList=[anormal,afighting,aflying,apoison,aground,arock,abug,aghost,asteel,afire,awater,agrass,aelectric,apsychic,aice,adragon,adark,afairy]

		mnormal=PokemonType('Normal')
		mfighting=PokemonType('Fighting')
		mflying=PokemonType('Flying')
		mpoison=PokemonType('Poison')
		mground=PokemonType('Ground')
		mrock=PokemonType('Rock')
		mbug=PokemonType('Bug')
		mghost=PokemonType('Ghost')
		msteel=PokemonType('Steel')
		mfire=PokemonType('Fire')
		mwater=PokemonType('Water')
		mgrass=PokemonType('Grass')
		melectric=PokemonType('Electric')
		mpsychic=PokemonType('Psychic')
		mice=PokemonType('Ice')
		mdragon=PokemonType('Dragon')
		mdark=PokemonType('Dark')
		mfairy=PokemonType('Fairy')

		mnormal.addTypeInteractions([mfighting],[],[mghost])
		mfighting.addTypeInteractions([mflying,mpsychic,mfairy],[mrock,mbug,mdark],[])
		mflying.addTypeInteractions([mrock,melectric,mice],[mfighting,mbug,mgrass],[mground])
		mpoison.addTypeInteractions([mground,mpsychic],[mfighting,mpoison,mbug,mgrass,mfairy],[])
		mground.addTypeInteractions([mwater,mgrass,mice],[mpoison,mrock],[melectric])
		mrock.addTypeInteractions([mfighting,mground,msteel,mwater,mgrass],[mnormal,mflying,mpoison,mfire],[])
		mbug.addTypeInteractions([mflying,mrock,mfire],[mfighting,mground,mgrass],[])
		mghost.addTypeInteractions([mghost,mdark],[mpoison,mbug],[mnormal,mfighting])
		msteel.addTypeInteractions([mfighting,mground,mfire],[mnormal,mflying,mrock,mbug,msteel,mgrass,mpsychic,mice,mdragon,mfairy],[mpoison])
		mfire.addTypeInteractions([mground,mrock,mwater],[mbug,msteel,mfire,mgrass,mice,mfairy],[])
		mwater.addTypeInteractions([mgrass,melectric],[msteel,mfire,mwater,mice],[])
		mgrass.addTypeInteractions([mflying,mpoison,mbug,mfire,mice],[mground,mwater,mgrass,melectric],[])
		melectric.addTypeInteractions([mground],[mflying,msteel,melectric],[])
		mpsychic.addTypeInteractions([mbug,mghost,mdark],[mfighting,mpsychic],[])
		mice.addTypeInteractions([mfighting,mrock,msteel,mfire],[mice],[])
		mdragon.addTypeInteractions([mice,mdragon,mfairy],[mfire,mwater,mgrass,melectric],[])
		mdark.addTypeInteractions([mfighting,mbug,mfairy],[mghost,mdark],[mpsychic])
		mfairy.addTypeInteractions([mpoison,msteel],[mfighting,mbug,mdark],[mdragon])

		self.modernTypeList=[mnormal,mfighting,mflying,mpoison,mground,mrock,mbug,mghost,msteel,mfire,mwater,mgrass,melectric,mpsychic,mice,mdragon,mdark,mfairy]

		self.typeNone=PokemonType('None')
		self.typeNone.addTypeInteractions([],[],[])

	def changeButtonColour(self):
		color_button_normal=get_color_from_hex('#bdffaa')
		color_button_down=get_color_from_hex('#87ff66')

		if self.toggleModern == 0:
			self.toggleModernButton.background_color = color_button_normal
			self.toggleAlteredButton.background_color = color_button_down
		elif self.toggleModern == 1:
			self.toggleModernButton.background_color = color_button_down
			self.toggleAlteredButton.background_color = color_button_normal
		else:
			self.toggleModernButton.background_color = color_button_normal
			self.toggleAlteredButton.background_color = color_button_normal

	def resetText(self):
		self.labelTimes4Weak.text=''
		self.labelTimes2Weak.text=''
		self.labelNeutral.text=''
		self.labelTimes2Resist.text=''
		self.labelTimes4Resist.text=''
		self.labelImmune.text=''

class TypeCalculator(App):
	def build(self):
		return MainLayout()

if __name__ == '__main__':
	TypeCalculator().run()