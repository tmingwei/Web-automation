from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

web = webdriver.Chrome()
web.get("https://docs.google.com/forms/d/e/1FAIpQLSfGjGj0opuahRHuJdARJCLYRE8qn_lm1pM5O52qEbjGbcOcpw/viewform")
time.sleep(1)

for i in range(20):
	gender_range=random.randint(0,1)
	gender1 = web.find_elements(By.CLASS_NAME,"appsMaterialWizToggleRadiogroupOffRadio")
	gender1[gender_range].click()
#time.sleep(1)

	age_range=random.randint(2,7)
	age2 = web.find_elements(By.CLASS_NAME,"appsMaterialWizToggleRadiogroupOffRadio")
	age2[age_range].click()
#time.sleep(1)

	marital_range=random.randint(8,11)
	marital3 = web.find_elements(By.CLASS_NAME,"appsMaterialWizToggleRadiogroupOffRadio")
	marital3[marital_range].click()
#time.sleep(1)

	income_range=random.randint(12,16)
	income4 = web.find_elements(By.CLASS_NAME,"appsMaterialWizToggleRadiogroupOffRadio")
	income4[income_range].click()
#time.sleep(1)

	enjoy_range=random.randint(17,19)
	enjoy5 = web.find_elements(By.CLASS_NAME,"appsMaterialWizToggleRadiogroupOffRadio")
	enjoy5[enjoy_range].click()
	#time.sleep(1)

	often_range=random.randint(20,24)
	often6 = web.find_elements(By.CLASS_NAME,"appsMaterialWizToggleRadiogroupOffRadio")
	often6[often_range].click()
	#time.sleep(1)

	cuisine_range=random.randint(0,4)#skip5
	cuisine7 = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
	cuisine7[cuisine_range].click()
	#time.sleep(1)

	local_range=random.randint(6,10)
	local8a = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
	local8a[local_range].click()
	#time.sleep(1)

	local_range=random.randint(11,16)
	local8b = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
	local8b[local_range].click()
	#time.sleep(1)

	local_range=random.randint(17,20)#skip21,22
	local8c = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
	local8c[local_range].click()
	#time.sleep(1)

	topten_range=random.randint(23,24)
	topten9a = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
	topten9a[topten_range].click()
	#time.sleep(1)

	topten_range=random.randint(25,26)
	topten9b = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
	topten9b[topten_range].click()
	#time.sleep(1)

	topten_range=random.randint(27,28)
	topten9c = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
	topten9c[topten_range].click()
	#time.sleep(1)

	topten_range=random.randint(29,30)
	topten9d = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
	topten9d[topten_range].click()
	#time.sleep(1)

	topten_range=random.randint(31,32)
	topten9e = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
	topten9e[topten_range].click()
	#time.sleep(1)

	topten_range=random.randint(33,34)
	topten9f = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
	topten9f[topten_range].click()
	#time.sleep(1)

	topten_range=random.randint(35,36)
	topten9g = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
	topten9g[topten_range].click()
	#time.sleep(1)

	topten_range=random.randint(37,40)
	topten9h = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
	topten9h[topten_range].click()
	#time.sleep(1)

	topten_range=random.randint(41,44)
	topten9i = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
	topten9i[topten_range].click()
	#time.sleep(1)

	topten_range=random.randint(45,47)
	topten9j = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
	topten9j[topten_range].click()
	#time.sleep(1)

	appliance_range=random.randint(48,52)
	appliance10a = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
	appliance10a[appliance_range].click()
	#time.sleep(1)

	appliance_range=random.randint(53,57)
	appliance10b = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
	appliance10b[appliance_range].click()
	#time.sleep(1)

	appliance_range=random.randint(58,63)
	appliance10c = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
	appliance10c[appliance_range].click()
	#time.sleep(1)

	appliance_range=random.randint(64,65)
	appliance10d = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
	appliance10d[appliance_range].click()
	#time.sleep(1)

	appliance_range=random.randint(66,67)#skip68
	appliance10e = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
	appliance10e[appliance_range].click()
	#time.sleep(1)

	purchase_range=random.randint(69,71)
	purchase11a = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
	purchase11a[purchase_range].click()
	#time.sleep(1)

	purchase_range=random.randint(72,74)#skip75
	purchase11b = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
	purchase11b[purchase_range].click()
	#time.sleep(1)

	impluse_range=random.randint(76,79)
	impluse12a = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
	impluse12a[impluse_range].click()
	#time.sleep(1)

	impluse_range=random.randint(80,89)
	impluse12b = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
	impluse12b[impluse_range].click()
	#time.sleep(1)

	impluse_range=random.randint(90,95)#skip96
	impluse12c = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
	impluse12c[impluse_range].click()
	#time.sleep(1)

	spend_range=random.randint(25,29)
	spend13 = web.find_elements(By.CLASS_NAME,"appsMaterialWizToggleRadiogroupOffRadio")
	spend13[spend_range].click()
	#time.sleep(1)

	workshop_range=random.randint(97,98)
	workshop14a = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
	workshop14a[workshop_range].click()
	#time.sleep(1)

	workshop_range=random.randint(99,100)
	workshop14b = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
	workshop14b[workshop_range].click()
	#time.sleep(1)

	workshop_range=random.randint(101,104)
	workshop14c = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
	workshop14c[workshop_range].click()
	#time.sleep(1)

	workshop_range=random.randint(105,110)#skip111
	workshop14d = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
	workshop14d[workshop_range].click()
	#time.sleep(1)

	pay_range=random.randint(30,33)
	pay15 = web.find_elements(By.CLASS_NAME,"appsMaterialWizToggleRadiogroupOffRadio")
	pay15[pay_range].click()
	#time.sleep(1)

	social_range=random.randint(112,113)#skip116,117
	social16a = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
	social16a[social_range].click()
	#time.sleep(1)

	social_range=random.randint(114,115)#skip116,117
	social16b = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
	social16b[social_range].click()
	#time.sleep(1)

	date_range=random.randint(34,35)
	date17 = web.find_elements(By.CLASS_NAME,"appsMaterialWizToggleRadiogroupOffRadio")
	date17[date_range].click()
	#time.sleep(1)

	venue_range=random.randint(36,38)
	venue18 = web.find_elements(By.CLASS_NAME,"appsMaterialWizToggleRadiogroupOffRadio")
	venue18[venue_range].click()
	#time.sleep(1)

	answer = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div/div[1]/div[2]/textarea')
	answer.click()
	answer.send_keys("NIL")


	submit = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
	submit.click()
	time.sleep(1)
	web.refresh()
