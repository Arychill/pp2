import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.playing = False
        self.paused = False
        self.current_track_index = 0
        self.tracks = self.load_tracks()

    def load_tracks(self):
        # Change this directory to the directory where your music files are stored
        music_directory = "/Users/argynmoldabek/Desktop/songs"
        tracks = [os.path.join(music_directory, file) for file in os.listdir(music_directory) if file.endswith((".mp3", ".wav"))]
        return tracks

    def play(self):
        if not self.playing:
            pygame.mixer.music.load(self.tracks[self.current_track_index])
            pygame.mixer.music.play()
            self.playing = True
            self.paused = False

    def pause(self):
        if self.playing and not self.paused:
            pygame.mixer.music.pause()
            self.paused = True

    def unpause(self):
        if self.playing and self.paused:
            pygame.mixer.music.unpause()
            self.paused = False

    def stop(self):
        if self.playing:
            pygame.mixer.music.stop()
            self.playing = False
            self.paused = False

    def next_track(self):
        self.stop()
        self.current_track_index = (self.current_track_index + 1) % len(self.tracks)
        self.play()

    def previous_track(self):
        self.stop()
        self.current_track_index = (self.current_track_index - 1) % len(self.tracks)
        self.play()

    def handle_key_press(self, key):
        if key == pygame.K_SPACE:
            if self.playing and not self.paused:
                self.pause()
            elif self.paused:
                self.unpause()
            else:
                self.play()
        elif key == pygame.K_n:
            self.next_track()
        elif key == pygame.K_p:
            self.previous_track()
        elif key == pygame.K_s:
            self.stop()

def main():
    player = MusicPlayer()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Set running to False to exit the loop and close the program
            elif event.type == pygame.KEYDOWN:
                player.handle_key_press(event.key)

    pygame.quit()  # Quit pygame when the loop exits

if __name__ == "__main__":
    main()
