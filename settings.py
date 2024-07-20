import configparser

class Settings:
	def __init__(self):
		self.config = configparser.ConfigParser()
		self.config.read('settings.ini')
		self.targetHz = int(self.config['woot-overlay-settings']['targetHz'])
		self.drawFPS = int(self.config['woot-overlay-settings']['drawFPS'])
		self.secondsKept = int(self.config['woot-overlay-settings']['secondsKept'])
		self.keybind1 = self.config['woot-overlay-settings']['keybind1']
		self.keybind2 = self.config['woot-overlay-settings']['keybind2']
		self.lineColor = self.config['woot-overlay-settings']['lineColor']
		self.thinTopBottomLineColor = self.config['woot-overlay-settings']['thinTopBottomLineColor']
		self.thinLineThickness = float(self.config['woot-overlay-settings']['thinLineThickness'])
		self.bgColor = self.config['woot-overlay-settings']['bgColor']
