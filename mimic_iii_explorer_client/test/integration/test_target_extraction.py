import unittest

from generated_client.models.extracted_target import ExtractedTarget
from generated_client.models.target_extraction_spec import TargetExtractionSpec
from mimic_iii_explorer_client.client.target_api_client import TargetApiClient


class TestTargetExtraction(unittest.TestCase):
    """Integration tests for target extraction"""

    def test_basic_target_extraction_patient_died_during_admission(self):
        id1 = 100001
        id2 = 100053

        target_extraction_spec = TargetExtractionSpec(
            target_type="PATIENT_DIED_DURING_ADMISSION",
            ids=[id1, id2]
        )

        client = TargetApiClient()

        res = client.target(target_extraction_spec)

        self.assertEqual(2, len(res))
        self.assertTrue(ExtractedTarget(int(id1), 0) in res)
        self.assertTrue(ExtractedTarget(int(id2), 1) in res)

    def test_target_extraction_with_invalid_target_spec(self):
        target_extraction_spec = TargetExtractionSpec(
            target_type="PATIENT_DIED_DURING_ADMISSION",
            ids=[-1]
        )

        client = TargetApiClient()

        self.assertEqual(0, len(client.target(target_extraction_spec)))
