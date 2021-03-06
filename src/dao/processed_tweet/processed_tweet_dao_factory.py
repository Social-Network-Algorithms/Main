from src.dao.processed_tweet.setter.processed_tweet_setter import ProcessedTweetSetter
from src.dao.processed_tweet.setter.mongo_processed_tweet_setter import MongoProcessedTweetSetter
from src.dao.processed_tweet.getter.processed_tweet_getter import ProcessedTweetGetter
from src.dao.processed_tweet.getter.mongo_processed_tweet_getter import MongoProcessedTweetGetter
from src.dao.mongo.mongo_dao_factory import MongoDAOFactory
from src.shared.mongo import get_collection_from_config
from typing import Dict


class ProcessedTweetDAOFactory():
    def create_getter(config: Dict) -> ProcessedTweetGetter:
        processed_tweet_getter = None
        if config["type"] == "Mongo":
            processed_tweet_getter = MongoProcessedTweetGetter()
            collection = get_collection_from_config(config["config"])
            processed_tweet_getter.set_collection(collection)
        else:
            raise Exception("Datastore type not supported")

        return processed_tweet_getter

    def create_setter(config: Dict) -> ProcessedTweetSetter:
        processed_tweet_setter = None
        if config["type"] == "Mongo":
            processed_tweet_setter = MongoProcessedTweetSetter()
            collection = get_collection_from_config(config["config"])
            processed_tweet_setter.set_collection(collection)
        else:
            raise Exception("Datastore type not supported")

        return processed_tweet_setter