from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as data

#url='https://google.com'
def GetUrl (url): #Función para obtener url con el DriverChrome.
    chromeOptions=webdriver.ChromeOptions()
    chromeOptions.add_argument('--headless')
    #browser=webdriver.Chrome(executable_path='./chromedriver.exe',chrome_options=chromeOptions)
    browser = webdriver.Chrome(chrome_options=chromeOptions)
    browser.get(url)
    return browser
#GetUrl (url)
#path='./ASIN.xlsx'
def DataFile (LocalFile): #Función para url's por archivo de excel en el botón adjuntar.
    file=data.read_excel(LocalFile,header=None)
    file=file[0].to_list()
    ASIN=file[1:]
    
    Urls=[]
    
    for i in ASIN:
        Urls.append('https://www.amazon.com/dp/'+str(i))
    print(Urls)
    return Urls
    #Scraping(Urls)
#DataFile(path)

def KWUrls(kw): #Función para url's por keyword.
    url='https://www.amazon.com/s?k=()&crid=18EWRADP7T4E6&sprefix=decanta%2Caps%2C233&ref=nb_sb_ss_ts-doa-p_3_7'
    urls=[]
    links=[]
    linksASIN=[]
    #kw='decantador de whisky'
    kw=kw.replace(' ','+')
    url=url.replace('()',kw)
    urls.append(url)
    next=True
    while next==True:
        try:
            browser=GetUrl(url)
            soup=BeautifulSoup(browser.page_source, 'html.parser')
            page=soup.find('ul',class_='a-pagination',)
            page=page.find('li',{'class':'a-last'})
            page=page.find('a')['href']
            url='https://www.amazon.com'+page
            urls.append(url)            
        except:
            next=False
    for i in urls:
        browser=GetUrl(i)           
        soup=BeautifulSoup(browser.page_source,'html.parser')
        page=soup.find_all('a',{'class':"a-link-normal a-text-normal"})
        page=str(page)
        page=page.split(' ')
        product=[]
        urlproducts=[]
        
        for i in page:
            if 'href' in i:
                product.append(i)
        for j in product:
            if 'dp/B0' in j:
                urlproducts.append(j)
        urlproducts=''.join(urlproducts)
        urlproducts=urlproducts.split('"')
        for i in urlproducts:
            if 'dp/B0' in i:
                links.append(i)        
    for i in links:
        linksASIN.append('https://www.amazon.com'+i)
    return linksASIN
    
#urls=DataFile (path)
def Scraping(urls):        
        Data=[['LINK','TITULO','PRECIO','DESCRIPCIÓN','ENVÍO','CARACTERÍSTICAS','IMG']]                
        for i in urls:
            try:
                browser=GetUrl (i)
                code=BeautifulSoup(browser.page_source, 'html.parser')
            except:
                print('no aplica')                        
            ProductData=[]
            ProductData.append(i)
            try:
                title=code.find('span', class_="a-size-large product-title-word-break").text
                title=title.replace('\n','')
                title=title.replace(',','')
                title=title.replace('-','')
            except:
                title='El producto fue eliminado'            
            try:
                Price=code.find('span', class_='a-size-medium a-color-price').text
                Price=Price.replace('.',',')
                Price=Price.replace('$','')
                Price=Price.replace('\n','')
                Price=Price.replace('"','')
                Price=Price.replace('US','')
                Price=Price.replace(' ','')

            except:
                Price='No hay stock'            
            try:
                Description=code.find('div',id="feature-bullets").text
            except:
                Description='No Aplica Descripción'
            try:
                Shipping=code.find('span',class_="a-size-base a-color-secondary").text
            except:
                Shipping='No Aplica Envío'
            try:
                Features=code.find('div',id="detailBullets_feature_div").text
            except:
                Features='No Aplican Características'
            try:
                Img=code.find('div',id='imgTagWrapperId')
                Img=str(Img).split(' ')
                ListImg=[]                
                for j in Img:
                    if 'https' in j:
                        j=str(j)
                        ListImg.append(j)
                ListImg=ListImg[1]
            except:
                ListImg='No Aplican Imágenes'                                            
            ProductData.append(title)
            ProductData.append(Price)
            ProductData.append(Description)
            ProductData.append(Shipping)
            ProductData.append(Features)
            ProductData.append(ListImg)                        
            Data.append(ProductData)        
        #ScrapingFile=data.DataFrame(Data)
        #ScrapingFile.to_excel('resultados.xlsx')
        return Data
#ASIN='B0797VH3MJ\nB07MPBJQ5N\nB07ZTNS6VN\nB088LDV7DC\nB017TXBKCC'

def UrlsByASIN(ASIN):
    MainUrl='https://amazon.com/dp/'
    ASIN=ASIN.split('\n')
    Urls=[]
    for i in ASIN:
        Urls.append(MainUrl+i)
    return Urls

#Urls=UrlsByASIN(ASIN)
#print(Scraping(Urls))
#FileData=[1,2,3,4,5,6]
#FileFolder='D:/NanoElMagno/Documentos/Programación/Python/CursoCompleto/PYSide6/CrawlerAMZ/rd'

def DataFrameCreator(FileData,FileFolder):
    ScrapingFile=data.DataFrame(FileData)
    #ScrapingFile.to_excel('Resultados.xlsx')
    ScrapingFile.to_excel(FileFolder+'.xlsx')
    
#DataFrameCreator(FileData,FileFolder)