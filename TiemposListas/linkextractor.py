import requests
import json

def extract_links(lmt=8):
    apikey = "LIVDSRZULELA"
    search_term = "excited"
    r = requests.get(f"https://g.tenor.com/v1/search?q={search_term}&key={apikey}&limit={lmt}")
    links = []
    if r.status_code == 200:
        top_8gifs = r.json()
        for x in range(min(lmt, len(top_8gifs['results']))):
            links.append({
                "text": top_8gifs['results'][x]['id'],
                "href": top_8gifs['results'][x]['media'][0]['webm']['preview']
            })
    return links

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("\nUsage:\n\t{} <URL>\n".format(sys.argv[0]))
        sys.exit(1)
    for link in extract_links(int(sys.argv[-1])):
        print(f"[{link['text']}]({link['href']})")
