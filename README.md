# Python3 requests module analysis

## requests 모듈이란?


간단하게 requests 모듈은 HTTP REQUEST / RESPONSE 기능을 사용할 수 있는 모듈입니다.

예시로 HTTP/1.1버전의 경우 GET, PUT, POST, HEAD, OPTIONS 등 다양한 HTTP 메서드로 요청이 가능하며 파일 업로드, 매크로 등 다양한 기능에 사용되는 모듈이기도 합니다.

#### References

+ [requests Github](https://github.com/psf/requests)
+ [requests Documentation](https://docs.python-requests.org/en/master/)

### requests module install

---

```bash
~$ pip install requests
~$ pip3 install requests

~$ python3
Python 3.8.10 (default, Jun  2 2021, 10:49:15)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>>
```

### requests REQUEST Code Example

---

```py
import requests

r = requests.get("http://httpbin.org")
print(r.status_code)
print(r.reason)
```

requests 모듈은 이와 같이 짧은 코드로도 요청을 보낼 수 있는 장점이 존재합니다.

만약 put, post, head 등 다양한 메서드로 요청해야되는 경우 requests 모듈 앞에 .method를 추가하여 실행시키면 됩니다.

```py
import requests

get = requests.get
post = requests.post
put = requests.put
head = requests.head
```

---

## requests 모듈 분석

먼저 requests 모듈의 파일 구조는 이렇게 구성되어 있습니다.

```
requests
   ├── __version__.py    
   ├── _internal_utils.py
   ├── adapters.py
   ├── api.py
   ├── auth.py
   ├── certs.py
   ├── compat.py
   ├── cookies.py
   ├── exceptions.py
   ├── help.py
   ├── hooks.py
   ├── models.py
   ├── packages.py
   ├── sessions.py
   ├── status_codes.py
   ├── structures.py
   └── utils.py
```

+ `\_\_version__`

    requests 모듈에 관한 버전과 requests 문서 링크 등 다양한 정보가 있는 파일입니다.

    ```py
    __title__ = 'requests'
    __description__ = 'Python HTTP for Humans.'
    __url__ = 'https://requests.readthedocs.io'
    __version__ = '2.25.1'
    __build__ = 0x022501
    __author__ = 'Kenneth Reitz'
    __author_email__ = 'me@kennethreitz.org'
    __license__ = 'Apache 2.0'
    __copyright__ = 'Copyright 2020 Kenneth Reitz'
    __cake__ = u'\u2728 \U0001f370 \u2728'
    ```

+ `_internal_utils.py`

    _internal_utils.py은 유니코드 문자열 ascii 문자 체크,  ascii 인코딩 정도의 유틸리티 기능을 제공하는 파일입니다.

    ```
    requests._internal_utils
    ~~~~~~~~~~~~~~

    Provides utility functions that are consumed internally by Requests
    which depend on extremely few external helpers (such as compat)
    ```

+ `adapters.py`

    adapters.py은 requests 모듈을 사용하는 데 있어 핵심적인 코드가 포함되어있는 파일입니다.
    
    urllib3에서 여러 모듈들을 불러온 후 모듈들을 이용해 헤더를 추가하고, 프록시 세팅, response build등 요청과 연결을 유지하는 코드와 클래스들이 정의되어 있습니다.


    ```
    requests.adapters
    ~~~~~~~~~~~~~~~~~

    This module contains the transport adapters that Requests uses to define
    and maintain connections.
    ```
    
    ```py
    class BaseAdapter(object):
       def send(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None): # ReadyRequest 오브젝트를 보냅니다.
       def close(self): # adapter의 items를 정리합니다.
       
    class HTTPAdapter(BaseAdapter):
      def cert_verify(self, conn, url, verify, cert): # SSL 인증서를 확인합니다.
      def build_response(self, req, resp): # response class를 빌드합니다.
      def get_connection(self, url, proxies=None): # 받은 url에 대한 rulib3에 대한 connection을 반환합니다.
      def request_url(self, request, proxies): # 최종 request를 보낼 URL을 가져옵니다.
      def add_headers(self, request, **kwargs): # 연결에 필요한 기본적인 header를 추가합니다.
      def proxy_headers(self, proxy): # proxy를 통해 보낼 헤더들의 dictionary를 반환합니다.
    ```

+ `api.py`

    api.py은 requests 모듈의 requests.get, requests.post 등 다양한 요청 api를 사용하기 위해 함수들이 정의되어있는 파일입니다.
    <br />api.py파일 내에서 새로운 함수를 정의하기 보단, 다른 모듈에서 정의된 함수를 가져와 사용자가 사용하기 편리한 방식으로 변환해줍니다. 

    ```py
    from . import sessions 
    def request(method, url, **kwargs): # request함수를 method(POST/GET), url(http://naver.com), **kwargs(기능X, 추가로 더 들어올 인자) 파라미터를 사용한다.
      with sessions.Session() as session:
         return session.request(method=method, url=url, **kwargs)
         
    def get(url, params=None, **kwargs): # GET메소드를 사용하여 request한다.
      return request('get', url, params=params, **kwargs)
      
    def options(url, **kwargs): # OPTIONS메소드를 사용하여 request한다.
      return request('options', url, **kwargs)
      
    def head(url, **kwargs): # HEAD메소드를 사용하여 request한다.
      return request('head', url, **kwargs)

    def post(url, data=None, json=None, **kwargs): # POST메소드를 사용하여 request한다. json데이터도 삽입할 수 있다.
      return request('post', url, data=data, json=json, **kwargs)
      
    def put(url, data=None, **kwargs): # PUT메소드를 사용하여 request한다.
      return request('put', url, data=data, **kwargs)
      
    def patch(url, data=None, **kwargs): # PATCH메소드를 사용하여 request한다.
      return request('patch', url, data=data, **kwargs)
    
    def delete(url, **kwargs): # DELETE메소드를 사용하여 reqeuest한다.
      return request('delete', url, **kwargs)
    ```

+ `auth.py`

    auth.py은 예시로 Authorization 같은 헤더를 구축하기 위한 즉 요청에 대한 인증을 처리하는 파일입니다.

    ```
    requests.auth
    ~~~~~~~~~~~~~

    This module contains the authentication handlers for Requests.
    ```

+ `certs.py`

    certs.py은 CA인증서 관련 처리하기 위한 파일입니다.

    ```
    requests.certs
    ~~~~~~~~~~~~~~

    This module returns the preferred default CA certificate bundle. There is
    only one — the one from the certifi package.

    If you are packaging Requests, e.g., for a Linux distribution or a managed
    environment, you can change the definition of where() to return a separately
    packaged CA bundle.
    ```

+ `compat.py`

    compat.py은 python2와 python3 간의 호환성 문제를 처리하는 파일입니다.

    ```
    requests.compat
    ~~~~~~~~~~~~~~~

    This module handles import compatibility issues between Python 2 and Python 3.
    ```

+ `cookies.py`

    cookies.py은 요청과 동시에 cookielib.CookieJar를 사용할 수 있는 호환성 코드가 있는 파일입니다.

    ```
    requests.cookies
    ~~~~~~~~~~~~~~~~

    Compatibility code to be able to use `cookielib.CookieJar` with requests.

    requests.utils imports from here, so be careful with imports.
    ```

+ `exceptions.py`

    exceptions.py은 다양한 예외 처리하기 위한 파일입니다.예외처리 목록은 다음과 같습니다.
    
    ```
    requests.exceptions
    ~~~~~~~~~~~~~~~~~~~
    
    This module contains the set of Requests' exceptions.
    ```
    
    + InvalidJSONError : A JSON error occurred.
    + JSONDecodeError : Couldn't decode the text into json.
    + HTTPError : An HTTP error occurred.
    + ConnectionError : A Connection error occurred.
    + ProxyError : A proxy error occurred.
    + SSLError : An SSL error occurred. 
    + ConnectTimeout : The request timed out while trying to connect to the remote server. Requests that produced this error are safe to retry.
    + ReadTimeout : The server did not send any data in the allotted amount of time.
    + URLRequired : A valid URL is required to make a request
    + TooManyRedirects :  Too many redirects.
    + MissingSchema : The URL schema (e.g. http or https) is missing.
    + InvalidSchema : See defaults.py for valid schemas.
    + InvalidURL : The URL provided was somehow invalid.
    + InvalidHeader : The header value provided was somehow invalid.
    + InvalidProxyURL : The proxy URL provided is invalid.
    + ChunkedEncodingError : The server declared chunked encoding but sent an invalid chunk.
    + ContentDecodingError : Failed to decode response content.
    + StreamConsumedError : The content for this response was already consumed.
    + RetryError : Custom retries logic failed
    + UnrewindableBodyError : Requests encountered an error when trying to rewind a body.
    + RequestsWarning : Base warning for Requests.
    + FileModeWarning : A file was opened in text mode, but Requests determined its binary length.
    + RequestsDependencyWarning : An imported dependency doesn't match the expected version range.

+ `help.py`

    help.py은 버그 리포트를 도와주는 모듈이 있는 파일입니다.
    ```
    Module containing bug report helper(s).
    ```

+ `hooks.py`
    
    hooks.py은 reqeuests hook 시스템을 위한 기능을 제공하는 파일입니다.
    
    ```
    requests.hooks
    ~~~~~~~~~~~~~~
    This module provides the capabilities for the Requests hooks system.
    Available hooks:
    ``response``:
        The response generated from a Request.
    ```
    
+ `models.py`
    
    models.py은 Requests에 대한 주요 객체를 포함하는 파일입니다.
    
    ```
    requests.models
    ~~~~~~~~~~~~~~~
    This module contains the primary objects that power Requests.
    ```

+ `packages.py`

    packages.py은 이전 버전과의 호환성을 위한 파일입니다.
    ```
    This code exists for backwards compatibility reasons.
    ```
+ `sessions.py`

    sessions.py은 세션을 유지관리하기 위한 파일입니다.
    ```
    requests.sessions
    ~~~~~~~~~~~~~~~~~
    This module provides a Session object to manage and persist settings across
    requests (cookies, auth, proxies).
    ```
    
+ `status_codes.py`
 
    status_codes.py은 HTTP status code에 대한 매핑을 해주는 파일입니다.
    ```
    The ``codes`` object defines a mapping from common names for HTTP statuses
    to their numerical codes, accessible either as attributes or as dictionary
    items.
    Example::
        >>> import requests
        >>> requests.codes['temporary_redirect']
        307
        >>> requests.codes.teapot
        418
        >>> requests.codes['\o/']
        200
    Some codes have multiple names, and both upper- and lower-case versions of
    the names are allowed. For example, ``codes.ok``, ``codes.OK``, and
    ``codes.okay`` all correspond to the HTTP status code 200.
    ```
    
+ `structures.py`

    structures.py은 Requests에 대한 데이터 구조를 포함하는 파일입니다.
    ```
    requests.structures
    ~~~~~~~~~~~~~~~~~~~
    Data structures that power Requests.
    ```
    
+ `utils.py`

    utils.py은 모듈 내에서 사용되는 유틸리티 기능을 제공하는 파일입니다.
    ```
    requests.utils
    ~~~~~~~~~~~~~~
    This module provides utility functions that are used within Requests
    that are also useful for external consumption.
    ```
