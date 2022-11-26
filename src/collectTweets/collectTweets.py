import tweepy
import pandas as pd

def main():
    # トークン周り
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''

    auth = tweepy.OAuth1UserHandler(
        consumer_key, consumer_secret, access_token, access_token_secret
    )

    # ツイートの取得
    api = tweepy.API(auth)
    search_word = 'ワールドカップ'
    tweets = tweepy.Cursor(api.search_tweets, q = search_word, lang='ja').items(1000)
    tweet_list = [tweet.text.replace('\n', '。') for tweet in tweets]
    
    df = pd.DataFrame(tweet_list, columns=['text'])
    df.to_csv('./data/tweets.csv', encoding='utf-8', index=False)


if __name__ == "__main__":
    main()

