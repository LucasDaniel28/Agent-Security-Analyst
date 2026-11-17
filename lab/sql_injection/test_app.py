import unittest

from app import (
    create_connection,
    initialize_database,
    search_users_safe,
    search_users_vulnerable,
)


class SqlInjectionLabTests(unittest.TestCase):
    def setUp(self):
        self.connection = create_connection()
        initialize_database(self.connection)

    def tearDown(self):
        self.connection.close()

    def test_normal_username_returns_expected_user(self):
        result = search_users_safe(self.connection, "ana")
        self.assertEqual([row["username"] for row in result], ["ana"])

    def test_vulnerable_query_can_be_manipulated(self):
        payload = "' OR '1'='1' -- "
        result = search_users_vulnerable(self.connection, payload)
        self.assertEqual(len(result), 3)

    def test_parameterized_query_treats_payload_as_data(self):
        payload = "' OR '1'='1' -- "
        result = search_users_safe(self.connection, payload)
        self.assertEqual(result, [])

    def test_safe_query_does_not_break_legitimate_search(self):
        result = search_users_safe(self.connection, "bruno")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["role"], "user")


if __name__ == "__main__":
    unittest.main()
