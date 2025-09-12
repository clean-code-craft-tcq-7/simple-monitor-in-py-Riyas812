import unittest
from monitor import vitals_ok

class MonitorTest(unittest.TestCase):
    def test_all_vitals_ok(self):
        # All vitals within normal ranges
        self.assertTrue(vitals_ok(
            temperature=98.6,
            pulseRate=75,
            spo2=95,
            blood_sugar=90,
            blood_pressure=120,
            respiratory_rate=16
        ))

    def test_temperature_critical(self):
        # Temperature too high
        self.assertFalse(vitals_ok(
            temperature=103,
            pulseRate=75,
            spo2=95,
            blood_sugar=90,
            blood_pressure=120,
            respiratory_rate=16
        ))

        # Temperature too low
        self.assertFalse(vitals_ok(
            temperature=94,
            pulseRate=75,
            spo2=95,
            blood_sugar=90,
            blood_pressure=120,
            respiratory_rate=16
        ))

    def test_pulse_rate_out_of_range(self):
        # Pulse rate too low
        self.assertFalse(vitals_ok(
            temperature=98.6,
            pulseRate=50,
            spo2=95,
            blood_sugar=90,
            blood_pressure=120,
            respiratory_rate=16
        ))

        # Pulse rate too high
        self.assertFalse(vitals_ok(
            temperature=98.6,
            pulseRate=110,
            spo2=95,
            blood_sugar=90,
            blood_pressure=120,
            respiratory_rate=16
        ))

    def test_spo2_out_of_range(self):
        # Oxygen saturation too low
        self.assertFalse(vitals_ok(
            temperature=98.6,
            pulseRate=75,
            spo2=85,
            blood_sugar=90,
            blood_pressure=120,
            respiratory_rate=16
        ))

    def test_blood_sugar_out_of_range(self):
        # Blood sugar too low
        self.assertFalse(vitals_ok(
            temperature=98.6,
            pulseRate=75,
            spo2=95,
            blood_sugar=60,
            blood_pressure=120,
            respiratory_rate=16
        ))

        # Blood sugar too high
        self.assertFalse(vitals_ok(
            temperature=98.6,
            pulseRate=75,
            spo2=95,
            blood_sugar=115,
            blood_pressure=120,
            respiratory_rate=16
        ))

    def test_blood_pressure_out_of_range(self):
        # Blood pressure too low
        self.assertFalse(vitals_ok(
            temperature=98.6,
            pulseRate=75,
            spo2=95,
            blood_sugar=90,
            blood_pressure=85,
            respiratory_rate=16
        ))

        # Blood pressure too high
        self.assertFalse(vitals_ok(
            temperature=98.6,
            pulseRate=75,
            spo2=95,
            blood_sugar=90,
            blood_pressure=160,
            respiratory_rate=16
        ))

    def test_respiratory_rate_out_of_range(self):
        # Respiratory rate too low
        self.assertFalse(vitals_ok(
            temperature=98.6,
            pulseRate=75,
            spo2=95,
            blood_sugar=90,
            blood_pressure=120,
            respiratory_rate=10
        ))

        # Respiratory rate too high
        self.assertFalse(vitals_ok(
            temperature=98.6,
            pulseRate=75,
            spo2=95,
            blood_sugar=90,
            blood_pressure=120,
            respiratory_rate=25
        ))

if __name__ == '__main__':
    unittest.main()
