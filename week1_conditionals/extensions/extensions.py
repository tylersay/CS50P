def main():
    file_name = input("File name: ")

    check_extension(file_name)

def check_extension(file):
    file = file.strip().lower()
    if file.endswith(".gif"):
        print("image/gif")
    elif file.endswith(".jpg") or file.endswith(".jpeg"):
        print("image/jpeg")
    elif file.endswith(".png"):
        print("image/png")
    elif file.endswith(".pdf"):
        print("application/pdf")
    elif file.endswith(".txt"):
        print("text/plain")
    elif file.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")


main()