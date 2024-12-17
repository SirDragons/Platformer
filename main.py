import pygame

pygame.init()

clock = pygame.time.Clock()
fps = 60

run = True
tile_size = 100
screen_width = 1500
screen_height = 950

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')

bg = pygame.image.load('Platformer_bg.png').convert_alpha()
bg = pygame.transform.scale(bg, (screen_width, screen_height))
blob_group = pygame.sprite.Group()
portal_group = pygame.sprite.Group()

class World:
	def __init__(self, data):
		self.tile_list = []
		grass_img = pygame.image.load('Grass.png').convert_alpha()
		ground_imgs = pygame.image.load('Ground_sheet.png').convert_alpha()
		ground_img2 = ground_imgs.subsurface(232, 124, 50, 50)
		ground_img3 = ground_imgs.subsurface(9, 124, 50, 50)
		ground_img4 = ground_imgs.subsurface(121, 179, 50, 50)
		ground_img5 = ground_imgs.subsurface(64, 179, 50, 50)
		ground_img6 = ground_imgs.subsurface(176, 179, 50, 50)
		ground_img7 = ground_imgs.subsurface(121, 233, 50, 50)
		ground_img11 = ground_imgs.subsurface(64, 68, 50, 50)
		ground_img20 = ground_imgs.subsurface(121, 68, 50, 50)
		ground_img21 = ground_imgs.subsurface(9, 68, 50, 50)
		ground_img22 = ground_imgs.subsurface(64, 124, 50, 50)
		ground_img23 = ground_imgs.subsurface(64, 12, 50, 50)
		ground_img24 = ground_imgs.subsurface(9, 12, 50, 50)
		ground_img25 = ground_imgs.subsurface(176, 124, 50, 50)
		ground_img26 = ground_imgs.subsurface(176, 12, 50, 50)
		ground_img31 = ground_imgs.subsurface(232, 12, 50, 50)
		ground_img32 = ground_imgs.subsurface(232, 68, 50, 50)
		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:
				if tile == 1:
					img = pygame.transform.scale(grass_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 2:
					img = pygame.transform.scale(ground_img2, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 3:
					img = pygame.transform.scale(ground_img3, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 4:
					img = pygame.transform.scale(ground_img4, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size - 12
					img_rect = img_rect.inflate(0, -24)
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 5:
					img = pygame.transform.scale(ground_img5, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size - 12
					img_rect = img_rect.inflate(0, -24)
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 6:
					img = pygame.transform.scale(ground_img6, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size - 12
					img_rect = img_rect.inflate(0, -24)
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 7:
					img = pygame.transform.scale(ground_img7, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					img_rect = img_rect.inflate(0, -40)
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 9:
					portal = Portal(col_count * tile_size, row_count * tile_size)
					portal_group.add(portal)
				if tile == 11:
					img = pygame.transform.scale(ground_img11, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 20:
					img = pygame.transform.scale(ground_img20, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 21:
					img = pygame.transform.scale(ground_img21, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 22:
					img = pygame.transform.scale(ground_img22, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 23:
					img = pygame.transform.scale(ground_img23, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 24:
					img = pygame.transform.scale(ground_img24, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 25:
					img = pygame.transform.scale(ground_img25, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 26:
					img = pygame.transform.scale(ground_img26, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 30:
					blob = Enemy(col_count * tile_size, row_count * tile_size + 65)
					blob_group.add(blob)
				if tile == 31:
					img = pygame.transform.scale(ground_img31, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					img_rect = img_rect.inflate(0, -50)
					tile = (img, img_rect, 'Water')
					self.tile_list.append(tile)
				if tile == 32:
					img = pygame.transform.scale(ground_img32, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect, 'Water')
					self.tile_list.append(tile)
				
				col_count += 1
			row_count += 1
	
	def draw(self):
		for tile in self.tile_list:
			screen.blit(tile[0], tile[1])
			# pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)

class Player:
	def __init__(self, x, y):
		self.images_right = []
		self.images_left = []
		self.index = 0
		self.counter = 0
		for num in range(1, 5):
			img_right = pygame.image.load(f'guy{num}.png').convert_alpha()
			img_right = pygame.transform.scale(img_right, (60, 120))
			img_left = pygame.transform.flip(img_right, True, False)
			self.images_right.append(img_right)
			self.images_left.append(img_left)
		self.image = self.images_right[self.index]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.vel_y = 0
		self.jumped = False
		self.can_jump = True
		self.empty = False
		self.direction = 0
	
	def update(self):
		global run
		dx = 0
		dy = 0
		walk_cooldown = 10
		pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
		key = pygame.key.get_pressed()
		if key[pygame.K_a] or key[pygame.K_LEFT]:
			self.counter += 1
			self.direction = -1
			dx -= 7
		if key[pygame.K_d] or key[pygame.K_RIGHT]:
			self.counter += 1
			self.direction = 1
			dx += 7
		if key[pygame.K_SPACE] and not self.jumped and self.can_jump:
			self.vel_y = -17
			self.jumped = True
			self.can_jump = False
		if not key[pygame.K_SPACE]:
			self.jumped = False
		if not key[pygame.K_a] and not key[pygame.K_d] and not key[pygame.K_RIGHT] and not key[pygame.K_LEFT]:
			self.counter = 0
			self.index = 0
			if self.direction == 1:
				self.image = self.images_right[self.index]
			if self.direction == -1:
				self.image = self.images_left[self.index]
		
		if self.counter > walk_cooldown:
			self.counter = 0
			self.index += 1
			if self.index >= len(self.images_right):
				self.index = 0
			if self.direction == 1:
				self.image = self.images_right[self.index]
			if self.direction == -1:
				self.image = self.images_left[self.index]
		
		self.vel_y += 1
		if self.vel_y > 10:
			self.vel_y = 10
		dy += self.vel_y
		
		for tile in world.tile_list:
			if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
				dx = 0
			if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
				if 'Water' in tile:
					self.empty = True
				if self.vel_y < 0:
					dy = tile[1].bottom - self.rect.top
					self.vel_y = 0
				elif self.vel_y >= 0 and not self.empty:
					dy = tile[1].top - self.rect.bottom
					self.vel_y = 0
					self.can_jump = True
		
		if pygame.sprite.spritecollide(self, blob_group, False):
			print('dead')
		if pygame.sprite.spritecollide(self, portal_group, False):
			print('dead')
		if self.rect.bottom > screen_height + 100:
			print('dead')
			run = False
		
		self.rect.x += dx
		self.rect.y += dy
		
		screen.blit(self.image, self.rect)

class Enemy(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('blob.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.move_speed = 5
		self.move_direction = self.move_speed
		self.move_counter = 0
	
	def update(self):
		self.rect.x += self.move_direction
		self.move_counter += self.move_speed
		if abs(self.move_counter) > 200:
			self.move_direction *= -1
			self.move_counter *= -1

class Portal(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		imgs = pygame.image.load('Portal.png').convert_alpha()
		portal = imgs.subsurface(12, 0, 225, 579)
		portal2 = imgs.subsurface(263, 0, 225, 592)
		portal3 = imgs.subsurface(513, 0, 225, 592)
		portal4 = imgs.subsurface(763, 0, 225, 592)
		self.portal = pygame.transform.scale(portal, (tile_size / 2, tile_size))
		self.portal2 = pygame.transform.scale(portal2, (tile_size / 2, tile_size))
		self.portal3 = pygame.transform.scale(portal3, (tile_size / 2, tile_size))
		self.portal4 = pygame.transform.scale(portal4, (tile_size / 2, tile_size))
		self.rect = self.portal.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.portals = []
		self.portals.append(self.portal)
		self.portals.append(self.portal2)
		self.portals.append(self.portal3)
		self.portals.append(self.portal4)
		self.counter = 0
		self.index = 1
		self.image = self.portals[self.index]
	
	def update(self):
		walk_cooldown = 10
		self.counter += 1
		if self.counter > walk_cooldown:
			self.counter = 0
			self.index += 1
			if self.index >= len(self.portals):
				self.index = 0
			self.image = self.portals[self.index]
			if self.image == self.portal:
				self.image = pygame.transform.scale(self.image, (tile_size / 2, tile_size))
			else:
				self.image = pygame.transform.scale(self.image, (tile_size / 2, tile_size + 2))
		
		screen.blit(self.image, self.rect)

world_data = [
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
	[0, 0, 0, 7, 0, 0, 0, 7, 0, 0, 7, 0, 0, 5, 6],
	[26, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[25, 24, 0, 0, 0, 0, 0, 0, 30, 0, 0, 0, 0, 0, 0],
	[20, 25, 2, 0, 0, 5, 4, 4, 4, 4, 4, 6, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 22],
	[0, 0, 0, 0, 0, 0, 30, 0, 0, 0, 0, 0, 21, 22, 20],
	[2, 3, 31, 2, 1, 1, 1, 1, 1, 3, 31, 31, 11, 20, 20],
	[20, 20, 32, 20, 20, 20, 20, 20, 20, 20, 32, 32, 11, 20, 20, 20]
]

world = World(world_data)
player = Player(100, screen_height - 200)


while run:
	clock.tick(fps)
	screen.blit(bg, (0, 0))
	
	world.draw()
	blob_group.update()
	blob_group.draw(screen)
	portal_group.update()
	player.update()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		
		pygame.display.update()

pygame.quit()
