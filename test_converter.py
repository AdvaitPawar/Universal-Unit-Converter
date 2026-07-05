"""
test_converter.py
==================================================================
Production-grade automated test suite for converter_engine.py

Author:      SDET Test Harness
Framework:   Python unittest (stdlib only)
Coverage:    Temperature | Standard Units | Currency/Network | Defensive Boundaries

Design Notes:
- unittest.subTest is used extensively so large data matrices run as
  independent, individually-reportable assertions without duplicating
  boilerplate test methods.
- The currency module is fully decoupled from the live internet via
  unittest.mock.patch on `requests.get`. No test in this suite makes
  a real network call.
- All floating point comparisons use assertAlmostEqual(places=4) to
  guard against binary floating point representation drift.
==================================================================
"""

import unittest
from unittest.mock import patch, MagicMock

import converter_engine as ce


# ==================================================================
# CATEGORY A: TEMPERATURE FORMULA PERMUTATIONS
# ==================================================================
class TestTemperatureConversions(unittest.TestCase):
    """
    Validates calculate_temperature() across identity transitions,
    extreme physical bounds (absolute zero), negative values, and
    floating-point precision edges.
    """

    def test_temperature_conversion_matrix(self):
        """Matrix of (input_val, unit_from, unit_to, expected) permutations."""
        matrix = [
            # --- Identity transitions (same unit in and out) ---
            (25.0, 'Celsius', 'Celsius', 25.0),
            (98.6, 'Fahrenheit', 'Fahrenheit', 98.6),
            (300.0, 'Kelvin', 'Kelvin', 300.0),
            (0.0, 'Celsius', 'Celsius', 0.0),

            # --- Absolute zero bounds ---
            (-273.15, 'Celsius', 'Kelvin', 0.0),
            (0.0, 'Kelvin', 'Celsius', -273.15),
            (-273.15, 'Celsius', 'Fahrenheit', -459.67),
            (0.0, 'Kelvin', 'Fahrenheit', -459.67),

            # --- Well-known reference points ---
            (0.0, 'Celsius', 'Fahrenheit', 32.0),
            (100.0, 'Celsius', 'Fahrenheit', 212.0),
            (32.0, 'Fahrenheit', 'Celsius', 0.0),
            (212.0, 'Fahrenheit', 'Celsius', 100.0),
            (0.0, 'Celsius', 'Kelvin', 273.15),
            (273.15, 'Kelvin', 'Celsius', 0.0),

            # --- Negative value handling ---
            (-40.0, 'Celsius', 'Fahrenheit', -40.0),   # -40 is the C/F crossover point
            (-40.0, 'Fahrenheit', 'Celsius', -40.0),
            (-10.0, 'Celsius', 'Kelvin', 263.15),
            (-459.67, 'Fahrenheit', 'Kelvin', 0.0),

            # --- Floating point precision edges ---
            (36.6, 'Celsius', 'Fahrenheit', 97.88),
            (98.6, 'Fahrenheit', 'Celsius', 37.0),
            (310.15, 'Kelvin', 'Celsius', 37.0),
            (0.1, 'Celsius', 'Fahrenheit', 32.18),
        ]

        for input_val, unit_from, unit_to, expected in matrix:
            with self.subTest(input_val=input_val, unit_from=unit_from, unit_to=unit_to):
                result = ce.calculate_temperature(input_val, unit_from, unit_to)
                self.assertAlmostEqual(result, expected, places=4)

    def test_temperature_round_trip_identity(self):
        """Converting A -> B -> A should return the original value (within precision)."""
        round_trips = [
            (100.0, 'Celsius', 'Fahrenheit'),
            (37.0, 'Celsius', 'Kelvin'),
            (-273.15, 'Celsius', 'Fahrenheit'),
            (0.0, 'Kelvin', 'Celsius'),
        ]
        for original, unit_a, unit_b in round_trips:
            with self.subTest(original=original, unit_a=unit_a, unit_b=unit_b):
                intermediate = ce.calculate_temperature(original, unit_a, unit_b)
                final = ce.calculate_temperature(intermediate, unit_b, unit_a)
                self.assertAlmostEqual(final, original, places=4)


