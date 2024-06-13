import time
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import resumeMatcher  # Import the Python script as a module

LINK_FILE = "links.json"

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        print(f"Detected new file: {event.src_path}")
        # Run your Python script here
        #resumeMatcher.convertResumeToText(event.src_path)
        open(LINK_FILE, 'w').close()
        linkedInLink = resumeMatcher.findLinkedIn()
        indeedLink = resumeMatcher.findIndeed()
        diceLink = resumeMatcher.findDice()
        simplyLink = resumeMatcher.findSimplyHired()
        glassLink = resumeMatcher.findGlassDoor()
        usaLink = resumeMatcher.findUSAJobs()
        jobLinks =[linkedInLink,indeedLink,diceLink,simplyLink,glassLink,usaLink]

        if jobLinks:
            with open(LINK_FILE, "w") as json_file:
                json.dump(jobLinks, json_file)




def watch_folder(folder):
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, folder, recursive=True)
    observer.start()
    print(f"Watching folder: {folder}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    folder_path = 'uploads'
    watch_folder(folder_path)


# def write_job_links(job_links):
#     with open('job_links.json', 'w') as f:
#         json.dump(job_links, f)


