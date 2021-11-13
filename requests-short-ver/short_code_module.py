from urllib3.util.timeout import Timeout as TimeoutSauce
from urllib3.poolmanager import PoolManager
from timeit import default_timer as dt
from urllib3.util.retry import Retry

CONST_CONNECTIONS = 10
CONST_MAXSIZE = 10
CONST_BLOCK = False
CONST_POOL_KWARGS = {}

CONST_REQUEST_INFO_TIMEOUT = None

REQUEST_URL = 'http://127.0.0.1:5000/'

RETRY_TOTAL = 0
RETRY_READ = False

class request:
    def __init__(self) -> None:
        poolmanager = PoolManager(
            num_pools=CONST_CONNECTIONS,
            maxsize=CONST_MAXSIZE,
            block=CONST_BLOCK,
            **CONST_POOL_KWARGS,
        )
        conn = poolmanager.connection_from_url(REQUEST_URL)
        self.resp = conn.urlopen(
            method = 'GET',
            url = '/',
            body = None,
            headers = {'User-Agent': 'python-requests/2.25.1', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'},
            redirect = False,
            assert_same_host = False,
            preload_content=False,
            decode_content=False,
            retries=Retry(
                RETRY_TOTAL,
                read=RETRY_READ,
            ),
            timeout=TimeoutSauce(
                connect=CONST_REQUEST_INFO_TIMEOUT,
                read=CONST_REQUEST_INFO_TIMEOUT
            )

        )

    @property
    def content(self):
        return b''.join(self.read())

    def read(self):
        content = b''
        while True:
            chunk = self.resp.read(10 * 1024)
            if not chunk:
                break
            yield chunk

time = dt()

for i in range(1,10000):
    request().content

print(dt() - time)
