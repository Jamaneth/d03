from local_lib import path

def file_writer(my_path, document_name):
    my_folder = path.Path(my_path)
    try:
        my_folder.mkdir()
    except FileExistsError:
        pass

    my_document = my_folder / document_name
    my_text = 'Success!'
    my_document.write_text(my_text)
    my_document.touch()

def file_reader(my_path, document_name):
    my_folder = path.Path(my_path)
    my_document = my_folder / document_name
    my_text = my_document.text()
    print(my_text)

if __name__ == '__main__':
    my_path = './my_folder'
    document_name = 'my_document.txt'
    file_writer(my_path, document_name)
    file_reader(my_path, document_name)
