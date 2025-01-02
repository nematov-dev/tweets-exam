import queries


def show_tweets() -> str:
    tweets = queries.show_tweets_query()
    message = f" Tweets all: {100 * '-'}\n\n"
    if tweets:
        for tweet in tweets:
             message += f"ID: {tweet[0]}\n Autor: {tweet[2]}\n Text: {tweet[3]}\n Datetime: {tweet[4]}\n\n{100 * '-'}"
        return message
    else:
        message = "Tweets not found"
        return message
    

def add_tweet() -> str:
    user_id = queries.get_active_user()[0]
    full_name = input("Enter your fullname: ")
    text = input("Enter your Text: ")
    if queries.add_tweet_query(user_id=user_id,full_name=full_name,text=text):
        message = "Your tweet has been added"
        return message
    else:
        message = "Something went wrong"
        return message


def update_tweet() -> str:
    user_id = queries.get_active_user()[0]
    text_id = int(input("Enter your tweet id: "))
    new_text = input("Enter your new text: ")

    if queries.get_tweet(user_id=user_id,text_id=text_id):
        if queries.update_tweet_query(user_id=user_id,text_id=text_id,text=new_text):
            message = "Your tweet has been updated"
            return message
        else:
            message = "Something went wrong"
            return message
    else:
        message = "Tweet id not found"
        return message
    

def delete_tweet():
    user_id = queries.get_active_user()[0]
    text_id = int(input("Enter your tweet id: "))
    if queries.get_tweet(user_id=user_id,text_id=text_id):
        if queries.delete_tweet_query(user_id=user_id,text_id=text_id):
            message = "Your tweet has been delete"
            return message
        else:
            message = "Something went wrong"
            return message
    else:
        message = "Tweet id not found"
        return message
        
def show_my_tweets():
    user_id = queries.get_active_user()[0]
    message = f"Your Tweets: {100 * '-'}\n\n"
    tweets = queries.show_my_tweets_query(user_id=user_id)
    if tweets:
        for tweet in tweets:
            message += f"id: {tweet[0]}\nauth: {tweet[2]}\ntext: {tweet[3]}\n\n{100 * '-'}"
        return message
    else:
        message = "Tweets not found"
        return message