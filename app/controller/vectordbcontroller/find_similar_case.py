from langchain_astradb import AstraDBVectorStore
from langchain_core.documents import Document
from astrapy.info import VectorServiceOptions
from app.core.config import settings
from typing import List, Dict, Any


vector_store = AstraDBVectorStore(
    collection_name="case_laws",
    api_endpoint=settings.ASTRA_DB_API_ENDPOINT,
    token=settings.ASTRA_DB_APPLICATION_TOKEN,
    namespace=settings.ASTRA_DB_KEYSPACE,
    collection_vector_service_options=VectorServiceOptions(
        provider="nvidia",
        model_name="NV-Embed-QA",
    ),
)



def find_similar_cases(incident_description: str):
    """
    Find similar cases with semantic search + optional metadata filter.
    Returns [] if nothing matches or if collection does not exist.
    """
    try:
        results_with_scores = vector_store.similarity_search_with_score(
            query=incident_description,
            k=1,
            filter={
                "court": {"$in": ["Supreme Court of India", "High Court", "District Court", "N/A"]},
            }
        )

        similar_cases = []
        for doc, score in results_with_scores:
            if score >= 0.70:
                formatted_case = format_case_details(doc.metadata)
                similar_cases.append({"case": formatted_case, "similarity_score": score})

        return similar_cases

    except Exception as e:
        error_message = str(e)
        if "COLLECTION_NOT_EXIST" in error_message or "collection name: case_laws" in error_message:
            print("Collection does not exist, returning empty case list.")
        else:
            print(f"Error in vector search: {error_message}")
        return []  # Unified empty result for both collection-not-found and no match
    

def format_case_details(case_data: dict) -> dict:
    return {
        "case_name": case_data.get("case_id_name", "N/A"),
        "court": case_data.get("court", "N/A"),
        "date": case_data.get("date_of_judgment", "N/A"),
        "ipc_sections": case_data.get("ipc_sections", []),
        "summary": case_data.get("case_summary", ""),
        "verdict": case_data.get("verdict_outcome", "N/A"),
        "legal_issues": case_data.get("legal_issues", []),
        "judgment_text": case_data.get("judgment_text", ""),
        "defense_raised": case_data.get("defense_raised", []),
        "evidence_discussed": case_data.get("evidence_discussed", []),
        "crime_type": case_data.get("crime_type", "N/A"),
        "precedents": case_data.get("key_precedents_cited", []),
        "severity": case_data.get("severity", "N/A"),
    }


