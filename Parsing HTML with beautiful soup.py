import bs4, requests

def getATBSWPtranscript(transcriptURL):
    res = requests.get(transcriptURL)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#ct-sidebar-scroll-container > div > div:nth-child(1) > p > span')
    return elems[0].text.strip()

Transcript = getATBSWPtranscript('https://www.getfootballnewsfrance.com/ligue-1/olympique-de-marseille/')
print('The transcript for this lesson was: ' + Transcript)