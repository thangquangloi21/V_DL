def getImageTypeFromName(fileName):
    print(fileName)
    fileType = ".bmp"
    new_name = fileName
    if fileName.endswith('.jpg'):
        fileType = ".jpg"
    elif fileName.endswith('.png'):
        fileType = ".png"
    elif fileName.endswith('.bmp'):
        fileType = ".bmp"
    elif fileName.endswith('.ico'):
        fileType = ".ico"
    elif fileName.endswith('.gif'):
        fileType = ".gif"
    elif fileName.endswith('.GIF'):
        fileType = ".GIF"
    elif fileName.endswith('.jpeg'):
        fileType = ".jpeg"
    else:
        fileType = ".bmp"
        new_name = fileName + ".bmp"

    return fileType, new_name