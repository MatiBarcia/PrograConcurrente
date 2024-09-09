import os
import sys
import time

def main():
    print(f"PID: {os.getpid()} PPID: {os.getppid()} Letra: A")
    time.sleep(5)

    pid = os.fork()

    if pid < 0:
        sys.exit("Error al crear el primer proceso.")

    if pid > 0:  #   1
        print(f"PID: {os.getpid()} PPID: {os.getppid()} Letra: B")
        time.sleep(5)
        pid = os.fork()

        if pid > 0:  #   2
            print(f"PID: {os.getpid()} PPID: {os.getppid()} Letra: C")
            time.sleep(5)
            pid = os.fork()

            if pid > 0:  #   3
                print(f"PID: {os.getpid()} PPID: {os.getppid()} Letra: E")
                time.sleep(5)
                pid = os.fork()

                if pid > 0:  #   4
                    print(f"PID: {os.getpid()} PPID: {os.getppid()} Letra: H")
                    time.sleep(5)
                    
                    os.wait()  
                else:  #   4
                    print(f"PID: {os.getpid()} PPID: {os.getppid()} Letra: I")
                    time.sleep(5)
                    
                    os._exit(os.EX_OK)
            else:  #   3
                os._exit(os.EX_OK)
            
            os.wait()
        else:   #   2
            print(f"PID: {os.getpid()} PPID: {os.getppid()} Letra: D")
            time.sleep(5)
            pid = os.fork()

            if pid > 0:  #   5
                print(f"PID: {os.getpid()} PPID: {os.getppid()} Letra: F")
                time.sleep(5)
                
                os.wait()  
            else:   #   5
                print(f"PID: {os.getpid()} PPID: {os.getppid()} Letra: G")
                time.sleep(5)
                
                os._exit(os.EX_OK)
            
            os._exit(os.EX_OK)
    # no hacemos os.wait() ya que el proceso hijo no hace nada
    else:  #   1
        os._exit(os.EX_OK) # Retornamos aunque no hallamos hecho os.wait()

if __name__ == "__main__":
    main()
