from agents.iqvia_agent import IQVIAAgent
from agents.exim_agent import EXIMAgent
from agents.patent_agent import PatentAgent
from agents.clinical_agent import ClinicalAgent
from agents.web_agent import WebAgent
from agents.internal_agent import InternalAgent
from utils.report_generator import create_pdf_report
from utils.summarizer import combine_summaries

class MasterAgent:
    def __init__(self):
        self.iqvia = IQVIAAgent()
        self.exim = EXIMAgent()
        self.patent = PatentAgent()
        self.clinical = ClinicalAgent()
        self.web = WebAgent()
        self.internal = InternalAgent()

    def run(self, query):
        iqvia_out = self.iqvia.run(query)
        clinical_out = self.clinical.run(query)
        patent_out = self.patent.run(query)
        exim_out = self.exim.run(query)
        internal_out = self.internal.run(query)
        web_out = self.web.run(query)

        combined = combine_summaries([
            iqvia_out, clinical_out, patent_out, exim_out, internal_out, web_out
        ])

        report_path = create_pdf_report(query, combined)
        return report_path
