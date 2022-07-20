from collections import OrderedDict
from netsuitesdk.internal.utils import PaginatedSearch

from netsuitesdk.api.base import ApiBase

import singer

logger = singer.get_logger()


def prepare_custom_fields(that, eod):
    if 'customFieldList' in eod and eod['customFieldList']:
        custom_fields = []
        for field in eod['customFieldList']:
            if field['type'] == 'String':
                custom_fields.append(
                    that.ns_client.StringCustomFieldRef(
                        scriptId=field['scriptId'] if 'scriptId' in field else None,
                        internalId=field['internalId'] if 'internalId' in field else None,
                        value=field['value']
                    )
                )
            elif field['type'] == 'Select':
                custom_fields.append(
                    that.ns_client.SelectCustomFieldRef(
                        scriptId=field['scriptId'] if 'scriptId' in field else None,
                        internalId=field['internalId'] if 'internalId' in field else None,
                        value=self.ns_client.ListOrRecordRef(
                            internalId=field['value']
                        )
                    )
                )
        return that.ns_client.CustomFieldList(custom_fields)

    return None


class Customers(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='customer')
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        search_record = self.ns_client.basic_search_factory(type_name="Customer",
                                                            lastModifiedDate=last_modified_date)
        ps = PaginatedSearch(client=self.ns_client, type_name='Customer', pageSize=page_size,
                             search_record=search_record)
        return self._paginated_search_to_generator(ps)

    def post(self, data) -> OrderedDict:
        return None

class InventoryItem(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='InventoryItem')
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='InventoryItem', operator='contains')
        search_record = self.ns_client.basic_search_factory(type_name="Item",
                                                            recordType=record_type_search_field,
                                                            lastModifiedDate=last_modified_date)
        ps = PaginatedSearch(client=self.ns_client, type_name='InventoryItem', pageSize=page_size,
                             search_record=search_record)
        return self._paginated_search_to_generator(ps)

    def post(self, data) -> OrderedDict:
        return None


class Opportunity(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='opportunity')
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='Opportunity', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction', recordType=record_type_search_field,
                                                           lastModifiedDate=last_modified_date)
        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)
        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class SalesOrders(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='salesOrder')
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='SalesOrder', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)
        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)
        
        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class InventoryTransfer(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='InventoryTransfer')
    
    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='InventoryTransfer', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           recordType=record_type_search_field,
                                                           lastModifiedDate=last_modified_date)
        paginated_search = PaginatedSearch(client=self.ns_client,
                                           type_name='Transaction',
                                           basic_search=basic_search,
                                           pageSize=page_size)
        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class Items(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Item')
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        search_record = self.ns_client.basic_search_factory(type_name="Item",
                                                            lastModifiedDate=last_modified_date)
        ps = PaginatedSearch(client=self.ns_client, type_name='Item', pageSize=page_size,
                             search_record=search_record)
        return self._paginated_search_to_generator(ps)

    def post(self, data) -> OrderedDict:
        return None


class InventoryAdjustment(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='InventoryAdjustment')
    
    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='InventoryAdjustment', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           recordType=record_type_search_field,
                                                           lastModifiedDate=last_modified_date)
        paginated_search = PaginatedSearch(client=self.ns_client,
                                           type_name='Transaction',
                                           basic_search=basic_search,
                                           pageSize=page_size)
        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None
    

class VendorBills(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='VendorBills')
    
    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='VendorBill', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           recordType=record_type_search_field,
                                                           lastModifiedDate=last_modified_date)
        paginated_search = PaginatedSearch(client=self.ns_client,
                                           type_name='Transaction',
                                           basic_search=basic_search,
                                           pageSize=page_size)
        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None
    
class VendorPayments(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='VendorPayment')
    
    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='VendorPayment', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           recordType=record_type_search_field,
                                                           lastModifiedDate=last_modified_date)
        paginated_search = PaginatedSearch(client=self.ns_client,
                                           type_name='Transaction',
                                           basic_search=basic_search,
                                           pageSize=page_size)
        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class JournalEntries(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='journalEntry')
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='JournalEntry', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        assert data['externalId'], 'missing external id'
        je = self.ns_client.JournalEntry(externalId=data['externalId'])
        line_list = []
        for eod in data['lineList']:
            eod['customFieldList'] = prepare_custom_fields(self, eod)
            jee = self.ns_client.JournalEntryLine(**eod)
            line_list.append(jee)

        je['lineList'] = self.ns_client.JournalEntryLineList(line=line_list)
        je['currency'] = self.ns_client.RecordRef(**(data['currency']))

        if 'memo' in data:
            je['memo'] = data['memo']

        if 'tranDate' in data:
            je['tranDate'] = data['tranDate']

        if 'tranId' in data:
            je['tranId'] = data['tranId']

        if 'subsidiary' in data:
            je['subsidiary'] = data['subsidiary']

        if 'class' in data:
            je['class'] = data['class']

        if 'location' in data:
            je['location'] = data['location']

        if 'department' in data:
            je['department'] = data['department']

        logger.info(
            f"Posting JournalEntries now with {len(je['lineList']['line'])} entries. ExternalId {je['externalId']} tranDate {je['tranDate']}")
        res = self.ns_client.upsert(je)
        return self._serialize(res)


