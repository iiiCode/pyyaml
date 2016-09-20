from config import ProdConfig

def main():

    C = ProdConfig()

    if cmp(C.USER_NAME, "user") == 0 and cmp(C.PASSWORD, "123456") == 0:
        print "Success..."
    else:
        print "FAILED..."


if __name__ == "__main__":
    main()
