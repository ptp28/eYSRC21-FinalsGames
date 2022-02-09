import sys
import os
import validators
import wget
import requests
from zipfile import ZipFile


ASSETS_PATH = './Assets/'
ASSETS_URL = 'https://github.com/ptp28/eYSRC21-FinalsGames/blob/Assets/12_Assets.zip?raw=true'

def extract(filename):
    # opening the zip file in READ mode
    try:
        with ZipFile(filename, 'r') as zip:
            # extracting all the files
            zip.extractall()
            return zip.filelist[0].filename
    except Exception as e:
        raise Exception("!!! ERROR EXTRACTING ARCHIVE !!!\n" + str(e))


def download_file(url):
    try:
        if not validators.url(url):
            raise ValueError('!!! INVALID URL !!!')
        file_name = wget.download(url)
        return file_name
    except requests.exceptions.HTTPError:
        raise Exception("!!! HTTP ERROR !!!")
    except requests.exceptions.ConnectionError:
        raise Exception("!!! ERROR CONNECTING !!!")
    except requests.exceptions.Timeout:
        raise Exception("!!! TIMEOUT ERROR !!!")
    except (requests.ConnectionError, requests.Timeout):
        raise Exception("!!! NO INTERNET CONNECTION !!!")
    except Exception:
        raise Exception("!!! DOWNLOAD ERROR !!!")


if __name__ == "__main__":
    # Try to run game twice
    i = 0
    while i <= 1: 
        i += 1
        isdir = os.path.isdir(ASSETS_PATH) 
        if isdir:
            print("Loading game...")
            import main
            i += 1
        else:
            print("Downloading assets...")
            try:
                downloaded_file = download_file(ASSETS_URL)
            except Exception as e:
                print("Error downloading assets :(")
                sys.exit()
            else:
                print("\nDownload complete  :)\n")

            try:
                print('\nExtracting files ... ')
                extraction_dir = extract(downloaded_file)
                print("Extraction complete")
            except Exception as e:
                os.remove(downloaded_file)
                sys.exit()
        

        
