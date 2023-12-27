def file_parse(file_path, search_string):
    try:
        with open(file=file_path, mode="r") as log_file:
            p_file = log_file.read()
            for line in p_file:
                line = line.rstrip('\n')
                print(line)
    except FileNotFoundError:
        print("No such file found")
    except Exception as e:
        print(f"An error has occurred {e}")


file_parse(file_path="log.txt", search_string="nithin_kumar_nobroker_in")