class Invoice(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='invoice')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='Invoice', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class CreditMemos(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='creditmemo')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='CreditMemo', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None

class PurchaseOrder(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='PurchaseOrder')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='PurchaseOrder', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None

class Address(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Address')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='Address', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class CustomFieldType(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='CustomFieldType')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='CustomFieldType', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class SubtotalItem(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='SubtotalItem')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='SubtotalItem', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class Topic(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Topic')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='Topic', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class CostCategory(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='CostCategory')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='CostCategory', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class ItemDemandPlan(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='ItemDemandPlan')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='ItemDemandPlan', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class Department(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Department')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='Department', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class LotNumberedInventoryItem(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='LotNumberedInventoryItem')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='LotNumberedInventoryItem',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class CampaignChannel(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='CampaignChannel')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='CampaignChannel', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class State(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='State')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='State', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class TaxAcct(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='TaxAcct')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='TaxAcct', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class CouponCode(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='CouponCode')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='CouponCode', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class VendorCategory(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='VendorCategory')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='VendorCategory', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class TaxType(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='TaxType')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='TaxType', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class NonInventorySaleItem(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='NonInventorySaleItem')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='NonInventorySaleItem',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class SupportCaseStatus(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='SupportCaseStatus')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='SupportCaseStatus',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class LeadSource(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='LeadSource')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='LeadSource', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class CurrencyRate(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='CurrencyRate')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='CurrencyRate', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class Folder(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Folder')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='Folder', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class Location(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Location')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='Location', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class WinLossReason(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='WinLossReason')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='WinLossReason', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class SupportCaseOrigin(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='SupportCaseOrigin')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='SupportCaseOrigin',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None



class Deposit(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Deposit')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='Deposit', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class TaxGroup(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='TaxGroup')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='TaxGroup', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class TransactionColumnCustomField(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='TransactionColumnCustomField')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='TransactionColumnCustomField',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class ItemNumberCustomField(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='ItemNumberCustomField')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='ItemNumberCustomField',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class StatisticalJournalEntry(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='StatisticalJournalEntry')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='StatisticalJournalEntry',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class InventoryDetail(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='InventoryDetail')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='InventoryDetail', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class CampaignSearchEngine(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='CampaignSearchEngine')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='CampaignSearchEngine',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class GlobalAccountMapping(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='GlobalAccountMapping')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='GlobalAccountMapping',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class FairValuePrice(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='FairValuePrice')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='FairValuePrice', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class SupportCaseType(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='SupportCaseType')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='SupportCaseType', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class Solution(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Solution')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='Solution', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class RevRecTemplate(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='RevRecTemplate')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='RevRecTemplate', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class TimeBill(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='TimeBill')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='TimeBill', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class Charge(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Charge')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='Charge', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class Subsidiary(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Subsidiary')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='Subsidiary', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class InterCompanyTransferOrder(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='InterCompanyTransferOrder')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='InterCompanyTransferOrder',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class ItemRevision(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='ItemRevision')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='ItemRevision', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class Contact(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Contact')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='Contact', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class CampaignResponse(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='CampaignResponse')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='CampaignResponse', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class PromotionCode(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='PromotionCode')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='PromotionCode', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class WorkOrderClose(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='WorkOrderClose')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='WorkOrderClose', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class Classification(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Classification')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='Classification', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class PurchaseRequisition(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='PurchaseRequisition')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='PurchaseRequisition',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class JobType(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='JobType')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='JobType', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class Term(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Term')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='Term', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None



class Issue(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Issue')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='Issue', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class ManufacturingRouting(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='ManufacturingRouting')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='ManufacturingRouting',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class ServiceSaleItem(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='ServiceSaleItem')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='ServiceSaleItem', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class ExpenseReport(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='ExpenseReport')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='ExpenseReport', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None



class InventoryCostRevaluation(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='InventoryCostRevaluation')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='InventoryCostRevaluation',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class UnitsType(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='UnitsType')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='UnitsType', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class EntityGroup(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='EntityGroup')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='EntityGroup', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class DepositApplication(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='DepositApplication')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='DepositApplication',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class SalesTaxItem(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='SalesTaxItem')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='SalesTaxItem', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class CustomTransaction(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='CustomTransaction')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='CustomTransaction',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class LandedCost(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='LandedCost')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='LandedCost', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class Task(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Task')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='Task', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class TimeSheet(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='TimeSheet')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='TimeSheet', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class GiftCertificate(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='GiftCertificate')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='GiftCertificate', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class KitItem(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='KitItem')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='KitItem', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class DescriptionItem(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='DescriptionItem')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='DescriptionItem', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class ItemFulfillment(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='ItemFulfillment')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='ItemFulfillment', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class ContactCategory(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='ContactCategory')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='ContactCategory', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class CustomerMessage(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='CustomerMessage')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='CustomerMessage', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class OtherChargeResaleItem(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='OtherChargeResaleItem')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='OtherChargeResaleItem',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class NoteType(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='NoteType')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='NoteType', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class VendorReturnAuthorization(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='VendorReturnAuthorization')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='VendorReturnAuthorization',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None



class Job(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Job')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='Job', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class ExpenseCategory(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='ExpenseCategory')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='ExpenseCategory', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class CampaignSubscription(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='CampaignSubscription')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='CampaignSubscription',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class CampaignFamily(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='CampaignFamily')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='CampaignFamily', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class CrmCustomField(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='CrmCustomField')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='CrmCustomField', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class BinWorksheet(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='BinWorksheet')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='BinWorksheet', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class SerializedInventoryItem(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='SerializedInventoryItem')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='SerializedInventoryItem',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class DiscountItem(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='DiscountItem')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='DiscountItem', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class CustomerRefund(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='CustomerRefund')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='CustomerRefund', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class TransferOrder(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='TransferOrder')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='TransferOrder', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class PartnerCategory(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='PartnerCategory')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='PartnerCategory', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class OtherChargePurchaseItem(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='OtherChargePurchaseItem')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='OtherChargePurchaseItem',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class BinTransfer(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='BinTransfer')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='BinTransfer', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class PaymentMethod(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='PaymentMethod')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='PaymentMethod', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class ItemAccountMapping(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='ItemAccountMapping')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='ItemAccountMapping',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class CustomerStatus(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='CustomerStatus')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='CustomerStatus', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None



class Estimate(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Estimate')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='Estimate', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class SalesRole(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='SalesRole')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='SalesRole', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class ManufacturingCostTemplate(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='ManufacturingCostTemplate')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='ManufacturingCostTemplate',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class AssemblyUnbuild(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='AssemblyUnbuild')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='AssemblyUnbuild', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class ItemSupplyPlan(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='ItemSupplyPlan')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='ItemSupplyPlan', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class NonInventoryResaleItem(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='NonInventoryResaleItem')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='NonInventoryResaleItem',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class BillingSchedule(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='BillingSchedule')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='BillingSchedule', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class PaymentItem(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='PaymentItem')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='PaymentItem', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class CustomRecord(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='CustomRecord')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='CustomRecord', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class ItemGroup(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='ItemGroup')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='ItemGroup', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class WorkOrder(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='WorkOrder')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='WorkOrder', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class WorkOrderIssue(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='WorkOrderIssue')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='WorkOrderIssue', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class SupportCaseIssue(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='SupportCaseIssue')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='SupportCaseIssue', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class ContactRole(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='ContactRole')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='ContactRole', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class CustomerPayment(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='CustomerPayment')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='CustomerPayment', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class Employee(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Employee')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='Employee', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class PricingGroup(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='PricingGroup')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='PricingGroup', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class Vendor(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Vendor')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='Vendor', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class SupportCasePriority(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='SupportCasePriority')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='SupportCasePriority',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class Campaign(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Campaign')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='Campaign', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class LotNumberedAssemblyItem(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='LotNumberedAssemblyItem')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='LotNumberedAssemblyItem',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class InventoryNumber(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='InventoryNumber')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='InventoryNumber', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class VendorCredit(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='VendorCredit')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='VendorCredit', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class CustomRecordCustomField(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='CustomRecordCustomField')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='CustomRecordCustomField',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class CustomerDeposit(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='CustomerDeposit')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='CustomerDeposit', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class SupportCase(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='SupportCase')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='SupportCase', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class ServicePurchaseItem(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='ServicePurchaseItem')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='ServicePurchaseItem',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class CampaignOffer(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='CampaignOffer')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='CampaignOffer', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None



class CampaignAudience(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='CampaignAudience')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='CampaignAudience', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class AccountingPeriod(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='AccountingPeriod')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='AccountingPeriod', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class ServiceResaleItem(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='ServiceResaleItem')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='ServiceResaleItem',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class CustomerCategory(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='CustomerCategory')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='CustomerCategory', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class RevRecSchedule(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='RevRecSchedule')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='RevRecSchedule', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class CashSale(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='CashSale')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='CashSale', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class CalendarEvent(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='CalendarEvent')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='CalendarEvent', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class File(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='File')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='File', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class CampaignVertical(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='CampaignVertical')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='CampaignVertical', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class OtherCustomField(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='OtherCustomField')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='OtherCustomField', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class Account(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Account')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='Account', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class EntityCustomField(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='EntityCustomField')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='EntityCustomField',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class PayrollItem(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='PayrollItem')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='PayrollItem', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class SerializedAssemblyItem(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='SerializedAssemblyItem')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='SerializedAssemblyItem',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class OtherNameCategory(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='OtherNameCategory')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='OtherNameCategory',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class ReturnAuthorization(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='ReturnAuthorization')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='ReturnAuthorization',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class CustomList(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='CustomList')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='CustomList', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class Nexus(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Nexus')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='Nexus', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class TransactionBodyCustomField(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='TransactionBodyCustomField')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='TransactionBodyCustomField',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class WorkOrderCompletion(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='WorkOrderCompletion')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='WorkOrderCompletion',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class BudgetCategory(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='BudgetCategory')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='BudgetCategory', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class SiteCategory(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='SiteCategory')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='SiteCategory', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class DownloadItem(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='DownloadItem')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='DownloadItem', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class CustomRecordType(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='CustomRecordType')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='CustomRecordType', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class ItemOptionCustomField(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='ItemOptionCustomField')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='ItemOptionCustomField',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class CashRefund(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='CashRefund')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='CashRefund', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class ResourceAllocation(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='ResourceAllocation')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='ResourceAllocation',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class ItemReceipt(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='ItemReceipt')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='ItemReceipt', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class ManufacturingOperationTask(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='ManufacturingOperationTask')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='ManufacturingOperationTask',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class PhoneCall(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='PhoneCall')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='PhoneCall', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class BillingAccount(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='BillingAccount')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='BillingAccount', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class NonInventoryPurchaseItem(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='NonInventoryPurchaseItem')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='NonInventoryPurchaseItem',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class MarkupItem(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='MarkupItem')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='MarkupItem', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class ProjectTask(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='ProjectTask')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='ProjectTask', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class PaycheckJournal(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='PaycheckJournal')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='PaycheckJournal', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class Partner(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Partner')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='Partner', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class AssemblyItem(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='AssemblyItem')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='AssemblyItem', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class GiftCertificateItem(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='GiftCertificateItem')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='GiftCertificateItem',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class PriceLevel(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='PriceLevel')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='PriceLevel', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class JobStatus(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='JobStatus')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='JobStatus', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class InterCompanyJournalEntry(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='InterCompanyJournalEntry')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='InterCompanyJournalEntry',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class Budget(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Budget')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='Budget', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class OtherChargeSaleItem(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='OtherChargeSaleItem')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='OtherChargeSaleItem',
                                                                    operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class Note(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Note')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='Note', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class AssemblyBuild(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='AssemblyBuild')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='AssemblyBuild', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class Currency(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Currency')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='Currency', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class Bin(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Bin')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='Bin', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class CampaignCategory(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='CampaignCategory')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='CampaignCategory', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class TimeEntry(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='TimeEntry')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='TimeEntry', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class Check(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Check')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='Check', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class ItemCustomField(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='ItemCustomField')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='ItemCustomField', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None


class Message(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Message')
        self.require_paging = True
        self.require_lastModified_date = True

    def get_all(self, last_modified_date=None):
        return self.get_all_generator(last_modified_date=last_modified_date)

    def get_all_generator(self, page_size=200, last_modified_date=None):
        record_type_search_field = self.ns_client.SearchStringField(searchValue='Message', operator='contains')
        basic_search = self.ns_client.basic_search_factory('Transaction',
                                                           lastModifiedDate=last_modified_date,
                                                           recordType=record_type_search_field)

        paginated_search = PaginatedSearch(client=self.ns_client,
                                           basic_search=basic_search,
                                           type_name='Transaction',
                                           pageSize=page_size)

        return self._paginated_search_to_generator(paginated_search=paginated_search)

    def post(self, data) -> OrderedDict:
        return None
