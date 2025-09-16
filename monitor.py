from time import sleep
import sys

# Global language variable: 'en' for English, 'de' for German
LANGUAGE = 'en'

# Dictionary for localized messages
MESSAGES = {
    'en': {
        'temperature': 'Temperature critical!',
        'pulseRate': 'Pulse Rate is out of range!',
        'spo2': 'Oxygen Saturation out of range!',
        'blood_sugar': 'Blood Sugar out of range!',
        'blood_pressure': 'Blood Pressure out of range!',
        'respiratory_rate': 'Respiratory Rate out of range!',
    },
    'de': {
        'temperature': 'Temperatur kritisch!',
        'pulseRate': 'Pulsrate außerhalb des Bereichs!',
        'spo2': 'Sauerstoffsättigung außerhalb des Bereichs!',
        'blood_sugar': 'Blutzucker außerhalb des Bereichs!',
        'blood_pressure': 'Blutdruck außerhalb des Bereichs!',
        'respiratory_rate': 'Atemfrequenz außerhalb des Bereichs!',
    }
}

# Vital parameters and their limits
VITALS_LIMITS = {
    'temperature': (95, 102),
    'pulseRate': (60, 100),
    'spo2': (90, 100),
    'blood_sugar': (70, 110),
    'blood_pressure': (90, 150),
    'respiratory_rate': (12, 20)
}

def blink_alert():
    """Blinking alert animation."""
    for _ in range(6):
        print('\r* ', end='')
        sys.stdout.flush()
        sleep(1)
        print('\r *', end='')
        sys.stdout.flush()
        sleep(1)
    print()

def check_vital(name, value):
    """Check a single vital sign value against limits."""
    low, high = VITALS_LIMITS[name]
    if not (low <= value <= high):
        print(MESSAGES[LANGUAGE][name])
        blink_alert()
        return False
    return True

def vitals_ok(temperature, pulseRate, spo2, blood_sugar, blood_pressure, respiratory_rate):
    """Check all vitals, return True only if all are OK."""
    vitals_values = {
        'temperature': temperature,
        'pulseRate': pulseRate,
        'spo2': spo2,
        'blood_sugar': blood_sugar,
        'blood_pressure': blood_pressure,
        'respiratory_rate': respiratory_rate
    }

    # Prepare table header
    print(f"{'Vital':<17} | {'Value':<7} | {'Status':<8}")
    print("-" * 38)

    all_ok = True
    for vital_name, vital_value in vitals_values.items():
        ok = check_vital(vital_name, vital_value)
        status = "OK" if ok else "Critical"
        print(f"{vital_name:<17} | {vital_value:<7} | {status:<8}")
        if not ok:
            all_ok = False

    return all_ok


# Example usage:
result = vitals_ok(temperature=98.6, pulseRate=55, spo2=95, blood_sugar=120, blood_pressure=135, respiratory_rate=15)
print("\nOverall Vitals Status:", "OK" if result else "CRITICAL")
