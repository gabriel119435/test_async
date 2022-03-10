import time,logging,threading

logging.basicConfig(level = logging.INFO,format='%(asctime)s %(levelname)s - %(message)s')

def thread_id():
    return str(threading.get_ident())[-5:]

class NewClass:
    def wait_from_newclass(self, info):
        logging.info(f'{info} thread {thread_id()} instance {str(id(self))[-5:]} waiting')
        time.sleep(3)