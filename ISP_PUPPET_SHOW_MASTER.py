import random
import webbrowser
import time
import threading

def load_links(file_path):
    """Load URLs from a file to hypnotize your ISP into a puppet show of confusion."""
    try:
        with open(file_path, 'r') as file:
            links = file.readlines()
        return [link.strip() for link in links if link.strip()]
    except FileNotFoundError:
        print("ERROR: Puppet show script failed; Spooky.txt not found.")
        return []

def open_links_chaos(links, delay_range=(1, 5)):
    """Open random links at chaotic intervals."""
    if not links:
        print("No links found. The puppets have no stage. Fix your Spooky.txt.")
        return
    while True:
        link = random.choice(links)
        print(f"Hypnotizing ISP puppet with: {link}")
        webbrowser.open(link)
        time.sleep(random.randint(*delay_range))

def synchronized_chaos(links, threads=5, delay_range=(1, 5)):
    """Run multiple puppeteers for maximum ISP confusion."""
    puppet_threads = []
    for i in range(threads):
        t = threading.Thread(target=open_links_chaos, args=(links, delay_range))
        puppet_threads.append(t)
        t.start()
    for t in puppet_threads:
        t.join()

if __name__ == "__main__":
    print("""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      ISP HYPNOTIZER PUPPET SHOW 🤡
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Watch the puppets dance! 😈
    """)
    file_path = "Spooky.txt"
    urls = load_links(file_path)
    synchronized_chaos(urls, threads=10, delay_range=(2, 7))
  
