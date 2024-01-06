def log_message(msg):
    with open("filename.txt", "a+") as log_file:
        log_file.write("{0}\n".format(msg))


log_message("I create a file and I am writing into in")
