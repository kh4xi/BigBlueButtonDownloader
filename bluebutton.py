from funcs import *

if __name__ == "__main__":
    # Validating Folders
    folder_integrity()
    log_time = datetime.now()
    current_time = log_time.strftime("%H:%M:%S")
    term_clear()
    print(MyColors.g_colr + current_time)
    url = input("Please enter the full url : ")
    try:
        response = requests.get(url)
        if not response.status_code == 200:
            raise requests.exceptions.ConnectionError()
    except (requests.exceptions.ConnectionError(), requests.exceptions.ConnectTimeout):
        print(MyColors.r_color, "Connection is not Stable")
    term_clear()
    # Split and Rejoin
    split_Url = url.split('/')[-1]
    base_Url = url.rsplit('/', 4)[0]
    parsed_Url = base_Url + '/presentation/' + split_Url

    # Start downloading
    print(MyColors.g_colr, current_time)
    print("Link : " + parsed_Url)
    print(MyColors.y_colr, "\n\t Downloading audio file... Please wait")
    webcams(parsed_Url)
    print(MyColors.g_colr, "\n\t File has been downloaded")

    print(MyColors.y_colr, "\n\t Downloading screen record file... Please wait")
    desk_share(parsed_Url)
    print(MyColors.g_colr, "\n\t File has been downloaded")
    term_clear()
    print(MyColors.y_colr, "\t Rendering media it will take a while ... Please wait")
    mix_clips()

    term_clear()
    print("\n Cleaning Temporary Files")
    clean_raw()

    print(MyColors.g_colr, current_time)
    print(MyColors.g_colr, "\n File has been rendered to output folder")
