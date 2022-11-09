from os import path
from sys import argv
import requests
from tempfile import gettempdir
import mimetypes


def streaming_download_file(url, file_path_without_extension):
    """
    Downloads `url` to the OS's temporary directory, named with the
    given file path
    """
    r = requests.get(url, stream=True)

    if not r.ok:
        print("Beep boop I couldn't download",
              file_path_without_extension, "at", url)

    mime = r.headers['content-type']

    extension = mimetypes.guess_extension(mime)

    filename = file_path_without_extension + extension

    print('Downloading: ', filename)

    with open(filename, 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)

    return filename


if __name__ == '__main__':
    url = argv[1]
    filepath = argv[2]

    print(f'Downloading URL {url} to {filepath}')
    download_path = streaming_download_file(url, filepath)
    print(f'Downloaded to {download_path}')
