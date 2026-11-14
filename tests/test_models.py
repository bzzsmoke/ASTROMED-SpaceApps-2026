import unittest
from models.health_model import assess_measurement
from models.resource_optimizer import allocate_medical_kits

class ModelTests(unittest.TestCase):
    def test_nominal_measurement_without_baseline(self):
        result = assess_measurement({"heart_rate":72,"spo2":98,"temperature":36.7,"systolic":118,"diastolic":76,"respiration":15,"glucose":95,"sleep_hours":7})
        self.assertEqual(result["risk_level"],"NOMINAL")

    def test_critical_demo_guardrail(self):
        result = assess_measurement({"heart_rate":150,"spo2":85,"temperature":39.5,"systolic":185,"diastolic":110,"glucose":300})
        self.assertEqual(result["risk_level"],"CRITICAL")

    def test_personal_baseline_drift(self):
        result = assess_measurement({"heart_rate":95,"sleep_hours":4}, {"heart_rate":65,"sleep_hours":7})
        self.assertEqual(result["risk_level"],"WARNING")
        self.assertGreaterEqual(len(result["flags"]),2)

    def test_resource_allocation(self):
        result = allocate_medical_kits({"A":1,"B":5,"C":3},2)
        self.assertEqual(result["assigned"],["B","C"])

    def test_negative_kits_rejected(self):
        with self.assertRaises(ValueError):
            allocate_medical_kits({"A":1},-1)

if __name__ == "__main__":
    unittest.main()
