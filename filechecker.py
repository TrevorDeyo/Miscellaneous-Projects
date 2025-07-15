import filetype

kind = filetype.guess("REPLACE ME!")
if kind is None:
    print('Cannot guess file type!')
    return
print('File extension:', kind.extension)
print('File MIME type:', kind.mime)
