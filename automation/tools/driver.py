from selenium import webdriver

from config.config import Browser


class BrowserSelect:
    """Create a instance webdriver

    Args:

    - local (bool, optional): Set to true if you need to 
    run test on the local machine. Defaults to False.
    - browser_version (str, optional): version browser
    """

    def __init__(
        self,
        browser_version: str,
        local: bool = False
    ):

        self._driver = None
        self._local = local
        self._browser_version = browser_version

    def get_driver(self, capabilitie='') -> object:
        """Getting webdriver

        capabilitie (str): json with webdriver extension
        options

        Returns:
        - browser (object): instance webdriver
        """
        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability("prefs", Browser.PREFS)
        chrome_options.add_argument('--ignore-certificate-errors')
        CAPABILITIES = capabilitie
        if self._local:
            self._driver = webdriver.Chrome(
                executable_path=Browser.CHROMEDRIVER_PATH,
                options=chrome_options
            )
        else:
            CAPABILITIES["browserVersion"] = self._browser_version
            self._driver = webdriver.Remote(
                command_executor="http://localhost:4444/wd/hub/",
                desired_capabilities=CAPABILITIES,
                options=chrome_options
            )
        self._driver.implicitly_wait(0.2)
        return self._driver


