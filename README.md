# DSA Music Player

## Overview
This project is a music player application developed as part of the "Algorithms and Data Structures" course at Vietnam National University – HCM, International University, School of Computer Science and Engineering, Semester 2, 2023 - 2024.

## Table of Contents
1. [Introduction](#introduction)
   - [Motivation](#motivation)
   - [Technologies](#technologies)
   - [Launch](#launch)
2. [Project Details](#project-details)
   - [Rules](#rules)
   - [Design](#design)
   - [Others](#others)
3. [Data Structures and Algorithms Application](#data-structures-and-algorithms-application)
   - [Hash Table](#hash-table)
   - [Doubly Linked List](#doubly-linked-list)
4. [Conclusion](#conclusion)
5. [References](#references)

## Introduction

### Motivation
Developing a music player app offers the opportunity to combine technical skills with a passion for music, aiming to improve user experience through an intuitive, feature-rich, and personalized application. The project also serves as a learning experience in software engineering, multimedia integration, and potentially audio processing and machine learning.

### Technologies
- **Language**: Python
- **Libraries**:
  - Tkinter
  - Customtkinter
  - Threading
  - Time
  - Pygame
  - MP3
  - OS

### Launch
To run the application, execute the following code file: .\Final\Final_UI.py

## Project Details

### Rules
#### Objective
1. Add your favorite music from the song library and click the play button (“▶”). The first music in the playlist will be played. The current song will be illustrated at the bottom of the function buttons (next, play, previous). The progress bar will show the song's progress.
2. After the current song finishes, the next song in the playlist will be played. The application stops if there is no next song. Adding a new song after stopping will resume the current song, followed by the new song.

#### Setup
To add a new song to the library:
1. Add the song file in the format `title-artist.mp3` to the “Music” folder.
2. Access the `get_title_artist` method of the `MusicManager` class in the `Final_Manager.py` file.
3. Add the artist and title in the format `title-artist`.

#### General Controls
- **Search**: Type letters or words of the title or artist; results will be shown in the song library.
- **Add**: Add the song from the song library to the playlist.
- **Delete**: Delete the selected song from the playlist or library.
- **▶**: Play or pause the current song.
- **<**: Play the previous song; does not respond if on the first song.
- **>**: Play the next song; does not respond if on the last song.
- **Process Bar**: Illustrates the current song's progress.
- **List Box**: Shows the title and artist of the current song.

### Design
The user interface is designed to be basic yet functional, allowing users to manage and play their music easily.

![Application UI](figures/II.B.1.png)

### Others
The project includes a UML diagram to outline the structure and interactions within the application.

## Data Structures and Algorithms Application

### Hash Table
#### Purpose
The hash table is used in the `SongLibrary` class to efficiently manage songs by quickly adding, retrieving, and removing them.

#### Implementation Details
- **Hash Method**: Generates a hash value for a song ID, mapping it to an index within the hash table. Time complexity: O(1).
- **Add Song Method**: Adds a new song to the hash table. Average case time complexity: O(1); Worst case: O(n).
- **Remove Song Method**: Removes a song from the hash table by ID. Average case time complexity: O(1); Worst case: O(n).
- **Find Song Method**: Finds songs matching a title or artist and displays results. Average case time complexity: O(m + k); Worst case: O(m * n + k).
- **Get Song Method**: Finds and returns a song matching a title or artist. Average case time complexity: O(m + k); Worst case: O(m * n + k).
- **Display Songs in Listbox Method**: Populates a Tkinter Listbox widget with song titles and artists. Average case time complexity: O(n + m + log(k)); Worst case: O(n * m + log(k)).
- **Display Empty Listbox Method**: Displays an empty Listbox widget. Time complexity: O(n + log(k)).

### Doubly Linked List
(Section details truncated; please refer to the project report for complete information)

## Conclusion
### Achieved Goals
- Successfully developed a functional music player with a user-friendly interface.
- Efficiently managed songs using hash tables and other data structures.

### Limitations
- Some features could be further optimized for performance.

### Future Enhancements
- Integrating advanced features like audio processing and machine learning for personalized recommendations.

## References
For a detailed list of references, please refer to the project report.

## Repository
[GitHub Repository](https://github.com/Son-SDT/DSA-Music_Player)

