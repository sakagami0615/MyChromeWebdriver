import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



class ChromeDriverGenerator:

    def __init__(self):
        self._params = {}


    def create_driver(self):

        # 引数で渡されたオプションを取得
        # 可変長引数にOptionsが無い場合は初期化する
        if self._params.get('options'):
            options = self._params.get('options')
        else:
            options = Options()

        # プロファイルの設定
        # profile_pathが無い場合は何もしない
        # また、profile_pathのフォルダが無い場合も何もしない
        if self._params.get('profile_path'):
            profile_path = self._params.get('profile_path')
            if os.path.isdir(profile_path):
                options.add_argument('--user-data-dir=' + profile_path)

        # ChromeのWebdriverを作成
        # ChromeDriver.exeのパス指定がない場合は、ChromeDriverManagerを使用して環境を用意する
        if self._params.get('executable_path'):
            executable_path = self._params.get('executable_path')
            driver = webdriver.Chrome(executable_path, options=options)
        else:
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

        return driver



class ChromeDriver_AWSLambda(ChromeDriverGenerator):

    def __init__(self):
        super().__init__()

        # Hidden setting
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument("--single-process")
        options.add_argument('--disable-dev-shm-usage')

        # hidden chromium setting
        options.binary_location = '/opt/headless/bin/headless-chromium'

        # setting parameter dict
        self._params['executable_path'] = '/opt/headless/bin/chromedriver'
        self._params['profile_path']    = '/opt/profile'
        self._params['options']         = options


class ChromeDriver_CircleCI(ChromeDriverGenerator):

    def __init__(self):
        super().__init__()

        # Hidden setting
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument("--single-process")
        options.add_argument('--disable-dev-shm-usage')

        # hidden chromium setting
        #options.binary_location = '/opt/headless/bin/headless-chromium'

        # setting parameter dict
        #self._params['executable_path'] = '/opt/headless/bin/chromedriver'
        #self._params['profile_path']    = '/opt/profile'
        self._params['options'] = options



class ChromeDriver_Local(ChromeDriverGenerator):

    def __init__(self, is_hidden=False):
        super().__init__()

        if is_hidden:
            # Hidden setting
            options = Options()
            options.add_argument('--headless')

            # setting parameter dict
            self._params['profile_path'] = os.path.join(os.getcwd(), 'profile')
            self._params['options']      = options

        else:
            # setting parameter dict
            self._params['profile_path'] = os.path.join(os.getcwd(), 'profile')
