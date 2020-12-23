import networkx as nx
from src.model.social_graph.social_graph import SocialGraph
from src.model.social_graph.union_social_graph import UnionSocialGraph
from src.model.social_graph.intersection_social_graph import IntersectionSocialGraph
from src.dao.social_graph.setter.social_graph_setter import SocialGraphSetter
from src.dao.local_neighbourhood.getter.local_neighbourhood_getter import LocalNeighbourhoodGetter


class SocialGraphConstructor():
    """
    Creates a graph of twitter friends representing a community
    """

    def __init__(self, local_neighbourhood_getter: LocalNeighbourhoodGetter, social_graph_setter: SocialGraphSetter):
        self.local_neighbourhood_getter = local_neighbourhood_getter
        self.social_graph_setter = social_graph_setter

    def construct_social_graph_from_local_neighbourhood(self, seed_id, params=None, is_union=True):
        local_neighbourhood = self.local_neighbourhood_getter.get_local_neighbourhood(seed_id, params)

        social_graph = None
        if is_union:
            social_graph = UnionSocialGraph.fromLocalNeighbourhood(local_neighbourhood)
        else:
            social_graph = IntersectionSocialGraph.fromLocalNeighbourhood(local_neighbourhood)

        self.social_graph_setter.store_social_graph(social_graph)
