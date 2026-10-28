import json
def load_data():
    try:
        with open('youtube.txt','r') as file:
            test=json.load(file)
            print(type(test))
            return test
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
      json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    if not videos:
        print('video is not available')
    else:
     for index,video in enumerate(videos,start=1):
        print(f"{index},{video['name']},Duration:{video['time']}")
    print("\n")
    print("*" * 70)
    
def add_videos(videos):
    name=input('Enter Video name: ')
    time=input('Enter Video time: ')
    videos.append({'name':name,'time':time})
    save_data_helper(videos)
def update_videos(videos):
    list_all_videos(videos)
    index=int(input('Enter Index Value: '))
    if 1<= index<=len(videos):
     name=input('Enter the Video name: ')
     time=input('Enter the Video time: ')
     videos[index-1]={'name':name,"time":time}
     save_data_helper(videos)
    else:
        print('Invalid Index value.')

def delete_videos(videos):
    list_all_videos(videos)
    index=int(input('Enter Index Value: '))
    if 1<= index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print('Invalid Index value.')
def main():
    videos=load_data()
    while True:
        print("\n Youtube Manager| choose an option ")
        print("1. List all Youtube Videos.")
        print("2. Add Youtube Video.")
        print("3. Update a Youtube Video details.")
        print("4. Delete Youtube Video.")
        print("5. Exit the app.")
        choice=input("Enter Your choice: ")
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                break
            case _:
                print('Invalid choice.')


if __name__=='__main__':
    main()