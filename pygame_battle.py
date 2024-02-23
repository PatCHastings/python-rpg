import pygame

pygame.init()

clock = pygame.time.Clock()
fps = 60

#game screen
bottom_panel = 150
screen_width = 800
screen_height = 400 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('battle')

#load images
#background image
background_img = pygame.image.load('images/colosseum_backdrop.png').convert_alpha()
#panel image
panel_img = pygame.image.load('images/Icons/panel.png').convert_alpha()
panel_img = pygame.transform.scale(panel_img, (800, 150))


#function for drawing background
def draw_bg():
	screen.blit(background_img, (0, 0))


#function for drawing panel
def draw_panel():
	screen.blit(panel_img, (0, screen_height - bottom_panel))


#fighter class
class Fighter():
	def __init__(self, x, y, name, max_hp, strength, potions):
		self.name = name
		self.max_hp = max_hp
		self.hp = max_hp
		self.strength = strength
		self.start_potions = potions
		self.potions = potions 
		self.alive = True 
		self.animation_list = []
		self.frame_index = 0
		self.action = 1 #0:idle, 1:attack, 2:damage, 3:death
		self.update_time = pygame.time.get_ticks()
		#load idle images
		temp_list = []
		for i in range(6):
			img = pygame.image.load(f'images/{self.name}/idle/{i}.png')
			img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
			temp_list.append(img)
		self.animation_list.append(temp_list)
		#load attack images
		temp_list = []
		for i in range(5):
			img = pygame.image.load(f'images/{self.name}/attack/{i}.png')
			img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
			temp_list.append(img)
		self.animation_list.append(temp_list)
		self.image = self.animation_list[self.action][self.frame_index]
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)


	def update(self):
		animation_cooldown = 100
		#handle animation
		#update image
		self.image = self.animation_list[self.action][self.frame_index]
		#check if enough time has passed sihce the last update
		if pygame.time.get_ticks() - self.update_time > animation_cooldown:
			self.update_time = pygame.time.get_ticks()
			self.frame_index += 1
		#if the animation has run out the reset back to the start
		if self.frame_index >= len(self.animation_list[self.action]):
			self.frame_index = 0


	def draw(self):
		screen.blit(self.image, self.rect)


alucard = Fighter(200, 275, 'Alucard', 30, 10, 3)
#demon1 = Fighter(550, 270, 'Demon', 20, 6, 1)
#demon2 = Fighter(690, 200, 'Demon', 20, 6, 2)
warg = Fighter(550, 250, 'Warg', 40, 7, 1)

demon_list = []
demon_list.append(warg)
#demon_list.append(demon2)

run = True 
while run: 
	clock.tick(fps)

	#draw background
	draw_bg()

	#draw panel
	draw_panel()

	#draw fighters
	alucard.update()
	alucard.draw()

	for demon in demon_list:
		demon.update()
		demon.draw()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()