from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# browser.get('https://instagram.com/')
browser.get('http://drnguyentt.com/moodle30/login/index.php')
# time.sleep(400)


def logIN():
    username=browser.find_element('xpath','/html/body/div[2]/div[2]/div/div/section/div/div[2]/div/div/div/div/div/div[1]/form/div[1]/input')
    username.send_keys('vuminhanhB19DCCN048dipg9')
    # S1mple))@
    password = browser.find_element('xpath','/html/body/div[2]/div[2]/div/div/section/div/div[2]/div/div/div/div/div/div[1]/form/div[2]/input')
    password.send_keys('S1mple))@')
    submit = browser.find_element('xpath','/html/body/div[2]/div[2]/div/div/section/div/div[2]/div/div/div/div/div/div[1]/form/button')
    submit.click()
    time.sleep(5)

# def action():
    clicksession=browser.find_element('xpath','/html/body/div[3]/div[3]/div/div/section[1]/div/aside/section[2]/div/div/div[1]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div[1]/a')
    clicksession.click()
    time.sleep(5)
    bt=browser.find_element('xpath','/html/body/div[2]/div[3]/div/div/section/div/div/ul/li[4]/div[3]/ul/li[6]/div/div/div[2]/div[1]/a')
    bt.click()
# action()
    time.sleep(5)
    edit = browser.find_element('xpath','/html/body/div[2]/div[3]/div/div/section/div[1]/ul/li[2]/a')
    edit.click()
    time.sleep(5)
    # content='''
    # #include<bits/stdc++.h>
    # using namespace std;
    # int main(){
    #     int a,b,L;
    #     cin>>a>>b>>L;
    #     int x[a][b];
    #     double g[a][b];
    #     int nm[L];
    #     for(int i=0;i<L;i++) nm[i]=0;
    #     for(int i=0;i<a;i++){
    #         for(int j=0;j<b;j++){
    #             cin>>x[i][j];
    #             nm[x[i][j]]+=1;
    #         }
    #     }
    #     double G[L];
    #     for(int i=0;i<L;i++) G[i] = 0;
    #     for(int i=0;i<L;i++){
    #         for(int j= 0;j<=i;j++){
    #             G[i] += ((double)nm[j]/(a*b));
    #         }
    #         G[i]*=(L-1);
    #     }
    #     for(int i=0;i<a;i++){
    #         for(int j=0;j<b;j++){
    #             cout<<round(G[x[i][j]])<<" ";
    #         }
    #         cout<<endl;
    #     }
    # }'''
    # price = browser.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/section/div[1]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div[3]')
    # price = browser.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/section/div[1]/div[1]/div/div[2]/div[2]/div[2]/textarea')
    # price_content = price.get_attribute('innerHTML')
    # print(price_content)
    # browser.execute_script("arguments[0].innerHTML = arguments[1];", price, ''+content+'')
    content = '''
    const ide = document.querySelector('#vplide');
    const ideUploadForm = document.querySelector('#vplide form');

    const resetFileName = () => {
    document.querySelector('#vplide form input').value = '';
    };

    const displayUploadForm = () => {
    ideUploadForm.style.display = 'block';
    const resetFileNameBtn = document.createElement('button');
    resetFileNameBtn.innerText = 'Reset file name';
    resetFileNameBtn.style.marginTop = '10px';
    resetFileNameBtn.style.backgroundColor = '#f00';
    resetFileNameBtn.style.color = '#fff';
    resetFileNameBtn.style.borderColor = '#fff';
    resetFileNameBtn.style.borderWidth = '1px';
    resetFileNameBtn.addEventListener('click', resetFileName);
    resetFileNameBtn.addEventListener('mouseover', () => {
        resetFileNameBtn.style.backgroundColor = '#c00';
    });
    resetFileNameBtn.addEventListener('mouseout', () => {
        resetFileNameBtn.style.backgroundColor = '#f00';
    });
    ide.appendChild(resetFileNameBtn);
    };

    if (ide) {
    displayUploadForm();
    };
    '''
    browser.execute_script(content);
logIN()
