import pandas as pd
import re
import neologdn


def main():
    df = pd.read_csv("./data/tweets.csv")
    tweet_list = []
    symbol = "[!\"#$%&'\\\\()*+,-./:;<=>?@[\\]^_`{|}~「」〔〕“”◇ᴗ●↓→♪★⊂⊃※△□◎〈〉『』【】＆＊・（）＄＃＠。、？！｀＋￥％]"

    for text in df.text:

        # 記号削除
        text = re.sub(symbol, " ", text)

        if text != "":
            tweet_list.append(text)

    df = pd.DataFrame(tweet_list, columns=["text"])
    df.to_csv("./data/processingTweets.csv", encoding="utf-8", index=False)


if __name__ == "__main__":
    main()
