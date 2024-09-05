import os
import sys
import time

def main():
    print("A")
    time.sleep(3)

    pid = os.fork()

    if pid < 0:
        sys.exit("Error al crear el primer proceso.")

    if pid > 0:  #   1
        print("B")
        time.sleep(3)
        pid = os.fork()

        if pid > 0:  #   2
            print("C")
            time.sleep(3)
            pid = os.fork()

            if pid > 0:  #   3
                print("E")
                time.sleep(3)
                pid = os.fork()

                if pid > 0:  #   4
                    print("H")
                    time.sleep(3)
                    
                    os.wait()  
                else:  #   4
                    print("I")
                    time.sleep(3)
                    
                    os._exit(os.EX_OK)
            else:  #   3
                os._exit(os.EX_OK)
            
            os.wait()
        else:   #   2
            print("D")
            time.sleep(3)
            pid = os.fork()

            if pid > 0:  #   5
                print("F")
                time.sleep(3)
                
                os.wait()  
            else:   #   5
                print("G")
                time.sleep(3)
                
                os._exit(os.EX_OK)
            
            os._exit(os.EX_OK)
    # no hacemos os.wait() ya que el proceso hijo no hace nada
    else:  #   1
        os._exit(os.EX_OK) # Retornamos aunque no hallamos hecho os.wait()

if __name__ == "__main__":
    main()
