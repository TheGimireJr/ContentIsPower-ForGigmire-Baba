import requests
import re
from termcolor import colored

# Y2Mate Urls
Y2Mate_urls = {'Main': 'https://www.y2mate.com/en349',
               'analyse': 'https://www.y2mate.com/mates/en349/analyze/ajax',
               'convert': 'https://www.y2mate.com/mates/convert'}


# Youtube_links_slicer
def VidIDExtractor(link):
    if link.find('https://www.youtube.com/watch?v=') != -1:
        vID = link.replace('https://www.youtube.com/watch?v=', '')
    else:
        vID = link.replace('https://www.youtube.com/shorts/', '')
    return vID


def ytDownloader(url):
    s = requests.Session()
    r1 = s.get(Y2Mate_urls['Main'])
    website_status = r1.status_code
    if (website_status == 200):
        live = True
        print(colored('Y2Mate is working...', 'green'))
    else:
        live = False
        print(colored('Y2Mate is Dead...', 'Red'))

    # Finaly retriving links
    if live:
        analyse_data = {
            'url': url,
            'q_auto': 0,
            'ajax': 1
        }
        req_analyse = s.post(Y2Mate_urls['analyse'], analyse_data)
        response_analyse = req_analyse.json()
        analyse_status = response_analyse['status']
        analyse_result = response_analyse['result']
        if analyse_status == "success":
            print(colored('Analysis suceeded...Finding kID', 'green'))
            pattern = 'k__id = "(.*?)"'
            kID = re.search(pattern, analyse_result).group(1)
            title_pattern = '</a> <div class="caption text-left"> <b>(.*?)</b>'
            title = re.search(title_pattern, analyse_result).group(1)
        else:
            print(colored('Analysis Failed', 'red'))
            title = None

        if kID:
            vID = VidIDExtractor(url)
            if analyse_result.find('data-fquality="1080"') != -1:
                quality = 1080
                convert_data = {
                    'type': 'youtube',
                    '_id': kID,
                    'v_id': vID,
                    'ajax': 1,
                    'token': None,
                    'ftype': 'mp4',
                    'fquality': quality
                }
                req_link = s.post(Y2Mate_urls['convert'], data=convert_data)
                response_link = req_link.json()
                link_status = response_link['status']
                link_result = response_link['result']
                if link_status == "success":
                    print(colored('CDN link obtained successfully...', 'green'))
                    pattern_cdn = '<a href="(.*?)"'
                    cdn_link = re.search(pattern_cdn, link_result).group(1)
                    output = {
                        'link': cdn_link,
                        'title': title
                    }
                else:
                    print(colored('CDN link couldn\'t be obtained...', 'red'))
                    output = {
                        'link': None,
                        'title': title
                    }
            elif analyse_result.find('data-fquality="720"') != -1:
                quality = 720
                convert_data = {
                    'type': 'youtube',
                    '_id': kID,
                    'v_id': vID,
                    'ajax': 1,
                    'token': None,
                    'ftype': 'mp4',
                    'fquality': quality
                }
                req_link = s.post(Y2Mate_urls['convert'], data=convert_data)
                response_link = req_link.json()
                link_status = response_link['status']
                link_result = response_link['result']
                if link_status == "success":
                    print(colored('CDN link obtained successfully...', 'green'))
                    pattern_cdn = '<a href="(.*?)"'
                    cdn_link = re.search(pattern_cdn, link_result).group(1)
                    output = {
                        'link': cdn_link,
                        'title': title
                    }
                else:
                    print(colored('CDN link couldn\'t be obtained...', 'red'))
                    output = {
                        'link': None,
                        'title': title
                    }
            else:
                print(colored('Couldn\'t find any hd link... ', 'red'))
                output = {
                    'link': None,
                    'title': title
                }
    else:
        output = {
            'link': None,
            'title': None
        }

    return output





