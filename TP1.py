import os
import sys
import time

def main():
    print("A")
    time.sleep(5)

    pid = os.fork()
    
    if pid < 0:
        sys.exit("Error al crear el primer proceso.")

    if pid:
        print("B")
        pid = os.fork()

        if pid:
            print("C")
            time.sleep(5)
            pid = os.fork()

            if pid:
                print("E")
                time.sleep(5)
                pid = os.fork()

                if pid:
                    print("H")
                    time.sleep(5)
                else:
                    print("I")
                    time.sleep(5)
            else:
                pass

        else:
            print("D")
            time.sleep(5)
            pid = os.fork()

            if pid:
                print("F")
                time.sleep(5)
            else:
                print("G")
                time.sleep(5)
    else:
        pass

if __name__ == "__main__":
    main()