import operator
import os

user_path = input("user_path: ")
excluded_user_paths = list(input("excluded_user_paths: ").split(","))

main_folders_paths = list(
    map(
        lambda element: os.path.join(user_path, element),
        list(
            filter(
                lambda element: os.path.isdir(os.path.join(user_path, element)),
                os.listdir(user_path),
            )
        ),
    )
)

folders_names_and_sizes = list()

for main_folder_path in main_folders_paths:
    if main_folder_path in excluded_user_paths:
        print(main_folder_path + " skipped")
    else:
        folder_size = 0
        for path, folder_names, file_names in os.walk(main_folder_path):
            for file_name in file_names:
                file_path = os.path.join(path, file_name)
                if not os.path.islink(file_path):  # skip symbolic links
                    folder_size += os.path.getsize(file_path)

        if folder_size > 10**8:  # skip folders with less than 100mb
            folders_names_and_sizes.append((main_folder_path, folder_size))
        print(main_folder_path + " processed")


folders_names_and_sizes.sort(key=operator.itemgetter(1), reverse=True)

for folder_name_and_size in folders_names_and_sizes:
    print(folder_name_and_size)
