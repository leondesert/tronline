
from collections import defaultdict

class AirShoppingResponse:
    def __init__(self, offers, data_lists):
        """Air Shopping Response
        
        :param offers: list of offers
        :type offers: list[Offer]
        :param data_lists: data lists
        :type data_lists: DataLists
        """
        self.offers = offers
        self.data_lists = data_lists

    def grouped_offers(self):
        grouped_offers = defaultdict(list)

        # Группируем офферы по validating_party_ref_id
        for offer in self.offers:
            for offer_item in offer.offer_items:
                for fare_detail in offer_item.fare_details:
                    for fare_component in fare_detail.fare_components:
                        fare_basis_code = fare_component.fare_basis_code
                        price_class_ref_id = fare_component.price_class_ref_id

                for service in offer_item.services:
                    if service.validating_party_ref_id:
                        offer_list = {
                            "fare_basis_code": fare_basis_code,
                            "price_class_ref_id": price_class_ref_id,
                        }

                        grouped_offers[service.validating_party_ref_id].append(offer_list)

        return grouped_offers


class Offer:
    def __init__(self, offer_id, offer_items, owner_code, offer_expiration_timelimit_datetime, ticket_docs_count=None, total_price=None):
        """Offer.

        :param offer_id: offer id
        :type offer_id: str
        :param offer_items: list of offer items
        :type offer_items: list[OfferItem]
        :param owner_code: owner code
        :type owner_code: str
        :param offer_expiration_timelimit_datetime: offer expiration timelimit datetime, in UTC
        :type offer_expiration_timelimit_datetime: datetime.datetime
        :param ticket_docs_count: ticket docs count
        :type ticket_docs_count: int or None
        :param total_price: (optional) total price
        :type total_price: Price or None
        """
        self.offer_id = offer_id
        self.offer_items = offer_items
        self.owner_code = owner_code 
        self.offer_expiration_timelimit_datetime = offer_expiration_timelimit_datetime
        self.ticket_docs_count = ticket_docs_count
        self.total_price = total_price


class OfferItem:
    def __init__(self, offer_item_id, price, services, fare_details=None):
        """Offer item.

        :param offer_item_id: offer item id
        :type offer_item_id: str
        :param price: price
        :type price: Price
        :param services: list of services
        :type service: list[Service]
        :param fare_details: (optional) fare details
        :type fare_details: list[FareDetail] or None
        """
        self.offer_item_id = offer_item_id
        self.price = price
        self.services = services
        self.fare_details = fare_details


class Service:
    def __init__(self, service_id, pax_ref_ids, service_associations, validating_party_ref_id=None, validating_party_type=None, pax_types=None):
        """Service.
        
        :param service_id: service id
        :type service_id: str
        :param pax_ref_ids: list of passenger reference ids
        :type pax_ref_ids: list[str]
        :param service_associations: service offer associations
        :type service_associations: ServiceOfferAssociations
        :param validating_party_ref_id: (optional) validating party reference id
        :type validating_party_ref_id: str or None
        :param validating_party_type: (optional) validating party type
        :type validating_party_type: ValidatingParty or None
        :param pax_types: (optional) list of pax types
        :type pax_types: list[Passenger] or None
        """
        self.service_id = service_id
        self.pax_ref_ids = pax_ref_ids
        self.service_associations = service_associations
        self.validating_party_ref_id = validating_party_ref_id
        self.validating_party_type = validating_party_type
        self.pax_types = pax_types


class FareDetail:
    def __init__(self, fare_components, pax_ref_id):
        """Fare.

        :param fare_components: fare components
        :type fare_components: list[FareComponent]
        :param pax_ref_id: passenger reference id
        :type pax_ref_id: str
        """
        self.fare_components = fare_components
        self.pax_ref_id = pax_ref_id


class FareComponent:
    def __init__(self, fare_basis_code, rbd, price, pax_segment_ref_id, price_class_ref_id):
        """Fare component.
        :param fare_basis_code: fare basis code
        :type fare_basis_code: str
        :param rbd: RBD
        :type rbd: RbdAvail
        :param price: price
        :type price: Price
        :param pax_segment_ref_id: passenger segment reference id
        :type pax_segment_ref_id: str
        :param price_class_ref_id: price class reference id
        :type price_class_ref_id: str
        """
        self.fare_basis_code = fare_basis_code
        self.rbd = rbd
        self.price = price
        self.pax_segment_ref_id = pax_segment_ref_id
        self.price_class_ref_id = price_class_ref_id


class DataLists:
    def __init__(self, origin_dest_list=None, pax_journey_list=None, pax_segment_list=None, validating_party_list=None, price_class_list=None):
        """Data lists.
        
        :param origin_dest_list: list of origin destinations
        :type origin_dest_list: list[OriginDest]
        :param pax_journey_list: list of passenger journeys
        :type pax_journey_list: list[PaxJourney]
        :param pax_segment_list: list of pax segments
        :type pax_segment_list: list[PaxSegment]
        :param validating_party_list: (optional) list of validating parties
        :type validating_party_list: list[ValidatingParty] or None
        :param price_class_list: list of price classes
        :type price_class_list: list[PriceClass]
        """
        self.origin_dest_list = origin_dest_list
        self.pax_journey_list = pax_journey_list
        self.pax_segment_list = pax_segment_list
        self.price_class_list = price_class_list
        self.validating_party_list = validating_party_list

