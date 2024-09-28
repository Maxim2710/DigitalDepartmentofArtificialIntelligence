def extensions_switcher(extension):
    if not hasattr(extensions_switcher, 'handlers'):
        extensions_switcher.handlers = {}

    def decorator(func):
        extensions_switcher.handlers[extension] = func

        def wrapper(filename):
            file_extension = filename.split('.')[-1]

            if file_extension in extensions_switcher.handlers:
                return extensions_switcher.handlers[file_extension](filename)
            else:
                return 'unsupported extension'

        return wrapper

    return decorator


@extensions_switcher('jpeg')
def open_image(filename):
    return 'open jpeg file'


@extensions_switcher('png')
def open_image(filename):
    return 'open png file'


@extensions_switcher('gif')
def open_image(filename):
    return 'open gif file'


files = input().split()

for file in files:
    print(open_image(file))
