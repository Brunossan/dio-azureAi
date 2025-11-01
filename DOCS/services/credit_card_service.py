from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeBatchDocumentsRequest
from utils.config import config

def analyze_credit_card(cardUrl):
    document_client = DocumentIntelligenceClient(
        endpoint=config.ENDPOINT,
        credential=AzureKeyCredential(config.KEY)
    )

    card_info = document_client.begin_read_document("prebuilt_creditCard", AnalyzeBatchDocumentsRequest(url_source=cardUrl))
    result = card_info.result()

    for document in result.documents:
        fields = document.get('fields', {})
        
        return {
            "card_name": fields.get("CardholderName", {}).get('content') if "CardholderName" in fields else None,
            "card_number": fields.get("CardNumber", {}).get('content') if "CardNumber" in fields else None,
            "expiry_date": fields.get("ExpirationDate", {}).get('content') if "ExpirationDate" in fields else None,
            "bank_name": fields.get("IssuingBank", {}).get('content') if "IssuingBank" in fields else None,
        }

    return card_info.result()
