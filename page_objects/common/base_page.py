#base_page.py
from utilities.config import DEFAULT_TIMEOUT, SCREENSHOT_DIR
from utilities.element_interactor import ElementInteractor
from utilities.element_locator import ElementLocator
from utilities.screenshot_manager import ScreenshotManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Base class for all page objects"""
    def __init__(self, driver):
        """
        Initialize BasePage with WebDriver instance and utility objects.

        Args:
            driver: Selenium WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, DEFAULT_TIMEOUT)
        self.locator = ElementLocator(driver)
        self.interactor = ElementInteractor(driver)
        self.screenshot = ScreenshotManager()
        
    class CommonLocators:
        """Common locators used across multiple pages"""
        HEADER_LOGO = "//section//img[@alt='logo']"
        LOGIN_LINK = "//section//button[text()='LOG IN']"
        LOGOUT_BUTTON = "//section//button[text()='LOG OUT']"
    
    class NavigationLocators:
        """Locators for navigation elements"""
        VIDEOS_LINK = "//li/a[contains(@href, '/') and contains(text(), 'Videos')]"
        VIDEO_CATALOGUES_LINK = "//li/a[@href='/videoCatalogues']"
        MAP_MARKERS_LINK = "//li/a[@href='/mapMarkers']"
        USERS_LINK = "//li/a[@href='/developmentNotice' and contains(text(), 'Users')]"
        DEFINITIONS_BUTTON = "//li//button[text()='Definitions']"
        ORGS_LINK = "//li/a[@href='/organizations']"
        INSTA_LINK = "//li/a[@href='/developmentNotice' and contains(text(), 'Installations')]"

        # Dropdown choices from Definitions link
        COUNTRIES_LINK = "//a[@href='/countries']"
        IUCNSTATUS_LINK = "//a[@href='/iucnStatus']"
        POP_TREND_LINK = "//a[@href='/populationTrend']"
        SPECIES_LINK = "//a[@href='/species']"
        TAGS_LINK = "//a[text()='Tags']"
        
    # Basic methods
    def find_logo(self):
        """Check if the logo is present on the page"""
        return self.locator.is_element_present(self.CommonLocators.HEADER_LOGO)
    
    def find_login_link(self):
        """Check if the login link is present on the page"""
        return self.locator.is_element_present(self.CommonLocators.LOGIN_LINK)
    
    def find_logout(self):
        """Check if the logout button is present on the page"""
        return self.locator.is_element_present(self.CommonLocators.LOGOUT_BUTTON)
    
    def logout_site(self):
        """Perform logout action"""
        self.interactor.element_click(self.CommonLocators.LOGOUT_BUTTON)
        
    def get_page_title(self):
        """Get the title of the current page"""
        return self.driver.title
    
    def get_current_url(self):
        """Get the URL of the current page"""
        return self.driver.current_url
    
    def navigate_to(self, url: str):
        """Navigate to a specified URL"""
        self.driver.get(url)
    
    def refresh_page(self):
        """Refresh the current page"""
        self.driver.refresh()
        
    def go_back(self):
        """Navigate to the previous page in browser history"""
        self.driver.back()
        
    def go_forward(self):
        """Navigate to the next page in browser history"""
        self.driver.forward()
        
    def switch_to_frame(self, frame_reference: str):
        """Switch to a specified frame"""
        self.driver.switch_to.frame(frame_reference)
    
    def switch_to_default_content(self):
        """Switch back to the default content"""
        self.driver.switch_to.default_content()
        
    def accept_alert(self):
        """Accept an alert"""
        self.driver.switch_to.alert.accept()
    
    def dismiss_alert(self):
        """Dismiss an alert"""
        self.driver.switch_to.alert.dismiss()
    
    def get_alert_text(self) -> str:
        """Get the text of an alert"""
        return self.driver.switch_to.alert.text
    
    # Navigation methods
    
    def find_videos_link(self):
        """Check if the Videos link is present"""
        return self.locator.is_element_present(self.NavigationLocators.VIDEOS_LINK)
    
    def go_videos_page(self):
        """Navigate to the Videos page"""
        self.interactor.element_click(self.NavigationLocators.VIDEOS_LINK)
        
    def find_video_catalogues_link(self):
        """Check if the Video Catalogues link is present"""
        return self.locator.is_element_present(self.NavigationLocators.VIDEO_CATALOGUES_LINK)
    
    def go_video_catalogues_page(self):
        """Navigate to the Video Catalogues page"""
        self.interactor.element_click(self.NavigationLocators.VIDEO_CATALOGUES_LINK)
        
    def find_map_markers_link(self):
        """Check if the Map Markers link is present"""
        return self.locator.is_element_present(self.NavigationLocators.MAP_MARKERS_LINK)
    
    def go_map_markers_page(self):
        """Navigate to the Map Markers page"""
        self.interactor.element_click(self.NavigationLocators.MAP_MARKERS_LINK)
    
    def find_users_link(self):
        """Check if the Users link is present"""
        return self.locator.is_element_present(self.NavigationLocators.USERS_LINK)
    
    def go_users_page(self):
        """Navigate to the Users page"""
        self.interactor.element_click(self.NavigationLocators.USERS_LINK)

    def find_organizations_link(self):
        """Check if the Organizations link is present"""
        return self.locator.is_element_present(self.NavigationLocators.ORGS_LINK)
    
    def go_organizations_page(self):
        """Navigate to the Organizations page"""
        self.interactor.element_click(self.NavigationLocators.ORGS_LINK)
        
    def find_installations_link(self):
        """Check if the Installations link is present"""
        return self.locator.is_element_present(self.NavigationLocators.INSTA_LINK)
    
    def go_installations_page(self):
        """Navigate to the Installations page"""
        self.interactor.element_click(self.NavigationLocators.INSTA_LINK)
        
    # Handle Definitions as it is a dropdown list
    
    def find_definitions_item(self):
        """Check if the Definitions item is present"""
        return self.locator.is_element_present(self.NavigationLocators.DEFINITIONS_ITEM)
        
    # Navigate the Definitions dropdown elements
        
    def find_countries_link(self):
        """Check if the Countries link is present in the Definitions dropdown"""
        return self.locator.is_element_present(self.NavigationLocators.COUNTRIES_LINK)

    def go_countries_page(self):
        """Navigate to the Countries page from the Definitions dropdown"""
        self.interactor.element_click(self.NavigationLocators.COUNTRIES_LINK)
    
    def find_iucnstatus_link(self):
        """Check if the IUCN Status link is present in the Definitions dropdown"""
        return self.locator.is_element_present(self.NavigationLocators.IUCNSTATUS_LINK)

    def go_iucnstatus_page(self):
        """Navigate to the IUCN Status page from the Definitions dropdown"""
        self.interactor.element_click(self.NavigationLocators.IUCNSTATUS_LINK)
    
    def find_pop_trend_link(self):
        """Check if the Population Trend link is present in the Definitions dropdown"""
        return self.locator.is_element_present(self.NavigationLocators.POP_TREND_LINK)

    def go_pop_trend_page(self):
        """Navigate to the Population Trend page from the Definitions dropdown"""
        self.interactor.element_click(self.NavigationLocators.POP_TREND_LINK)
    
    def find_species_link(self):
        """Check if the Species link is present in the Definitions dropdown"""
        return self.locator.is_element_present(self.NavigationLocators.SPECIES_LINK)

    def go_species_page(self):
        """Navigate to the Species page from the Definitions dropdown"""
        self.interactor.element_click(self.NavigationLocators.SPECIES_LINK)
    
    def find_tags_link(self):
        """Check if the Tags link is present in the Definitions dropdown"""
        return self.locator.is_element_present(self.NavigationLocators.TAGS_LINK)

    def go_tags_page(self):
        """Navigate to the Tags page from the Definitions dropdown"""
        self.interactor.element_click(self.NavigationLocators.TAGS_LINK)