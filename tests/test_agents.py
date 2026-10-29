"""Agent tests run without Ollama: the LLM class is replaced by a stub."""
import os
import sys
import tempfile
import types
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class FakeOllama:
    def __init__(self, model=None, **kwargs):
        self.model = model

    def invoke(self, prompt):
        return "FAKE-LLM-OUTPUT"


def _install_fake_langchain():
    community = types.ModuleType("langchain_community")
    llms = types.ModuleType("langchain_community.llms")
    llms.Ollama = FakeOllama
    community.llms = llms
    sys.modules["langchain_community"] = community
    sys.modules["langchain_community.llms"] = llms


class AgentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        os.chdir(ROOT)
        cls._saved = {k: sys.modules.get(k) for k in ("langchain_community", "langchain_community.llms")}
        _install_fake_langchain()

    @classmethod
    def tearDownClass(cls):
        for name, module in cls._saved.items():
            if module is None:
                sys.modules.pop(name, None)
            else:
                sys.modules[name] = module

    def test_every_agent_returns_llm_text(self):
        from agents.iqvia_agent import IQVIAAgent
        from agents.exim_agent import EXIMAgent
        from agents.patent_agent import PatentAgent
        from agents.clinical_agent import ClinicalAgent
        from agents.web_agent import WebAgent
        from agents.internal_agent import InternalAgent
        for cls in (IQVIAAgent, EXIMAgent, PatentAgent, ClinicalAgent, WebAgent, InternalAgent):
            self.assertEqual(cls().run("Paracetamol"), "FAKE-LLM-OUTPUT", cls.__name__)

    def test_master_agent_builds_a_pdf(self):
        from master_agent import MasterAgent
        with tempfile.TemporaryDirectory() as tmp:
            os.chdir(tmp)
            try:
                path = MasterAgent().run("Paracetamol")
                self.assertTrue(path.endswith("Paracetamol_report.pdf"))
                self.assertTrue(os.path.exists(path))
            finally:
                os.chdir(ROOT)


if __name__ == "__main__":
    unittest.main()
