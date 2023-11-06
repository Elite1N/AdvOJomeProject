import os
import pygame


def load_images_from_folder(folder_path, no=""):
    #images = []
    filenames = []
    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')) and filename != no:
            #images.append(image)
            filenames.append(filename)
    return filenames

