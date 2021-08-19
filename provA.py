import os

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("nome progetto (no_space):")
    project_name = str(input())
    if project_name == "" :
        print("le virgolette sono il nulla")
    else:
        print("le virgonette non funzionano")

    print("Insert path to write whitout'/' ")
    path_write = str(input()) + "/cacca/"
    print(path_write)


