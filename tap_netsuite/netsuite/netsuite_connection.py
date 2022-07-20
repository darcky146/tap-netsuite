from netsuitesdk.api.accounts import Accounts
from netsuitesdk.api.classifications import Classifications
from netsuitesdk.api.departments import Departments
from netsuitesdk.api.currencies import Currencies
from netsuitesdk.api.locations import Locations
from netsuitesdk.api.vendors import Vendors
from netsuitesdk.api.subsidiaries import Subsidiaries
from netsuitesdk.api.employees import Employees
from netsuitesdk.api.expense_reports import ExpenseReports
from netsuitesdk.api.folders import Folders
from netsuitesdk.api.files import Files
from netsuitesdk.api.projects import Projects
from netsuitesdk.api.expense_categories import ExpenseCategory
from netsuitesdk.api.custom_lists import CustomLists
from netsuitesdk.api.custom_records import CustomRecords
from netsuitesdk.api.price_level import PriceLevel

import time
import json
import singer
from .transaction_entities import Customers, PurchaseOrder, Invoice, JournalEntries, InventoryTransfer, InventoryAdjustment, InventoryItem, VendorBills, VendorPayments, SalesOrders, CreditMemos, Items
from .netsuite_client import ExtendedNetSuiteClient

LOGGER = singer.get_logger()