# ==================================================================
# CATEGORY B: STANDARD UNIT CONVERSIONS (Distance, Weight, Volume, Time)
# ==================================================================
class TestStandardConversions(unittest.TestCase):
    """
    Validates calculate_standard() across Distance, Weight, Volume, and
    Time categories, including zero values and large-magnitude scaling.
    """

    def test_cross_conversion_matrix(self):
        """Matrix of (category, input_val, unit_from, unit_to, expected)."""
        matrix = [
            # --- Distance ---
            ('Distance', 1.0, 'Kilometer', 'Meter', 1000.0),
            ('Distance', 1.0, 'Mile', 'Feet', 5279.9869),
            ('Distance', 12.0, 'Inch', 'Feet', 1.0),
            ('Distance', 1.0, 'Yard', 'Meter', 0.9144),
            ('Distance', 100.0, 'Centimeter', 'Meter', 1.0),
            ('Distance', 1.0, 'Millimeter', 'Centimeter', 0.1),

            # --- Weight ---
            ('Weight', 1.0, 'Kilogram', 'Gram', 1000.0),
            ('Weight', 1.0, 'Ton', 'Kilogram', 1000.0),
            ('Weight', 1.0, 'Pound', 'Gram', 453.592),
            ('Weight', 1000.0, 'Milligram', 'Gram', 1.0),

            # --- Volume ---
            ('Volume', 1.0, 'Gallon', 'Quart', 4.0),
            ('Volume', 1.0, 'Quart', 'Pint', 2.0),
            ('Volume', 1.0, 'Pint', 'Cup', 2.0),
            ('Volume', 16.0, 'Ounce', 'Pint', 1.0),

            # --- Time ---
            ('Time', 1.0, 'Hour', 'Minutes', 60.0),
            ('Time', 1.0, 'Day', 'Hour', 24.0),
            ('Time', 60.0, 'Seconds', 'Minutes', 1.0),
            ('Time', 1.0, 'Year', 'Day', 365.0),

            # --- Identity transitions (same unit) ---
            ('Distance', 42.0, 'Meter', 'Meter', 42.0),
            ('Weight', 7.0, 'Gram', 'Gram', 7.0),

            # --- Zero value handling ---
            ('Distance', 0.0, 'Kilometer', 'Mile', 0.0),
            ('Weight', 0.0, 'Ton', 'Milligram', 0.0),
            ('Volume', 0.0, 'Gallon', 'Ounce', 0.0),
            ('Time', 0.0, 'Year', 'Seconds', 0.0),

            # --- Large magnitude scaling (1,000,000 units) ---
            ('Distance', 1000000.0, 'Millimeter', 'Kilometer', 1.0),
            ('Weight', 1000000.0, 'Gram', 'Ton', 1.0),
            ('Volume', 1000000.0, 'Ounce', 'Gallon', 7812.5),
            ('Time', 1000000.0, 'Seconds', 'Day', 11.5741),
        ]

        for category, input_val, unit_from, unit_to, expected in matrix:
            with self.subTest(category=category, input_val=input_val,
                               unit_from=unit_from, unit_to=unit_to):
                result = ce.calculate_standard(input_val, category, unit_from, unit_to,
                                                ce.ConversionFactors)
                self.assertAlmostEqual(result, expected, places=4)

    def test_negative_input_scales_linearly(self):
        """Standard unit math is linear, so negative inputs should negate cleanly."""
        result = ce.calculate_standard(-5.0, 'Distance', 'Kilometer', 'Meter',
                                        ce.ConversionFactors)
        self.assertAlmostEqual(result, -5000.0, places=4)


# ==================================================================
# CATEGORY C: ADVANCED NETWORK & CACHE MOCKING (Currency Module)
# ==================================================================
class TestCurrencyNetworkAndCache(unittest.TestCase):
    """
    Fully mocks requests.get to validate currency conversion logic without
    touching the live internet. Covers cold cache, warm cache, network
    failure fallback, and identity short-circuiting.
    """

    def setUp(self):
        """Reset the module-level cache before every test to guarantee isolation."""
        ce.exchange_rates_cache = {}

    @patch('converter_engine.requests.get')
    def test_cold_cache_fetches_and_applies_rate(self, mock_get):
        """First-ever lookup for a currency pair should hit the network and compute correctly."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'rates': {'EUR': 0.85, 'GBP': 0.75}}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        result = ce.calculate_currency(100.0, 'USD', 'EUR')

        mock_get.assert_called_once()
        self.assertAlmostEqual(result, 85.0, places=4)
        self.assertIn('USD', ce.exchange_rates_cache)

    @patch('converter_engine.requests.get')
    def test_warm_cache_skips_network_on_subsequent_calls(self, mock_get):
        """Once a currency's rate table is cached, repeat calls must not re-hit the network."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'rates': {'EUR': 0.85, 'JPY': 110.0}}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        first = ce.calculate_currency(50.0, 'USD', 'EUR')
        second = ce.calculate_currency(200.0, 'USD', 'JPY')

        # Same base currency (USD) queried twice -> network should fire only ONCE
        mock_get.assert_called_once()
        self.assertAlmostEqual(first, 42.5, places=4)
        self.assertAlmostEqual(second, 22000.0, places=4)

    @patch('converter_engine.requests.get')
    def test_network_failure_returns_error_sentinel(self, mock_get):
        """A timeout or connection error must be caught and surfaced as 'NETWORK_ERROR', not raised."""
        mock_get.side_effect = Exception("Connection timed out")

        result = ce.calculate_currency(100.0, 'USD', 'EUR')

        self.assertEqual(result, "NETWORK_ERROR")

    @patch('converter_engine.requests.get')
    def test_http_error_status_returns_error_sentinel(self, mock_get):
        """A non-2xx HTTP status (raise_for_status) must also degrade gracefully."""
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = Exception("503 Service Unavailable")
        mock_get.return_value = mock_response

        result = ce.calculate_currency(100.0, 'USD', 'EUR')

        self.assertEqual(result, "NETWORK_ERROR")

    @patch('converter_engine.requests.get')
    def test_identity_currency_short_circuits_network(self, mock_get):
        """USD -> USD (and any X -> X) must never touch the network at all."""
        result = ce.calculate_currency(500.0, 'USD', 'USD')

        mock_get.assert_not_called()
        self.assertAlmostEqual(result, 500.0, places=4)

    @patch('converter_engine.requests.get')
    def test_missing_target_currency_returns_none(self, mock_get):
        """If the API returns rates but the target currency isn't in them, return None (not crash)."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'rates': {'EUR': 0.85}}  # no 'XYZ'
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        result = ce.calculate_currency(100.0, 'USD', 'XYZ')

        self.assertIsNone(result)

    @patch('converter_engine.requests.get')
    def test_zero_value_currency_conversion(self, mock_get):
        """Zero should convert to zero without triggering any special-casing bugs."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'rates': {'EUR': 0.85}}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        result = ce.calculate_currency(0.0, 'USD', 'EUR')

        self.assertAlmostEqual(result, 0.0, places=4)


