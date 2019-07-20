import requests

URL = "https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page={0}"


def getTopicCount(topic):
    """
    Counts the number of times a topic appears in the Wikipedia article about that topic.
    This search is case sensitive
    :param topic: topic to search on Wikipedia
    :return: integer representing the count
    """
    topic_url = URL.format(topic)
    resp = requests.get(url=topic_url)

    text = resp.json()["parse"]["text"]["*"]

    topic_len = len(topic)
    topic_count = 0

    i = 0
    while i < len(text):
        if text[i] == topic[0] and text[i:i+topic_len] == topic:
            topic_count += 1
            i += topic_len
        i += 1

    print(topic_count)
    return topic_count


if __name__ == "__main__":
    getTopicCount("pizza")
