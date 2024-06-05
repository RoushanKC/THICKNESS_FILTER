import zmq
import typing
import logging
import time

logging.basicConfig(level=logging.DEBUG)

class Connection:
    def __init__(self ,host:str ,port:int):
        self.sock=zmq.Context().socket(zmq.SUB)
        self.sock.connect(f'tcp://{host}:{port}')
        self.sock.setsockopt(zmq.SUBSCRIBE ,'THICKNESS_ARRAY'.encode('utf-8'))
        self.push_sock=zmq.Context().socket(zmq.PUSH)
        self.push_sock.connect('tcp://127.0.0.1:4000')
    def run(self):
        try:
            while True:
                msg=self.sock.recv_json(1)
                self.push_sock.send_json(msg)
                logging.info(f'{msg}')
        except Exception as e:
            logging.exception(f'Connection : error :{time.time()} : {e}')
def main():
    con=Connection('127.0.0.1' ,3000)
    try:
        con.run()
    except KeyboardInterrupt:
        logging.info(f'connection discontinued...')

if __name__=='__main__':
    main()


                

                 


