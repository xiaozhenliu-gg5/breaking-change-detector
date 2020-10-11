import json 
from src.findings.utils import Finding
from src.findings.utils import FindingCategory

class FindingContainer:
    _FINDINGS = []

    @classmethod
    def addFinding (
        cls, 
        category: FindingCategory, 
        location: str,
        message: str,
        actionable: bool,
        extra_info = None):
        cls._FINDINGS.append(Finding(category, location, message, actionable, extra_info))

    @classmethod
    def getAllFindings (cls):
        return cls._FINDINGS
    
    @classmethod
    def toJson(cls):
        findingDictArr = []
        for finding in cls._FINDINGS:
            findingDictArr.append(finding.toDict())
        return json.dumps(findingDictArr)
    
    @classmethod
    def reset(cls):
        cls._FINDINGS = []
