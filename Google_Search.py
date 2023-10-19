from google_images_search import GoogleImagesSearch
API_KEY = "KEYS"
# you can provide API key and CX using arguments,
# or you can set environment variables: GCS_DEVELOPER_KEY, GCS_CX
gis = GoogleImagesSearch('AIzaSyDe9EjdP3iS59a_zQAx1mJyUyR42a9fkC0', 'f24c9039d68244b43')

# define search params
# option for commonly used search param are shown below for easy reference.
# For param marked with '##':
#   - Multiselect is currently not feasible. Choose ONE option only
#   - This param can also be omitted from _search_params if you do not wish to define any value
# this will search, download and resize:
#gis.search(search_params=_search_params, path_to_dir='/path/', width=500, height=500)

# search first, then download and resize afterwards


#This function will return substring
def GetSubString(open, close, str):

    ok = False
    ans = ""
    for i in str:
        if i == open:
            ok = True
        elif i == close:
            ok = False
        elif (ok):
            ans += i
    return ans

def DownloadImage(descr, name):
    _search_params = {
        'q': f'{descr.title()}',
        'num': 1,
        'fileType': 'jpg|gif|png',
        'imgSize': 'large',
    }
    gis.search(search_params=_search_params, path_to_dir='D:\Scripts\ToastmastersProject\Images',
               custom_image_name=str(name))
