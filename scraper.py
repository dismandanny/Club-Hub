import requests
from bs4 import BeautifulSoup
import pandas as pd

myDataset = {
    'Organization Name' : ['100% Triumph', '123 I Like to Ski :)', 'Academic Quiz Team'],
    'Organization Description' : ['The purpose of this organization shall be to assist students at the University of Maryland in adjusting to school life on the campus and to bring their pursuit of academics under the lordship of Jesus Christ so they can brilliantly excel.', 
                                  'The purpose of Ski Club is to bring together like-minded individuals who love to ski or want to ski. It is a club where individuals can learn a new skill (skiing or snowboarding) and make new friends and have memorable experiences.',
                                  'The Academic Quiz Team provides an opportunity for students to compete in intercollegiate academic question-and-answer competitions against students from other colleges and universities. We also hosts similar competitions at the University of Maryland.'],
    'Average Rating' : ['3.3', '4.4', '5.0']
}

df = pd.DataFrame(myDataset)

print(df)