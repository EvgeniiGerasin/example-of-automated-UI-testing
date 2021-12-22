import allure
import json

from config.config import Path


class Screenshot:
    """Class for getting a screenshot into the report
    """

    def shot(self, driver: object, description: str):
        """Method for generating a screenshot for a report. 
        As for a mistake, and for the correct result

        Args:
            driver (object): instace webdriver
            description (str): screenshot discription
        """
        scr = driver.get_screenshot_as_png()
        allure.attach(
            body=scr,
            name=f'{description}',
            attachment_type=allure.attachment_type.PNG
        )


class Report:
    """Helper methods needed for
    generating a report
    """

    @staticmethod
    def attachment_json(data: any, name: str) -> None:
        """Outputs the transmitted data in json format
        to the report

        Args:
        - data (dict): data to report
        - name (str): data name
        """
        allure.attach(
            json.dumps(data, ensure_ascii=False),
            name,
            allure.attachment_type.JSON
        )


class FileForTest:
    """Create test files of different sizes and formats
    """
    @staticmethod
    def create(name, size=1, file_extension='txt') -> str:
        """
        Args:
            size (int, optional): size in mb
            file_extension(str): file extension (pdf,txt,jpeg etc).
        Returns:
            (str): path to created file
        """
        name_file = name + file_extension
        size_file = 127000 * size
        with open(name_file, 'w') as file:
            for _ in range(0, size_file):
                file.write('textTest')
        return Path.ROOT_DIR + name_file


class DownloadWindowsBrowser:

    def __init__(self, driver: object) -> None:
        """Content class methods for interacting with the page
        downloads in Chrome browser

        Args:
            driver (object): instance webdriver
        """
        self.driver = driver
        self.driver.get("chrome://downloads")

    def chrome_get_status_dowloads(self) -> bool:
        """Getting information about the availability
        of downloads

        Return:
        - number availability of downloads
        """
        number_dowloads = self.driver.execute_script(
            "return document.querySelector('downloads-manager')."
            "shadowRoot.querySelector('#downloadsList')."
            "getAttribute('aria-rowcount')"
        )
        Screenshot().shot(self.driver, 'Window of downloads')
        try:
            num_int = int(number_dowloads)
        except ValueError:
            assert False, ValueError
        return num_int