# ==================================================================
# CATEGORY D: ROBUSTNESS & DEFENSIVE BOUNDARIES
# ==================================================================
class TestDefensiveBoundaries(unittest.TestCase):
    """
    Probes the engine's failure modes: invalid unit strings, mismatched
    categories, empty inputs, and other malformed data that a real UI
    could accidentally pass through.
    """

    def test_invalid_unit_string_raises_keyerror(self):
        """A completely made-up unit name should raise KeyError, not silently miscompute."""
        with self.assertRaises(KeyError):
            ce.calculate_standard(10.0, 'Distance', 'Lightyear', 'Meter', ce.ConversionFactors)

    def test_invalid_category_raises_keyerror(self):
        """A category that doesn't exist in ConversionFactors must raise KeyError."""
        with self.assertRaises(KeyError):
            ce.calculate_standard(10.0, 'Temperature', 'Meter', 'Feet', ce.ConversionFactors)

    def test_mismatched_category_unit_raises_keyerror(self):
        """A unit belonging to a different category (e.g. Weight unit under Distance) must fail loudly."""
        with self.assertRaises(KeyError):
            ce.calculate_standard(10.0, 'Distance', 'Kilogram', 'Meter', ce.ConversionFactors)

    def test_empty_string_unit_raises_keyerror(self):
        """Empty string inputs for unit_from/unit_to should not be silently accepted."""
        with self.assertRaises(KeyError):
            ce.calculate_standard(10.0, 'Distance', '', 'Meter', ce.ConversionFactors)

    def test_temperature_invalid_unit_from_raises(self):
        """
        An invalid unit_from leaves `celsius` unassigned in calculate_temperature,
        which currently surfaces as an UnboundLocalError. This test locks in
        that (undesirable but current) behavior so any future refactor is
        forced to consciously change it rather than regress silently.
        """
        with self.assertRaises(UnboundLocalError):
            ce.calculate_temperature(100.0, 'Rankine', 'Celsius')

    def test_temperature_invalid_unit_to_returns_none(self):
        """An invalid unit_to falls through all branches and implicitly returns None."""
        result = ce.calculate_temperature(100.0, 'Celsius', 'Rankine')
        self.assertIsNone(result)

    def test_currency_empty_string_currency_triggers_network_path(self):
        """
        Empty string currency codes are not caught by identity check (since
        '' != '' is False... actually '' == '' is True) -- verify the
        engine treats empty-to-empty as an identity short circuit.
        """
        result = ce.calculate_currency(50.0, '', '')
        self.assertAlmostEqual(result, 50.0, places=4)

    @patch('converter_engine.requests.get')
    def test_currency_none_value_propagates_safely(self, mock_get):
        """Passing None as the numeric value should not crash arithmetic silently mid-cache-hit."""
        mock_response = MagicMock()
        mock_response.json.return_value = {'rates': {'EUR': 0.85}}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        with self.assertRaises(TypeError):
            ce.calculate_currency(None, 'USD', 'EUR')


# ==================================================================
# TEST RUNNER ENTRY POINT
# ==================================================================
if __name__ == '__main__':
    unittest.main(verbosity=2)