class ExtendedNetSuiteConnection:
    def __init__(self, account, consumer_key, consumer_secret, token_key, token_secret, caching=True):
        # NetSuiteConnection.__init__(self, account, consumer_key, consumer_secret, token_key, token_secret)
        # ns_client: NetSuiteClient = self.client

        ns_client = ExtendedNetSuiteClient(account=account, caching=caching)
        ns_client.connect_tba(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            token_key=token_key,
            token_secret=token_secret
        )
        self.client = ns_client
        self.departments = Departments(ns_client)
        self.currencies = Currencies(ns_client)
        self.locations = Locations(ns_client)
        self.vendor_bills = VendorBills(ns_client)
        self.vendors = Vendors(ns_client)
        self.subsidiaries = Subsidiaries(ns_client)
        self.employees = Employees(ns_client)
        self.expense_reports = ExpenseReports(ns_client)
        self.folders = Folders(ns_client)
        self.files = Files(ns_client)
        self.expense_categories = ExpenseCategory(ns_client)
        self.custom_lists = CustomLists(ns_client)
        self.custom_records = CustomRecords(ns_client)
        self.projects = Projects(ns_client)
        self.vendor_payments = VendorPayments(ns_client)
        self.invoice = Invoice(ns_client)

        self.entities = {
            'Customer': Customers(ns_client),
            'Invoice': Invoice(ns_client),
            'Accounts': Accounts(ns_client),
            'JournalEntry': JournalEntries(ns_client),
            'Commission': JournalEntries(ns_client),
            'Classifications': Classifications(ns_client),
            'Vendors': self.vendors,
            'VendorBills': self.vendor_bills,
            'VendorPayment': self.vendor_payments,
            'InventoryAdjustment': InventoryAdjustment(ns_client),
            'InventoryTransfer': InventoryTransfer(ns_client),
            'PriceLevel': PriceLevel(ns_client),
            'InventoryItem': InventoryItem(ns_client),
            'SalesOrders': SalesOrders(ns_client),
            'CreditMemos': CreditMemos(ns_client),
            'Items': Items(ns_client),
            'PurchaseOrder': PurchaseOrder(ns_client)
        }            'NonInventorySaleItem': NonInventorySaleItem(ns_client),
            'SupportCaseStatus': SupportCaseStatus(ns_client),
            'LeadSource': LeadSource(ns_client),
            'CurrencyRate': CurrencyRate(ns_client),
            'WinLossReason': WinLossReason(ns_client),
            'SupportCaseOrigin': SupportCaseOrigin(ns_client),
            'Deposit': Deposit(ns_client),
            'TaxGroup': TaxGroup(ns_client),
            'TransactionColumnCustomField': TransactionColumnCustomField(ns_client),
            'ItemNumberCustomField': ItemNumberCustomField(ns_client),
            'StatisticalJournalEntry': StatisticalJournalEntry(ns_client),
            'InventoryDetail': InventoryDetail(ns_client),
            'CampaignSearchEngine': CampaignSearchEngine(ns_client),
            'GlobalAccountMapping': GlobalAccountMapping(ns_client),
            'FairValuePrice': FairValuePrice(ns_client),
            'SupportCaseType': SupportCaseType(ns_client),
            'Solution': Solution(ns_client),
            'RevRecTemplate': RevRecTemplate(ns_client),
            'TimeBill': TimeBill(ns_client),
            'Charge': Charge(ns_client),
            'InterCompanyTransferOrder': InterCompanyTransferOrder(ns_client),
            'ItemRevision': ItemRevision(ns_client),
            'Contact': Contact(ns_client),
            'CampaignResponse': CampaignResponse(ns_client),
            'PromotionCode': PromotionCode(ns_client),
            'WorkOrderClose': WorkOrderClose(ns_client),
            'PurchaseRequisition': PurchaseRequisition(ns_client),
            'JobType': JobType(ns_client),
            'Term': Term(ns_client),
            'Issue': Issue(ns_client),
            'ManufacturingRouting': ManufacturingRouting(ns_client),
            'ServiceSaleItem': ServiceSaleItem(ns_client),
            'InventoryCostRevaluation': InventoryCostRevaluation(ns_client),
            'UnitsType': UnitsType(ns_client),
            'EntityGroup': EntityGroup(ns_client),
            'DepositApplication': DepositApplication(ns_client),
            'SalesTaxItem': SalesTaxItem(ns_client),
            'CustomTransaction': CustomTransaction(ns_client),
            'LandedCost': LandedCost(ns_client),
            'Task': Task(ns_client),
            'TimeSheet': TimeSheet(ns_client),
            'GiftCertificate': GiftCertificate(ns_client),
            'KitItem': KitItem(ns_client),
            'DescriptionItem': DescriptionItem(ns_client),
            'ItemFulfillment': ItemFulfillment(ns_client),
            'ContactCategory': ContactCategory(ns_client),
            'CustomerMessage': CustomerMessage(ns_client),
            'OtherChargeResaleItem': OtherChargeResaleItem(ns_client),
            'NoteType': NoteType(ns_client),
            'VendorReturnAuthorization': VendorReturnAuthorization(ns_client),
            'Job': Job(ns_client),
            'CampaignSubscription': CampaignSubscription(ns_client),
            'CampaignFamily': CampaignFamily(ns_client),
            'CrmCustomField': CrmCustomField(ns_client),
            'BinWorksheet': BinWorksheet(ns_client),
            'SerializedInventoryItem': SerializedInventoryItem(ns_client),
            'DiscountItem': DiscountItem(ns_client),
            'CustomerRefund': CustomerRefund(ns_client),
            'TransferOrder': TransferOrder(ns_client),
            'PartnerCategory': PartnerCategory(ns_client),
            'OtherChargePurchaseItem': OtherChargePurchaseItem(ns_client),
            'BinTransfer': BinTransfer(ns_client),
            'VendorBill': VendorBills(ns_client),
            'PaymentMethod': PaymentMethod(ns_client),
            'ItemAccountMapping': ItemAccountMapping(ns_client),
            'CustomerStatus': CustomerStatus(ns_client),
            'Estimate': Estimate(ns_client),
            'SalesRole': SalesRole(ns_client),
            'ManufacturingCostTemplate': ManufacturingCostTemplate(ns_client),
            'AssemblyUnbuild': AssemblyUnbuild(ns_client),
            'ItemSupplyPlan': ItemSupplyPlan(ns_client),
            'NonInventoryResaleItem': NonInventoryResaleItem(ns_client),
            'BillingSchedule': BillingSchedule(ns_client),
            'PaymentItem': PaymentItem(ns_client),
            'ItemGroup': ItemGroup(ns_client),
            'WorkOrder': WorkOrder(ns_client),
            'WorkOrderIssue': WorkOrderIssue(ns_client),
            'SupportCaseIssue': SupportCaseIssue(ns_client),
            'ContactRole': ContactRole(ns_client),
            'CustomerPayment': CustomerPayment(ns_client),
            'PricingGroup': PricingGroup(ns_client),
            'SupportCasePriority': SupportCasePriority(ns_client),
            'Campaign': Campaign(ns_client),
            'LotNumberedAssemblyItem': LotNumberedAssemblyItem(ns_client),
            'InventoryNumber': InventoryNumber(ns_client),
            'VendorCredit': VendorCredit(ns_client),
            'CustomRecordCustomField': CustomRecordCustomField(ns_client),
            'CustomerDeposit': CustomerDeposit(ns_client),
            'SupportCase': SupportCase(ns_client),
            'ServicePurchaseItem': ServicePurchaseItem(ns_client),
            'CampaignOffer': CampaignOffer(ns_client),
            'CampaignAudience': CampaignAudience(ns_client),
            'ServiceResaleItem': ServiceResaleItem(ns_client),
            'CustomerCategory': CustomerCategory(ns_client),
            'RevRecSchedule': RevRecSchedule(ns_client),
            'CashSale': CashSale(ns_client),
            'CalendarEvent': CalendarEvent(ns_client),
            'CampaignVertical': CampaignVertical(ns_client),
            'OtherCustomField': OtherCustomField(ns_client),
            'EntityCustomField': EntityCustomField(ns_client),
            'PayrollItem': PayrollItem(ns_client),
            'SerializedAssemblyItem': SerializedAssemblyItem(ns_client),
            'OtherNameCategory': OtherNameCategory(ns_client),
            'ReturnAuthorization': ReturnAuthorization(ns_client),
            'Nexus': Nexus(ns_client),
            'TransactionBodyCustomField': TransactionBodyCustomField(ns_client),
            'WorkOrderCompletion': WorkOrderCompletion(ns_client),
            'BudgetCategory': BudgetCategory(ns_client),
            'SiteCategory': SiteCategory(ns_client),
            'DownloadItem': DownloadItem(ns_client),
            'CustomRecordType': CustomRecordType(ns_client),
            'ItemOptionCustomField': ItemOptionCustomField(ns_client),
            'CashRefund': CashRefund(ns_client),
            'ResourceAllocation': ResourceAllocation(ns_client),
            'ItemReceipt': ItemReceipt(ns_client),
            'ManufacturingOperationTask': ManufacturingOperationTask(ns_client),
            'PhoneCall': PhoneCall(ns_client),
            'BillingAccount': BillingAccount(ns_client),
            'NonInventoryPurchaseItem': NonInventoryPurchaseItem(ns_client),
            'MarkupItem': MarkupItem(ns_client),
            'ProjectTask': ProjectTask(ns_client),
            'PaycheckJournal': PaycheckJournal(ns_client),
            'Partner': Partner(ns_client),
            'AssemblyItem': AssemblyItem(ns_client),
            'GiftCertificateItem': GiftCertificateItem(ns_client),
            'JobStatus': JobStatus(ns_client),
            'InterCompanyJournalEntry': InterCompanyJournalEntry(ns_client),
            'Budget': Budget(ns_client),
            'OtherChargeSaleItem': OtherChargeSaleItem(ns_client),
            'Note': Note(ns_client),
            'AssemblyBuild': AssemblyBuild(ns_client),
            'Bin': Bin(ns_client),
            'CampaignCategory': CampaignCategory(ns_client),
            'TimeEntry': TimeEntry(ns_client),
            'Check': Check(ns_client),
            'ItemCustomField': ItemCustomField(ns_client),
            'Message': Message(ns_client)
        }

    def _query_entity(self, data, entity, stream):
        to_get_results_for = data.get(stream)
        for element in to_get_results_for:
            start_time = time.time()
            internal_id = element.get('internalId')
            LOGGER.info(f"fetching data for internalId {internal_id}")
            to_return = entity.get(internalId=internal_id)
            LOGGER.info(f"Successfully fetched data for internalId {internal_id} --- %s seconds ---" % (
                        time.time() - start_time))
            yield to_return

    def query_entity(self, stream=None, lastModifiedDate=None):
        start_time = time.time()
        LOGGER.info(f"Starting fetch data for stream {stream}")
        entity = self.entities[stream]

        if hasattr(entity, 'require_lastModified_date') and entity.require_lastModified_date is True:
            data = entity.get_all(lastModifiedDate)
        else:
            data = entity.get_all()

        # It is broken, maybe because of the change in the _paginated_search_to_generator in the API
        # if hasattr(entity, 'require_paging') and entity.require_paging is True:
        #     transformed_data = json.dumps({stream: data}, default=str, indent=2)
        #     data = json.loads(transformed_data)
        #     to_return = list(self._query_entity(data, entity, stream))
        # else:
        to_return = data

        LOGGER.info(f"Successfully fetched data for stream {stream}")
        LOGGER.info("--- %s seconds ---" % (time.time() - start_time))

        # with open('/tmp/salesorders.json', 'w') as oj:
        #     oj.write(json.dumps({stream: to_return}, default=str, indent=2))

        return to_return
