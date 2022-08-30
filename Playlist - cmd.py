import webbrowser

class Video:
	def __init__(self, title, link):
		self.title = title
		self.link = link
		self.seen = "Bạn chưa xem video này !"

	def open(self):
		webbrowser.open(self.link)
		self.seen = "Bạn đã xem video này rồi !"

class Playlist:
	def __init__(self, name, description, rating, videos):
		self.name = name
		self.description = description
		self.rating = rating
		self.videos = videos
		
def Enter_videos():
	total = int(input("Nhập số lượng video cần lưu trữ: "))
	videos = []
	for i in range(total):
		print('\n' + "Nhập thông tin của video", i+1)
		video = Enter_video()
		videos.append(video)
	return videos

def Enter_video():
	title = input("Nhập title: ")
	link = input("Nhập link: ")
	video = Video(title, link)
	return video

def Print_videos(videos):
	total = len(videos)
	for i in range(total):
		print('\n' + "----- Video", str(i+1) +" -----")
		Print_video(videos[i])

def Print_video(video):
	print("Title:", video.title)
	print("Link:", video.link)

def Write_videos_to_txt(videos, file):
	total = len(videos)
	# Chỉ ghi được string vào file text
	file.write(str(total) + '\n')
	for i in range(total):
		Write_video_to_txt(videos[i], file)

def Write_video_to_txt(video, file):
	file.write(video.title + '\n')
	file.write(video.link + '\n')

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

def Enter_playlists():
	total = int(input("Nhập số lượng Playlist cần lưu trữ: "))
	playlists = []
	for i in range (total):
		print("\n" + "Nhập thông tin Playlist", str(i+1))
		playlist = Enter_playlist()
		playlists.append(playlist)
	return playlists

def Enter_playlist():
	name = input("Nhập tên Playlist: ")
	description = input("Nhập mô tả: ")
	rating = input("Nhập đánh giá: ")
	videos = Enter_videos()
	playlist = Playlist(name, description, rating, videos)
	return playlist

def Print_playlists(playlists):
	total = len(playlists)
	for i in range(total):
		print("\n" + "_____Playlist" + str(i+1) + "_____")
		Print_playlist(playlists[i])

def Print_playlist(playlist):
	print("Name:", playlist.name)
	print("Description:", playlist.description)
	print("Rating:", playlist.rating)
	Print_videos(playlist.videos)

def Write_playlists_to_txt(playlists):
	total = len(playlists)
	with open("data.txt", "w") as file:
		file.write(str(total) + '\n')
		for i in range(total):
			Write_playlist_to_txt(playlists[i], file)
	print("\n" + "Write playlists to text successfully !!!")

def Write_playlist_to_txt(playlist, file):
	file.write(playlist.name + '\n')
	file.write(playlist.description + '\n')
	file.write(playlist.rating + '\n')
	Write_videos_to_txt(playlist.videos, file)

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

def show_menu():
	print("+------------+---------------------+")
	print("|   Option   |       Function      |")
	print("+------------+---------------------+")
	print("|  Option 1: |  Create playlists   |")
	print("|  Option 2: |  Show playlists     |")
	print("|  Option 3: |  Play a video       |")
	print("|  Option 4: |  Add a video        |")
	print("|  Option 5: |  Update a playlist  |")
	print("|  Option 6: |  Delete video       |")
	print("|  Option 7: |  Save and exit      |")
	print("+------------+---------------------+")

def require_int(prompt, min, max):
	select = input(prompt)
	# Hàm isdigit() có chức năng kiểm tra xem biến select có phải số hay không (số ở đây có thể là string or numberic đều được)
	while (not select.isdigit()) or (int(select) < min) or (int(select) > max):
		print("Bạn đã nhập sai ! Hãy nhập lại !")
		select = input(prompt)
	return int(select)

def Select_playlist(playlists, prompt):
	total = len(playlists)
	select = require_int(("Chọn {2} bạn cần sử dụng ({0}, {1}): ").format(1, total, prompt), 1, total)
	return int(select)

def Play_video(playlists):
	# Chọn playlist cần sử dụng
	select = Select_playlist(playlists, "playlists")
	playlist = playlists[select-1]
	total = len(playlist.videos)
	Print_videos(playlist.videos)
	# Chọn video cần sử dụng
	choice = Select_playlist(playlist.videos, "videos")
	video = playlist.videos[choice-1]
	print(video.seen)
	video.open() # Object video gọi thuộc tính trong hàm open

def Add_video(playlists):
	select = Select_playlist(playlists, "playlists")
	playlist = playlists[select-1]
	# Biến video này đã là 1 object
	print("Nhập thông tin video mới")
	video = Enter_video()
	(playlist.videos).append(video)
	# Trả về List videos đã được thêm video mới
	print("Đã thêm video thành công !!!")
	return playlists

def Update_playlist(playlists):
	select = Select_playlist(playlists, "playlists")
	playlist = playlists[select-1]
	print("Các thuộc tính có thể thay đổi được:")
	print("1. Name")
	print("2. Description")
	print("3. Rating")
	while True:
		choice = require_int("Bạn muốn thay đổi nội dung nào: ", 1, 3)
		if choice == 1:
			new_name = input("Nhập tên mới: ")
			playlist.name = new_name
		elif choice == 2:
			new_description = input("Nhập mô tả mới: ")
			playlist.description = new_description
		else:
			new_rating = input("Nhập đánh giá mới: ")
			playlist.rating = new_rating
		select = input("Bạn muốn thay đổi thêm nội dụng nào nữa không ? Yes or No: ")
		if (select == 'Yes') or (select == 'YES') or (select == 'yes'):
			continue
		elif (select == 'No') or (select == 'NO') or (select == 'no'):
			break
		else:
			break
	print("Đã update playlist thành công !!!")
	return playlists

def Delete_video(playlists):
	select = Select_playlist(playlists, "playlists")
	playlist = playlists[select-1]
	Print_videos(playlist.videos)
	print("Chọn video bạn cần xóa")
	choice = Select_playlist(playlist.videos, "videos")
	(playlist.videos).pop(choice-1)
	print("Video đã được xóa !!!")
	return playlists

def main():
	try:
		playlists = Read_txt_to_playlists()
		print("\n" + "Read text file successfully !!!")
	except:
		print("\n" + "Bạn là người dùng đầu tiên")

	while True:
		show_menu()
		select = require_int("Nhập lựa chọn của bạn: ", 1, 7)
		if select == 1: # Create a playlist
			playlists = Enter_playlists()
			input("Press Enter to continue ")
		else:
			try: 
				if select == 2: # Show a playlists
					Print_playlists(playlists)
					input("Press Enter to continue ")
				elif select == 3: # Play a video
					Play_video(playlists)
					input("Press Enter to continue ")
				elif select == 4: # Add a video
					playlists = Add_video(playlists)
					input("Press Enter to continue ")
				elif select == 5: # Update playlist
					playlists = Update_playlist(playlists)
					input("Press Enter to continue ")
				elif select == 6: # Delete a video
					playlists = Delete_video(playlists)
					input("Press Enter to continue ")
				else: # Save and exit
					Write_playlists_to_txt(playlists)
					break
			except:
				print("File thông tin của bạn đang trống hay tạo 1 playlists mới !")
				input("Press Enter to continue ")
	
main()