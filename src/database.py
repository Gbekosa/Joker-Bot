import os.path

DATABASE_DIR = '~/joker-bot/src/database/' # You may need to change this
#if you are on a different platform

#File with all reddit jokes
MASTER_REDDIT = DATABASE_DIR+'MASTER_REDDIT.joke'
# functions to save and load jokes to database
def save_reddit_jokes(jokes):
    file_name = os.path.expanduser(MASTER_REDDIT)
    f = open(file_name, 'w')
    for joke in jokes: 
        title = joke[0] 
        text = joke[1]
        score = joke[2]
        flair = joke[3]
        f.write("[START]"+ title + "***\n" + text + "***\n" + str(score) + "***\d" + str(flair) + "[END]\n")
    f.close()
    print("Saved succesfully.")

if __name__ == "__main__":
    import sys

    

