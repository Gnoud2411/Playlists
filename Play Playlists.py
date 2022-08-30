# Chương trình này chỉ đọc file và xuất lên GUI chứ không yêu cầu User nhập thông tin
import pygame
import webbrowser
from pygame.locals import *

class Video:
	def __init__(self, title, link):
		self.title = title
		self.link = link

	def open(self):
		webbrowser.open(self.link)

class Playlist:
	def __init__(self, name, description, rating, videos):
		self.name = name
		self.description = description
		self.rating = rating
		self.videos = videos

class TextButton:
	def __init__(self, text, position):
		self.text = text
		self.position = position

	def draw(self):
		Font = pygame.font.SysFont('sans', 30)
		Text_render = Font.render(self.text, True, BLACK)
		self.Text_box = Text_render.get_rect()
		# Kiểm tra xem chuột đã nằm trong vùng của text chưa
		if self.is_mouse_on_text():
			Text_render = Font.render(self.text, True, BLUE)
			# Thêm dấu gạch dưới Text
			pygame.draw.line(screen, BLUE, (self.position[0], self.position[1] + self.Text_box[3]), (self.position[0] + self.Text_box[2], self.position[1] + self.Text_box[3]))
		# Xuất text lên màn hình
		screen.blit(Text_render, (self.position[0], self.position[1]))	

	def is_mouse_on_text(self):
		mouse_x, mouse_y = pygame.mouse.get_pos()
		if (self.position[0] < mouse_x < (self.position[0] + self.Text_box[2])) and (self.position[1] < mouse_y < (self.position[1] + self.Text_box[3])):
			return True
		return False

def Read_txt_to_playlists():
	playlists = []
	with open("data.txt") as file:
		total = int(file.readline().strip())
		for i in range(total):
			playlist = Read_txt_to_playlist(file)
			playlists.append(playlist)
	return playlists

def Read_txt_to_playlist(file):
	name = file.readline().strip()
	description = file.readline().strip()
	rating = file.readline().strip()
	videos = Read_txt_to_videos(file)
	playlist = Playlist(name, description, rating, videos)
	return playlist

def Read_txt_to_videos(file):
	total = int(file.readline().strip())
	videos = []
	for i in range(total):
		video = Read_txt_to_video(file)
		videos.append(video)
	return videos

def Read_txt_to_video(file):
	title = file.readline().strip()
	link = file.readline().strip()
	video = Video(title, link)
	return video

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Playlists')
clock = pygame.time.Clock()
running = True
BLACK = (0, 0, 0)
BLUE = (0,0,225)

playlists = Read_txt_to_playlists()

add = 75
videos_btn_list = []
playlist_name_btn = []
for i in range(len(playlists)):
	playlist_btn = TextButton(playlists[i].name, (50, 50 + add*i))
	playlist_name_btn.append(playlist_btn)

while running:
	clock.tick(120)
	screen.fill((255, 255, 255))

	for i in range(len(playlist_name_btn)):
		playlist_name_btn[i].draw()
		
	for i in range(len(videos_btn_list)):
		videos_btn_list[i].draw()

	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN: # Câu lệnh if này kiểm tra thao tác chuột
			if event.button == 1:	# 1: click chuột phải
				for i in range(len(playlist_name_btn)):
					if playlist_name_btn[i].is_mouse_on_text():
						videos_btn_list = []
						# Lưu lại playlist đã chọn
						playlist = playlists[i]
						for j in range(len(playlist.videos)):
							video_btn = TextButton("{0}. {1}".format(str(j+1), playlist.videos[j].title), (300, 50 + add*j))
							videos_btn_list.append(video_btn)
				
				# Vòng lặp này có tác dụng để play video
				for z in range(len(videos_btn_list)):
					if videos_btn_list[z].is_mouse_on_text():
						playlist.videos[z].open()

		if event.type == pygame.QUIT:
			running = False

	pygame.display.flip()

pygame.quit()