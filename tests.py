from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time


# class Hosttest(LiveServerTestCase):
#     def testhomepage(self):
#         driver=webdriver.Chrome()
#         driver.get('http://127.0.0.1:8000/')
#         time.sleep(5)
#         assert "HOME" in driver.title

class LoginFormTest(LiveServerTestCase):

	def testform(self):
		driver = webdriver.Chrome()

		driver.get('http://127.0.0.1:8000/user/login/')

		time.sleep(3)

		user_name = driver.find_element_by_name('username')
		user_password = driver.find_element_by_name('password')

		time.sleep(3)

		submit = driver.find_element_by_id('submit')

		user_name.send_keys('satish')
		user_password.send_keys('admin')
		time.sleep(3)

		submit.send_keys(Keys.RETURN)

		assert 'Logout' in driver.page_source

class RegisterformTest(LiveServerTestCase):
    def testform(self):
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/user/employer_register/')
        # driver.maximize_window()
        time.sleep(3)
        user_name = driver.find_element_by_name('username')
        first_name=driver.find_element_by_name('first_name')
        last_name=driver.find_element_by_name('last_name')
        email=driver.find_element_by_name('email')
        mobile=driver.find_element_by_name('mobile')
        address=driver.find_element_by_name('address')
        user_password = driver.find_element_by_name('password1')
        password2=driver.find_element_by_name('password2')
        resume=driver.find_element_by_name('resume')
        submit = driver.find_element_by_id('submit')
        time.sleep(3)
        user_name.send_keys('taran1')
        user_password.send_keys('#admin123#')
        password2.send_keys('#admin123#')
        mobile.send_keys('33244')
        address.send_keys('3E WA,US')
        resume.send_keys('enter image location here') 
        email.send_keys('taran1@gmail.com')
        first_name.send_keys('Taranbeer')
        last_name.send_keys('singh')

        time.sleep(3)
        submit.send_keys(Keys.RETURN)
        assert 'Logout' in driver.page_source

class Register_employerFormTest(LiveServerTestCase):
    def testform(self):
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/user/employer_register/')
        # driver.maximize_window()
        time.sleep(3)
        user_name = driver.find_element_by_name('username')
        first_name=driver.find_element_by_name('first_name')
        last_name=driver.find_element_by_name('last_name')
        email=driver.find_element_by_name('email')
        user_password = driver.find_element_by_name('password1')
        password2=driver.find_element_by_name('password2')
        submit = driver.find_element_by_id('submit')
        time.sleep(3)
        user_name.send_keys('taran1')
        user_password.send_keys('#admin123#')
        password2.send_keys('#admin123#')
        email.send_keys('taran1@gmail.com')
        first_name.send_keys('Taranbeer')
        last_name.send_keys('singh')
        time.sleep(3)
        submit.send_keys(Keys.RETURN)
        assert 'Logout' in driver.page_source

class CreateJobformTest(LiveServerTestCase):
    def testform(self):
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/add_job/')
        # driver.maximize_window()
        time.sleep(3)
        position = driver.find_element_by_name('position')
        company=driver.find_element_by_name('company')
        job_type=driver.find_element_by_name('job_type')
        start_date=driver.find_element_by_name('start_date')
        package=driver.find_element_by_name('package')
        apply_by=driver.find_element_by_name('apply_by')
        location = driver.find_element_by_name('location')
        about_company=driver.find_element_by_name('about_company')
        job_description=driver.find_element_by_name('job_description')
        eligibility=driver.find_element_by_name('eligibility')
        perks=driver.find_element_by_name('perks')
        openings=driver.find_element_by_name('openings')
        # created_by=driver.find_element_by_name('created_by')
        Select objSelect = new Select(driver.findElement(By.id("id_created_by")))
        Select.selectByIndex(2)

        submit = driver.find_element_by_id('add')
        time.sleep(3)
        position.send_keys('Senior Developer')
        company.send_keys('Leanvia')
        job_type.send_keys('Full Time')
        start_date.send_keys('13/11/2021')
        package.send_keys('12')
        apply_by.send_keys('20/12/2021') 
        location.send_keys('Silicon Valley,California')
        about_company.send_keys('Multinational company')
        job_description.send_keys('Full Time Senior developer ')
        eligibility.send_keys('2 year experience')
        perks.send_keys('5 working days')
        openings.send_keys('5')
        # created_by.send_keys('2')




        time.sleep(5)
        submit.send_keys(Keys.RETURN)
        # assert 'Logout' in driver.page_source

class Searchform(LiveServerTestCase):

	def testform(self):
		driver = webdriver.Chrome()

		driver.get('http://127.0.0.1:8000/')

		time.sleep(3)

		position = driver.find_element_by_name('positionq')
		location = driver.find_element_by_name('locationq')

		time.sleep(3)

		submit = driver.find_element_by_id('search')

		position.send_keys('MEAN stack developer')
		location.send_keys('Pune')
		time.sleep(3)

		submit.send_keys(Keys.RETURN)
        time.sleep(3)
