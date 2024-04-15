import os
import unreal
# Function to create a flipbook from textures
def create_flipbook_from_textures(textures, destination_directory, flipbook_name):
    # Ensure there are textures to process
    if not textures:
        print("No textures provided.")
        return

    # Create a new flipbook asset
    flipbook_factory = unreal.PaperFlipbookFactory()
    created_flipbook = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
        flipbook_name, destination_directory, unreal.PaperFlipbook, flipbook_factory)

    # Ensure the flipbook was created
    if not created_flipbook:
        print("Failed to create PaperFlipbook asset.")
        return

    # Initialize a list to hold key frames
    key_frames = []

    for i, texture in enumerate(textures):
        # Create a new sprite for each texture
        sprite_factory = unreal.PaperSpriteFactory()
        sprite_name = "Sprite_{}".format(i)
        sprite = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
            sprite_name, destination_directory, unreal.PaperSprite, sprite_factory)

        # Set the source texture of the sprite
        if sprite:
            sprite.set_editor_property('SourceTexture', texture)
            
            # Create a key frame for the sprite
            frame = unreal.PaperFlipbookKeyFrame()
            frame.sprite = sprite
            frame.frame_run = 1
            key_frames.append(frame)

    # Check if key frames were added
    if not key_frames:
        print("No key frames were created.")
        return

    # Set the key frames to the flipbook
    created_flipbook.set_editor_property('KeyFrames', key_frames)

    # Save the flipbook asset
    flipbook_path = "{}/{}".format(destination_directory, flipbook_name)
    if unreal.EditorAssetLibrary.save_asset(flipbook_path):
        print("Flipbook saved successfully.")
    else:
        print("Failed to save the flipbook.")

# specify the directory where your PNGs are stored
source_directory = r"C:\Users\PC\Downloads\语音识别\听"

# specify the destination directory within Unreal where you want to import the PNGs
destination_directory = "/Game/Textures"
flipbook_path ="/Game/Flipbook"
# get a list of all PNG files in the source directory
all_files = os.listdir(source_directory)

# filter to get only PNG files
png_files = [file for file in all_files if file.endswith(".png")]

# sort the files in case they are not in order
png_files.sort()

# import each PNG file
textures = []
for png_file in png_files:
    # construct the full file path
    full_file_path = source_directory + "/" + png_file

    # construct the destination path
    destination_path = destination_directory + "/" + png_file[:-4]  # remove the ".png" from the file name

    # import the PNG file
    texture_task = unreal.AssetImportTask()
    texture_task.automated = True
    texture_task.replace_existing = True
    texture_task.filename = full_file_path
    texture_task.destination_name = destination_path
    texture_task.destination_path = destination_directory
    texture_task.save = True

    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([texture_task])

    # add the imported texture to the list
    imported_texture = unreal.find_asset(destination_path)
    if imported_texture is not None:
        textures.append(imported_texture)

flipbook_name='flipbook_name'
create_flipbook_from_textures(textures, destination_directory, flipbook_name)



# # create a flipbook from the imported textures
# flipbook = unreal.PaperFlipbook()
# flipbook_factory = unreal.PaperFlipbookFactory()

# # Create a new flipbook asset in the destination directory
# created_flipbook = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
#     "MyFlipbook",  # Name of the new asset
#     destination_directory,  # Path where the asset will be created
#     unreal.PaperFlipbook,  # Class type of the asset to create
#     flipbook_factory  # The factory to use for creating the asset
# )

# # Make sure the flipbook was created successfully
# if created_flipbook:
#     # Collect key frames for the flipbook
#     key_frames = []

#     for i, texture in enumerate(textures):
#         # Create a new sprite asset for each texture
#         sprite_factory = unreal.PaperSpriteFactory()
#         sprite_name = "Sprite_{}".format(i)
#         sprite = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
#             sprite_name,  # Name of the new asset
#             destination_directory,  # Path where the asset will be created
#             unreal.PaperSprite,  # Class type of the asset to create
#             sprite_factory  # The factory to use for creating the asset
#         )

#         # Set the source texture property of the sprite
#         if sprite:
#             sprite.set_editor_property('SourceTexture', texture)

#             # Create a new key frame
#             frame = unreal.PaperFlipbookKeyFrame()
#             frame.sprite = sprite
#             frame.frame_run = 1

#             # Add the key frame to the list
#             key_frames.append(frame)

#     # Set the key frames to the flipbook
#     created_flipbook.set_editor_property('KeyFrames', key_frames)

#     # Save the flipbook asset
#     unreal.EditorAssetLibrary.save_asset(flipbook_path, created_flipbook)
# else:
#     print("Failed to create PaperFlipbook asset.")

